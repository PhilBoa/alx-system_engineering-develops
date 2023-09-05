# This Puppet manifest configures Nginx and performs a 301 redirection

  package { 'nginx':
    ensure => installed,
  }

  file { '/var/www/html/nginx':
    ensure => 'directory',
  }

  exec { 'display_page':
    command => '/usr/bin/sudo /bin/echo Hello World! > /var/www/html/nginx/index.nginx-debian.html',
  }

  exec { 'redirect_config':
    command => '/usr/bin/sudo /bin/echo "location /redirect_me { return 301 http://innovateweb.tech; }" >> /etc/nginx/sites-available/default',
  }

  exec { 'server_start':
    command => '/usr/bin/sudo /usr/sbin/service nginx start',
  }                                                              
