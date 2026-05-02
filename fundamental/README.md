# 🔐 Hackers do Bem – Fundamental Level

> **Fundamental level** of the Hackers do Bem program (ESR / RNP) — **completed ✅**
> 96-hour synchronous course covering core cybersecurity domains through theory, labs, and hands-on exercises.
> **Duration:** 9 weeks | **Format:** Live online classes + async labs | **Modules:** 12

---

## 🧭 Why This Level Matters for My Career Transition

The Fundamental level is where the QA → Cybersecurity transition became real for me. This course forced me to go beyond understanding *what* vulnerabilities are and start thinking about *how* to find, exploit, and defend against them — in controlled, hands-on environments.

| What I Brought from QA | What I Gained at Fundamental Level |
|------------------------|-----------------------------------|
| Structured thinking & test planning | Threat modeling & attack scenario design |
| API & web testing experience | Web security, auth bypass, and secure design |
| Bug documentation & reproduction steps | Vulnerability writeups & incident reporting |
| Understanding system behavior | Recognizing abnormal behavior as a security signal |
| Working in CI/CD pipelines | Secure architecture and development practices |

---

## 📅 Course Timeline

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

## 🗂️ Repository Structure

```
fundamental/
│
├── README.md                              ← You are here
│
├── module-01-threats-attacks-vulnerabilities/
│   ├── README.md
│   └── notes.md
├── module-02-identifying-threats/
│   ├── README.md
│   └── notes.md
├── module-03-secure-architecture-design/
│   ├── README.md
│   └── notes.md
├── module-04-secure-development/
│   ├── README.md
│   └── notes.md
├── module-05-authentication-authorization-audit/
│   ├── README.md
│   └── notes.md
├── module-06-resilience-specialized-systems/
│   ├── README.md
│   └── notes.md
├── module-07-cryptography/
│   ├── README.md
│   └── notes.md
├── module-08-host-security-equipment/
│   ├── README.md
│   └── notes.md
├── module-09-wireless-mobile-security/
│   ├── README.md
│   └── notes.md
├── module-10-virtualization-cloud-security/
│   ├── README.md
│   └── notes.md
├── module-11-incident-response/
│   ├── README.md
│   └── notes.md
├── module-12-grc/
│   ├── README.md
│   └── notes.md
│
└── labs/
    └── README.md                          ← Index of all lab exercises
```

---

## 📦 Module Overview

### Module 01 – Threats, Attacks & Vulnerabilities
**Sessions:** 1st & 2nd online meetings (Feb 02 & 04)

Core topic: Understanding the threat landscape — types of attacks, CVEs, attack surfaces, and vulnerability taxonomy.

**Key concepts:** threat actors, attack vectors, CVSS scoring, common vulnerability types.

**My QA connection:** In QA I reported bugs with severity levels — here I learned the industry-standard way to score vulnerabilities (CVSS). Same concept, more rigorous framework.

---

### Module 02 – Techniques for Identifying Threats
**Sessions:** 3rd online meeting (Feb 06)

Core topic: How to actively identify threats using scanning, enumeration, and threat intelligence techniques.

**Key concepts:** reconnaissance, footprinting, Nmap scanning, OSINT basics, threat intelligence feeds.

**My QA connection:** Test case discovery in QA is essentially reconnaissance — finding all the surfaces to test before writing a single case.

---

### Module 03 – Secure Architecture & Design
**Sessions:** 4th online meeting (Feb 09)

Core topic: Principles of designing systems with security built in from the start, not bolted on.

**Key concepts:** defense in depth, zero trust, least privilege, secure network segmentation, DMZ design.

**My QA connection:** QA often catches issues late in the SDLC — this module showed me how "shift left" security design prevents those bugs from existing in the first place.

---

### Module 04 – Secure Development
**Sessions:** 5th online meeting (Feb 20) | Labs: Feb 16 – Feb 27

Core topic: Writing and reviewing code with security in mind — OWASP Top 10, input validation, and secure coding standards.

**Key concepts:** SQL injection, XSS, CSRF, input sanitization, secure code review, SAST basics.

**My QA connection:** I've always tested *whether* input was validated. This module taught me *how* attackers exploit it when it isn't — completely changed how I think about test case design.

---

### Module 05 – Authentication, Authorization & Audit
**Sessions:** 6th online meeting (Feb 23) | Labs: Feb 23 – Mar 06

Core topic: How identity and access management works — and how it fails.

**Key concepts:** MFA, OAuth, session management, privilege escalation, access control models (DAC, MAC, RBAC), audit logging.

**My QA connection:** API testing always involved auth flows. This module deepened my understanding of *why* those flows are the most attacked surface in any application.

---

### Module 06 – Resilience, Specialized Systems & Physical Security
**Sessions:** 7th & 8th online meetings | Labs: Mar 02 – Mar 13

Core topic: Business continuity, disaster recovery, ICS/SCADA security, and physical access controls.

**Key concepts:** BCP, DRP, RTO/RPO, IoT security, SCADA vulnerabilities, physical security controls.

