import os
import subprocess

def run_subdomains(domain):
    print(f"[+] Running Subfinder on {domain}")
    output_dir = f"results/{domain}"
    os.makedirs(output_dir, exist_ok=True)
    output_file = f"{output_dir}/subdomains.txt"
    
    cmd = f"subfinder -d {domain} -silent > {output_file}"
    subprocess.call(cmd, shell=True)

    print(f"[+] Subdomains saved to {output_file}")

