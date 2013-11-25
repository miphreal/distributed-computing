class app {
  include baseconfig::config

  user { $baseconfig::config::project_user:
    ensure => present,
    shell => '/bin/bash',
  } ->
  class { 'python':
    version    => 'system',
    pip        => true,
    dev        => true,
    virtualenv => true,
  } ->
  python::requirements { $baseconfig::config::project_reqs:
    virtualenv  => 'system',
  }
}


