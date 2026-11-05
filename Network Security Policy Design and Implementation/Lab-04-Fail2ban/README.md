# Lab 4: Block Repeated Attackers with Fail2ban

## Policy Requirement

Automatically block repeated SSH authentication failures to prevent password guessing and brute-force attempts.

## Objective

To install and configure Fail2ban on Ubuntu, automatically block IP addresses after repeated failed SSH authentication attempts, verify the active SSH jail, and demonstrate automatic IP banning.

## Files Used

| File | Purpose |
|---|---|
| `jail.local` | Fail2ban configuration |
| `README.md` | Lab procedure and verification |
| `screenshot/` | Evidence of configuration and testing |

## Step 1: Install Fail2ban

Install Fail2ban on the Ubuntu server:

```bash
sudo apt install -y fail2ban
```

## Step 2: Configure Fail2ban

Create or edit the local configuration file:

```bash
sudo nano /etc/fail2ban/jail.local
```

Copy the configuration from `jail.local` in this repository.

The configuration defines:

- Ban duration: 1 hour
- Detection window: 10 minutes
- Maximum failed attempts: 5
- Trusted IP addresses: localhost and admin VLAN
- SSH protection enabled using the systemd backend

## Step 3: Restart Fail2ban

Restart the service to apply the configuration:

```bash
sudo systemctl restart fail2ban
```

Check whether Fail2ban is running:

```bash
sudo systemctl status fail2ban
```

## Step 4: Verify Fail2ban

Check the overall Fail2ban status:

```bash
sudo fail2ban-client status
```

Check the SSH jail status:

```bash
sudo fail2ban-client status sshd
```

The SSH jail should be enabled and display its monitored status, including banned IP addresses when applicable.

## Step 5: Test Automatic IP Banning

From a separate lab machine, perform five unsuccessful SSH authentication attempts against the Ubuntu server.

Check the SSH jail status:

```bash
sudo fail2ban-client status sshd
```

Expected result:

- The source IP address of the repeated failed attempts appears in the banned IP list.
- The SSH jail records failed authentication attempts.
- The offending IP address is automatically blocked according to the configured ban duration.

## Step 6: Remove a Ban Manually

If an IP address was accidentally banned, remove the ban using:

```bash
sudo fail2ban-client set sshd unbanip 192.168.20.55
```

Replace the example address with the actual banned IP address.

## Result

Fail2ban was installed and configured to monitor SSH authentication failures. Repeated failed login attempts triggered automatic IP banning according to the configured thresholds.

The SSH jail status was verified, and manual unban functionality was demonstrated.

## Screenshots

Store screenshots demonstrating:

- Fail2ban installation
- `jail.local` configuration
- Fail2ban service status
- Overall Fail2ban status
- SSH jail status
- Banned IP address after repeated failed login attempts
- Manual unban command

## Teaching Point

Fail2ban automatically responds to repeated authentication failures by blocking offending IP addresses. This reduces the risk of continued password-guessing attempts against SSH services.

## Disclaimer

This lab was performed in a controlled virtual machine environment for educational purposes. All configurations and tests were conducted on systems under authorised administration.