# Module 11 – Secure Networking & Security Devices

> **Status:** ✅ Completed | **Sessions:** 21st & 22nd online meetings (Mar 25 & 27) | **Lab deadline:** Apr 03,2026

---

## What This Module Covers

This module focuses on securing network communication through traffic filtering, firewall configuration, VPN tunneling, and network control mechanisms. It explores how to protect hosts and manage network behavior in both Linux and Windows environments.

---

## Key Concepts

- Network security and perimeter defense  
- Firewall rules and packet filtering (Netfilter/Iptables)  
- NAT (Network Address Translation)  
- Traffic shaping and Quality of Service (QoS)  
- Secure communication via VPN (OpenVPN, SSL/TLS)  
- DNS behavior and redirection  
- MAC address spoofing and Layer 2 security  
- Network segmentation and access control  

---

## Commands & Tools Used in Labs

```bash
# List iptables rules
iptables -L

# Block specific IP
iptables -A INPUT -s <IP> -j DROP

# NAT rule (example)
iptables -t nat -A PREROUTING -p udp --dport 53 -j DNAT --to-destination <local_ip>

# Check network interfaces
ip link show

# Change MAC address
ip link set dev eth0 address XX:XX:XX:XX:XX:XX

# OpenVPN connection
openvpn --config client.ovpn

# DNS lookup
nslookup example.com
```

**Tools & Technologies:**

- Kali Linux, Windows Server 2022  
- Iptables (Netfilter), Windows Defender Firewall  
- OpenVPN  
- iproute2 (ip link), nslookup  

**Protocols & Services:**
- DNS, ICMP, HTTP/HTTPS, SSL/TLS  

---

## Lab Exercise Notes

**Objective:** Implement network security controls including firewalls, traffic shaping, VPN tunneling, and network manipulation techniques to understand both defensive and offensive perspectives.

---

### Steps I Followed

1. Configured firewall rules using Iptables:
   - Managed filter and NAT tables  
   - Implemented DROP policies for specific IPs and traffic  

2. Applied network traffic control (QoS):
   - Configured policies in Windows Server using Group Policy (GPO)  
   - Limited outbound traffic using throttle rate settings  

3. Established secure VPN connections:
   - Configured OpenVPN client connections  
   - Verified encrypted communication using SSL/TLS  

4. Performed DNS and traffic redirection:
   - Used DNAT rules to redirect DNS traffic (port 53)  
   - Simulated controlled traffic redirection scenarios  

5. Tested Layer 2 manipulation techniques:
   - Performed MAC address spoofing using `ip link`  
   - Observed behavior related to access control bypass scenarios  

---

### Findings / Observations

- Firewall rules provide strong control over inbound and outbound traffic when properly configured  
- NAT enables flexible traffic redirection but can be abused if misconfigured  
- QoS policies help maintain network stability and service availability  
- VPN tunneling ensures confidentiality and integrity of data in transit  
- DNS manipulation demonstrates how traffic can be redirected or controlled  
- MAC spoofing highlights weaknesses in hardware-based access control  
- Network security requires layered controls to be effective  

---

## My QA → Cybersecurity Connection

In QA, I tested APIs and network communication without focusing on how traffic was controlled or protected.

This module helped me understand:

- how network traffic can be filtered, redirected, or intercepted  
- how security controls operate at the network layer  
- how communication between systems can be secured or manipulated  

It shifted my mindset from:

> *“Is the request/response working?”*  
to  
> *“Is this communication secure and properly controlled?”*  

---

## Things to Explore Further

- [ ] Study advanced firewall configurations and intrusion detection systems (IDS/IPS)  
- [ ] Explore Zero Trust network architectures  
- [ ] Practice packet analysis using Wireshark  
- [ ] Learn about network segmentation in cloud environments  
- [ ] Study common network attacks (ARP spoofing, DNS poisoning)  

---

## References

- [Iptables Documentation](https://netfilter.org/documentation) — Linux firewall management 
- [OpenVPN Documentation](https://openvpn.net/community-resources) — VPN configuration and security 
- [Microsoft Firewall Documentation](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall) — Windows firewall management  
- [Nmap Network Security Guide](https://nmap.org/book) — network scanning and security concepts
- [OWASP Network Security](https://owasp.org/www-project-top-ten) — security risks and best practices  
