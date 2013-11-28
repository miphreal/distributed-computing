class baseconfig::config {
  $project_name = 'dc'
  $project_path = '/opt/app'
  $project_reqs = "${project_path}/requirements/default.txt"
  $project_user = 'appuser'

  group { $baseconfig::config::project_user:
    ensure => present,
  } ->
  user { $baseconfig::config::project_user:
    gid   => $baseconfig::config::project_user,
    ensure => present,
    shell => '/bin/bash',
  }
}
