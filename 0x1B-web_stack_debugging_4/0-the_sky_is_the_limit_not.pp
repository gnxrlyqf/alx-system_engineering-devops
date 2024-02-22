#fix user limit
exec { 'nginx fix':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}
exec { '/usr/bin/env service nginx restart': }