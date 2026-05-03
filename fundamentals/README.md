# Hackers do Bem – Fundamentals

> **Fundamentals** of the Hackers do Bem program (ESR / RNP) — **completed ✅**
> 96-hour synchronous course covering core cybersecurity domains through theory, labs, and hands-on exercises.
> **Duration:** 9 weeks | **Format:** Live online classes + async labs | **Modules:** 12

---

## Why This Level Matters for My Career Transition

The Fundamental level is where the QA → Cybersecurity transition became real for me. This course forced me to go beyond understanding *what* vulnerabilities are and start thinking about *how* to find, exploit, and defend against them — in controlled, hands-on environments.

| What I Brought from QA | What I Gained at Fundamental Level |
|------------------------|-----------------------------------|
| Structured thinking & test planning | Threat modeling & attack scenario design |
| API & web testing experience | Web security, auth bypass, and secure design |
| Bug documentation & reproduction steps | Vulnerability writeups & incident reporting |
| Understanding system behavior | Recognizing abnormal behavior as a security signal |
| Working in CI/CD pipelines | Secure architecture and development practices |

---

## Course Timeline

| Period | Activity |
|--------|----------|
| Feb 02 – Feb 22, 2026 | Modules 1, 2 & 3 — labs open |
| Feb 09 – Feb 22, 2026 | Module 3 — labs open |
| Feb 16–18, 2026 | 🎉 Carnival recess |
| Feb 16 – Feb 27, 2026 | Module 4 — labs open |
| Feb 23 – Mar 06, 2026 | Module 5 — labs open |
| Mar 02 – Mar 13, 2026 | Modules 6 & 7 — labs open |
| Mar 09 – Mar 20, 2026 | Module 8 — labs open |
| Mar 16 – Mar 27, 2026 | Modules 9 & 10 — labs open |
| Mar 23 – Apr 03, 2026 | Module 11 — labs open |
| Mar 30 – Apr 03, 2026 | Module 12 — labs open |
| Apr 05, 2026 | 🏁 Last day — Final Exam + Course ends |

---

## Repository Structure

```
fundamentals/
│
├── README.md                              ← You are here
│
├── 01-security-principles-and-social-engineering/
│   └── README.md
├── 02-threats-malware-and-controls/
│   └── README.md
├── 03-threat-identification-techniques/
│   └── README.md
├── 04-access-controls/
│   └── README.md
├── 05-identity-and-account-management/
│   └── README.md
├── 06-web-security-and-secure-development/
│   └── README.md
├── 07-redundancy-backup-physical-security-and-data-destruction/
│   └── README.md
├── 08-cryptography-concepts/
│   └── README.md
├── 09-public-key-infrastructure-and-blockchain/
│   └── README.md
├── 10-host-security/
│   └── README.md
├── 11-secure-networking-and-security-devices/
│   └── README.md
└── 12-incident-response-and-secure-protocols/
│   └── README.md
└── fundamentals-certificate.pdf                       
```

---

## Module Overview

### [Module 01 – Security Principles & Social Engineering](../fundamentals/01-security-principles-and-social-engineering)
**Sessions:** 1st & 2nd online meetings (Feb 2 & 4) | Labs: Feb 02 – Feb 22

Core topic: Foundations of information security and human-centered attacks.

**Key concepts:** CIA triad, risk, security policies, phishing, pretexting, social engineering techniques.

**My QA connection:** In QA, I focused on system behavior; here I learned that humans are often the weakest link. Security isn’t just technical — it’s behavioral.

---

### [Module 02 – Threats, Malware & Controls](../fundamentals/02-threats-malware-and-controls)
**Sessions:** 3rd & 4th online meeting (Feb 6 & 9) | Labs: Feb 02 – Feb 22

Core topic: Types of threats and how defensive controls mitigate them.

**Key concepts:** malware types (ransomware, trojans, spyware), threat landscape, preventive/detective/corrective controls.

**My QA connection:** Similar to validating edge cases in QA, here I learned to think about how systems fail under malicious conditions.

---

### [Module 03 – Threat Identification Techniques](../fundamentals/03-threat-identification-techniques)
**Sessions:** 5th & 6th online meeting (Feb 11 & 13) | Labs: Feb 09 – Feb 22

Core topic: Methods for identifying and analyzing threats.

**Key concepts:** threat modeling, indicators of compromise (IoCs), logs, monitoring, basic analysis techniques.

**My QA connection:** Just like debugging in QA, this involves investigating signals and narrowing down root causes — but with a security mindset.

---

### [Module 04 – Access Controls](../fundamentals/04-access-controls)
**Sessions:** 7th & 8th online meeting (Feb 20 & 23) | Labs: Feb 16 – Mar 1

Core topic: Mechanisms to control who can access what.

**Key concepts:** authentication vs authorization, RBAC, least privilege, multi-factor authentication (MFA).

**My QA connection:** In QA I test permissions and roles — here I understood the principles behind designing secure access systems.

---

### [Module 05 – Identity & Account Management](../fundamentals/05-identity-and-account-management)
**Sessions:**  9th & 10th online meeting (Feb 25 & 27) | Labs: Feb 23 – Mar 6

Core topic: Managing digital identities securely.

**Key concepts:** IAM, account lifecycle, identity verification, provisioning/deprovisioning.

**My QA connection:** Similar to validating user flows in QA, but focused on identity integrity and preventing unauthorized access.

---

### [Module 06 – Web Security & Secure Development](../fundamentals/06-web-security-and-secure-development)
**Sessions:** 11st & 12nd online meetings (Mar 2 & 6) | Labs: Mar 2 – Mar 13

