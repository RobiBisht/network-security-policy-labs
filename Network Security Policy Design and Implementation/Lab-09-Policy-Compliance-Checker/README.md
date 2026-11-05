# Lab 9: Automated Security Policy Compliance Checker

**Policy:** STI Network Security Policy Compliance

## Aim

To develop a Python-based security compliance checker that automatically verifies selected Linux security settings against the STI Network Security Policy.

## Objectives

- Check SSH security configuration.
- Verify minimum password length and password aging.
- Check whether the host firewall is active.
- Verify permissions of sensitive system files.
- Check whether the auditing service is running.
- Generate a PASS/FAIL compliance report.

## Software and Tools

- Ubuntu Linux
- Python 3
- OpenSSH
- UFW or nftables
- auditd
- Linux terminal

## Repository Files

| File | Description |
|---|---|
| `policy_check.py` | Python security compliance checker |
| `screenshot/` | Practical screenshots |
| `README.md` | Lab documentation |

## Procedure

### Step 1: Verify Python Installation

Check whether Python 3 is installed.

```bash
python3 --version
```

### Step 2: Create the Python Script

Create the script.

```bash
nano policy_check.py
```

Paste the code from `policy_check.py` in this repository and save the file.

### Step 3: Make the Script Executable

```bash
chmod +x policy_check.py
```

### Step 4: Run the Compliance Checker

Execute the script with administrator privileges.

```bash
sudo ./policy_check.py
```

### Step 5: Check the Exit Status

```bash
echo $?
```

- `0` indicates that all implemented checks passed.
- `1` indicates that at least one check failed.

## Security Checks Performed

| Policy | Requirement | Verification |
|---|---|---|
| 4.3 | Root SSH login disabled | PermitRootLogin |
| 4.3 | SSH password authentication disabled | PasswordAuthentication |
| 4.3 | Maximum SSH authentication attempts | MaxAuthTries |
| 4.2 | Minimum password length | minlen |
| 4.2 | Maximum password age | PASS_MAX_DAYS |
| 4.5 | Host firewall active with default deny | UFW or nftables |
| 4.1 | Sensitive file permissions | /etc/shadow |
| 4.9 | Auditing service active | auditd |

## Sample Output

```text
Ref   Requirement                                   Result Detail
------------------------------------------------------------------------------------------
4.3   Root login over SSH disabled                 PASS   PermitRootLogin=no
4.3   SSH password login disabled                  PASS   PasswordAuthentication=no
4.3   MaxAuthTries <= 4                            PASS   MaxAuthTries=3
4.2   Minimum password length >= 12                PASS   minlen=12
4.2   Password max age <= 90 days                  PASS   PASS_MAX_DAYS=90
4.5   Host firewall active with default deny       PASS   ufw active
4.1   /etc/shadow has no world permissions         PASS   0o640
4.9   auditd running                               PASS   active
------------------------------------------------------------------------------------------
8 of 8 checks passed
```

*Note: The sample output is illustrative. Actual results depend on the Linux host configuration.*

## Verification

- Python script executes successfully.
- Security requirements are displayed in the report.
- Each check returns PASS or FAIL.
- Failed checks are counted.
- Exit status indicates the overall result.

## Limitations

This script checks only the selected security settings implemented in its code.

It does not perform a complete security audit or guarantee that the entire host complies with the STI Network Security Policy.

For example, password complexity, password history, account lockout, VPN MFA, and other requirements are not verified by this version.

The checker uses configuration files and service status to evaluate selected settings. Some checks may require additional validation of effective configuration or firewall rules.

## Result

Developed and executed a Python-based Linux security compliance checker that evaluates selected security policy requirements and generates a PASS/FAIL report.