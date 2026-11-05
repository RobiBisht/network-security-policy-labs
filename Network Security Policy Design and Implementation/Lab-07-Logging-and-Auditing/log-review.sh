# top source addresses of failed SSH logins
sudo grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' \
 | sort | uniq -c | sort -nr | head

# the same on systems that use the journal
sudo journalctl -u ssh --since "24 hours ago" | grep "Failed password"