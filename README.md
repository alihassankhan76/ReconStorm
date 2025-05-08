# ReconStorm 🔍

**Modular Recon Tool for Bug Bounty Hunters & Security Researchers**  
Built with Python, Go-based tools, and real-world recon workflows.

---

## Features

- 🔍 Subdomain Enumeration via `subfinder`
- 🧠 DNS Recon using `dnsrecon`
- ⚡ Fast Port Scanning with `naabu`
- 🕵️ Wayback URL Collection using `gau`
- 🌐 Related Domains Finder via `amass intel`
- ✅ `--all` flag to run everything
- 📄 Outputs organized by domain
- 🧾 Auto-generated `recon_summary.txt` file for consolidated results

---

## Installation

Install these tools before running:

```bash
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest
go install -v github.com/lc/gau@latest
sudo apt install amass dnsrecon -y
