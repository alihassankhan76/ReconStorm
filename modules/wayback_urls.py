import os
import subprocess

def run_wayback(domain):
    print(f"[+] Collecting URLs from Wayback sources using gau on {domain}")
    output_dir = f"results/{domain}"
    os.makedirs(output_dir, exist_ok=True)
    output_file = f"{output_dir}/wayback_urls.txt"

    cmd = f"gau {domain} > {output_file}"
    subprocess.call(cmd, shell=True)

    print(f"[+] Wayback URLs saved to {output_file}")
