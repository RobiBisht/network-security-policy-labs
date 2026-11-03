# Lab 2 - SSH Hardening

## Aim
Harden administrative SSH access on the Ubuntu server.

## Policy Requirements
Use SSH for administration, individual accounts, no direct root login, key-based authentication, and a legal warning banner.

## Tools and Technologies
Ubuntu Linux, OpenSSH, SSH key authentication.

## Implementation

### 1. Generate a key and copy it to the server
Run on the admin workstation:
```bash
ssh-keygen -t ed25519 -C "admin@sti"
ssh-copy-id student1@192.168.30.10
ssh student1@192.168.30.10
```
Confirm key login works before disabling password authentication.

### 2. Back up and edit SSH configuration
```bash
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak
sudo nano /etc/ssh/sshd_config
```
Set the required directives:
```text
PermitRootLogin no
PubkeyAuthentication yes
PasswordAuthentication no
PermitEmptyPasswords no
MaxAuthTries 3
LoginGraceTime 30
AllowUsers student1 netadmin
ClientAliveInterval 300
ClientAliveCountMax 2
X11Forwarding no
Banner /etc/issue.net
```

### 3. Configure warning banner
Edit `/etc/issue.net`:
```text
*** Authorised use only. Activity is monitored and logged. ***
*** Unauthorised access is prohibited and may be prosecuted. ***
```

### 4. Validate and reload
```bash
sudo sshd -t
sudo systemctl reload ssh
```
Test from another terminal:
```bash
ssh root@192.168.30.10
ssh -o PubkeyAuthentication=no student1@192.168.30.10
```
Show effective settings:
```bash
sudo sshd -T | grep -Ei "permitrootlogin|passwordauthentication|maxauthtries"
```

## Verification
- `sshd -t` returns no output when syntax is valid.
- Root SSH and password-only SSH attempts should be refused.
- `sshd -T` displays effective configuration.

## Screenshots
Store SSH configuration and verification screenshots in `screenshots/`.

## Result
SSH administrative access was hardened and verified in the lab.

## Learning Outcomes
- Configured key-based SSH authentication.
- Disabled direct root and password login.
- Added a legal warning banner and connection limits.
