import os
import subprocess

def run_related(domain):
    print(f"[+] Gathering related domains using Amass Intel on {domain}")
    output_dir = f"results/{domain}"
    os.makedirs(output_dir, exist_ok=True)
    output_file = f"{output_dir}/related_domains.txt"

    cmd = f"amass intel -d {domain} -whois > {output_file}"
    subprocess.call(cmd, shell=True)

    print(f"[+] Related domains saved to {output_file}")

