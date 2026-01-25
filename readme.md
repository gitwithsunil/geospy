#  Geo-Spy : The Digital Footprint Hunter

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-red?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/OS-Kali%20Linux-lightgrey?style=for-the-badge&logo=kali-linux" alt="Kali Linux">
  <img src="https://img.shields.io/badge/Category-OSINT-blue?style=for-the-badge" alt="OSINT">
</p>

---

##  The "Silent Leak" Narrative
We live in an era of instant sharing. We take a photo, we post it, and we forget about it. But behind every pixel lies a hidden layer of **EXIF Metadata**. While you see a memory, a tracker sees a precise set of GPS coordinates leading straight to your doorstep.

**Geo-Spy** was engineered to reveal the invisible. It is a reconnaissance tool that hunts through your local image archives, extracts these "digital breadcrumbs," and visualizes your invisible footprint on a global, interactive map.

---

##  Features
- **Big Banner Interface:** A professional ASCII art welcome screen.
- **Deep Metadata Extraction:** Leverages `ExifTool` to pull precision decimal coordinates.
- **Automated Mapping:** Generates high-fidelity interactive maps using `Folium`.
- **Hybrid CLI/GUI:** Real-time terminal logs with automatic browser launch for results.
- **Recursive Scan:** Hunts through folders and sub-folders to find every hidden tag.

---

##  Arsenal Setup

### 1. System Engine (ExifTool)
Geo-Spy requires the industry-standard `ExifTool` binary.
```bash
# On Kali Linux / Debian
sudo apt update && sudo apt install libimage-exiftool-perl -y
