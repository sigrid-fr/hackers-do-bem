# Module 12 – Incident Response & Secure Protocols

> **Status:** ✅ Completed | **Sessions:** 23rd & 24th online meetings (Mar 30 & Apr 1) | **Lab deadline:** Apr 05, 2026

---

## What This Module Covers

This module focuses on monitoring systems, responding to security incidents, and performing basic digital forensics. It explores how to collect and analyze logs, preserve evidence, and understand secure communication protocols.

---

## Key Concepts

- Incident response lifecycle (detection, analysis, containment, recovery)  
- Log collection and analysis  
- Time synchronization (NTP) for forensic accuracy  
- Network traffic analysis (TLS handshake)  
- Digital forensics fundamentals  
- Evidence preservation (bit-by-bit imaging)  
- Metadata analysis  
- Chain of custody and data integrity  

---

## Commands & Tools Used in Labs

```bash
# Time synchronization (Windows)
w32tm /query /status

# Analyze logs (Linux)
grep "error" /var/log/syslog

# View file metadata
stat file.txt

# Create disk image (forensics)
dd if=/dev/sdX of=image.dd bs=4M status=progress

# List files in filesystem (TSK)
fls image.dd

# Analyze inodes (TSK)
ils image.dd
```

**Tools & Technologies:**

- Windows 11, Kali Linux  
- Wireshark  
- ExifTool  
- The Sleuth Kit (fls, ils)  

**Protocols:**
- NTP, TLS, TCP/IP  

---

## Lab Exercise Notes

**Objective:** Monitor systems, analyze logs and network traffic, and perform basic forensic procedures to identify and investigate security incidents.

---

### Steps I Followed

1. Configured system auditing in Windows:
   - Enabled logon/logoff monitoring via gpedit.msc  
   - Verified event logs for user activity  

2. Implemented time synchronization (NTP):
   - Used w32tm to ensure accurate timestamps  
   - Understood the importance of synchronized logs for investigations  

3. Performed log analysis in Linux:
   - Reviewed system logs using terminal commands and graphical tools  
   - Identified boot messages and system errors  

4. Captured and analyzed network traffic:
   - Used Wireshark to inspect packets  
   - Analyzed TLS handshake behavior  

5. Conducted metadata analysis:
   - Used ExifTool to extract and manipulate image metadata  
   - Identified embedded information in files  

6. Performed digital forensics tasks:
   - Used The Sleuth Kit (fls, ils) to analyze filesystem structures  
   - Investigated file entries and inode data  

7. Created forensic disk images:
   - Used dd to generate bit-by-bit copies of storage devices  
   - Ensured data preservation for further analysis  

---

### Findings / Observations

- Accurate time synchronization (NTP) is critical for correlating events during investigations  
- Logs provide valuable insights but require filtering and analysis to identify anomalies  
- Network traffic analysis reveals secure communication patterns and potential issues  
- Metadata can expose hidden information that may be relevant to investigations  
- Forensic imaging preserves evidence integrity and prevents data alteration  
- File system analysis provides deeper visibility into deleted or hidden data  
- Incident response requires structured processes and reliable data sources  

---

## My QA → Cybersecurity Connection

In QA, I focused on identifying issues based on system behavior and logs.

This module helped me understand:

- how logs can be used not only for debugging, but for security investigations  
- how to analyze system and network data to identify suspicious activity  
- the importance of preserving evidence and maintaining data integrity  

It shifted my mindset from:

> *“What caused the bug?”*  
to  
> *“What evidence explains what happened?”*  

---

## Things to Explore Further

- [ ] Study SIEM tools (e.g., Splunk, ELK Stack) for centralized log analysis  
- [ ] Learn advanced digital forensics techniques  
- [ ] Explore incident response frameworks (NIST, SANS)  
- [ ] Practice analyzing real-world incident scenarios  
- [ ] Study memory forensics (Volatility)  

---

## References

- [NIST Incident Response Guide](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf) — incident handling framework
- [Wireshark Documentation](https://www.wireshark.org/docs) — network analysis 
- [The Sleuth Kit Documentation](https://www.sleuthkit.org/sleuthkit/docs) — digital forensics tools  
- [ExifTool Documentation](https://exiftool.org) — metadata analysis  
- [NTP Documentation](https://www.ntp.org/documentation) — time synchronization 
