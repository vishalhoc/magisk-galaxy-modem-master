# 📡 Galaxy 5G Modem & Band Master (SM-M326B)

A dedicated, real-time cellular modem control panel, RF signal telemetry monitor, hardware band viewer, and network mode locker designed specifically for the **Samsung Galaxy M32 5G** (`SM-M326B` / MediaTek Dimensity 720 `MT6853`).

---

## 🚀 Key Features

### 1. 📡 Live 5G NR & 4G LTE Telemetry
- **Active Band Recognition**: Real-time display of serving carrier band (e.g. `n78` / `n77` 3.5GHz C-band, `n28` 700MHz low-band, `B1`, `B3`, `B5`, `B8`, `B40`, `B41`).
- **Carrier Channel Frequency**: Live NR-ARFCN and EARFCN tracking.
- **Channel Bandwidth**: Real-time bandwidth display (e.g. `100 MHz` ultra-wide 5G channel).
- **Cell Identifiers**: Physical Cell ID (PCI) and Tracking Area Code (TAC).
- **High-Precision RF Signal Metrics**:
  - **SS-RSRP** (Signal Power in dBm) with live color-coded meter.
  - **SS-RSRQ** (Signal Quality in dB).
  - **SS-SINR** (Signal-to-Interference-plus-Noise Ratio in dB).
  - **Signal Bars** (0–4 bars).

### 2. 📋 Complete Hardware Certified Bands Directory
- Full visual matrix of all **12 certified 5G NR bands**:
  - `n1, n3, n5, n7, n8, n20, n28, n38, n40, n41, n77, n78`
- Full visual matrix of all **15 certified 4G LTE bands**:
  - `B1, B2, B3, B4, B5, B7, B8, B12, B17, B20, B26, B28, B38, B40, B41, B66`
- Active serving band is dynamically highlighted with a glowing green badge in real-time.

### 3. 🔒 1-Click Network Mode Locker
- **⚡ Force 5G Only (NR Only - Pure Standalone)**: Locks modem strictly to 5G SA; completely prevents random drops to 4G LTE in fringe coverage!
- **🚀 Force 5G / 4G (NR / LTE)**: Disables legacy 2G/3G fallbacks.
- **📶 Force 4G Only (LTE Only)**: Locks modem strictly to 4G LTE.
- **🔄 Auto 5G / 4G / 3G / 2G**: Restores Samsung factory default auto-selection.

### 4. 📞 VoLTE & VoWiFi Controller
- **VoLTE (Voice over LTE / VoNR)**: 1-click toggle with live IMS daemon (`imsd`) status tracking.
- **VoWiFi (Wi-Fi Calling)**: 1-click toggle with Wi-Fi preferred mode configuration.

### 5. 🛠️ Direct Samsung Native Tool Launchers
- **Launch ServiceMode (*#0011#)**: Direct trigger to open Samsung's native engineering screen.
- **Launch Band Selection (*#2263#)**: Direct trigger to open Samsung's native band selection interface.

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
