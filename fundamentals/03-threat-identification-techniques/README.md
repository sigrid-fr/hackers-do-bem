# Module 03 – Threat Identification Techniques

> **Status:** ✅ Completed | **Sessions:** 4th online meeting (Feb 09, 2026) | **Lab deadline:** Feb 22, 2026

---

## What This Module Covers

This module focuses on identifying potential threats through reconnaissance, traffic analysis, and infrastructure enumeration. It emphasizes how attackers discover vulnerabilities and how defenders can detect suspicious activity across systems and networks.

---

## Key Concepts

- Threat identification vs vulnerability assessment
- Active vs passive reconnaissance
- Indicators of compromise (IoCs)
- Network traffic analysis (OSI layers)
- DNS enumeration and exposure risks
- Defense in depth and active defense strategies
- Basic resilience and disaster recovery concepts (failover, redundancy)

---

## 💻 Commands & Tools Used in Labs

```bash
# Network scanning and service discovery
nmap -sV <target>
nmap -p- <target>

# DNS enumeration
nslookup <domain>
dig <domain>
host <domain>

# Network diagnostics
ping <target>
traceroute <target>
arp -a
ifconfig

# Listening and testing connections
nc -lvp <port>
nc <target> <port>

# Checking active connections
netstat -tulnp

```

---

**Tools & Technologies:**

- Kali Linux, Windows Server 2022
- Nmap, Searchsploit (Exploit-DB)
- Burp Suite (Proxy Intercept), Wireshark
- Netcat / Ncat
- PentBox (Honeypots)

---

## Lab Exercise Notes

**Objective:** Identify potential threats by analyzing network behavior, enumerating services, and correlating findings with known vulnerabilities (CVE database).

**Steps I followed:**
1. Set up a controlled environment using Kali Linux and Windows Server 2022 to simulate a target infrastructure.
2. Performed reconnaissance and service discovery using Nmap, identifying open ports and running services.
3. Cross-referenced identified services with known vulnerabilities using Searchsploit (Exploit-DB).
4. Conducted traffic analysis using Wireshark and Burp Suite to inspect network and application-layer communication.
5. Used Netcat to establish and test network connections, simulating attacker interaction scenarios.
6. Performed DNS enumeration (`dig`, `nslookup`, `host`) to identify exposed records (MX, TXT, CNAME) and potential misconfigurations.
7. Explored defensive strategies by simulating honeypot deployment with PentBox and reviewing redundancy concepts (hot, warm, cold sites).

**Findings / observations:**
- Identified open ports and services that could be mapped to known vulnerabilities via CVE databases
- Observed how network traffic can reveal sensitive patterns when not properly secured
- DNS records can expose internal structure or security configurations (e.g., SPF policies)
- Traffic interception tools (Burp, Wireshark) provide deep visibility into communication flows
- Honeypots can be used to detect and study attacker behavior proactively
- Combining reconnaissance, traffic analysis, and threat intelligence provides a more complete threat picture

---

## My QA → Cybersecurity Connection

In QA, I focused on validating system behavior and API communication.
This module expanded that perspective by showing that:
- Network behavior itself can indicate security risks
- Analyzing requests/responses (similar to API testing) is critical for detecting anomalies
- Identifying misconfigurations is as important as finding functional bugs

It shifted my mindset from:

> *“Is the system responding correctly?”*
to
> *“What hidden risks can be identified from this behavior?”*


---

## Things to Explore Further

- [ ] Practice advanced Nmap scanning techniques (scripts, stealth scans)
- [ ] Study MITRE ATT&CK techniques related to reconnaissance and discovery
- [ ] Explore Wireshark filters for detecting suspicious traffic patterns
- [ ] Learn how SIEM tools correlate logs and network data for threat detection
- [ ] Practice building simple honeypots and analyzing collected data

---

## References

- [MITRE ATT&CK Framework](https://attack.mitre.org/) — map adversary techniques to reconnaissance and discovery behaviors  
- [Exploit Database (Searchsploit)](https://www.exploit-db.com/) — vulnerability and exploit reference  
- [Wireshark Documentation](https://www.wireshark.org/docs/) — network traffic analysis  
- [Nmap Documentation](https://nmap.org/docs.html) — network scanning and enumeration  
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) — web and network testing methodology  
