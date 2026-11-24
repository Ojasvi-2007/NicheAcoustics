<div align="center">

# 🌿 NicheAcoustics
### Evaluating the Acoustic Niche Hypothesis Across an Urban-to-Forest Gradient

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Librosa](https://img.shields.io/badge/DSP-Librosa%20%7C%20NumPy%20%7C%20SciPy-013243?style=for-the-badge)](https://librosa.org/)
[![Study Area](https://img.shields.io/badge/Location-IIT%20Madras%20%26%20Guindy%20NP-2E7D32?style=for-the-badge)](#2-field-study-sites--habitat-documentation)
[![Dataset](https://img.shields.io/badge/Dataset-18%20WAV%20%7C%2044.1%20kHz%20Mono-6A1B9A?style=for-the-badge)](#4-quantitative-results--spectral-partitioning-analysis)

*An end-to-end Digital Signal Processing (DSP) and bioacoustics pipeline quantifying spatial and diurnal soundscape recovery across Chennai's urban-forest interface.*

**Author:** Ojasvi Kumar  |  **Sampling Protocol:** 3 Consecutive Days (`Thu–Sat`)  |  **Windows:** Dawn (`06:00 IST`) & Dusk (`18:00 IST`)

</div>

---

## 1. Overview & Ecological Motivation

Urban expansion and vehicular traffic increasingly encroach upon peri-urban tropical forests, compressing the acoustic bandwidth available for wildlife communication. According to Bernie Krause's **Acoustic Niche Hypothesis (ANH)**, intact ecosystems exhibit **spectral frequency partitioning**—where birds, insects, and amphibians vocalize within distinct, non-overlapping frequency bands—whereas anthropogenic noise ($0.1\text{--}1.5\text{ kHz}$) masks biological signaling ($2.0\text{--}8.0\text{ kHz}$).

**NicheAcoustics** processes **18 uncompressed 60-second field recordings** (`44.1 kHz`, 16-bit Mono WAV) collected synchronously across a three-point transect spanning the **IIT Madras Campus** and the **Guindy National Park** forest boundary in Chennai, India. Using Short-Time Fourier Transform (STFT) **Power Spectral Density (PSD)**, the pipeline computes three ecoacoustic indices alongside dB-scaled spectral profiles:

* **Normalized Difference Soundscape Index (`NDSI`)** — Quantifies the ratio of biophony ($2.0\text{--}8.0\text{ kHz}$) to anthropophony ($0.1\text{--}1.5\text{ kHz}$).
* **Acoustic Complexity Index (`ACI`)** — Measures rapid temporal intensity modulation characteristic of multi-species bird vocalizations.
* **Normalized Shannon Spectral Entropy (`H`)** — Evaluates spectral evenness and frequency-niche occupancy across $0.1\text{--}8.0\text{ kHz}$.

---

## 2. Field Study Sites & Habitat Documentation

| Site ID | Ecological Zone | Landmark / Location | GPS Coordinates | Habitat & Acoustic Profile |
| :--- | :--- | :--- | :--- | :--- |
| **Site A** | **Urban Perimeter Control** | IIT Madras In-Gate Rd / Main Gate Roundabout | `13.005440, 80.241901` | Multi-lane paved entry roundabout adjacent to security gates and Sardar Patel Rd arterial traffic; manicured lawn strips and sparse ornamental trees. |
| **Site B** | **Buffered Campus Interior** | Ground Road near SAC Rd & Vindhya Mess | `12.990387, 80.235948` | Tree-lined internal campus road (~1.5 km from perimeter highways) flanked by dense shrubs, overhanging canopy, and damp wooded undergrowth. |
| **Site C** | **Deep Forest Refuge** | Madras Avenue (Guindy National Park Border) | `13.000776, 80.238422` | Closed-canopy tropical dry evergreen forest corridor with mature banyan aerial roots, thick leaf litter, and zero through-traffic. |

---

### 📍 Site A — Urban Perimeter Control (`13.005440, 80.241901`)
> **Acoustic Regime:** Chronic low-frequency traffic dominance (`0.1–1.5 kHz`) across both dawn (`-0.86` NDSI) and dusk (`-0.87` NDSI).

<table>
  <tr>
    <th width="42%">GPS Location Pin</th>
    <th width="58%">Ground Habitat View</th>
  </tr>
  <tr>
    <td align="center">
      <img src="assets/Screenshot_20261118-060054_Maps.png" alt="Site A GPS Map" height="340">
    </td>
    <td align="center">
      <img src="assets/IMG_20261118_180024174_HDR.jpg" alt="Site A Ground Habitat" height="340">
    </td>
  </tr>
  <tr>
    <th colspan="2">360° Horizon Panorama</th>
  </tr>
  <tr>
    <td colspan="2" align="center">
      <img src="assets/IMG_20261119_060018803.jpg" alt="Site A 360 Panorama" width="100%">
    </td>
  </tr>
</table>

---

### 📍 Site B — Buffered Campus Interior (`12.990387, 80.235948`)
> **Acoustic Regime:** Bimodal diurnal niche turnover — avian dawn chorus (`+0.51` NDSI) transitioning into a strong dusk insect/cricket chorus (`+0.17` NDSI).

<table>
  <tr>
    <th width="42%">GPS Location Pin</th>
    <th width="58%">Ground Habitat View</th>
  </tr>
  <tr>
    <td align="center">
      <img src="assets/Screenshot_20261118-062118_Maps.png" alt="Site B GPS Map" height="340">
    </td>
    <td align="center">
      <img src="assets/IMG_20261118_181542354_HDR.jpg" alt="Site B Ground Habitat" height="340">
    </td>
  </tr>
  <tr>
    <th colspan="2">360° Horizon Panorama</th>
  </tr>
  <tr>
    <td colspan="2" align="center">
      <img src="assets/IMG_20261119_062202644.jpg" alt="Site B 360 Panorama" width="100%">
    </td>
  </tr>
</table>

---

### 📍 Site C — Deep Forest Refuge (`13.000776, 80.238422`)
> **Acoustic Regime:** Dense diurnal avian sanctuary at dawn (`+0.50` NDSI, `0.78` Entropy) followed by deep post-dusk acoustic stillness (`-56 dB` noise floor).

<table>
  <tr>
    <th width="42%">GPS Location Pin</th>
    <th width="58%">Ground Habitat View</th>
  </tr>
  <tr>
    <td align="center">
      <img src="assets/Screenshot_20261121-055906_Maps.png" alt="Site C GPS Map" height="340">
    </td>
    <td align="center">
      <img src="assets/IMG_20261119_060818374_HDR.jpg" alt="Site C Ground Habitat" height="340">
    </td>
  </tr>
  <tr>
    <th colspan="2">360° Horizon Panorama</th>
  </tr>
  <tr>
    <td colspan="2" align="center">
      <img src="assets/IMG_20261120_062203221.jpg" alt="Site C 360 Panorama" width="100%">
    </td>
  </tr>
</table>

---

## 3. Signal Processing Methodology

All recordings were captured at `44.1 kHz` (16-bit PCM WAV) held horizontally at chest height (`1.3 m`) facing into the vegetation away from road edges. Each 60-second waveform $x[n]$ is transformed into a time-frequency power spectrogram $S[k, m] = \vert{}X[k, m]\vert{}^2$ (`n_fft = 2048`, `hop_length = 512`) and averaged across time to obtain the 1D **Mean Power Spectral Density** $\bar{P}[k]$.

1. **Normalized Difference Soundscape Index (NDSI):**
   $$\text{NDSI} = \frac{B - A}{B + A} \in [-1, +1]$$
   where $A = \sum_{k \in [0.1, 1.5\text{ kHz}]} \bar{P}[k]$ (anthropophony) and $B = \sum_{k \in [2.0, 8.0\text{ kHz}]} \bar{P}[k]$ (biophony).

2. **Acoustic Complexity Index (ACI):**
   $$\text{ACI} = \sum_{k \in B} \frac{\sum_{m=1}^{M-1} \vert{}S[k, m+1] - S[k, m]\vert{}}{\sum_{m=1}^{M} S[k, m]}$$
   Captures rapid temporal amplitude fluctuations from bird songs while filtering out steady mechanical engine hum.

3. **Normalized Shannon Spectral Entropy ($H$):**
   $$H = -\frac{1}{\log_2(K)} \sum_{k=1}^{K} p_k \log_2(p_k), \quad p_k = \frac{\bar{P}[k]}{\sum_{j=1}^{K} \bar{P}[j]}$$
   Quantifies spectral evenness across $0.1\text{--}8.0\text{ kHz}$ ($H \to 1$ indicates broad, multi-species frequency niche occupation; $H \to 0$ indicates narrowband dominance).

---

## 4. Quantitative Results & Spectral Partitioning Analysis

### 3-Day Diurnal Summary (`Thu–Sat` Averages, $N = 18$)

| Site | Session | Mean NDSI | Mean ACI | Mean Entropy ($H$) | Dominant Acoustic Regime |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Site A** | Morning (`06:00`) | `-0.86` | `223.2` | `0.57` | Continuous traffic masking (`0.1–1.5 kHz`) |
| **Site A** | Evening (`18:00`) | `-0.87` | `227.0` | `0.53` | Peak commuter traffic roar (`+2 dB` low-end spike) |
| **Site B** | Morning (`06:00`) | **`+0.51`** | **`250.0`** | **`0.82`** | Multi-species avian dawn chorus (`2.0–5.0 kHz`) |
| **Site B** | Evening (`18:00`) | **`+0.17`** | `229.7` | `0.69` | Nocturnal insect/cricket chorus (`6.5–8.5 kHz`) |
| **Site C** | Morning (`06:00`) | **`+0.50`** | **`239.4`** | **`0.78`** | Dense forest canopy dawn chorus (`2.0–5.5 kHz`) |
| **Site C** | Evening (`18:00`) | `-0.56` | `217.7` | `0.57` | Post-dusk acoustic stillness (`-56 dB` noise floor) |

### 3-Day Mean Power Spectral Density (`0–10 kHz`, dB Scale)

<p align="center">
  <img src="outputs/spectral_niches.png" alt="NicheAcoustics: 3-Day Mean Spectral Partitioning" width="92%">
</p>

### What the Spectral Partitioning Graph Shows
Plotting Mean Power Spectral Density on a logarithmic decibel ($\text{dB}$) scale reveals distinct frequency-band partitioning across space (**color**) and time of day (**solid vs. dashed lines**):

1. **Anthropogenic Traffic Band (`0.1–1.5 kHz`, Grey Shaded Region):**
   * **Site A (Red curves)** dominates the low-frequency band, peaking at **`+2 dB` in the evening** (dashed red) and **`-7 dB` in the morning** (solid red) due to continuous vehicle engines, horns, and tire rumble at the Main Gate roundabout.
   * **Sites B & C (Blue and Green curves)** drop by **`20–30 dB`** across this band (`-20` to `-46 dB`), demonstrating strong acoustic attenuation of urban traffic inside the vegetated campus interior.

2. **Avian Dawn Chorus Niche (`2.0–5.5 kHz`, Green Shaded Region — Solid Curves):**
   * At `06:00 IST`, **Site B Morning (solid blue)** and **Site C Morning (solid green)** rise sharply above their traffic baselines, forming broad, multi-peaked plateaus between **`-21 dB` and `-33 dB`** across `2.0–5.5 kHz` (with distinct vocal peaks near `2.4 kHz`, `3.7 kHz`, `4.2 kHz`, and `5.1 kHz`).
   * This elevated, multi-channel biological energy directly drives the high **Shannon Entropy (`0.82` and `0.78`)** and **ACI (`250.0` and `239.4`)** observed at dawn.

3. **Dusk Turnover: Insect Chorus vs. Forest Stillness (`2.0–8.5 kHz` — Dashed Curves):**
   * **Site B Evening (dashed blue)** exhibits **temporal & spectral niche turnover**: while mid-frequency bird calls (`2.0–4.5 kHz`) subside to `-44 dB`, a prominent **nocturnal cricket/cicada chorus** emerges between **`6.5–8.5 kHz`**, peaking at **`-23 dB` around `7.7 kHz`** and sustaining positive NDSI (`+0.17`).
   * **Site C Evening (dashed green)** exhibits **post-dusk ecological stillness**: once diurnal canopy birds roost at sunset, power across `2.0–4.5 kHz` drops to **`-50` to `-56 dB`** (the quietest noise floor on campus) without a loud high-frequency insect swarm—illustrating how a silent forest dusk yields a negative NDSI ratio (`-0.56`) despite having virtually zero traffic noise.

---

## 5. Key Conclusions

1. **Acoustic Refuge Recovery Along the Spatial Gradient:** Moving from the urban perimeter (**Site A**: `-0.86` Morning NDSI) into the vegetated campus interior (**Sites B & C**) produces a **`+1.36` surge in Morning NDSI** (`+0.51` and `+0.50`), alongside substantial gains in **ACI** (`223.2` $\to$ `250.0`) and **Spectral Entropy** (`0.57` $\to$ `0.82`), confirming active avian niche partitioning across $2.0\text{--}5.5\text{ kHz}$.
2. **Diurnal Species-Guild Turnover (Site B vs. Site C):**
   * **Site B** displays **bimodal diurnal partitioning**: birds dominate the $2.0\text{--}5.0\text{ kHz}$ band at dawn (`+0.51`), while stridulating insects occupy the $6.5\text{--}8.5\text{ kHz}$ band at dusk (`-23 dB` peak), maintaining positive biophonic dominance (`+0.17`) into the evening.
   * **Site C** operates as a **pure diurnal avian sanctuary**: strong dawn chorus activity (`+0.50`) gives way to deep post-dusk silence at `18:00` (`-56 dB` across $2\text{--}4\text{ kHz}$).
3. **Methodological Insight for NDSI in Ultra-Quiet Habitats:** Although `Site C Evening` has the lowest traffic power on campus (`-30` to `-46 dB` in $0.1\text{--}1.5\text{ kHz}$), its normalized NDSI evaluates to `-0.56` because diurnal birds have roosted ($B \to 0$) while a faint low-frequency background ambient floor remains. Pairing **NDSI with dB Power Spectral Density, ACI, and Entropy** prevents misclassifying a silent forest dusk as traffic-polluted.

---

## 6. Repository Structure & Quickstart

```text
NicheAcoustics/
├── assets/                   # Site GPS pins, habitat views, and 360° panoramas
├── data/
│   ├── raw/                  # 18 uncompressed 44.1 kHz mono .wav recordings
│   └── processed/            # ecoacoustic_summary.csv
├── outputs/
│   └── spectral_niches.png   # 3-day mean dB Power Spectral Density plot
├── main.py                   # STFT PSD, NDSI, ACI, Entropy & plotting pipeline
├── requirements.txt          # Python dependencies
└── README.md