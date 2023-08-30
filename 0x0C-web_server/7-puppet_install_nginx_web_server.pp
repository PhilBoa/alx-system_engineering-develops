# This Puppet manifest configures Nginx and performs a 301 redirection

package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure => running,
  enable => true,
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file { '/etc/nginx/sites-available/default':
  source => 'puppet:///etc/nginx/nginx.conf',
  notify => Service['nginx'],
}

file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

exec { 'disable_default_site':
  command => 'rm /etc/nginx/sites-enabled/default',
  onlyif  => 'test -L /etc/nginx/sites-enabled/default',
  notify  => Service['nginx'],
}

exec { 'redirect_config':
  command => '/bin/echo "location /redirect_me { return 301 http://innovateweb.tech; }" >> /etc/nginx/sites-available/default',
  unless  => '/bin/grep -q "location /redirect_me { return 301 http://innovateweb.tech; }" /etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify  => Service['nginx'],
}
