domain = 'local.edu'

# host machine - 192.168.0.101
# management systems - 192.168.0.21 - .29
# dbs - 192.168.0.31 - .39
# mqs - 192.168.0.41 - .49 & .40 - can work as a cluster access point
# workers - 192.168.0.61 - .79
# clients - 192.168.0.81 - .99

nodes = [
  # http://mon1.local.edu:8080/
  { :hostname => 'mon1',     :ip => '192.168.0.21', :box => 'precise32', :ram => 256, :provision => 'mon-celery' },

  { :hostname => 'db1',      :ip => '192.168.0.31', :box => 'precise32', :ram => 256, :provision => 'redis' },

  # http://mq1:15672/  -- rabbitmq admin dashboard (http://mq1.local.edu:15672/)
  { :hostname => 'mq1',      :ip => '192.168.0.41', :box => 'precise32', :ram => 256, :provision => 'mq' },

  { :hostname => 'worker1',  :ip => '192.168.0.61', :box => 'precise32', :ram => 256, :provision => 'worker' },
  { :hostname => 'worker2',  :ip => '192.168.0.62', :box => 'precise32', :ram => 256, :provision => 'worker' },
  { :hostname => 'worker3',  :ip => '192.168.0.63', :box => 'precise32', :ram => 256, :provision => 'worker' },
  { :hostname => 'worker4',  :ip => '192.168.0.64', :box => 'precise32', :ram => 256, :provision => 'worker' },

  { :hostname => 'client1',  :ip => '192.168.0.81', :box => 'precise32', :ram => 256, :provision => 'client', :ui => true },
]

Vagrant.configure("2") do |config|
    config.ssh.shell = "bash -c 'BASH_ENV=/etc/profile exec bash'"
    nodes.each do |node|

        config.vm.define node[:hostname] do |node_config|
            node_config.vm.box = node[:box]
            node_config.vm.host_name = node[:hostname] + '.' + domain
            node_config.vm.network :public_network, :public_network => "eth0", :ip => node[:ip]

            node_config.vm.provider :virtualbox do |vb|
                memory = node[:ram] ? node[:ram] : 256
                vb.customize [
                    'modifyvm', :id,
                    '--name', node[:hostname],
                    '--memory', memory.to_s
                ]
                vb.gui = node[:ui]
            end

            provision = node[:provision] ? node[:provision] : 'worker'
            node_config.vm.provision :puppet do |puppet|
                puppet.manifests_path = 'vm/puppet/manifests'
                puppet.manifest_file = provision + '.pp'
                puppet.module_path = 'vm/puppet/modules'
            end
        end
    end



    config.vm.provision :shell, :path => 'vm/common.sh'
end
