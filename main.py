import argparse
import os
from modules import subdomains, dns_info, ports, wayback_urls, related_domains

def create_summary(domain):
    summary_path = f"results/{domain}/recon_summary.txt"
    with open(summary_path, "w") as summary:
        for file_name in [
            "subdomains.txt",
            "dns_info.txt",
            "open_ports.txt",
            "wayback_urls.txt",
            "related_domains.txt"
        ]:
            file_path = f"results/{domain}/{file_name}"
            summary.write(f"\n\n===== {file_name} =====\n")
            if os.path.exists(file_path):
                with open(file_path, "r") as f:
                    summary.write(f.read())
            else:
                summary.write("No data found.")

def main():
    parser = argparse.ArgumentParser(description="ReconStorm - Modular Recon Tool")
    parser.add_argument("--target", required=True, help="Target domain")
    parser.add_argument("--subdomains", action="store_true", help="Run subdomain scan")
    parser.add_argument("--dns", action="store_true", help="Run DNS recon")
    parser.add_argument("--ports", action="store_true", help="Run port scan with Naabu")
    parser.add_argument("--wayback", action="store_true", help="Collect Wayback URLs using gau")
    parser.add_argument("--related", action="store_true", help="Discover related domains via Amass Intel")
    parser.add_argument("--all", action="store_true", help="Run all modules and generate summary")

    args = parser.parse_args()

    if args.all:
        subdomains.run_subdomains(args.target)
        dns_info.run_dns(args.target)
        ports.run_ports(args.target)
        wayback_urls.run_wayback(args.target)
        related_domains.run_related(args.target)
        create_summary(args.target)
    else:
        if args.subdomains:
            subdomains.run_subdomains(args.target)
        if args.dns:
            dns_info.run_dns(args.target)
        if args.ports:
            ports.run_ports(args.target)
        if args.wayback:
            wayback_urls.run_wayback(args.target)
        if args.related:
            related_domains.run_related(args.target)

if __name__ == "__main__":
    main()

