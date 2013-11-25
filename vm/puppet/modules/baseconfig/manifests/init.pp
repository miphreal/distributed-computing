class baseconfig {
  include baseconfig::config

  exec { 'apt-get update':
    command => '/usr/bin/apt-get update';
  }

  host {
    'hostmachine':
      ip => '192.168.0.101';

    'mq1':
      ip => '192.168.0.41';

    'worker1':
      ip => '192.168.0.61';
    'worker2':
      ip => '192.168.0.62';
  }

  class { 'python':
    version    => 'system',
    pip        => true,
    dev        => true,
    virtualenv => true,
  } ->
  file { ["/var/local/${baseconfig::config::project_name}", "${baseconfig::config::project_venv}"]:
    ensure => "directory",
    owner  => $baseconfig::config::project_user,
    group  => $baseconfig::config::project_user,
    mode   => 750,
  } ->
  python::virtualenv { $baseconfig::config::project_venv:
    ensure       => present,
    owner        => $baseconfig::config::project_user,
    group        => $baseconfig::config::project_user,
  } ->
  notify {$baseconfig::config::project_reqs:} ->
  python::requirements { $baseconfig::config::project_reqs:
    virtualenv  => 'system',
  }
}


