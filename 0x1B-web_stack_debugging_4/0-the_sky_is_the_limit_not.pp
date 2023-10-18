# Puppet script that fix high load requests by increasing the limit of allowed requests
exec { '/usr/bin/env sed -i s/15/2000/ /etc/default/nginx': }
-> exec { '/usr/bin/env service nginx restart': }