Core topic: Securing web applications and adopting secure coding practices.

**Key concepts:** OWASP Top 10, input validation, XSS, SQL injection, secure SDLC.

**My QA connection:** Strong overlap — I already test web apps; now I understand how vulnerabilities are introduced and how to prevent them earlier.

---

### [Module 07 – Backup, Redundancy & Physical Security](../fundamentals/07-redundancy-backup-physical-security-and-data-destruction)
**Sessions:** 13rd & 14th online meetings (Mar 9 & 10) | Labs: Mar 02 – Mar 13

Core topic: Ensuring availability and protecting physical assets.

**Key concepts:** backup strategies, redundancy, disaster recovery, physical access control.

**My QA connection:** In QA we validate system reliability; here I learned how systems stay resilient even after failures or attacks.

---

### [Module 08 – Cryptography Concepts](../fundamentals/08-cryptography-concepts)
**Sessions:** 15th & 16th online meeting (Mar 11 & 13) | Labs: Mar 09 – Mar 20

Core topic: Protecting data through encryption.

**Key concepts:** symmetric/asymmetric encryption, hashing, digital signatures.

**My QA connection:** I used to validate encrypted flows without understanding them — now I know how data is actually protected.

---

### [Module 09 – Public Key Infrastructure & Blockchain](../fundamentals/09-public-key-infrastructure-and-blockchain)
**Sessions:** 17th & 18th online meetings (Mar 16 & 19) | Labs: Mar 16 – Mar 27

Core topic: Trust models and decentralized security.

**Key concepts:** PKI, certificates, certificate authorities, blockchain basics.

**My QA connection:** Similar to validating secure connections (HTTPS), but now I understand what happens behind the scenes.

---

### [Module 10 – Host Security](../fundamentals/10-host-security)
**Sessions:** 19th & 20th online meetings (Mar 20 & 23) | Labs: Mar 16 – Mar 27

Core topic: Securing individual machines and operating systems.

**Key concepts:** hardening, patching, endpoint protection, system monitoring.

**My QA connection:** Like testing environments in QA, but focused on securing the host against attacks and misconfigurations.

---

### [Module 11 – Secure Networking & Security Devices](../fundamentals/11-secure-networking-and-security-devices)
**Sessions:** 21st & 22nd online meetings (Mar 25 & 27) | Labs: Mar 23 – Apr 03

Core topic: Protecting network infrastructure.

**Key concepts:** firewalls, IDS/IPS, VPNs, network segmentation.

**My QA connection:** I used to focus on API/network behavior — now I understand how traffic is controlled and protected.

---

### [Module 12 – Incident Response & Secure Protocols](../fundamentals/12-incident-response-and-secure-protocols)
**Sessions:** 23rd & 24th online meetings (Mar 30 & Apr 1) | Labs: Mar 23 – Apr 05

Core topic: Responding to security incidents and using secure communication protocols.

**Key concepts:** incident lifecycle, containment, recovery, HTTPS, TLS.

**My QA connection:** Similar to handling production bugs — but with structured response processes and security impact in mind.

---

## Labs — Hands-on Exercises

> Each module included virtual lab exercises applying concepts in controlled environments. Notes and key commands are documented in each module folder.

| Lab | Module | Topic | Completed |
|-----|--------|-------|-----------|
| Lab 01 | M1 | Social engineering analysis & phishing detection techniques | ✅ |
| Lab 02 | M2 | Malware identification & basic threat classification | ✅ |
| Lab 03 | M3 | Threat identification using logs & IoCs | ✅ |
| Lab 04 | M4 | Access control testing (RBAC & least privilege scenarios) | ✅ |
| Lab 05 | M5 | Identity lifecycle & account management simulation | ✅ |
| Lab 06 | M6 | OWASP vulnerabilities testing (XSS, SQLi) & secure coding fixes | ✅ |
| Lab 07 | M7 | Backup & disaster recovery planning exercise | ✅ |
| Lab 08 | M8 | Cryptography practice (encryption, hashing, signatures) | ✅ |
| Lab 09 | M9 | PKI basics & certificate validation | ✅ |
| Lab 10 | M10 | Host security hardening (Linux/Windows baseline) | ✅ |
| Lab 11 | M11 | Network security analysis (firewalls, segmentation) | ✅ |
| Lab 12 | M12 | Incident response simulation & secure protocols usage | ✅ |

---

## Tools Used Throughout the Course

| Tool | Purpose |
|------|---------|
| **Nmap** | Network scanning & enumeration |
| **Wireshark** | Packet capture & protocol analysis |
| **Burp Suite** | Web application security testing |
| **Kali Linux** | Attack & lab environment |
| **OpenSSL** | Cryptography hands-on practice |
| **OSINT tools** | Reconnaissance & information gathering |
| **SIEM (basics)** | Log analysis & threat detection |

---

## Outcome

- ✅ **96 hours** of live synchronous training completed
- ✅ **12 modules** covering the full cybersecurity domain
- ✅ All lab exercises submitted on time
- ✅ Final assessment completed (Apr 05, 2026)
- ✅ **Progressed to the Specialized Level — DevSecOps track**

---

## What's in This Repository

Each module folder contains:
- `README.md` — summary of what was covered, key takeaways, and QA connection

> This documentation was written *during* the course to reinforce learning and build a public record of what I know — not just that I attended.

---

*Fundamental level completed: April 2026 | Next: [DevSecOps Specialization →](../devsecops-specialization/)*  
