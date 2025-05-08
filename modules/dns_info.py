import os
import subprocess

def run_dns(domain):
    print(f"[+] Running DNSRecon on {domain}")
    output_dir = f"results/{domain}"
    os.makedirs(output_dir, exist_ok=True)
    output_file = f"{output_dir}/dns_info.txt"

    cmd = f"dnsrecon -d {domain} -t std > {output_file}"
    subprocess.call(cmd, shell=True)

    print(f"[+] DNS info saved to {output_file}")
