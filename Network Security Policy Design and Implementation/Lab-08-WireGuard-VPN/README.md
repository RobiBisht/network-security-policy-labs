# Lab 8 - Remote Access with WireGuard VPN

## Aim
Configure encrypted remote access through a WireGuard VPN in a lab environment.

## Policy Requirement
Remote access should use the VPN, be encrypted, and avoid exposing internal services directly to the internet.

## Tools and Technologies
Ubuntu Linux, WireGuard, UFW, systemd.

## Implementation

### 1. Install WireGuard and generate lab keys
```bash
sudo apt install -y wireguard
cd /etc/wireguard
umask 077
wg genkey | tee server.key | wg pubkey > server.pub
wg genkey | tee client1.key | wg pubkey > client1.pub
```
Keep private keys private. Do not commit real key files to GitHub.

### 2. Server configuration
Create `/etc/wireguard/wg0.conf` with the server interface and client peer settings:
```ini
[Interface]
Address = 10.8.0.1/24
ListenPort = 51820
PrivateKey = <SERVER_PRIVATE_KEY>

[Peer]
PublicKey = <CLIENT_PUBLIC_KEY>
AllowedIPs = 10.8.0.2/32
```

### 3. Client configuration
```ini
[Interface]
Address = 10.8.0.2/24
PrivateKey = <CLIENT_PRIVATE_KEY>

[Peer]
PublicKey = <SERVER_PUBLIC_KEY>
Endpoint = vpn.example.edu:51820
AllowedIPs = 10.8.0.0/24, 192.168.10.0/24
PersistentKeepalive = 25
```
Use placeholders in repository examples.

### 4. Enable routing and start VPN
```bash
echo "net.ipv4.ip_forward=1" | sudo tee /etc/sysctl.d/99-vpn.conf
sudo sysctl --system
sudo ufw allow 51820/udp
sudo systemctl enable --now wg-quick@wg0
sudo wg show
```
On the client:
```bash
sudo wg-quick up wg0
ping 10.8.0.1
```

## Verification
- `wg show` displays the interface and peer.
- The client can ping the VPN server address after connection.
- Check that only intended services are reachable through the VPN.

## Security Note
The practical notes that WireGuard key authentication does not provide built-in second factor. If policy requires MFA, an additional compatible gateway or solution is needed.

## Screenshots
Store VPN status and connectivity screenshots in `screenshots/`.

## Result
A WireGuard VPN lab was configured and basic connectivity was verified.

## Learning Outcomes
- Generated WireGuard key pairs.
- Configured server and client peers.
- Enabled IP forwarding and VPN service.
- Understood the difference between key authentication and MFA.
