# Lab 3 - Host Firewall with Default Deny

## Aim
Configure a Linux host firewall to restrict inbound traffic according to the network security policy.

## Policy Requirements
- Deny inbound traffic by default.
- Allow HTTP and HTTPS to the web server.
- Allow SSH only from the admin VLAN.

## Tools and Technologies
Ubuntu Linux, UFW or nftables, Nmap.

## Implementation

### Option A - UFW
Use UFW or nftables, not both at the same time:
```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw limit from 192.168.10.0/24 to any port 22 proto tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw logging medium
sudo ufw enable
sudo ufw status verbose
sudo ufw status numbered
```

### Option B - nftables
Create `/etc/nftables.conf` using the rules from the practical manual. The rules should include an input chain with `policy drop`, loopback and established traffic acceptance, admin-VLAN SSH, HTTP/HTTPS, and rate-limited logging.
Validate and load:
```bash
sudo nft -c -f /etc/nftables.conf
sudo nft -f /etc/nftables.conf
sudo systemctl enable --now nftables
sudo nft list ruleset
```

### 3. Test the policy
From a student VLAN machine:
```bash
nmap -Pn -p 22,80,443 192.168.30.10
```
Repeat from an admin VLAN machine and compare SSH access.

## Verification
- Inspect `ufw status verbose` or `nft list ruleset`.
- Compare Nmap results from student and admin VLANs.
- SSH should be restricted to the admin VLAN; web ports should be accessible as required.

## Screenshots
Store firewall rules and test results in `screenshots/`.

## Result
A default-deny host firewall policy was configured and tested.

## Learning Outcomes
- Applied default-deny firewall rules.
- Restricted SSH by source network.
- Verified firewall behavior using Nmap.
