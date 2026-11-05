# Lab 3: Host Firewall with Default Deny

## Policy Requirement (4.5)

Deny all inbound traffic by default. The web server accepts HTTP/HTTPS from anyone and SSH only from the admin VLAN.

## Objective

To implement a host-based firewall on Ubuntu using UFW or nftables, enforce a default-deny inbound policy, allow HTTP and HTTPS traffic, restrict SSH access to the administrator VLAN, and verify firewall behavior through network scanning.

## Files Used

| File | Purpose |
|---|---|
| `ufw-rules.sh` | UFW firewall configuration commands |
| `nftables.conf` | nftables firewall rules |
| `README.md` | Lab procedure and verification |
| `screenshot/` | Evidence of configuration and testing |

## Step 1: Choose the Firewall Implementation

This lab provides two firewall implementation options:

- Option A: UFW
- Option B: nftables

**Use either UFW or nftables, not both simultaneously.**

## Step 2: Configure the Firewall

### Option A: UFW

Execute the commands from `ufw-rules.sh` on the Ubuntu server.

Configure the firewall to:

- Deny all incoming traffic by default.
- Allow outgoing traffic.
- Allow SSH from the admin VLAN with rate limiting.
- Allow HTTP on TCP port 80.
- Allow HTTPS on TCP port 443.
- Enable firewall logging.

Verify the configuration:

```bash
sudo ufw status verbose
sudo ufw status numbered
```

### Option B: nftables

Copy the configuration file to the nftables configuration location:

```bash
sudo cp nftables.conf /etc/nftables.conf
```

Check the configuration syntax:

```bash
sudo nft -c -f /etc/nftables.conf
```

Load the firewall rules:

```bash
sudo nft -f /etc/nftables.conf
```

Enable nftables at boot:

```bash
sudo systemctl enable --now nftables
```

Verify the active ruleset:

```bash
sudo nft list ruleset
```

## Step 3: Test the Firewall Policy

Perform network scanning from two different VLAN machines.

### Test 1: Student VLAN

From the student VLAN machine, execute:

```bash
nmap -Pn -p 22,80,443 192.168.30.10
```

Expected result:

- Port 22 should be filtered.
- Ports 80 and 443 should be accessible if the corresponding web services are running.

### Test 2: Admin VLAN

From the admin VLAN machine, execute:

```bash
nmap -Pn -p 22,80,443 192.168.30.10
```

Expected result:

- Port 22 should be accessible if SSH is running.
- Ports 80 and 443 should be accessible if the web services are running.

## Step 4: Verify Firewall Configuration

For UFW:

```bash
sudo ufw status verbose
sudo ufw status numbered
```

For nftables:

```bash
sudo nft list ruleset
```

Confirm that the firewall enforces the intended inbound access policy.

## Result

The Ubuntu host firewall was configured with a default-deny inbound policy. HTTP and HTTPS traffic were permitted, while SSH access was restricted to the admin VLAN.

Firewall rules were verified, and network scanning was performed from student and administrator VLAN machines to confirm the access restrictions.

## Screenshots

Store screenshots demonstrating:

- Firewall configuration
- Active firewall rules
- UFW or nftables status
- Nmap scan from student VLAN
- Nmap scan from admin VLAN
- Verification of restricted SSH access

## Teaching Point

Testing from outside the server proves that the firewall control works as intended. A security policy that has never been tested is only an assumption.

## Disclaimer

This lab was performed in a controlled virtual machine environment for educational purposes. All configurations and tests were conducted on systems under authorised administration.