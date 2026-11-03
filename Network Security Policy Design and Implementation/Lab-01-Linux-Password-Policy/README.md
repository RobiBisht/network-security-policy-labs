# Lab 1 - Linux Password and Account Lockout Policy

## Aim
Implement password complexity, password aging, and temporary account lockout on Ubuntu Linux.

## Policy Requirements
- Minimum password length: 12 characters.
- Require at least one digit, uppercase letter, lowercase letter, and symbol.
- Maximum password age: 90 days.
- Lock an account for 15 minutes after 5 failed attempts.

## Tools and Technologies
Ubuntu Linux, PAM, `libpam-pwquality`, `pam_faillock`.

## Implementation

### 1. Install password-quality module
```bash
sudo apt update
sudo apt install -y libpam-pwquality
```

### 2. Configure password complexity
Edit `/etc/security/pwquality.conf`:
```ini
minlen = 12
dcredit = -1
ucredit = -1
lcredit = -1
ocredit = -1
maxrepeat = 3
usercheck = 1
retry = 3
```

### 3. Configure password aging
Edit `/etc/login.defs`:
```text
PASS_MAX_DAYS 90
PASS_MIN_DAYS 1
PASS_WARN_AGE 7
```
These defaults apply to new users. Apply the settings to an existing account:
```bash
sudo chage -M 90 -m 1 -W 7 student1
sudo chage -l student1
```

### 4. Test password quality
```bash
echo "abc123" | pwscore
echo "Tr4in!Stat1on-Blue" | pwscore
```
Try changing a test account password with `passwd` and observe weak-password rejection.

### 5. Configure account lockout
Edit `/etc/security/faillock.conf`:
```ini
deny = 5
fail_interval = 900
unlock_time = 900
```
Back up PAM configuration before editing:
```bash
sudo cp /etc/pam.d/common-auth /etc/pam.d/common-auth.bak
```
Configure the authentication stack as directed in the practical manual, and add the account rule in `/etc/pam.d/common-account`:
```text
account required pam_faillock.so
```
Check failures and reset a test account when required:
```bash
sudo faillock --user student1
sudo faillock --user student1 --reset
```

## Verification
- `chage -l student1` displays the account aging values.
- `pwscore` evaluates sample passwords.
- `faillock --user student1` displays recorded failed attempts.

## Screenshots
Store implementation and verification screenshots in `screenshots/`.

## Result
Password complexity, password aging, and temporary account lockout were configured and tested in the Ubuntu lab.

## Learning Outcomes
- Configured Linux password-quality rules.
- Applied password aging to an account.
- Learned how PAM and `pam_faillock` support account lockout.
