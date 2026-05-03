# Module 05 – Identity & Account Management

> **Status:** ✅ Completed | **Sessions:** 9th & 10th online meeting (Feb 25 & 27) | **Lab deadline:** Mar 6, 2026

---

## What This Module Covers

This module focuses on identity and account management in enterprise and Linux environments. It covers how users, groups, and permissions are structured, managed, and secured through directory services and access control policies.

---

## Key Concepts

- Identity and account lifecycle management  
- Directory services (Active Directory)  
- Organizational Units (OU), Groups, and Users  
- Group Policy Objects (GPO)  
- Access control models (DAC and MAC)  
- Password policies and credential management  
- File system permissions (NTFS, Linux rwx)  
- Domain environments and system integration  

---

## Commands & Tools Used in Labs

```bash
# Checking file permissions (Linux)
ls -l

# Changing file permissions
chmod 755 file.txt

# Viewing password policy configuration
cat /etc/login.defs

# Testing connectivity
ping <target>
```

**Tools & Technologies:**

- Windows Server 2022, Windows 10/11, Kali Linux  
- Active Directory Domain Services (AD DS)  
- Group Policy Management (GPO)  
- AppArmor (MAC)  
- Linux file permissions (DAC – rwx)  

**Protocols & Services:**
- RDP, SMB, DNS, ICMP  

---

## Lab Exercise Notes

**Objective:** Implement and manage identities, access controls, and security policies across Windows and Linux systems, ensuring proper user management and system protection.

---

### Steps I Followed

1. Installed and configured **Active Directory Domain Services (AD DS)** on Windows Server 2022 to establish a domain controller.

2. Created and organized **Organizational Units (OUs)**, users, and groups to simulate a corporate directory structure.

3. Configured **Group Policy Objects (GPO)** to enforce:
   - Password complexity  
   - Minimum length  
   - Password history policies  

4. Managed **access permissions**:
   - Configured NTFS permissions  
   - Set up shared folders with controlled access  

5. Integrated **Windows client machines** into the domain environment.

6. Performed Linux system administration tasks:
   - Managed file permissions using `chmod` and `ls -l` (DAC)  
   - Configured password policies via `/etc/login.defs`  
   - Implemented and audited security profiles using **AppArmor (MAC)**  

---

### Findings / Observations

- Centralized identity management (Active Directory) significantly improves scalability and control  
- GPOs are powerful tools for enforcing consistent security policies across an organization  
- Improper permission configuration (NTFS or Linux) can lead to privilege escalation risks  
- Linux access control (DAC vs MAC) provides flexibility but requires careful configuration  
- Domain integration simplifies user authentication but introduces dependency on directory services  
- Strong password policies and lifecycle management are critical for preventing unauthorized access  

---

## My QA → Cybersecurity Connection

In QA, I validated user roles, permissions, and system access behaviors.

This module helped me understand:
- how access control is actually implemented behind user roles  
- the risks associated with misconfigured permissions and identity management  
- how authentication and authorization are enforced at the system level  

It shifted my mindset from:

> *“Does the user have access?”*  
to  
> *“Is access correctly controlled, monitored, and secured?”*

---

## Things to Explore Further

- [ ] Explore Identity and Access Management (IAM) platforms (Azure AD, Okta)  
- [ ] Study privilege escalation techniques related to misconfigured permissions  
- [ ] Practice auditing Active Directory environments  
- [ ] Learn about Zero Trust identity models  
- [ ] Explore LDAP queries and directory enumeration techniques  

---

## References

- [Microsoft Active Directory Documentation](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds) — directory services and domain management
- [OWASP Access Control Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html) — secure access control practices
- [AppArmor Documentation](https://wiki.ubuntu.com/AppArmor) — Linux mandatory access control
- [Linux File Permissions Guide](https://www.redhat.com/sysadmin/linux-file-permissions-explained) — DAC concepts and usage
- [Microsoft Group Policy Documentation](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/gpresult) — policy management
