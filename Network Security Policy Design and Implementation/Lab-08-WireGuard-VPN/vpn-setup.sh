#!/bin/bash

# Install WireGuard
sudo apt update
sudo apt install -y wireguard

# Generate server and client keys
cd /etc/wireguard
sudo sh -c 'umask 077; wg genkey | tee server.key | wg pubkey > server.pub'
sudo sh -c 'umask 077; wg genkey | tee client1.key | wg pubkey > client1.pub'

# Enable IPv4 forwarding
echo "net.ipv4.ip_forward=1" | sudo tee /etc/sysctl.d/99-vpn.conf
sudo sysctl --system

# Allow WireGuard VPN traffic
sudo ufw allow 51820/udp

# Start and enable WireGuard
sudo systemctl enable --now wg-quick@wg0

# Verify VPN status
sudo wg show