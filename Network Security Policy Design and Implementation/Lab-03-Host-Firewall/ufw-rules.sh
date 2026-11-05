#!/bin/bash

# Option A: UFW

sudo ufw default deny incoming
sudo ufw default allow outgoing

# SSH from Admin VLAN only
sudo ufw limit from 192.168.10.0/24 to any port 22 proto tcp

# Allow HTTP and HTTPS
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# Enable firewall logging
sudo ufw logging medium

# Enable firewall
sudo ufw enable

# Verify firewall status
sudo ufw status verbose
sudo ufw status numbered
