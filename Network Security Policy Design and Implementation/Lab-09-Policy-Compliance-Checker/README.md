# Lab 9 - Automated Policy Compliance Checker in Python

## Aim
Create a Python script that reads Linux security settings and compares them with selected network security policy requirements.

## Tools and Technologies
Python 3, Ubuntu Linux, SSH, UFW/nftables, auditd.

## Script
`policy_check.py` checks selected requirements:
- SSH root login disabled.
- SSH password authentication disabled.
- SSH authentication attempts limited.
- Minimum password length and maximum password age.
- Host firewall active with default deny.
- `/etc/shadow` is not world-readable.
- `auditd` is running.

## Implementation
Save the practical's script as `policy_check.py`. The script uses commands and configuration files to collect settings, evaluates each requirement, and prints a PASS/FAIL report.

## Execution
```bash
chmod +x policy_check.py
sudo ./policy_check.py
echo $?
```
Run as root for more accurate results. Exit code `0` means all checks passed; `1` means at least one check failed.

## Verification
- Review each requirement and its PASS/FAIL status.
- Compare the output before and after completing the relevant labs.
- The script is a teaching tool, not a replacement for a full compliance scanner.

## Screenshots
Store the compliance report output in `screenshots/`.

## Result
A Python compliance checker was executed to evaluate selected Linux security policy settings.

## Learning Outcomes
- Read system configuration and command output using Python.
- Compare actual settings against policy requirements.
- Produce a basic automated PASS/FAIL compliance report.
- Understand the limitations of a simple compliance script.
