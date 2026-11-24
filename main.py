import glob
import os
import re
import numpy as np
import pandas as pd
import librosa
import matplotlib.pyplot as plt


def compute_ecoacoustic_indices(file_path, sr=44100, n_fft=2048, hop_length=512):
    y, sr = librosa.load(file_path, sr=sr, mono=True)
    S = np.abs(librosa.stft(y, n_fft=n_fft, hop_length=hop_length)) ** 2
    freqs = librosa.fft_frequencies(sr=sr, n_fft=n_fft)
    mean_power = np.mean(S, axis=1)

    # 1. NDSI (Traffic: 0.1-1.5 kHz | Biophony: 2.0-8.0 kHz)
    anthro_mask = (freqs >= 100) & (freqs <= 1500)
    bio_mask = (freqs >= 2000) & (freqs <= 8000)
    anthro_power = np.sum(mean_power[anthro_mask])
    bio_power = np.sum(mean_power[bio_mask])
    ndsi = (bio_power - anthro_power) / (bio_power + anthro_power + 1e-12)

    # 2. Acoustic Complexity Index (ACI)
    S_bio = S[bio_mask, :]
    diff = np.abs(np.diff(S_bio, axis=1))
    aci = np.sum(np.sum(diff, axis=1) / (np.sum(S_bio, axis=1) + 1e-12))

    # 3. Normalized Shannon Spectral Entropy (H)
    band_mask = (freqs >= 100) & (freqs <= 8000)
    psd_band = mean_power[band_mask]
    prob_dist = psd_band / (np.sum(psd_band) + 1e-12)
    entropy = -np.sum(prob_dist * np.log2(prob_dist + 1e-12)) / np.log2(len(prob_dist))

    return freqs, mean_power, ndsi, aci, entropy


def main():
    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    wav_files = sorted(glob.glob("data/raw/*.wav"))
    if not wav_files:
        print("No .wav files found in data/raw/")
        return

    records = []
    spectra_by_group = {}
    freqs_ref = None

    for file_path in wav_files:
        fname = os.path.splitext(os.path.basename(file_path))[0]
        match = re.search(r"(Site[ABC])_[A-Za-z]+([ME])", fname)
        if not match:
            continue

        site = match.group(1)
        session = "Morning" if match.group(2) == "M" else "Evening"
        group_key = (site, session)

        freqs, mean_power, ndsi, aci, entropy = compute_ecoacoustic_indices(file_path)
        freqs_ref = freqs

        records.append({
            "Site": site,
            "Session": session,
            "NDSI": ndsi,
            "ACI": aci,
            "Entropy (H)": entropy,
        })
        spectra_by_group.setdefault(group_key, []).append(mean_power)

    # Compute 3-day averages per Site & Session
    df = pd.DataFrame(records)
    summary = (
        df.groupby(["Site", "Session"], as_index=False)[["NDSI", "ACI", "Entropy (H)"]]
        .mean()
        .sort_values(["Site", "Session"], ascending=[True, False])  # Morning first, then Evening
    )

    # Format cleanly for display and CSV
    display_df = summary.copy()
    display_df["NDSI"] = display_df["NDSI"].map(lambda x: f"{x:+.2f}")
    display_df["ACI"] = display_df["ACI"].round(1)
    display_df["Entropy (H)"] = display_df["Entropy (H)"].round(2)

    print("\n=== 3-Day Average Ecoacoustic Summary ===")
    print(display_df.to_string(index=False) + "\n")
    display_df.to_csv("data/processed/ecoacoustic_summary.csv", index=False)

    # Plot only the 6 averaged spectra (Morning vs Evening for each site)
    plt.figure(figsize=(10.5, 5.5), dpi=150)
    colors = {"SiteA": "#d62728", "SiteB": "#1f77b4", "SiteC": "#2ca02c"}
    styles = {"Morning": "-", "Evening": "--"}

    for _, row in summary.iterrows():
        site, session, ndsi_avg = row["Site"], row["Session"], row["NDSI"]
        avg_power = np.mean(spectra_by_group[(site, session)], axis=0)
        power_db = 10 * np.log10(avg_power + 1e-12)

        mask_10k = freqs_ref <= 10000
        plt.plot(
            freqs_ref[mask_10k],
            power_db[mask_10k],
            color=colors[site],
            linestyle=styles[session],
            linewidth=2.0,
            label=f"{site} {session} (Mean NDSI: {ndsi_avg:+.2f})",
        )

    plt.axvspan(100, 1500, color="gray", alpha=0.15, label="Traffic (0.1-1.5 kHz)")
    plt.axvspan(2000, 8000, color="green", alpha=0.10, label="Biophony (2-8 kHz)")

    plt.title("NicheAcoustics: 3-Day Mean Spectral Partitioning (Morning vs. Evening)", fontsize=12.5)
    plt.xlabel("Frequency (Hz)", fontsize=11)
    plt.ylabel("Mean Sound Power (dB)", fontsize=11)
    plt.xlim(0, 10000)
    plt.grid(True, linestyle="--", alpha=0.35)
    plt.legend(loc="upper right", fontsize=9)
    plt.tight_layout()

    output_plot = "outputs/spectral_niches.png"
    plt.savefig(output_plot)
    print(f"Saved averaged plot to {output_plot}")
    plt.show()


if __name__ == "__main__":
    main()