**My QA connection:** Resilience in systems is something QA tests under load and failure conditions. Here I learned the security dimensions of the same resilience thinking.

---

### Module 07 – Cryptography
**Sessions:** 8th & 9th online meetings | Labs: Mar 02 – Mar 13

Core topic: The mathematics and practical application of encryption, hashing, and PKI.

**Key concepts:** symmetric vs asymmetric encryption, AES, RSA, TLS/SSL, digital signatures, certificate chains, PKI, hashing algorithms (SHA, MD5).

**My QA connection:** I tested HTTPS endpoints without truly understanding what happened underneath. Now I can verify crypto implementations and spot misconfigurations.

---

### Module 08 – Host Security & Security Equipment
**Sessions:** 10th online meeting | Labs: Mar 09 – Mar 20

Core topic: Hardening operating systems and configuring security appliances.

**Key concepts:** OS hardening (Windows & Linux), endpoint protection, firewall configuration, IDS/IPS, WAF, SIEM basics.

**My QA connection:** I ran automated tests on application servers — this module taught me how to secure those servers themselves, not just the apps on them.

---

### Module 09 – Wireless & Mobile Security
**Sessions:** 11th & 12th online meetings | Labs: Mar 16 – Mar 27

Core topic: Security risks specific to wireless networks and mobile devices.

**Key concepts:** WPA2/WPA3, rogue AP attacks, evil twin, MDM (Mobile Device Management), BYOD policies, mobile app security.

**My QA connection:** Mobile testing was part of my QA work — this extended that into the attack surface of mobile devices and Wi-Fi protocols.

---

### Module 10 – Virtualization & Cloud Security
**Sessions:** 13th & 14th online meetings | Labs: Mar 16 – Mar 27

Core topic: Security in virtualized environments and cloud platforms.

**Key concepts:** hypervisor security, container security, shared responsibility model, cloud misconfigurations, IAM in cloud, S3 bucket exposure.

**My QA connection:** CI/CD pipelines I've worked with run on cloud infrastructure. This module showed me the attack surface of those environments and how to secure them.

---

### Module 11 – Incident Response
**Sessions:** 15th & 16th online meetings | Labs: Mar 23 – Apr 03

Core topic: How to detect, contain, and recover from security incidents.

**Key concepts:** IR lifecycle (Preparation → Identification → Containment → Eradication → Recovery → Lessons Learned), CSIRT, forensic basics, chain of custody, log analysis.

**My QA connection:** Bug triage in QA mirrors incident response — both require fast identification, severity assessment, escalation, and a post-mortem. The structured IR lifecycle felt very familiar.

---

### Module 12 – Governance, Risk & Compliance (GRC)
**Sessions:** 17th & 18th online meetings | Labs: Mar 30 – Apr 03

Core topic: The management layer of cybersecurity — policies, risk frameworks, and regulatory compliance.

**Key concepts:** ISO 27001, NIST framework, LGPD (Brazil's data protection law), risk assessment, security policies, audit processes.

**My QA connection:** QA involves compliance with test standards and quality policies. GRC is the same discipline applied to organizational security — I already understood the importance of documented processes and accountability.

---

## 🧪 Labs — Hands-on Exercises

> Each module included virtual lab exercises applying concepts in controlled environments. Notes and key commands are documented in each module folder.

| Lab | Module | Topic | Completed |
|-----|--------|-------|-----------|
| Lab 01 | M1 | Vulnerability scanning & CVE research | ✅ |
| Lab 02 | M2 | Reconnaissance with OSINT tools | ✅ |
| Lab 03 | M3 | Secure network design exercise | ✅ |
| Lab 04 | M4 | Exploiting & fixing OWASP vulnerabilities | ✅ |
| Lab 05 | M5 | Auth bypass & session hijacking scenarios | ✅ |
| Lab 06 | M6 | BCP/DR tabletop exercise | ✅ |
| Lab 07 | M7 | Cryptography: encrypt, hash, verify | ✅ |
| Lab 08 | M8 | OS hardening checklist (Linux & Windows) | ✅ |
| Lab 09 | M9 | Wi-Fi attack simulation & defense | ✅ |
| Lab 10 | M10 | Cloud misconfiguration analysis | ✅ |
| Lab 11 | M11 | Incident response tabletop scenario | ✅ |
| Lab 12 | M12 | Risk assessment exercise | ✅ |

---

## 🛠️ Tools Used Throughout the Course

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

## 🏆 Outcome

- ✅ **96 hours** of live synchronous training completed
- ✅ **12 modules** covering the full cybersecurity domain
- ✅ All lab exercises submitted on time
- ✅ Final assessment completed (Apr 05, 2026)
- ✅ **Progressed to the Specialized Level — DevSecOps track**

---

## 📁 What's in This Repository

Each module folder contains:
- `README.md` — summary of what was covered, key takeaways, and QA connection
- `notes.md` — detailed lesson notes, commands used, and lab outputs

> This documentation was written *during* the course to reinforce learning and build a public record of what I know — not just that I attended.

---

*Fundamental level completed: April 2026 | Next: [DevSecOps Specialization →](../devsecops-specialization/)*  
