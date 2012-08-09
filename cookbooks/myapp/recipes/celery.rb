# The Django Celery stack
# 
# Author: Keisuke Nishida <knishida@bizmobile.co.jp>
# Version: 0.1
# Date: 2012-08-09

app_id = 'myapp'
app_node = node[:myapp]
app_dir = app_node['deploy_to'] || "/home/#{app_node[:owner]}/#{app_id}"

# rabbitmq

include_recipe "rabbitmq"

# log

directory "/var/log/celery" do
  owner "root"
  group "root"
  mode "0755"
end

template "/etc/logrotate.d/celery" do
  source "logrotate.d/celery.erb"
  owner "root"
  group "root"
  mode "0644"
end

# celery worker

file "/etc/init/celeryd.conf" do
  owner "root"
  group "root"
  mode "0644"
  action :create
  content <<-EOH
description "Celery worker"
start on runlevel [2345]
stop on runlevel [!2345]

script
  exec #{app_dir}/bin/manage.py celery worker -f /var/log/celery/celeryd.log -l INFO
end script
EOH
  notifies :restart, "service[celeryd]"
end

service "celeryd" do
  provider Chef::Provider::Service::Upstart
  supports :status => true, :restart => true, :reload => true
  action [ :enable, :start ]
end

# celery beat

file "/etc/init/celerybeat.conf" do
  owner "root"
  group "root"
  mode "0644"
  action :create
  content <<-EOH
description "Celery beat"
start on started celeryd
stop on stopping celeryd

script
  exec #{app_dir}/bin/manage.py celery beat -f /var/log/celery/celerybeat.log -l INFO --schedule=/var/run/celerybeat-schedule
end script
EOH
  notifies :restart, "service[celerybeat]"
end

service "celerybeat" do
  provider Chef::Provider::Service::Upstart
  supports :status => true, :restart => true, :reload => true
  action [ :enable, :start ]
end
