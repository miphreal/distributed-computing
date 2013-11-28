class {'baseconfig':} ->
class {'app':} ->
class { 'supervisor':
  conf_dir => '/etc/supervisor/conf.d',
  conf_ext => '.conf',
} ->
user { 'flower':
  groups     => $baseconfig::config::project_user,
  ensure  => present,
  shell   => '/bin/bash',
} ->
supervisor::service { 'flower':
  ensure      => present,
  directory   => $baseconfig::config::project_path,
  command     => "/usr/local/bin/celery flower --broker_api=http://rmq_user:rmq_pass@mq1:15672/api/app --address=${hostname} --port=8080 --config=app.config",
  user        => 'flower',
  group       => $baseconfig::config::project_user,
}
