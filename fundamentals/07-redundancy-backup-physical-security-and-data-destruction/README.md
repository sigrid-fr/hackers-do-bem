# Module 07 – Redundancy, Backup, Physical Security & Data Destruction

> **Status:** ✅ Completed | **Sessions:** 13rd & 14th online meetings (Mar 9 & 10) | **Lab deadline:** Mar 13, 2026

---

## What This Module Covers

This module focuses on ensuring system availability, data integrity, and confidentiality through redundancy, backup strategies, and secure data destruction. It explores both local and cloud-based solutions to improve resilience and disaster recovery capabilities.

---

## Key Concepts

- CIA Triad (Confidentiality, Integrity, Availability)  
- RAID (Redundant Array of Independent Disks)  
- Backup strategies (full, incremental, encrypted)  
- Disaster recovery concepts (RTO, data restoration)  
- Task automation (cron jobs)  
- Data sanitization and secure deletion  
- Cloud backup and geographic redundancy  
- Secure data handling and storage  

---

## Commands & Tools Used in Labs

```bash
# RAID management
mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sdX /dev/sdY
cat /proc/mdstat

# File synchronization
rsync -av /source/ /destination/

# Scheduling tasks
crontab -e

# Encrypted backup (duplicity)
duplicity /source file:///backup-location

# Secure file deletion (DoD method)
shred -u -n 3 file.txt

# Disk sanitization
wipefs -a /dev/nvme0n1
dd if=/dev/urandom of=/dev/nvme0n1 bs=1M
```

**Tools & Technologies:**

- Kali Linux, Windows Server 2022  
- mdadm, rsync, duplicity  
- OneDrive (Windows integration)  
- shred, wipefs, dd  

---

## Lab Exercise Notes

**Objective:** Implement redundancy, automate backup processes, ensure data confidentiality through encryption, and apply secure data destruction techniques.

---

### Steps I Followed

1. Configured RAID arrays using mdadm:
   - RAID 0 for performance  
   - RAID 1 for redundancy (mirroring)  

2. Managed disk structures:
   - Created partitions using fdisk  
   - Formatted file systems with mkfs.ext4  
   - Monitored RAID integrity via /proc/mdstat  

3. Implemented automated backup strategies:
   - Used rsync to synchronize directories with metadata preservation  
   - Scheduled backup jobs using crontab  

4. Configured cloud-based backup:
   - Integrated Windows Server 2022 with OneDrive  
   - Enabled automatic folder synchronization for data availability  

5. Implemented encrypted and incremental backups:
   - Used duplicity for delta-based backups  
   - Applied GPG encryption to protect stored data  

6. Performed disaster recovery validation:
   - Tested backup restoration processes  
   - Evaluated data integrity and recovery time  

7. Applied secure data destruction techniques:
   - Used shred with multiple overwrite passes (DoD 5220.22-M)  
   - Cleared filesystem signatures with wipefs  
   - Overwrote disks using dd with /dev/urandom  

---

### Findings / Observations

- RAID improves availability but does not replace backup strategies  
- Incremental backups significantly reduce storage usage while maintaining data integrity  
- Encryption (GPG) is essential for protecting data at rest, especially in external or cloud storage  
- Automation (cron jobs) ensures reliability and consistency of backup processes  
- Cloud integration enhances availability but introduces dependency on external services  
- Proper data sanitization is critical to prevent data recovery and ensure confidentiality  
- Testing recovery procedures is essential to validate backup effectiveness  

---

## My QA → Cybersecurity Connection

In QA, I focused on system reliability and validating expected behaviors.

This module helped me understand:

- how systems maintain availability even during failures  
- the importance of validating not just functionality, but data recovery processes  
- how data handling (storage, backup, deletion) directly impacts security  

It shifted my mindset from:

> *“Does the system work?”*   
to  
> *“Can the system recover safely and protect data under failure conditions?”*  

---

## Things to Explore Further

- [ ] Explore enterprise backup solutions (e.g., Veeam, AWS Backup)  
- [ ] Study high availability architectures and load balancing  
- [ ] Practice recovery scenarios with different RTO/RPO requirements  
- [ ] Learn secure data destruction standards beyond DoD (e.g., NIST SP 800-88)  
- [ ] Explore cloud-native backup and disaster recovery strategies  

---

## References

- [NIST SP 800-88](https://csrc.nist.gov/publications/detail/sp/800-88/rev-1/final) — guidelines for media sanitization  
- [GNU dd Documentation](https://www.gnu.org/software/coreutils/manual/html_node/dd-invocation.html) — disk overwrite and data operations
- [Rsync Documentation](https://download.samba.org/pub/rsync/rsync.html) — file synchronization
- [Duplicity Documentation](http://duplicity.nongnu.org) — encrypted incremental backups  
- [Linux RAID (mdadm) Guide](https://raid.wiki.kernel.org/index.php/Linux_Raid) — RAID configuration and management  
