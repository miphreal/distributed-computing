include baseconfig
include rabbitmq


rabbitmq_user { 'rmq_user':
  admin    => true,
  password => 'rmq_pass'
}
