# Puppet script to modify the /etc/security/limits.conf file, replacing 'holberton' with 'foo' to resolve file limit issues.
exec { '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf': }
