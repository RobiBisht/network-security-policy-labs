# Lab 4 - Block Repeated Attackers with Fail2ban

## Aim
Configure Fail2ban to automatically ban repeated failed SSH login attempts.

## Tools and Technologies
Ubuntu Linux, Fail2ban, systemd.

## Implementation

### 1. Install Fail2ban
```bash
sudo apt install -y fail2ban
```

### 2. Configure jail
Create or edit `/etc/fail2ban/jail.local`:
```ini
[DEFAULT]
bantime = 1h
findtime = 10m
maxretry = 5
ignoreip = 127.0.0.1/8 192.168.10.0/24

[sshd]
enabled = true
port = ssh
backend = systemd
```

### 3. Restart and check service
```bash
sudo systemctl restart fail2ban
sudo fail2ban-client status
sudo fail2ban-client status sshd
```

### 4. Unban an address if needed
```bash
sudo fail2ban-client set sshd unbanip 192.168.20.55
```

Test only from an authorized lab machine by generating failed SSH logins as directed by the practical.

## Verification
- `fail2ban-client status` shows active jails.
- `fail2ban-client status sshd` displays SSH jail status and banned addresses.

## Screenshots
Store service status and jail verification screenshots in `screenshots/`.

## Result
Fail2ban was configured to detect repeated SSH failures and temporarily ban offending addresses.

## Learning Outcomes
- Configured a Fail2ban jail.
- Understood bantime, findtime, and maxretry.
- Checked and managed jail status.
