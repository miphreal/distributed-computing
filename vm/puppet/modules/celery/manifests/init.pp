class celery {
  group {'celery':
    ensure  => present,
  } ->
  user { 'celery':
    gid     => 'celery',
    ensure  => present,
    shell   => '/bin/bash',
  } ->
  file { '/etc/default/celeryd':
    content => template('celery/celeryd.erb'),
    owner   => 'root',
    group   => 'root',
    notify  => Service['celeryd'],
  } ->
  file { '/etc/init.d/celeryd':
    source  => 'puppet:///modules/celery/celeryd',
    owner   => 'root',
    group   => 'root',
    mode    => 755,
  } ->
  file { '/etc/init.d/celerybeet':
    source  => 'puppet:///modules/celery/celerybeet',
    owner   => 'root',
    group   => 'root',
    mode    => 755,
  } ->
  service { 'celeryd':
    ensure  => running,
    enable  => true,
  }
}
