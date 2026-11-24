import numpy as np
import librosa

def get_spectrum(y, sr):
    """Computes STFT magnitude, frequency axis, and time-averaged power."""
    stft = np.abs(librosa.stft(y))
    freqs = librosa.fft_frequencies(sr=sr)
    avg_power = np.mean(stft, axis=1)
    return stft, freqs, avg_power

def get_ndsi(freqs, pwr):
    """NDSI: Nature (2-8 kHz) vs. Traffic (0.1-1.5 kHz)."""
    traffic = np.sum(pwr[(freqs >= 100) & (freqs <= 1500)])
    nature = np.sum(pwr[(freqs >= 2000) & (freqs <= 8000)])
    return (nature - traffic) / (nature + traffic)

def get_aci(stft):
    """ACI: Millisecond volume jumps (pulse vs. drone)."""
    diffs = np.sum(np.abs(np.diff(stft, axis=1)), axis=1)
    totals = np.sum(stft[:, :-1], axis=1)
    valid = totals > 0
    return np.mean(diffs[valid] / totals[valid]) * 1000

def get_entropy(freqs, pwr):
    """Shannon Entropy: Channel sharing evenness (0 to 1)."""
    p = pwr[(freqs >= 100) & (freqs <= 10000)]
    p = p / np.sum(p)
    h = -np.sum(p * np.log2(np.where(p > 0, p, 1)))
    return h / np.log2(len(p))