<div align="center">

# 🌿 NicheAcoustics

### *Empirical Verification of Bernie Krause's Acoustic Niche Hypothesis Across Urban–Canopy Gradients*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![DSP-Librosa](https://img.shields.io/badge/Signal_Processing-Librosa-orange?style=for-the-badge)](https://librosa.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Field_Evaluation_Active-brightgreen?style=for-the-badge)]()

<p align="center">
  <b>A lightweight Digital Signal Processing (DSP) framework for soundscape ecology, bioacoustic entropy extraction, and spectral niche partitioning analysis.</b>
</p>

[Key Concepts](#-theoretical-framework) • [Architecture](#-system-architecture) • [Metrics](#-mathematical-formulation) • [Getting Started](#-getting-started) • [Field Protocol](#-field-sampling-protocol)

---

</div>

## 📌 Executive Summary

Urban encroachment introduces high-amplitude, low-frequency acoustic noise (**anthropophony**, $0.1\text{--}1.5\text{ kHz}$) into natural habitats. According to Bernie Krause's **Acoustic Niche Hypothesis (ANH)**, coexisting vocal taxa in healthy biomes avoid mutual acoustic masking by dividing the frequency domain into segregated acoustic channels.

`NicheAcoustics` is an automated, end-to-end Python pipeline designed to quantify this biological partitioning. By computing Short-Time Fourier Transforms (STFT) on field recordings collected across an urban-to-canopy transect, the framework extracts three foundational soundscape indices: **NDSI**, **ACI**, and **Shannon Spectral Entropy ($H$)**.

---
1. **NDSI (Normalized Difference Soundscape Index):**
   * Contrasts biological vocalizations ($2.0\text{--}8.0\text{ kHz}$) against anthropogenic vehicle noise ($0.1\text{--}1.5\text{ kHz}$).
   * Scale: $-1.0$ (traffic dominated) to $+1.0$ (biophony dominated).

2. **ACI (Acoustic Complexity Index):**
   * Computes millisecond-by-millisecond absolute amplitude changes across timeframes.
   * Differentiates dynamic, pulsed wildlife vocalizations (high variability) from flat, stationary machine drones (near-zero variability).

3. **Shannon Spectral Entropy ($H$):**
   * Adapts Information Entropy to measure the uniformity and spread of sound energy across discrete frequency bins.
   * High values ($H > 0.8$) prove multi-channel niche distribution; low values ($H < 0.4$) indicate acoustic monopolization by single-frequency noise sources.

## 🗂️ Project Structure

```text
NicheAcoustics/
├── data/
│   ├── raw/                 # Input .wav field recordings (uncompressed PCM, 44.1 kHz)
│   └── processed/           # Exported summary metrics (CSV)
├── outputs/                 # Multi-panel spectral curves and figures
├── src/
│   ├── __init__.py          # Module exports
│   ├── indices.py           # Core DSP algorithms (STFT, NDSI, ACI, Spectral Entropy)
│   └── visualizer.py        # Spectral plotting and band shading routines
├── main.py                  # Master batch pipeline runner
├── requirements.txt         # Project dependencies
├── .gitignore               # Excludes large audio files and environment caches
└── README.md                # Project documentation

---
## 📋 Field Sampling Protocol

* **Duration:** Exactly 60 seconds per recording.
* **Format:** Uncompressed 16-bit PCM WAV at 44.1 kHz.
* **Temporal Windows:** 
  * Dawn Chorus: 06:00 AM (peak avian communication)
  * Dusk Chorus: 06:00 PM (peak insect stridulation)
* **Sampling Locations:**
  * **Site A (Urban Edge):** Boundary road/perimeter wall under direct vehicular traffic exposure.
  * **Site B (Transition Zone):** Parkland or campus walkway with partial canopy cover.
  * **Site C (Forest Refuge):** Interior dense canopy core away from roads.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/](https://github.com/)<your-username>/NicheAcoustics.git
cd NicheAcoustics
```

### 2. Set Up Virtual Environment

**Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Analysis
Place your recorded `.wav` files into `data/raw/` and run:
```bash
python main.py
```

---

## 📊 Outputs

Executing the pipeline automatically generates:
1. **Console Summary Table:** Instant printout of computed indices for each audio sample.
2. **Processed CSV:** Stored at `data/processed/ecoacoustic_summary.csv`.
3. **Spectral Plot:** High-resolution multi-curve comparison plot with labeled traffic and biological corridors saved at `outputs/spectral_niches.png`.

---

## 🛠️ Built With

* **Librosa** — Audio analysis and Short-Time Fourier Transforms
* **NumPy** — Matrix and array computations
* **Pandas** — Data organization and CSV export
* **Matplotlib** — Spectral visualization