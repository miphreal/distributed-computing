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

    'db1':
      ip => '192.168.0.31';

    'mq1':
      ip => '192.168.0.41';

    'worker1':
      ip => '192.168.0.61';
    'worker2':
      ip => '192.168.0.62';
    'worker3':
      ip => '192.168.0.63';
    'worker4':
      ip => '192.168.0.64';

    'client1':
      ip => '192.168.0.81';
  }
}


