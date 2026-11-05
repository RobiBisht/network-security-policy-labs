# Network Security Policy Design and Implementation

## Overview

This directory contains practical laboratory exercises for the subject **Network Security Policy Design and Implementation**.

The labs demonstrate the implementation, configuration, testing, and verification of security policies across Linux, Windows, networking devices, and VPN environments.

## Objectives

- Implement password and account security policies.
- Harden SSH and administrative access.
- Configure host firewalls and access control.
- Protect systems against repeated authentication attempts.
- Apply Cisco device security and network ACLs.
- Configure Windows password, lockout, and firewall policies.
- Implement security logging and auditing.
- Configure encrypted remote access using WireGuard VPN.
- Automate Linux security compliance verification using Python.

## Laboratory Index

| Lab | Title | Policy Reference |
|---|---|---|
| Lab 1 | Linux Password and Account Lockout Policy | 4.2 |
| Lab 2 | SSH Hardening | 4.3 |
| Lab 3 | Host Firewall with Default Deny | 4.5 |
| Lab 4 | Block Repeated Attackers with Fail2ban | 4.5 |
| Lab 5 | Cisco Device Hardening, Port Security, and ACLs | 4.3, 4.4 |
| Lab 6 | Windows Password, Lockout, and Firewall Policy | 4.2, 4.5 |
| Lab 7 | Security Logging and Auditing | Logging and Auditing |
| Lab 8 | Remote Access with WireGuard VPN | 4.7 |
| Lab 9 | Automated Security Policy Compliance Checker | Multiple Policies |

## Repository Structure

```text
Network Security Policy Design and Implementation/
│
├── README.md
│
├── Lab 1/
│   ├── README.md
│   ├── Configuration Files
│   └── screenshot/
│
├── Lab 2/
│   ├── README.md
│   ├── Configuration Files
│   └── screenshot/
│
├── Lab 3/
│   ├── README.md
│   ├── Configuration Files
│   └── screenshot/
│
├── Lab 4/
│   ├── README.md
│   ├── Configuration Files
│   └── screenshot/
│
├── Lab 5/
│   ├── README.md
│   ├── Configuration Files
│   └── screenshot/
│
├── Lab 6/
│   ├── README.md
│   ├── Configuration Files
│   └── screenshot/
│
├── Lab 7/
│   ├── README.md
│   ├── Configuration Files
│   └── screenshot/
│
├── Lab 8/
│   ├── README.md
│   ├── Configuration Files
│   └── screenshot/
│
└── Lab 9/
    ├── README.md
    ├── policy_check.py
    └── screenshot/
```

## Technologies Used

- Ubuntu Linux
- Kali Linux
- Windows
- Cisco Packet Tracer
- OpenSSH
- UFW and nftables
- Fail2ban
- WireGuard VPN
- Python 3
- Linux auditing tools

## Documentation

Each laboratory folder contains:

- **README.md:** Aim, policy requirements, procedure, commands, verification, and result.
- **Configuration Files:** Reference configurations or scripts used in the practical.
- **screenshot/:** Screenshots demonstrating practical execution and verification.

## Security Notice

Configuration files and scripts are provided for educational and laboratory purposes.

- Review configurations before applying them to real systems.
- Use isolated virtual machines or authorized lab environments.
- Never publish passwords, private keys, or sensitive credentials.
- Maintain backups before modifying security configurations.
- Verify security settings after implementation.

## Learning Outcome

These practical exercises provide hands-on experience in implementing security controls, hardening systems, protecting network access, monitoring security events, and evaluating security policy compliance.

