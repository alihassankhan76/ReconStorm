import os
import subprocess

def run_ports(domain):
    print(f"[+] Running Naabu Port Scan on {domain}")
    output_dir = f"results/{domain}"
    os.makedirs(output_dir, exist_ok=True)
    output_file = f"{output_dir}/open_ports.txt"

    cmd = f"naabu -host {domain} -silent > {output_file}"
    subprocess.call(cmd, shell=True)

    print(f"[+] Open ports saved to {output_file}")

