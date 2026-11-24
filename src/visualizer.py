import matplotlib.pyplot as plt

def plot_curves(results, out_path="outputs/spectral_niches.png"):
    """Plots overlaid frequency curves with ecological bands."""
    plt.figure(figsize=(10, 5))
    
    for r in results:
        mask = r["freqs"] <= 10000
        plt.plot(r["freqs"][mask], r["pwr"][mask], label=f"{r['name']} (NDSI: {r['ndsi']:+.2f})")

    # Shaded reference zones
    plt.axvspan(100, 1500, color="gray", alpha=0.15, label="Traffic (0.1-1.5 kHz)")
    plt.axvspan(2000, 8000, color="green", alpha=0.08, label="Biophony (2-8 kHz)")

    plt.title("NicheAcoustics: Frequency Partitioning")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Sound Power")
    plt.xlim(0, 10000)
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_path, dpi=200)
    plt.close()