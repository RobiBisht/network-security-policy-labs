# Lab 1: Password and Account Lockout Policy on Linux (Ubuntu)

## Policy Requirement (4.2)

Passwords must be at least 12 characters long and contain uppercase letters, lowercase letters, digits, and special characters. Passwords must be changed every 90 days. Accounts must be temporarily locked for 15 minutes after 5 failed login attempts.

## Objective

- Configure password complexity requirements.
- Implement password aging policies.
- Configure account lockout after repeated failed authentication attempts.
- Verify password policies and account lockout settings.

## Files Included

| File | Description |
|---|---|
| `pwquality.conf` | Password complexity configuration |
| `login.defs` | Password aging defaults |
| `faillock.conf` | Account lockout configuration |
| `common-auth` | PAM authentication configuration reference |
| `common-account` | PAM account configuration reference |

## Step 1: Install the Password Quality Module

Install the password quality package:

```bash
sudo apt update
sudo apt install -y libpam-pwquality
```

## Step 2: Configure Password Complexity

Open the password quality configuration file:

```bash
sudo nano /etc/security/pwquality.conf
```

Apply the settings from `pwquality.conf`.

### Password Policy Settings

| Setting | Purpose |
|---|---|
| `minlen = 12` | Minimum password length |
| `dcredit = -1` | Require at least one digit |
| `ucredit = -1` | Require at least one uppercase letter |
| `lcredit = -1` | Require at least one lowercase letter |
| `ocredit = -1` | Require at least one special character |
| `maxrepeat = 3` | Limit consecutive repeated characters |
| `usercheck = 1` | Check for username in password |
| `retry = 3` | Allow three password-entry attempts |

Negative credit values require at least the specified number of characters of that type.

## Step 3: Configure Password Aging

Open the login definitions file:

```bash
sudo nano /etc/login.defs
```

Apply the settings from `login.defs`.

### Password Aging Settings

| Setting | Purpose |
|---|---|
| `PASS_MAX_DAYS 90` | Maximum password age of 90 days |
| `PASS_MIN_DAYS 1` | Minimum one day between password changes |
| `PASS_WARN_AGE 7` | Warn users seven days before expiration |

These settings primarily establish defaults for newly created accounts.

## Step 4: Apply Password Aging to an Existing User

Apply the password aging policy to `student1`:

```bash
sudo chage -M 90 -m 1 -W 7 student1
```

Verify the configuration:

```bash
sudo chage -l student1
```

## Step 5: Test Password Complexity

Test password strength using `pwscore`:

```bash
echo "abc123" | pwscore
echo "Tr4in!Stat1on-Blue" | pwscore
```

The first example should fail the configured requirements, while the second should pass the complexity checks and return a score.

Test actual password changes using `passwd` and verify that weak passwords are rejected.

## Step 6: Configure Account Lockout

Open the faillock configuration file:

```bash
sudo nano /etc/security/faillock.conf
```

Apply the settings from `faillock.conf`.

### Account Lockout Settings

| Setting | Purpose |
|---|---|
| `deny = 5` | Lock account after five failed attempts |
| `fail_interval = 900` | Count failures within 15 minutes |
| `unlock_time = 900` | Unlock account after 15 minutes |

## Step 7: Configure PAM Authentication

Back up the existing PAM authentication configuration:

```bash
sudo cp /etc/pam.d/common-auth /etc/pam.d/common-auth.bak
sudo cp /etc/pam.d/common-account /etc/pam.d/common-account.bak
```

Configure the PAM authentication stack using the appropriate Ubuntu PAM configuration.

The repository contains reference snippets in:

- `common-auth`
- `common-account`

**Important:** Preserve Ubuntu's existing PAM rules and module ordering. Do not blindly replace the complete PAM files with the reference snippets.

Keep an administrative session open while testing PAM changes.

## Step 8: Verify Account Lockout

After testing failed authentication attempts for `student1`, inspect the failure records:

```bash
sudo faillock --user student1
```

Reset the failure records when necessary:

```bash
sudo faillock --user student1 --reset
```

## Teaching Point

Account lockout helps prevent online password guessing attacks. However, repeated failed authentication attempts can also lock out legitimate users, creating a denial-of-service risk.

A temporary 15-minute lockout reduces this risk compared with a permanent account lock.

## Verification

- Password complexity settings are configured.
- Password aging is applied to the existing user.
- Weak passwords are rejected.
- Account lockout settings are configured.
- Failed authentication records can be inspected.
- Account lockout can be reset when required.

## Result

Password complexity, password aging, and account lockout policies were configured and verified in Ubuntu Linux to improve account security.

## Screenshots

Screenshots of configuration files, policy verification, and test results are available in the `screenshot/` directory.

## Disclaimer

This practical is intended for educational purposes and authorized lab environments only.