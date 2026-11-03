# Lab 7 - Logging and Auditing

## Aim
Configure Linux auditing, centralized log forwarding, time synchronization checks, and log retention.

## Policy Requirements
- Log authentication and administrative activity.
- Synchronize system time.
- Forward logs to a central server.
- Retain logs for at least 180 days.

## Tools and Technologies
Ubuntu Linux, auditd, rsyslog, systemd journal, logrotate.

## Implementation

### 1. Install auditd and configure file watches
```bash
sudo apt install -y auditd
sudo nano /etc/audit/rules.d/policy.rules
```
Add:
```text
-w /etc/passwd -p wa -k identity
-w /etc/shadow -p wa -k identity
-w /etc/sudoers -p wa -k privilege
-w /etc/ssh/sshd_config -p wa -k sshconfig
```
Load and verify:
```bash
sudo augenrules --load
sudo auditctl -l
sudo ausearch -k privilege -i | tail -20
```

### 2. Forward logs to central syslog
On the client, create `/etc/rsyslog.d/90-forward.conf`:
```text
*.* @@192.168.10.50:514
```
`@@` uses TCP; a single `@` uses UDP.
```bash
sudo systemctl restart rsyslog
```
On the central server, configure the TCP listener in `/etc/rsyslog.conf`:
```text
module(load="imtcp")
input(type="imtcp" port="514")
```

### 3. Check time and retention
```bash
timedatectl status
```
The practical's logrotate example keeps 26 weekly files (about 6 months); review retention against the 180-day requirement.

### 4. Review failed SSH logins
```bash
sudo grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' \
 | sort | uniq -c | sort -nr | head

sudo journalctl -u ssh --since "24 hours ago" | grep "Failed password"
```

## Verification
- `auditctl -l` lists audit rules.
- `ausearch` returns matching audit events.
- `timedatectl status` reports synchronization status.
- Review forwarded logs on the central server and confirm retention settings.

## Screenshots
Store audit rules, service status, and log-review screenshots in `screenshots/`.

## Result
Linux auditing and centralized logging settings were configured and checked.

## Learning Outcomes
- Added audit watches for sensitive files.
- Forwarded syslog messages to a central server.
- Checked time synchronization and log retention.
- Reviewed failed authentication events.
