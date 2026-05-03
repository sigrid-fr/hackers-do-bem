# Module 08 – Cryptography Concepts

> **Status:** ✅ Completed | **Sessions:** 15th & 16th online meeting (Mar 11 & 13) | **Lab deadline:** Mar 20, 2026

---

## What This Module Covers

This module focuses on protecting data through cryptographic techniques, ensuring confidentiality, integrity, and authenticity. It explores both classical and modern cryptographic approaches, including encryption, hashing, digital signatures, and data hiding techniques.

---

## Key Concepts

- CIA Triad + Authenticity  
- Symmetric vs Asymmetric Encryption  
- Hash functions and data integrity  
- Digital signatures and non-repudiation  
- Public Key Infrastructure (PKI) basics  
- Steganography and data obfuscation  
- Encryption modes (CTR, CFB)  
- Secure data handling at rest  

---

## Commands & Tools Used in Labs

```bash
# AES-256 encryption (OpenSSL)
openssl enc -aes-256-ctr -salt -in file.txt -out file.enc

# Decryption
openssl enc -aes-256-ctr -d -in file.enc -out file.txt

# Generate hash (SHA-512)
openssl dgst -sha512 file.txt

# Generate RSA key pair
openssl genpkey -algorithm RSA -out private.pem -pkeyopt rsa_keygen_bits:2048

# Generate ECC key pair
openssl ecparam -genkey -name prime256v1 -noout -out ecc_private.pem

# Sign file
openssl dgst -sha256 -sign private.pem -out signature.bin file.txt

# Verify signature
openssl dgst -sha256 -verify public.pem -signature signature.bin file.txt

# Hide file inside image
steghide embed -cf image.jpg -ef secret.txt
```

**Tools & Technologies:**

- Kali Linux  
- OpenSSL (enc, dgst, pkeyutl, genpkey, rsa, ec)  
- Steghide  
- Python (bytecode compilation)  

**Algorithms:**
- AES-256, 3DES, Blowfish  
- RSA-2048, ECC-256  
- SHA-2, SHA-3, RIPEMD-160, Blake2  

---

## Lab Exercise Notes

**Objective:** Apply cryptographic techniques to protect data confidentiality, verify integrity, and ensure authenticity through encryption, hashing, and digital signatures.

---

### Steps I Followed

1. Implemented steganography techniques using Steghide:
   - Embedded text files into JPG images  
   - Verified hidden data extraction  

2. Applied code protection techniques:
   - Converted Python scripts into bytecode  
   - Explored basic obfuscation to reduce code readability  

3. Performed symmetric encryption:
   - Used OpenSSL to encrypt files with AES-256 (CTR mode)  
   - Tested alternative algorithms such as 3DES and Blowfish  

4. Validated data integrity:
   - Generated hashes using multiple algorithms (MD5, SHA-2, SHA-3, Blake2)  
   - Compared outputs to detect file modifications  

5. Implemented asymmetric cryptography:
   - Generated key pairs using RSA-2048 and ECC-256  
   - Managed private and public keys securely  

6. Created and verified digital signatures:
   - Signed files using private keys  
   - Verified authenticity using public keys  

---

### Findings / Observations

- AES-256 provides strong confidentiality when properly configured with secure modes (e.g., CTR)  
- Hash functions are essential for detecting data tampering but do not provide confidentiality  
- Digital signatures ensure authenticity and non-repudiation of data  
- Asymmetric cryptography enables secure key exchange and trust establishment  
- Steganography hides data presence but does not replace encryption  
- Older algorithms (e.g., MD5, 3DES) are less secure and should be avoided in modern systems  
- Combining encryption + hashing + signatures provides a complete security approach  

---

## My QA → Cybersecurity Connection

In QA, I validated data flows and system outputs without focusing on how data was protected.

This module helped me understand:

- how data is secured at rest and during processing  
- the importance of validating integrity, not just correctness  
- how encryption and hashing impact system behavior and testing scenarios  

It shifted my mindset from:

> *“Is the data correct?”*  
to  
> *“Is the data protected, verifiable, and trustworthy?”*  

---

## Things to Explore Further

- [ ] Study TLS/HTTPS and how cryptography is applied in real-world communication  
- [ ] Explore key management systems (KMS)  
- [ ] Practice implementing cryptography using programming libraries (Python, Java)  
- [ ] Learn common cryptographic failures (OWASP)  
- [ ] Study quantum-resistant cryptography basics  

---

## References

- [OpenSSL Documentation](https://www.openssl.org/docs) — cryptographic toolkit usage 
- [NIST Cryptographic Standards](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines) — encryption and hashing standards  
- [OWASP Cryptographic Failures](https://owasp.org/Top10/A02_2021-Cryptographic_Failures) — common mistakes in crypto implementations
- [Steghide Documentation](https://steghide.sourceforge.net) — steganography tool 
- [RFC 8017 (RSA Standard)](https://datatracker.ietf.org/doc/html/rfc8017) — RSA cryptography specification
