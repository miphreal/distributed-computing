class baseconfig::config {
  $project_name = 'dc'
  $project_path = '/vagrant'
  $project_venv = "/var/local/${project_name}/venv"
  $project_reqs = "${project_path}/requirements.txt"
  $project_user = 'appuser'

  user { $project_user:
    ensure => present,
    shell => '/bin/bash',
  }
}
