class app {
  include baseconfig::config

  file { $baseconfig::config::project_path:
    source  => "/vagrant",
    owner   => $baseconfig::config::project_user,
    group   => $baseconfig::config::project_user,
    recurse => true,
  } ->
  class { 'python':
    version    => 'system',
    pip        => true,
    dev        => true,
    virtualenv => true,
  } ->
  python::requirements { '/vagrant/requirements.txt':
    virtualenv  => 'system',
  }
}


