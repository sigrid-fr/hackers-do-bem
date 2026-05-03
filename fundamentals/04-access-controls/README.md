# Module 04 – Access Controls

> **Status:** ✅ Completed | **Sessions:** 5th online meeting (Feb 11, 2026) | **Lab deadline:** Mar 01, 2026

---

## What This Module Covers

This module explores access control mechanisms, focusing on identification, authentication, authorization, and accounting (IAAA). It covers how systems verify identities, enforce permissions, and track user activity across Linux, Windows, and network environments.

---

## Key Concepts

- IAAA (Identification, Authentication, Authorization, Accounting)
- Authentication factors (something you know, have, are)
- Multi-Factor Authentication (MFA)
- Access control models (RBAC, MAC, DAC)
- Centralized authentication (RADIUS)
- Credential storage and protection
- Authentication protocols (Kerberos, NTLM, PAP, CHAP, MS-CHAPv2)
- Secure credential management

---

## 💻 Commands & Tools Used in Labs

```bash
# Password cracking (offline analysis)
john --wordlist=wordlist.txt hashes.txt

# RADIUS authentication test
radtest user password localhost 0 testing123

# Checking SELinux status
sestatus

# Viewing shadow file (requires root)
cat /etc/shadow

```

---

**Tools & Technologies:**

- Kali Linux, Windows Server 2022
- John the Ripper
- FreeRADIUS
- Google Authenticator / OTPClient
- KeePassXC
- SELinux

**Protocols:**

- RADIUS, PAP, CHAP, MS-CHAPv2
- Kerberos, NTLM
- LDAP, SSH, TOTP

---

## Lab Exercise Notes

**Objective:** Understand and apply authentication and access control mechanisms across different systems, including password security, MFA, and centralized authentication.

**Steps I followed:**
1. Performed offline password cracking using John the Ripper against hashed credentials from `/etc/shadow` to understand password strength and attack techniques.
2. Configured and tested a FreeRADIUS server, validating centralized authentication using the `radtest` command.
3. Implemented Multi-Factor Authentication (MFA) using TOTP, integrating Google Authenticator and managing tokens via OTPClient.
4. Explored Linux security mechanisms, including:
   - SELinux (mandatory access control)
   - TPM presence verification
   - Secure credential storage using KeePassXC (AES-256)
5. Analyzed Windows Server 2022 authentication mechanisms, including:
   - Credential Manager (credential storage and auditing)
   - Kerberos and NTLM authentication within Active Directory

**Findings / observations:**
- Weak passwords are highly vulnerable to dictionary attacks when proper policies are not enforced
- Centralized authentication (RADIUS) simplifies access control management across systems
- MFA significantly increases security by adding an additional verification layer
- SELinux provides strong control over system access through mandatory policies
- Credential storage solutions (KeePassXC) are essential for secure password management
- Kerberos is more secure than NTLM due to ticket-based authentication and reduced exposure of credentials

---

## My QA → Cybersecurity Connection

In QA, I frequently tested authentication flows and role-based permissions.
This module helped me understand:
- How authentication mechanisms actually work behind login systems
- The risks of weak credential handling and improper access control
- The importance of validating not only functionality, but also security of access flows

It shifted my mindset from:

> *“Can the user log in?”*  
to  
> *“How secure is the authentication and access control process?”*

---

## Things to Explore Further

- [ ] Explore advanced Kerberos attacks (Pass-the-Ticket, Golden Ticket)
- [ ] Study IAM solutions (e.g., Azure AD, Okta)
- [ ] Practice configuring LDAP-based authentication
- [ ] Implement MFA in real web applications
- [ ] Study Zero Trust architecture and identity-based security

---

## References

- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) — secure authentication practices  
- [MITRE ATT&CK – Credential Access](https://attack.mitre.org/tactics/TA0006/) — techniques targeting authentication systems  
- [FreeRADIUS Documentation](https://freeradius.org/documentation/) — AAA implementation  
- [Microsoft Kerberos Documentation](https://learn.microsoft.com/en-us/windows-server/security/kerberos/) — authentication protocol reference  
- [SELinux Project](https://selinuxproject.org/) — mandatory access control in Linux    
