# 🔍 ReconStorm

**Modular Reconnaissance Automation Framework**  
Built for bug bounty hunters & security researchers.  
Perform deep recon on any domain with a single command.

---

## 🚀 Features

- ✅ Subdomain Enumeration (`subfinder`)
- ✅ DNS Reconnaissance (`dnsrecon`)
- ✅ Port Scanning (`naabu`)
- ✅ Wayback URL Collection (`gau`)
- ✅ JavaScript File Analysis (for endpoints and secrets)
- ✅ URL Parameter Discovery
- ✅ Directory Bruteforcing (`ffuf`)
- ✅ Tech Stack Detection (`httpx`)
- ✅ Related Domain Enumeration (`amass intel`)
- ✅ Auto Markdown Report Generation (`recon_report.md`)

---

## 📦 Installation

```bash
git clone https://github.com/alihassankhan76/ReconStorm.git
cd ReconStorm
````

### ⚙️ Install Dependencies

```bash
# Go-based tools
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install -v github.com/lc/gau@latest

# Apt-based tools
sudo apt install dnsrecon amass ffuf -y
```

---

## 💡 Usage

Run all modules on a target:

```bash
python3 main.py --target example.com --all
```

Or run individual modules:

```bash
python3 main.py --target example.com --subdomains
python3 main.py --target example.com --js
python3 main.py --target example.com --report
```

---

## 📁 Output Directory Structure

```
results/example.com/
├── subdomains.txt
├── dns_info.txt
├── open_ports.txt
├── wayback_urls.txt
├── js_endpoints.txt
├── secrets.txt
├── discovered_params.txt
├── dirs_found.txt
├── tech_stack.txt
├── related_domains.txt
└── recon_report.md
```

---

## 🧠 Author

Developed by [Ali Hassan Khan](https://github.com/alihassankhan76)
Bug Bounty Hunter | Security Automation Enthusiast

