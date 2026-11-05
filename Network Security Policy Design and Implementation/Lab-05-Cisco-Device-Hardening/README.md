# Lab 5: Cisco Device Hardening, Port Security and ACLs

## Policy Requirements (4.3, 4.4)

SSH-only management with individual accounts, encrypted passwords, a warning banner, port security against rogue devices, and student VLAN restricted from admin and server VLANs.

## Objective

To secure Cisco network devices in Packet Tracer by configuring SSH-based administrative access, individual administrator accounts, password protection, warning banners, switch port security, and extended access control lists (ACLs) for VLAN traffic restrictions.

## Files Used

| File | Purpose |
|---|---|
| `device-hardening.txt` | Router and switch management security |
| `port-security.txt` | Access switch port security configuration |
| `student-acl.txt` | Student VLAN extended ACL configuration |
| `README.md` | Lab procedure and verification |
| `screenshot/` | Evidence of configuration and testing |

## Step 1: Secure Cisco Device Administrative Access

Open the router or switch CLI in Cisco Packet Tracer.

Use the commands from `device-hardening.txt` to configure:

- Device hostname and domain name
- Encrypted enable password
- Individual administrator account
- Minimum password length
- Legal warning banner
- SSH version 2
- SSH authentication retry and timeout limits
- Login brute-force protection
- Console and remote access restrictions
- SSH-only remote management

Save the configuration:

```text
write memory
```

## Step 2: Configure Switch Port Security

Open the access switch CLI.

Use the commands from `port-security.txt` to:

- Configure access ports
- Enable port security
- Limit the number of permitted MAC addresses
- Enable sticky MAC address learning
- Configure violation shutdown
- Enable spanning-tree PortFast and BPDU Guard
- Disable unused switch ports
- Assign unused ports to VLAN 999

Save the configuration:

```text
write memory
```

## Step 3: Configure the Student VLAN ACL

Open the router CLI.

Use the commands from `student-acl.txt` to create the extended ACL named `STUDENT-IN`.

The ACL implements the following policy:

- Allow DHCP traffic
- Allow DNS traffic
- Permit HTTP and HTTPS access to the web server
- Deny access to the admin VLAN
- Deny other access to the server VLAN
- Permit HTTP and HTTPS browsing to other destinations
- Deny remaining traffic

Apply the ACL inbound on the student VLAN subinterface:

```text
interface gigabitEthernet 0/0.20
 ip access-group STUDENT-IN in
```

Save the configuration:

```text
write memory
```

## Step 4: Verify Device Hardening

Check the remote access configuration:

```text
show running-config | section line vty
show ip ssh
```

Verify SSH-only management and SSH version 2.

## Step 5: Verify Port Security

Check port security:

```text
show port-security
show port-security interface fastEthernet 0/1
```

Verify that port security is enabled and the configured maximum MAC address limit is applied.

## Step 6: Verify ACL Configuration

Display the extended ACL:

```text
show access-lists STUDENT-IN
```

Verify ACL application:

```text
show ip interface gigabitEthernet 0/0.20 | include access list
```

Observe ACL hit counters to confirm that traffic matches the configured rules.

## Step 7: Test Student VLAN Restrictions

From a student PC in Cisco Packet Tracer, test the following:

### Test 1: Admin VLAN Access

```text
ping 192.168.10.10
```

Expected result: Access should fail because the admin VLAN is restricted.

### Test 2: Web Server Access

Open the student PC web browser and visit:

```text
http://192.168.30.10
```

Expected result: The web page should load if the web server is running.

### Test 3: HTTPS Access

Visit:

```text
https://192.168.30.10
```

Expected result: HTTPS access should work if the server has HTTPS configured.

### Test 4: ACL Hit Counters

Run:

```text
show access-lists STUDENT-IN
```

Expected result: ACL counters increase when student traffic matches the configured rules.

## Result

Cisco device management was secured using SSH version 2, individual administrator accounts, password protection, and a legal warning banner.

Switch port security was configured to limit unauthorized device connections. An extended ACL was applied to the student VLAN to restrict access to the admin and server VLANs while permitting required DHCP, DNS, HTTP, and HTTPS traffic.

The configurations were verified using Cisco IOS show commands and Packet Tracer connectivity tests.

## Screenshots

Store screenshots demonstrating:

- SSH configuration and device hardening
- SSH version verification
- Port security configuration
- Port security verification
- Student VLAN ACL configuration
- ACL hit counters
- Failed student access to admin VLAN
- Successful student access to web server

## Teaching Point

Extended ACLs are processed from top to bottom, and the first matching rule determines the action.

ACL hit counters provide visible evidence that network access restrictions are being enforced.

## Disclaimer

This lab was performed in Cisco Packet Tracer for educational purposes. All configurations and tests were conducted in a simulated network environment.