# Lab 6: Windows Password, Lockout and Firewall Policy

## Policy Requirements (4.2, 4.5)

12-character passwords with complexity, 90-day maximum age, 5-password history, lockout after 5 failures, firewall enabled with inbound default block, and RDP restricted to the admin VLAN.

## Objective

To configure Windows password and account lockout policies, enable Windows Defender Firewall with a default-deny inbound policy, restrict Remote Desktop Protocol (RDP) access to the administrator VLAN, and disable the legacy SMBv1 protocol.

## Files Used

| File | Purpose |
|---|---|
| `password-lockout.cmd` | Password aging, password history, and account lockout |
| `password-complexity.cmd` | Password complexity configuration |
| `firewall-rules.ps1` | Windows Defender Firewall and RDP restrictions |
| `disable-smb1.ps1` | Disable legacy SMBv1 |
| `README.md` | Lab procedure and verification |
| `screenshot/` | Evidence of configuration and testing |

## Step 1: Configure Windows Password and Lockout Policy

Run `password-lockout.cmd` from an elevated Command Prompt.

The configuration establishes:

- Minimum password length: 12 characters
- Maximum password age: 90 days
- Minimum password age: 1 day
- Password history: 5 previous passwords
- Account lockout threshold: 5 failed attempts
- Account lockout duration: 15 minutes
- Reset failed attempt counter after: 15 minutes

Verify the policy:

```cmd
net accounts
```

## Step 2: Enable Password Complexity

Run `password-complexity.cmd` as Administrator.

Export the local security policy:

```cmd
secedit /export /cfg C:\sec.cfg
```

Open the exported file:

```cmd
notepad C:\sec.cfg
```

Change the following setting:

```text
PasswordComplexity = 0
```

to:

```text
PasswordComplexity = 1
```

Save the file and apply the security policy:

```cmd
secedit /configure /db C:\Windows\security\local.sdb /cfg C:\sec.cfg /areas SECURITYPOLICY
```

Refresh the policy:

```cmd
gpupdate /force
```

## Step 3: Configure Windows Defender Firewall

Run `firewall-rules.ps1` in PowerShell as Administrator.

The configuration:

- Enables Windows Defender Firewall for Domain, Private, and Public profiles
- Sets the default inbound action to Block
- Allows outbound traffic by default
- Enables logging of blocked traffic
- Creates an inbound RDP rule for the administrator VLAN

The RDP rule permits TCP port 3389 from:

```text
192.168.10.0/24
```

**Important:** Review existing Remote Desktop firewall rules. Disable or restrict any broader RDP allow rules so that RDP is genuinely limited to the admin VLAN.

## Step 4: Disable SMBv1

Run `disable-smb1.ps1` in PowerShell as Administrator.

The configuration disables the legacy SMBv1 server protocol.

## Step 5: Verify Windows Security Policies

### Verify Password and Lockout Policy

```cmd
net accounts
```

Confirm that the password length, maximum age, password history, and lockout settings match the policy.

### Verify Windows Defender Firewall

```powershell
Get-NetFirewallProfile | Format-Table Name, Enabled, DefaultInboundAction
```

Expected result:

- Firewall is enabled.
- Default inbound action is Block.

### Verify RDP Firewall Rule

```powershell
Get-NetFirewallRule -DisplayName "Allow RDP*" | Format-List DisplayName, Enabled, Action
```

Review the associated remote address restrictions:

```powershell
Get-NetFirewallRule -DisplayName "Allow RDP from Admin VLAN" |
Get-NetFirewallAddressFilter
```

Expected result: The rule allows RDP traffic from the admin VLAN.

### Verify SMBv1

```powershell
Get-SmbServerConfiguration | Select-Object EnableSMB1Protocol
```

Expected result:

```text
EnableSMB1Protocol : False
```

## Result

Windows password and account lockout policies were configured according to the security requirements.

Windows Defender Firewall was enabled with a default inbound block policy, and RDP access was restricted to the admin VLAN.

The legacy SMBv1 protocol was disabled, and the security settings were verified using Windows command-line and PowerShell tools.

## Screenshots

Store screenshots demonstrating:

- Password and account lockout policy
- Password complexity configuration
- Windows Defender Firewall enabled
- Default inbound block policy
- RDP firewall rule
- RDP remote address restriction
- SMBv1 disabled
- Security policy verification

## Disclaimer

This lab was performed in a controlled Windows virtual machine environment for educational purposes. All configurations and tests were conducted on systems under authorised administration.