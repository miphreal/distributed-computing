class baseconfig {
  include baseconfig::config

  exec { 'apt-get update':
    command => '/usr/bin/apt-get update';
  }

  host {
    'hostmachine':
      ip => '192.168.0.101';

    'mon1':
      ip => '192.168.0.21';

    'mq1':
      ip => '192.168.0.41';

    'worker1':
      ip => '192.168.0.61';
    'worker2':
      ip => '192.168.0.62';
    'worker3':
      ip => '192.168.0.63';
  }
}


