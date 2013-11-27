include baseconfig


class { 'rabbitmq':
  admin_enable  => true,
  node_ip_address => $ipaddress_eth1,
}

rabbitmq_user { 'rmq_user':
  admin    => true,
  password => 'rmq_pass'
} ->
rabbitmq_vhost { 'app':
  ensure => present,
} ->
rabbitmq_user_permissions { "rmq_user@app":
  configure_permission => '.*',
  read_permission      => '.*',
  write_permission     => '.*',
}
