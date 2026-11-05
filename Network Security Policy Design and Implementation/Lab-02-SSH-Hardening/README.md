# Lab 2: SSH Hardening

## Policy Requirement (4.3)

Administrative access uses SSH only, individual accounts, no direct root login, key-based authentication, and shows a legal warning banner.

## Objective

To secure SSH remote administration on an Ubuntu server by disabling root login and password authentication, enforcing SSH key-based authentication, restricting permitted users, configuring connection limits, and displaying a legal warning banner.

## Files Used

| File | Purpose |
|---|---|
| `sshd_config` | SSH daemon security configuration |
| `issue.net` | Legal warning banner displayed during SSH login |
| `README.md` | Lab procedure, commands, and verification |
| `screenshot/` | Evidence of configuration and testing |

## Step 1: Generate SSH Keys and Copy Them to the Server

On the administrator workstation, generate an SSH key pair:

```bash
ssh-keygen -t ed25519 -C "admin@sti"
```

Copy the public key to the Ubuntu server:

```bash
ssh-copy-id student1@192.168.30.10
```

Test SSH key authentication:

```bash
ssh student1@192.168.30.10
```

Confirm that login works using the SSH key before continuing.

## Step 2: Configure SSH Daemon Security

Create a backup of the original SSH configuration:

```bash
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak
```

Edit the SSH daemon configuration:

```bash
sudo nano /etc/ssh/sshd_config
```

Configure the following security settings:

```text
PermitRootLogin no
PubkeyAuthentication yes
PasswordAuthentication no
PermitEmptyPasswords no
MaxAuthTries 3
LoginGraceTime 30
AllowUsers student1 netadmin
ClientAliveInterval 300
ClientAliveCountMax 2
X11Forwarding no
Banner /etc/issue.net
```

Save the file and exit the editor.

**Important:** Ubuntu may include additional SSH configuration files inside `/etc/ssh/sshd_config.d/`. Check the effective configuration using `sshd -T` to ensure the intended security settings are applied.

## Step 3: Configure the Legal Warning Banner

Create or edit the SSH warning banner:

```bash
sudo nano /etc/issue.net
```

Add the following warning message:

```text
*** Authorised use only. Activity is monitored and logged. ***
*** Unauthorised access is prohibited and may be prosecuted. ***
```

Save the file and exit.

## Step 4: Test and Reload SSH Configuration

Validate the SSH configuration syntax:

```bash
sudo sshd -t
```

No output indicates that the configuration syntax is valid.

Reload the SSH