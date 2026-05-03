# Module 06 – Web Security & Secure Development

> **Status:** ✅ Completed | **Sessions:** 11st & 12nd online meeting (Mar 2 e 6) | **Lab deadline:** Mar 13, 2026

---

## What This Module Covers

This module focuses on web application security, secure development practices, and automation. It explores common vulnerabilities from the OWASP Top 10, secure coding environments, and how security integrates into the Software Development Life Cycle (SDLC).

---

## Key Concepts

- Secure Software Development Life Cycle (SDLC)  
- OWASP Top 10 vulnerabilities  
- Input validation and encoding (e.g., URL/Percent Encoding)  
- SQL Injection (SQLi)  
- Clickjacking (UI Redressing)  
- Secure API usage and automation  
- Vulnerability research (CVE, NVD)  
- Defensive tools and malware detection  

---

## Commands & Tools Used in Labs

```bash
# SQL Injection testing (automated)
sqlmap -u "http://target.com/page?id=1" --dbs

# URL encoding example
curl "http://target.com/page?param=%27%20OR%201%3D1--"

# Generate QR Code from terminal
qrencode -o output.png "https://example.com"

# Scan system for malware
clamscan -r /

# Extract system information (Linux)
uname -a
```

**Tools & Technologies:**

- Kali Linux, Windows Server 2022  
- SQLmap, ClamAV, Curl, Qrencode  
- Apache NetBeans, OpenJDK  
- Python (Pillow), PowerShell  

**Languages:**
- Python, PowerShell, Java, SQL, HTML/CSS  

**Security Frameworks:**
- OWASP, NVD, CVE Details  

---

## Lab Exercise Notes

**Objective:** Identify and exploit common web vulnerabilities, understand secure development practices, and apply automation techniques to support security analysis.

---

### Steps I followed

1. Set up a secure development environment using OpenJDK and Apache NetBeans on Linux.

2. Performed vulnerability research using CVE databases (NVD, CVE Details), analyzing cases such as CVE-2017-12099 (Integer Overflow).

3. Conducted web security testing:
   - Used SQLmap to identify and exploit SQL Injection vulnerabilities  
   - Tested authentication bypass scenarios  
   - Analyzed HTTP requests and applied URL encoding techniques  

4. Simulated client-side attacks:
   - Created Clickjacking proof-of-concept using invisible <iframe> layers  
   - Analyzed security headers such as X-Frame-Options and Content-Security-Policy  

5. Developed automation scripts:
   - Python scripts using Pillow (PIL) for image processing  
   - PowerShell scripts for:
     - Event log extraction (Event IDs 6005/6006)  
     - Hardware inventory via CIM  

6. Integrated tools and APIs:
   - Automated URL shortening  
   - Generated QR codes via terminal tools  

7. Applied defensive techniques:
   - Used ClamAV for malware detection  
   - Analyzed signature-based detection using sigtool  

---

### Findings / Observations

- SQL Injection remains a critical vulnerability when input validation is not properly enforced  
- Security headers play a key role in preventing client-side attacks like clickjacking  
- Automation improves efficiency in both offensive testing and defensive monitoring  
- Vulnerabilities in third-party libraries (CVE) can introduce serious risks if not managed  
- Secure development environments reduce exposure to misconfigurations and unsafe dependencies  
- Combining offensive and defensive tools provides a more complete understanding of web security  

---

## My QA → Cybersecurity Connection

In QA, I tested web applications focusing on functionality and user flows.

This module helped me understand:

- how common vulnerabilities are introduced during development  
- how input handling can be exploited beyond functional edge cases  
- how automation (which I already use in testing) can be applied to security validation  

It shifted my mindset from:

> “Does the feature work as expected?”  
to  
> “Can this feature be exploited or abused?”

---

## Things to Explore Further

- [ ] Practice manual testing with Burp Suite (beyond automated tools like SQLmap)  
- [ ] Study OWASP Top 10 in depth with real-world examples  
- [ ] Learn secure coding practices in Java and JavaScript  
- [ ] Explore API security testing (authentication, rate limiting, injection)  
- [ ] Integrate security checks into CI/CD pipelines  

---

## References

- [OWASP Top 10](https://owasp.org/www-project-top-ten) — most critical web application security risks
- [National Vulnerability Database (NVD)](https://nvd.nist.gov) — vulnerability research
- [CVE Details](https://www.cvedetails.com) — CVE database and analysis
- [SQLmap Documentation](https://sqlmap.org) — automated SQL injection testing tool
- [ClamAV Documentation](https://docs.clamav.net) — antivirus and malware detection
