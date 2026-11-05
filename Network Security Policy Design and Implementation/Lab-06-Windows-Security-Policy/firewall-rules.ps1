# Run PowerShell as Administrator

# Enable firewall and default inbound block
Set-NetFirewallProfile -Profile Domain,Private,Public -Enabled True `
 -DefaultInboundAction Block -DefaultOutboundAction Allow `
 -LogAllowed False -LogBlocked True

# Allow RDP only from Admin VLAN
New-NetFirewallRule -DisplayName "Allow RDP from Admin VLAN" `
 -Direction Inbound -Protocol TCP -LocalPort 3389 `
 -RemoteAddress 192.168.10.0/24 -Action Allow
