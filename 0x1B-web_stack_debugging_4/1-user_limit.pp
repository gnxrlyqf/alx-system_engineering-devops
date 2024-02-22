#fix hard limit
exec { 'increase hard file limit':
  command => '/usr/bin/env sed -i "s/5/50000/" /etc/security/limits.conf'
}
#fix soft limit
exec { 'increase soft file limit':
  command => '/usr/bin/env sed -i "s/4/50000/" /etc/security/limits.conf'
}