#!/usr/bin/env python3
import os
import subprocess
import folium
import webbrowser
from colorama import Fore, init

# Initialize colors for the terminal
init(autoreset=True)

def get_gps_data(image_path):
    """Extracts GPS decimal coordinates using ExifTool."""
    try:
        # -n: decimal output, -S: short tag names
        cmd = ["exiftool", "-gpslatitude", "-gpslongitude", "-n", "-S", image_path]
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode()
        
        coords = {}
        for line in output.splitlines():
            if ":" in line:
                key, val = line.split(":", 1)
                coords[key.strip()] = float(val.strip())
        
        if "GPSLatitude" in coords and "GPSLongitude" in coords:
            return [coords["GPSLatitude"], coords["GPSLongitude"]]
    except Exception:
        return None
    return None

def main():
    print(Fore.CYAN + "="*50)
    print(Fore.CYAN + "       GEO-SPY: OSINT METADATA MAPPER        ")
    print(Fore.CYAN + "="*50 + "\n")

    target_dir = input(Fore.WHITE + "Enter folder path to scan (or press Enter for current): ") or "."
    
    # Initialize Map
    m = folium.Map(location=[20, 0], zoom_start=2, tiles="OpenStreetMap")
    found_count = 0

    print(Fore.YELLOW + f"[*] Scanning images in: {os.path.abspath(target_dir)}...\n")

    for file in os.listdir(target_dir):
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            path = os.path.join(target_dir, file)
            gps = get_gps_data(path)
            
            if gps:
                print(Fore.GREEN + f"[+] SUCCESS: {file} -> {gps}")
                folium.Marker(
                    location=gps, 
                    popup=f"File: {file}", 
                    icon=folium.Icon(color='red', icon='screenshot')
                ).add_to(m)
                found_count += 1
            else:
                print(Fore.RED + f"[-] NO GPS:  {file}")

    if found_count > 0:
        output_file = "map_results.html"
        m.save(output_file)
        full_path = "file://" + os.path.abspath(output_file)
        print(Fore.CYAN + f"\n[!] Done! {found_count} points mapped. Opening results...")
        webbrowser.open(full_path)
    else:
        print(Fore.RED + "\n[!] No GPS data found. Try images taken with a smartphone.")

if __name__ == "__main__":
    main()