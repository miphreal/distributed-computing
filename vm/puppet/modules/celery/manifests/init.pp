class celery {
  include baseconfig::config

  user { 'celery':
    groups  => $baseconfig::config::project_user,
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
  file { '/var/run/celery':
    ensure  => directory,
    owner   => 'celery',
    group   => 'appuser',
  } ->
  service { 'celeryd':
    ensure  => running,
    enable  => true,
  }
}
