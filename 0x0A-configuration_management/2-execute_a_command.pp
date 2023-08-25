# This Puppet manifest kills the "killmenow" process using pkill
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => ['/bin', '/usr/bin'],
  }
