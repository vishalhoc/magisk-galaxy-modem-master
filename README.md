# 📡 Galaxy 5G Modem & Band Master v3.0 (by hoc)

A professional-grade, multi-tab cellular modem engineering console, RF signal telemetry dashboard (Cellular-Pro & Network Signal Guru style), multi-ARFCN & multi-PCI target locker, 3GPP 4G/5G carrier aggregation & EN-DC matrix, and baseband/kernel/ROM parameter customizer designed specifically for the **Samsung Galaxy M32 5G** (`SM-M326B` / MediaTek Dimensity 720 `MT6853`).

Author: **hoc**

---

## 🚀 Key Features in v3.0

### 1. 📊 Tab 1: Real-Time Cellular-Pro / NSG Diagnostic Dashboard
- **Serving Cell Cockpit**: Live display of active network type (5G SA / 5G NSA / LTE+ / LTE), PLMN operator, primary band (`n78`, `n77`, `n28`, `B1`, `B3`, `B5`, `B8`, `B40`, `B41`), channel bandwidth (`100 MHz`, `20 MHz`, etc.), NR-ARFCN / EARFCN, Physical Cell ID (PCI), Tracking Area Code (TAC), and 5G New Radio Cell Identity (NCI).
- **High-Precision RF Signal Meters**:
  - **SS-RSRP** (Reference Signal Received Power in dBm) with dynamic color gradient.
  - **SS-RSRQ** (Reference Signal Received Quality in dB).
  - **SS-SINR** (Signal-to-Interference-plus-Noise Ratio in dB).
  - **RSSI** (Received Signal Strength Indicator in dBm).
- **Carrier Aggregation (CA) & Component Carrier Matrix**:
  - Live CA indicator badge (`ACTIVE (CA)` vs `INACTIVE (Single Carrier)`).
  - Component Carrier grid breaking down PCC (Primary Component Carrier) and up to 2 SCCs (Secondary Component Carriers) with frequency, bandwidth, and MIMO stream details.
- **Cellular Bearers & IMS State**: Real-time status tags for VoLTE, VoWiFi, ViLTE, VoNR, 5G SA Core, and EN-DC dual connectivity.

---

### 2. 🎛️ Tab 2: Cell, ARFCN, PCI & Multi-Band Locker
- **Multi-ARFCN & Multi-PCI Target Whitelist Locking**:
  - **Can we lock multiple ARFCN and PCI simultaneously?** **YES!** In 3GPP specifications, baseband transceivers support a candidate target cell whitelist. You can define multiple `ARFCN:PCI` candidate pairs (e.g. 3-sector cluster on n78 or n78 primary with n28 fallback), preventing unwanted handovers to distant or degraded towers.
  - Add, manage, and delete custom target cell candidates dynamically.
  - 1-Click candidate presets for Indian carriers (Jio n78 100MHz Sector 155, Jio n78 Sector 156, Jio n28 700MHz, Airtel n78 C-Band, Airtel n3 Mid-Band, Vi n78 Trial).
- **3GPP-Standard Band Locking (Whitelist Mask)**:
  - **4G LTE Band Whitelist Matrix**: B1 (2100), B3 (1800), B5 (850), B8 (900), B28 (700), B40 (2300 TDD), B41 (2500 TDD).
  - **5G NR Band Whitelist Matrix**: n1 (2100), n3 (1800), n5 (850), n8 (900), n20 (800), n28 (700), n38 (2600), n40 (2300), n41 (2500), n77 (3700), n78 (3500).
- **1-Tap Carrier Aggregation (CA) & EN-DC Combos**:
  - 📶 **LTE 2CA / 3CA (4G+)**:
    - `B3 + B40` (Up to 40 MHz)
    - `B1 + B3 + B40` (Up to 60 MHz)
    - `B3 + B40 + B41` (Up to 60 MHz, 3 carriers, PCC + 2 SCCs)
  - ⚡ **5G NR-CA (5G+5G SA)**:
    - `n28 + n78` (Up to 110 MHz, 2 carriers, 5G Next-Gen Core)
    - `n78 + n78` (Up to 110 MHz, 2 contiguous/inter-band carriers)
  - 🚀 **4G + 5G EN-DC Dual Connectivity**:
    - `B3[20MHz] + B40[20MHz] + n78[100MHz]` (Up to 140 MHz aggregate bandwidth bonding LTE anchors with 100 MHz 5G carrier simultaneously!)
  - 🇮🇳 **Indian Operator Quick Combos**: Jio 5G Max Speed, Airtel 5G Aggregation, Pure 5G Dual-Band SA.
- **1-Click Clear / Restore**: Instant release back to OEM full auto-band roaming and cell selection.

---

### 3. ⚙️ Tab 3: Modem, Kernel & ROM Tweaker
- **Modem & Radio Transceiver Tweaks**:
  - Standalone (SA) / Non-Standalone (NSA) mode toggles.
  - EN-DC Dual Connectivity & LTE Carrier Aggregation forcing.
  - NR CA Max Component Carriers (1 CC or 2 CC).
  - LTE CA Max Component Carriers (2 CC, 3 CC, 4 CC).
  - 256-QAM Downlink Boost (`persist.vendor.radio.nr_256qam`).
  - Uplink MIMO & Rank 2 Transmission (`persist.vendor.radio.nr_ul_mimo`, `nr_ul_rank`).
  - 4Rx Diversity & 4-Layer Beamforming (`persist.vendor.radio.nr_dl_4rx`, `nr_rx_diversity`).
  - Connected Mode DRX (`persist.vendor.radio.nr_cdrx_enable`).
- **Linux Kernel Network Stack Tuning**:
  - TCP Congestion Control Algorithm (`cubic`, `bic`, `reno`).
  - TCP Window Scaling (`/proc/sys/net/ipv4/tcp_window_scaling`).
  - TCP Fast Open (`/proc/sys/net/ipv4/tcp_fastopen`).
  - IP Forwarding (`/proc/sys/net/ipv4/ip_forward`).
  - Cellular Interface MTU (`rmnet0` 1500 / 1420 bytes).
- **Samsung ROM & Telephony Settings**:
  - Preferred Network Mode bitmask (NR/LTE/WCDMA/GSM, NR/LTE, LTE only).
  - Samsung IMS switches: VoLTE, ViLTE, VoNR, VoWiFi, SMS over IP, RCS.
  - Wi-Fi Calling Preference (Wi-Fi Preferred vs Cellular Preferred).
  - Global Data Roaming.

---

### 4. 🛠️ Tab 4: Samsung Secret Tools & Spectrum Reference
- **ServiceMode & Secret Menu Launchers**:
  - Hardware Band Selection (`*#2263#`).
  - Main ServiceMode (`*#0011#`).
  - MediaTek EngineerMode launcher.
- **Complete Indian Carrier Spectrum Allocation Guide**:
  - Reliance Jio, Bharti Airtel, Vodafone Idea, and BSNL frequency bands, duplex modes, and channel bandwidths.

---

## 💻 Web Engineering Console

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

1. Download the flashable module zip: `galaxy-modem-master-v3.0.zip`
2. Open the **Magisk App** -> **Modules** -> **Install from storage**.
3. Select `galaxy-modem-master-v3.0.zip` and flash.
4. Reboot your device.
5. Open `http://localhost:8092` or tap the **Action** button in Magisk to access the dashboard.
