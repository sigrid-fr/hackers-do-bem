# Module 10 – Host Security

> **Status:** ✅ Completed | **Sessions:** 19th & 20th online meetings (Mar 20 & 23) | **Lab deadline:** Mar 27, 2026

---

## What This Module Covers

This module focuses on securing systems at the host level, including virtualization, disk encryption, and containerization. It explores how isolation, hardening techniques, and secure configurations protect operating systems and applications from threats.

---

## Key Concepts

- Host security and system hardening  
- Virtualization vs containerization  
- Hypervisors and virtual machine isolation  
- Full Disk Encryption (FDE) with LUKS  
- Secure boot concepts (BIOS/UEFI)  
- Container security fundamentals (Docker)  
- Stateless architecture and application isolation  
- Data protection at rest  

---

## Commands & Tools Used in Labs

```bash
# Create encrypted partition (LUKS)
cryptsetup luksFormat /dev/sdX

# Open encrypted volume
cryptsetup open /dev/sdX secure_volume

# Create filesystem
mkfs.ext4 /dev/mapper/secure_volume

# Mount encrypted volume
mount /dev/mapper/secure_volume /mnt/secure

# Docker - run container
docker run -it ubuntu bash

# List running containers
docker ps

# Stop container
docker stop <container_id>
```

**Tools & Technologies:**

- Kali Linux, Windows  
- Oracle VM VirtualBox  
- Docker (CLI)  
- LUKS, cryptsetup  
- Thunar (file manager)  

---

## Lab Exercise Notes

**Objective:** Implement host-level security techniques including virtualization, disk encryption, and containerization to protect systems and applications.

---

### Steps I Followed

1. Configured virtual machines using VirtualBox:
   - Managed system resources (CPU, RAM, storage)  
   - Created snapshots for safe testing environments  
   - Configured network isolation for controlled lab scenarios  

2. Explored BIOS/UEFI settings:
   - Analyzed boot order configurations  
   - Understood secure boot concepts and system initialization  

3. Implemented Full Disk Encryption (LUKS):
   - Created encrypted partitions using cryptsetup  
   - Mounted and managed secure volumes  
   - Applied best practices for key management  

4. Managed Docker containers:
   - Created and executed isolated containers  
   - Tested application behavior in containerized environments  
   - Stopped and monitored running instances  

5. Analyzed containerization benefits:
   - Compared containers vs traditional virtual machines  
   - Observed portability and isolation advantages  
   - Explored stateless architecture concepts  

---

### Findings / Observations

- Virtual machines provide strong isolation but require more resources than containers  
- Containers offer lightweight isolation and improved portability for applications  
- Full Disk Encryption (LUKS) effectively protects data at rest against unauthorized access  
- Improper key management can compromise encrypted systems  
- Snapshots are essential for safe testing and recovery in virtual environments  
- Containerization reduces attack surface when properly configured  
- Host-level security is foundational — weaknesses here affect all higher layers  

---

## My QA → Cybersecurity Connection

In QA, I worked with test environments but did not focus on how they were secured.

This module helped me understand:

- how test environments can be isolated and secured using virtualization  
- how containerization can improve consistency across environments  
- how system-level configurations impact application security  

It shifted my mindset from:

> *“Does the environment work correctly?”*  
to  
> *“Is the environment secure and properly isolated?”*  

---

## Things to Explore Further

- [ ] Explore container security tools (e.g., Docker Bench, Trivy)  
- [ ] Study Kubernetes security fundamentals  
- [ ] Learn advanced Linux hardening techniques  
- [ ] Explore secure boot and TPM integration  
- [ ] Practice securing cloud-based virtual machines  

---

## References

- [Docker Documentation](https://docs.docker.com) — container management and security
- [cryptsetup Documentation](https://gitlab.com/cryptsetup/cryptsetup) — disk encryption with LUKS  
- [VirtualBox Documentation](https://www.virtualbox.org/wiki/Documentation) — virtualization platform
- [NIST Guide to Storage Encryption](https://csrc.nist.gov/publications/detail/sp/800-111/final) — encryption best practices  
- [Linux Hardening Guide](https://www.cyberciti.biz/tips/linux-security.html) — system security practices
