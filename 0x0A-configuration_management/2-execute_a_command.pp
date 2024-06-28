# create a manifest

exec { 'pkill':
  command  => 'pkill -f killmenow',
  provider => 'shell',
}
