# Module 01 – Security Principles & Social Engineering

> **Status:** ✅ Completed | **Sessions:** 1st & 2nd online meetings | **Lab deadline:** Feb 22, 2026

---

## What This Module Covers

This module introduces the core principles of information security and explores how human behavior can be exploited through social engineering. It combines foundational security concepts with practical awareness of how attackers gather information and manipulate users.

---

## Key Concepts

- CIA Triad (Confidentiality, Integrity, Availability)
- Risk, Threats, and Vulnerabilities
- Security Awareness and Human Factors
- Social Engineering Techniques (phishing, pretexting, baiting)
- Data Integrity and Hashing Concepts
- Basic Cryptography (classical ciphers)

---

## Commands & Tools Used in Labs

- **Environment:** Kali Linux
- **Integrity Verification:** `diff`, `cmp`, `md5sum`
- **Cryptography (basic):** Python (Caesar Cipher, ROT13)
- **OSINT:** WHOIS, Maltego
- **Analysis tools:** Browser DevTools (URL inspection, link validation)

```bash
md5sum file.txt
```

---

## Lab Exercise Notes

Hands-on activities focused on understanding both technical and human aspects of security:

- Performed file comparison and integrity validation using hashing tools
- Developed a simple Caesar Cipher script `(/scripts/caesar_cipher.py)` to understand basic encryption concepts
- Explored OSINT techniques to identify publicly exposed information
- Analyzed phishing scenarios and suspicious URLs to recognize social engineering patterns  

⚠️ **Ethical Note:**
`All activities were conducted in a controlled, educational environment, focusing on methodology and awareness without exposing sensitive data or real exploitation techniques.`

---

## My QA → Cybersecurity Connection

In QA, I focused on validating system functionality and user flows.

This module expanded my perspective by showing that:

- Systems can be secure in code but vulnerable through user interaction
- Data integrity validation (e.g., hashing) is conceptually similar to verifying expected vs actual results
- Input handling is not only a functional concern, but also a security risk

It shifted my mindset from:
> *“Does it work correctly?”*  
to  
> *“How could this be manipulated or compromised?”*

---

## Things to Explore Further

- [ ] Advanced phishing detection and prevention techniques
- [ ] Security awareness program design
- [ ] Modern cryptography (AES, RSA) vs classical methods
- [ ] OSINT automation and intelligence correlation
- [ ] Human-centered security design

---

## References

The following resources were used to support the concepts explored in this module:

- [OWASP Social Engineering](https://owasp.org/www-community/attacks/Social_Engineering)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [SANS Security Awareness](https://www.sans.org/security-awareness-training/)
- [Maltego Documentation](https://docs.maltego.com/)
- [WHOIS Protocol (ICANN)](https://www.icann.org/resources/pages/whois-2018-01-26-en)
- [Google Phishing Quiz](https://phishingquiz.withgoogle.com/)  
