# Lab 5 - Cisco Device Hardening, Port Security, and ACLs

## Aim
Harden Cisco router/switch management and restrict student VLAN traffic using Packet Tracer.

## Policy Requirements
- SSH-only management with individual accounts and encrypted passwords.
- Warning banner and login throttling.
- Port security against unauthorized devices.
- Student VLAN restricted from admin and server VLANs.

## Tools and Technologies
Cisco Packet Tracer, Cisco IOS CLI, VLANs, SSH, port security, ACLs.

## Implementation

### 1. Secure device access
Apply the router/switch hardening commands from the practical:
```text
enable
configure terminal
hostname STI-R1
no ip domain-lookup
ip domain-name sti.local
enable secret <lab-enable-secret>
service password-encryption
security passwords min-length 10
username netadmin secret <lab-admin-secret>
banner motd # Authorised use only. Activity is monitored and logged. #
crypto key generate rsa modulus 2048
ip ssh version 2
ip ssh time-out 60
ip ssh authentication-retries 3
login block-for 120 attempts 3 within 60
line console 0
 login local
 exec-timeout 5 0
 logging synchronous
line vty 0 4
 login local
 transport input ssh
 exec-timeout 5 0
end
write memory
```
Use lab-only secrets; never publish real credentials.

### 2. Configure port security
Configure access ports with port security, sticky MAC addresses, a maximum of two MAC addresses, shutdown on violation, PortFast, and BPDU Guard. Shut down unused ports and place them in an unused VLAN as shown in the practical manual.

### 3. Configure student VLAN ACL
Create the `STUDENT-IN` extended ACL following the practical's rule order:
- Permit DHCP and DNS.
- Permit HTTP/HTTPS to the specified web server.
- Deny student VLAN access to admin and server VLAN networks.
- Permit internet HTTP/HTTPS.
- Deny remaining traffic.
Apply it inbound on `GigabitEthernet0/0.20`.

### 4. Verify
```text
show running-config | section line vty
show ip ssh
show port-security
show port-security interface fastEthernet 0/1
show access-lists STUDENT-IN
show ip interface gigabitEthernet 0/0.20 | include access list
```
Test the policy from a student PC in Packet Tracer.

## Verification
- SSH settings and port-security status are visible in CLI.
- ACL hit counters increase during tests.
- Admin VLAN access is blocked from the student VLAN; permitted web access works.

## Screenshots
Store Packet Tracer topology, CLI configuration, and test screenshots in `screenshots/`.

## Result
Cisco device hardening, port security, and student VLAN ACL restrictions were configured and verified in Packet Tracer.

## Learning Outcomes
- Hardened Cisco device management.
- Configured access-port security.
- Created and applied an extended ACL.
- Verified policy behavior with CLI counters and connectivity tests.
