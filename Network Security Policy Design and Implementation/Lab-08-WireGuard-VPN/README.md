# Lab 8: Remote Access with WireGuard VPN

**Policy:** 4.7 — Remote Access Security

## Aim

To configure secure remote access using WireGuard VPN, allowing authorized remote devices to access internal network resources through an encrypted VPN tunnel.

## Policy Requirement

- Remote access must use an encrypted VPN connection.
- Internal services must not be directly exposed to the internet.
- Only authorized devices may connect to the VPN.
- VPN access must follow the organization's authentication requirements.
- Multi-factor authentication (MFA) must be required by the organization's remote-access policy.

## Software and Tools

- Ubuntu Server
- WireGuard VPN
- UFW firewall
- WireGuard client
- Linux terminal

## Repository Files

| File | Description |
|---|---|
| `server-wg0.conf` | WireGuard server configuration |
| `client-wg0.conf` | WireGuard client configuration |
| `vpn-setup.sh` | Installation, key generation, routing, and service setup |
| `screenshot/` | Practical screenshots |

## Procedure

### Step 1: Install WireGuard

Install WireGuard on the Ubuntu VPN server.

```bash
sudo apt update
sudo apt install -y wireguard
```

### Step 2: Generate Cryptographic Keys

Generate the server and client key pairs.

```bash
cd /etc/wireguard
sudo sh -c 'umask 077; wg genkey | tee server.key | wg pubkey > server.pub'
sudo sh -c 'umask 077; wg genkey | tee client1.key | wg pubkey > client1.pub'
```

The private keys must remain confidential. Only public keys are shared between peers.

### Step 3: Configure the VPN Server

Create the server configuration file.

```bash
sudo nano /etc/wireguard/wg0.conf
```

Add the server configuration from `server-wg0.conf`.

Replace the private-key placeholder with the contents of `server.key` and the client public-key placeholder with the contents of `client1.pub`.

### Step 4: Configure the VPN Client

Create the client configuration file.

```bash
sudo nano /etc/wireguard/wg0.conf
```

Add the client configuration from `client-wg0.conf`.

Replace the client private-key placeholder with the contents of `client1.key` and the server public-key placeholder with the contents of `server.pub`.

Replace `vpn.example.edu` with the VPN server's actual public IP address or DNS name.

### Step 5: Enable IP Forwarding

Enable IPv4 forwarding on the VPN server.

```bash
echo "net.ipv4.ip_forward=1" | sudo tee /etc/sysctl.d/99-vpn.conf
sudo sysctl --system
```

### Step 6: Configure the Firewall

Allow WireGuard traffic through the server firewall.

```bash
sudo ufw allow 51820/udp
```

The VPN server should expose only the required VPN endpoint and necessary services. Internal administrative and application services should not be directly accessible from the internet.

### Step 7: Start WireGuard

Enable and start the VPN interface.

```bash
sudo systemctl enable --now wg-quick@wg0
```

Verify the VPN configuration and interface.

```bash
sudo wg show
```

### Step 8: Connect the Client

Start the WireGuard tunnel on the client.

```bash
sudo wg-quick up wg0
```

Test connectivity to the VPN server.

```bash
ping 10.8.0.1
```

Verify the connection and handshake.

```bash
sudo wg show
```

## Verification

- WireGuard service is active on the server.
- VPN interface `wg0` is configured.
- Client can reach the VPN server through the tunnel.
- WireGuard reports a successful handshake.
- Internal resources are accessible through the VPN according to routing and firewall rules.
- Direct internet access to internal services is blocked.
- Only the required VPN endpoint is exposed externally.

## Security Limitation

WireGuard uses cryptographic public/private key pairs to authenticate peers. It does not provide built-in MFA.

If the organization's policy requires MFA for VPN access, an additional MFA-capable authentication gateway or another VPN solution with MFA integration is required.

Therefore, WireGuard alone does not fully satisfy a policy requiring MFA.

## Result

Configured a WireGuard VPN for encrypted remote access and verified VPN connectivity. Identified the limitation of WireGuard regarding built-in MFA and the need for additional authentication controls to satisfy the organization's security policy.