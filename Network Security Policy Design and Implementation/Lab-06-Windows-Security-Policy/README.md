# Lab 6 - Windows Password, Lockout, and Firewall Policy

## Aim
Configure password, account lockout, and Windows Defender Firewall policies.

## Policy Requirements
- Minimum password length: 12 characters with complexity.
- Maximum password age: 90 days.
- Password history: 5.
- Lockout after 5 failed attempts.
- Firewall enabled with inbound default block.
- RDP permitted only from the admin VLAN.

## Tools and Technologies
Windows, elevated Command Prompt, PowerShell, Local Security Policy or Group Policy.

## Implementation

### 1. Configure password and lockout settings
Run Command Prompt as Administrator:
```bat
net accounts /minpwlen:12 /maxpwage:90 /minpwage:1 /uniquepw:5
net accounts /lockoutthreshold:5 /lockoutduration:15 /lockoutwindow:15
net accounts
```
Configure password complexity through Group Policy/Local Security Policy, or follow the `secedit` steps in the practical manual.

### 2. Configure Windows Defender Firewall
Run PowerShell as Administrator:
```powershell
Set-NetFirewallProfile -Profile Domain,Private,Public -Enabled True `
  -DefaultInboundAction Block -DefaultOutboundAction Allow `
  -LogAllowed False -LogBlocked True

New-NetFirewallRule -DisplayName "Allow RDP from Admin VLAN" `
  -Direction Inbound -Protocol TCP -LocalPort 3389 `
  -RemoteAddress 192.168.10.0/24 -Action Allow
```

### 3. Disable SMBv1
```powershell
Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force
```

### 4. Verify
```powershell
Get-NetFirewallProfile | Format-Table Name, Enabled, DefaultInboundAction
Get-NetFirewallRule -DisplayName "Allow RDP*" | Format-List DisplayName, Enabled, Action
```

## Verification
Confirm password/lockout settings and firewall profile values. Verify the RDP rule is enabled and limited to the admin VLAN.

## Screenshots
Store Windows policy and PowerShell verification screenshots in `screenshots/`.

## Result
Windows password, lockout, and firewall settings were configured and verified.

## Learning Outcomes
- Configured Windows account policies.
- Applied inbound firewall restrictions.
- Created a source-restricted RDP rule.
- Disabled SMBv1.
