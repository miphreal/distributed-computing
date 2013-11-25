#!/bin/sh

MODULES='/etc/puppet/modules:/tmp/vagrant-puppet/modules-0'
PUPPET_TARGET='/etc/puppet/modules'
mkdir -p $PUPPET_TARGET
[ ! -d "$PUPPET_TARGET/rabbitmq" ] &&
puppet module install --target-dir $PUPPET_TARGET --modulepath $MODULES puppetlabs-rabbitmq ||
[ ! -d "$PUPPET_TARGET/python" ] &&
puppet module install --target-dir $PUPPET_TARGET --modulepath $MODULES stankevich-python || exit 0
