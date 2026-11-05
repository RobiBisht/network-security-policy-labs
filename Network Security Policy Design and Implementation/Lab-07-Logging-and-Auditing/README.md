# Lab 7: Logging and Auditing

## Policy Requirement (4.9)

Authentication and administrative activity must be logged, system time must be synchronized, logs must be forwarded to a central server, and logs must be retained for at least 180 days.

## Objective

- Monitor important system files using `auditd`.
- Configure centralized log forwarding using `rsyslog`.
- Verify system time synchronization.
- Configure log rotation and retention.
- Review failed SSH login attempts.

## Files Included

| File | Description |
|---|---|
| `policy.rules` | Audit rules for identity, privilege, and SSH configuration files |
| `90-forward.conf` | Rsyslog client forwarding configuration |
| `logrotate-rsyslog.conf` | Log rotation and retention configuration |
| `log-review.sh` | Commands for reviewing failed SSH login attempts |

## Step 1: Configure File Auditing with auditd

Install the audit package:

```bash
sudo apt update
sudo apt install -y auditd
```

Create the audit rules file:

```bash
sudo nano /etc/audit/rules.d/policy.rules
```

Copy the contents of `policy.rules` into the configuration file.

Load and verify the rules:

```bash
sudo augenrules --load
sudo auditctl -l
```

Generate an audit event and search for privilege-related activity:

```bash
sudo touch /etc/sudoers.d/test && sudo rm /etc/sudoers.d/test
sudo ausearch -k privilege -i | tail -20
```

**Note:** Validate any test file before placing it in `/etc/sudoers.d/`, and avoid unnecessary changes to sudo configuration.

## Step 2: Configure Centralized Log Forwarding

On the client system, open:

```bash
sudo nano /etc/rsyslog.d/90-forward.conf
```

Copy the contents of `90-forward.conf` into the configuration file.

Restart rsyslog:

```bash
sudo systemctl restart rsyslog
```

On the central syslog server, enable the TCP listener in `/etc/rsyslog.conf`:

```conf
module(load="imtcp")
input(type="imtcp" port="514")
```

Restart rsyslog on the server:

```bash
sudo systemctl restart rsyslog
```

**Note:** TCP port 514 must be allowed through the central server firewall.

## Step 3: Verify Time Synchronization and Configure Log Retention

Check time synchronization:

```bash
timedatectl status
```

Verify that the system clock is synchronized.

Configure log rotation:

```bash
sudo nano /etc/logrotate.d/rsyslog
```

Use the contents of `logrotate-rsyslog.conf` as the configuration reference.

The configuration uses weekly rotation and 26 rotated files, approximately six months of retention under normal rotation conditions.

**Note:** Rotation alone does not guarantee 180