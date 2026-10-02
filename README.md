# 📡 Galaxy 5G Modem & Band Master v2.0 (by hoc)

A dedicated, real-time cellular modem control panel, RF signal telemetry monitor, hardware band viewer, NR cell locker, and 5G NSA/SA architecture suite designed specifically for the **Samsung Galaxy M32 5G** (`SM-M326B` / MediaTek Dimensity 720 `MT6853`).

Author: **hoc**

---

## 🚀 Key Features in v2.0

### 1. 🔒 NR ARFCN & NR PCI Target Locking
- **Direct Target Locking**: Lock your device to a specific 5G carrier frequency (**NR-ARFCN**) and cell tower sector (**NR-PCI**).
- **Prevents Down-Banding**: Keeps the device locked to high-capacity 100 MHz C-Band carriers without dropping down to low-band coverage layers.
- **1-Click Presets for Indian Carriers**:
  - **Jio 5G n78 Fast (3500 MHz)**: `ARFCN: 634080` | `PCI: 155` (100 MHz channel)
  - **Jio 5G n28 Range (700 MHz)**: `ARFCN: 156510` (Low-band indoor penetration)
  - **Airtel 5G n78 C-Band**: `ARFCN: 627264` / `631000` (Airtel primary 5G carrier)
  - **Airtel 5G n3 Mid-Band**: `ARFCN: 361000` (1800 MHz FDD 5G)
  - **Vi 5G Trial n78**: `ARFCN: 623000` (Vodafone Idea 5G trial carrier)
- **Live Lock Telemetry**: Status badge indicates whether the active serving cell matches the target lock.
- **1-Click Clear**: Instant release button to return to automatic cell handover.
- **Samsung Official *#2263# Band Selection**: Direct shortcut launcher.

### 2. ⚡ 5G NSA (Option 3x) & SA (Option 2) Architecture Suite
- **⚡ SA Only (Jio 5G)**: Forces pure Standalone 5G (Option 2) connected directly to 5G Core (5GC).
- **📶 NSA Only (Airtel 5G)**: Enables Non-Standalone 5G (Option 3x) anchored to 4G LTE with ENDC aggregation. Required for Airtel 5G Plus.
- **🔄 Dual SA + NSA**: Universal mode enabling both Standalone and Non-Standalone simultaneously (ideal for Dual-SIM setups).
- **🚫 LTE Only**: Disables NR baseband transceivers to maximize battery savings in low-coverage areas.
- **Granular Toggles**:
  - `5G SA Mode` (`persist.vendor.radio.nr_sa_mode`)
  - `5G NSA Mode` (`persist.vendor.radio.nr_nsa_mode`)
  - `ENDC Dual Connectivity` (`persist.vendor.radio.endc_enabled`)
  - `LTE Carrier Aggregation` (`persist.vendor.radio.lte_ca_enabled`)

### 3. 🇮🇳 Indian Carrier Spectrum & Live Status Matrix
- Complete breakdown of 5G/4G spectrum allocations across Indian operators:
  - **Reliance Jio**: Pure SA (Option 2), Band n78 (100 MHz TDD) + Band n28 (700 MHz FDD).
  - **Bharti Airtel**: Pure NSA (Option 3x), Band n78 (100 MHz TDD) + Band n3/n8 (FDD) with LTE B1/B3/B8/B40 anchors.
  - **Vodafone Idea (Vi)**: NSA (Option 3x), Band n78 + B3/B1/B40 anchors.
  - **BSNL Mobile**: 4G LTE / 5G Ready rollout on Band 28 and Band 41.
- Live badge dynamically indicates active serving operator and carrier connection state.

### 4. 📡 Live RF Signal & Telemetry Monitor
- **Active Band Recognition**: Real-time display of serving carrier band (`n78`, `n77`, `n28`, `B1`, `B3`, `B5`, `B8`, `B40`, `B41`).
- **Carrier Channel Frequency**: Live NR-ARFCN and EARFCN tracking.
- **Channel Bandwidth**: Real-time bandwidth display (e.g. `100 MHz` ultra-wide 5G channel).
- **Cell Identifiers**: Physical Cell ID (PCI) and Tracking Area Code (TAC).
- **High-Precision RF Signal Metrics**:
  - **SS-RSRP** (Signal Power in dBm) with live color-coded meter.
  - **SS-RSRQ** (Signal Quality in dB).
  - **SS-SINR** (Signal-to-Interference-plus-Noise Ratio in dB).
  - **Signal Bars** (0–4 bars).

### 5. 📞 IMS & Telephony Suite
- **VoLTE (Voice over LTE)**: 1-click toggle with live IMS daemon tracking.
- **VoWiFi (Wi-Fi Calling)**: 1-click toggle with Wi-Fi preferred mode configuration.
- **VoNR (Voice over 5G NR)**: Low-latency native 5G voice calling toggle.
- **ViLTE (Video over LTE)**: Native carrier video calling toggle.
- **Data Roaming & Dual-SIM Smart Switch**: Quick toggles.

### 6. 🛡️ 100% Safe & Reversible
- **Zero Risk**: Systemless Magisk architecture; does not modify system partition or flash NVRAM.
- **1-Click Factory Revert**: Built-in "Revert Stock Defaults" button instantly clears all custom parameters and restores OEM Samsung defaults.

---

## 💻 Web Control Panel

The module runs an embedded web server on **Port 8092**:
- **From Magisk App**: Tap the **"Action"** button on the module card to open the dashboard directly in your browser.
- **On Phone Browser**: Navigate to `http://localhost:8092`
- **Via USB / ADB**:
  ```bash
  adb forward tcp:8092 tcp:8092
  ```
  Then open `http://localhost:8092` in your PC browser.

---

## 📦 Installation

1. Download the flashable module zip: `galaxy-modem-master-v2.0.zip`
2. Open the **Magisk App** -> **Modules** -> **Install from storage**.
3. Select `galaxy-modem-master-v2.0.zip` and flash.
4. Reboot your device.
5. Open `http://localhost:8092` or tap the **Action** button in Magisk to access the dashboard.
