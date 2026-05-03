# Module 09 – Public Key Infrastructure & Blockchain

> **Status:** ✅ Completed | **Sessions:** 17th & 18th online meetings (Mar 16 & 19) | **Lab deadline:** Mar 27, 2026

---

## What This Module Covers

This module focuses on digital identity management through Public Key Infrastructure (PKI) and explores decentralized trust models using Blockchain technology. It covers certificate lifecycle, trust hierarchies, and how cryptographic systems enable secure communication and authentication.

---

## Key Concepts

- Public Key Infrastructure (PKI)  
- Certificate lifecycle (issuance, renewal, revocation)  
- Certificate Authorities (Root CA, Intermediate CA)  
- Digital certificates (X.509 standard)  
- Certificate formats (PEM, DER, PFX)  
- Certificate Signing Requests (CSR)  
- Certificate Revocation Lists (CRL)  
- Blockchain fundamentals (immutability, decentralization)  
- Consensus mechanisms  
- Wallets and private key management  

---

## Commands & Tools Used in Labs

```bash
# Generate private key
openssl genpkey -algorithm RSA -out private.key -pkeyopt rsa_keygen_bits:2048

# Generate CSR
openssl req -new -key private.key -out request.csr

# Generate self-signed certificate
openssl x509 -req -days 365 -in request.csr -signkey private.key -out certificate.crt

# View certificate details
openssl x509 -in certificate.crt -text -noout

# Convert certificate formats
openssl x509 -in certificate.crt -outform der -out certificate.der
```

**Tools & Technologies:**

- Kali Linux  
- OpenSSL  
- Electrum Wallet (Bitcoin)  

**Protocols & Standards:**
- X.509, PKCS#7, CRL  

---

## Lab Exercise Notes

**Objective:** Understand digital identity management through PKI and explore decentralized systems using Blockchain, focusing on trust, authentication, and secure communication.

---

### Steps I Followed

1. Explored PKI fundamentals:
   - Understood the hierarchy of trust (Root CA and Intermediate CA)  
   - Studied certificate lifecycle processes (issuance, renewal, revocation)  

2. Worked with digital certificates:
   - Generated private keys using OpenSSL  
   - Created Certificate Signing Requests (CSR)  
   - Generated self-signed certificates  

3. Analyzed certificate formats and standards:
   - Worked with PEM, DER, and PFX formats  
   - Explored X.509 certificate structure and metadata  

4. Studied revocation mechanisms:
   - Reviewed Certificate Revocation Lists (CRL)  
   - Understood how compromised certificates are invalidated  

5. Explored Blockchain concepts:
   - Studied block structure and immutability  
   - Analyzed consensus mechanisms and decentralized validation  

6. Practiced with cryptocurrency wallets:
   - Used Electrum to generate wallet addresses  
   - Simulated transactions and key management  
   - Explored private key ownership and security implications  

---

### Findings / Observations

- PKI provides a structured trust model essential for secure communication (e.g., HTTPS)  
- Certificate lifecycle management is critical to maintaining trust and preventing misuse  
- Improper handling of private keys compromises the entire trust chain  
- Self-signed certificates are useful for testing but not trusted in production environments  
- Blockchain removes the need for centralized authorities but introduces new security considerations  
- Private key management is the most critical aspect of both PKI and Blockchain systems  
- Trust models differ: centralized (PKI) vs decentralized (Blockchain), each with trade-offs  

---

## My QA → Cybersecurity Connection

In QA, I validated secure connections and API communications without fully understanding the trust mechanisms behind them.

This module helped me understand:

- how HTTPS and secure communications rely on certificates and PKI  
- the importance of validating certificate trust chains  
- how identity and trust are enforced in distributed systems  

It shifted my mindset from:

> *“Is the connection working?”*  
to  
> *“Can this connection be trusted?”*  

---

## Things to Explore Further

- [ ] Study TLS/SSL handshake and certificate validation process  
- [ ] Explore Public Key Infrastructure in enterprise environments  
- [ ] Learn about certificate pinning and trust store management  
- [ ] Study smart contracts and blockchain security risks  
- [ ] Explore hardware wallets and advanced key management techniques  

---

## References

- [OpenSSL Documentation](https://www.openssl.org/docs) — certificate and key management
- [NIST PKI Guidelines](https://csrc.nist.gov/projects/public-key-infrastructure) — PKI standards
- [RFC 5280 (X.509)](https://datatracker.ietf.org/doc/html/rfc5280) — certificate standard  
- [Bitcoin Whitepaper](https://bitcoin.org/bitcoin.pdf) — foundational blockchain concepts
- [Electrum Documentation](https://electrum.readthedocs.io) — wallet usage and security
