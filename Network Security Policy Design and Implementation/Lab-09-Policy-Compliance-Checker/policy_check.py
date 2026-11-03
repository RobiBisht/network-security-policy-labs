#!/usr/bin/env python3
"""policy_check.py - check a Linux host against the STI Network Security Policy."""
import os
import re
import stat
import subprocess
import sys

def run(cmd):
 try:
 r = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
 return r.stdout
 except (FileNotFoundError, subprocess.TimeoutExpired):
 return ""

def read_pairs(path, sep=None):
 """Read 'key value' or 'key = value' files into a dict (lower-case keys)."""
 data = {}
 try:
 with open(path) as f:
 for line in f:
 line = line.split("#", 1)[0].strip()
 if not line:
 continue
 parts = line.split(sep, 1) if sep else line.split(None, 1)
 if len(parts) == 2:
 data[parts[0].strip().lower()] = parts[1].strip()
 except (FileNotFoundError, PermissionError):
 pass
 return data

def sshd_effective():
 out = run(["sshd", "-T"]) or run(["/usr/sbin/sshd", "-T"])
 cfg = {}
 for line in out.splitlines():
 parts = line.split(None, 1)
 if len(parts) == 2:
 cfg[parts[0].lower()] = parts[1].strip()
 return cfg

ssh = sshd_effective()
pwq = read_pairs("/etc/security/pwquality.conf", sep="=")
logindefs = read_pairs("/etc/login.defs")
results = []

def check(ref, text, ok, detail):
 results.append((ref, text, ok, detail))

# 4.3 SSH rules
v = ssh.get("permitrootlogin", "unknown")
check("4.3", "Root login over SSH disabled", v == "no", "PermitRootLogin=" + v)

v = ssh.get("passwordauthentication", "unknown")
check("4.3", "SSH password login disabled", v == "no", "PasswordAuthentication=" + v)

v = ssh.get("maxauthtries", "0")
check("4.3", "MaxAuthTries <= 4", v.isdigit() and int(v) <= 4, "MaxAuthTries=" + v)

# 4.2 Password rules
v = pwq.get("minlen", "0")

check("4.2", "Minimum password length >= 12", v.isdigit() and int(v) >= 12, "minlen=" + v)

v = logindefs.get("pass_max_days", "99999")
ok = v.isdigit() and int(v) <= 90
check("4.2", "Password max age <= 90 days", ok, "PASS_MAX_DAYS=" + v)

# 4.5 Firewall active (UFW or nftables with a default drop policy)
ufw = run(["ufw", "status"])
nft = run(["nft", "list", "ruleset"])
ufw_on = "Status: active" in ufw
nft_on = re.search(r"policy drop", nft) is not None
detail = "no firewall found"
if ufw_on:
 detail = "ufw active"
elif nft_on:
 detail = "nftables drop policy"
check("4.5", "Host firewall active with default deny", ufw_on or nft_on, detail)

# File permission rule: /etc/shadow must not be world-readable
try:
 mode = stat.S_IMODE(os.stat("/etc/shadow").st_mode)
 check("4.1", "/etc/shadow has no world permissions", (mode & 0o007) == 0, oct(mode))
except OSError as e:
 check("4.1", "/etc/shadow permissions", False, str(e))

# 4.9 Auditing service
active = run(["systemctl", "is-active", "auditd"]).strip() == "active"
check("4.9", "auditd running", active, "active" if active else "not active")

# Report
if os.geteuid() != 0:
 print("Warning: run as root for accurate results.\n")
print("%-5s %-45s %-6s %s" % ("Ref", "Requirement", "Result", "Detail"))
print("-" * 90)
failed = 0
for ref, text, ok, detail in results:
 failed += 0 if ok else 1
 print("%-5s %-45s %-6s %s" % (ref, text, "PASS" if ok else "FAIL", detail))
print("-" * 90)
print("%d of %d checks passed" % (len(results) - failed, len(results)))
sys.exit(1 if failed else 0)

chmod +x policy_check.py
sudo ./policy_check.py
echo $? # 0 = all passed, 1 = at least one failure