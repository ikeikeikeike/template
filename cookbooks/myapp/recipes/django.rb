# The Django application stack
# 
# Author: Keisuke Nishida
# Version: 0.4
# Date: 2012-06-13

app_id = 'myapp'
app_node = node[:myapp]
app_data = data_bag_item('apps', app_id)
app_dir = app_node['deploy_to'] || "/home/#{app_node[:owner]}/#{app_id}"

# python setup

package "python-dev"
package "python-pip"
package "python-virtualenv"

directory app_dir do
  owner app_node[:owner]
  group app_node[:group]
  mode '0755'
  recursive true
end

python_virtualenv app_id do
  path "#{app_dir}/env"
  interpreter "python"
  owner app_node[:owner]
  group app_node[:group]
  action :create
end

if app_data['packages']
  app_data['packages'].each do |pkg,ver|
    package pkg do
      action :install
      version ver if ver && ver != "latest"
    end
  end
end

if app_data['pybundles']
  app_data['pybundles'].each do |pybundle|
    file_name = pybundle.split(/[\\\/]/).last

    remote_file "#{app_dir}/env/#{file_name}" do
      source pybundle
      owner app_node[:owner]
      mode "0644"
      action :create_if_missing
    end

    execute file_name do
      command "#{app_dir}/env/bin/pip install #{file_name} > #{app_dir}/env/#{file_name}.log"
      creates "#{app_dir}/env/#{file_name}.log"
      cwd "#{app_dir}/env"
      user app_node[:owner]
    end
  end
end

if app_data['pips']
  app_data['pips'].each do |pip,ver|
    python_pip pip do
      version ver if ver && ver != "latest"
      virtualenv "#{app_dir}/env"
      action :install
    end
  end
end

# django

python_pip "django" do
  virtualenv "#{app_dir}/env"
  action :install
end

file "#{app_dir}/bin/manage.py" do
  owner app_node[:owner]
  group app_node[:group]
  mode "0755"
  action :create
  content <<-EOH
#!/bin/sh
. #{app_dir}/env/bin/activate
cd #{app_dir}/src
export PROJECT_ROOT=#{app_dir}
export PYTHONPATH=#{app_dir}/src
python manage.py $@
EOH
end

# gunicorn

GUNICORN_CONF = "#{app_dir}/etc/gunicorn.py"

["setproctitle", "gunicorn"].each do |pkg|
  python_pip pkg do
    virtualenv "#{app_dir}/env"
    action :install
  end
end

template GUNICORN_CONF do
  source "gunicorn.py.erb"
  owner app_node[:owner]
  group app_node[:group]
  mode "0644"
  variables :app_id => app_id, :app_dir => app_dir, :app_node => app_node
  notifies :reload, "service[#{app_id}]"
end

file "/etc/init/#{app_id}.conf" do
  owner "root"
  group "root"
  mode "0644"
  action :create
  content <<-EOH
description "Application server for #{app_id}"
start on runlevel [2345]
stop on runlevel [!2345]

script
  . #{app_dir}/env/bin/activate
  cd #{app_dir}/src
  export PROJECT_ROOT=#{app_dir}
  export PYTHONPATH=#{app_dir}/src
  exec gunicorn_django -c #{GUNICORN_CONF} --user #{app_node[:owner]} --group #{app_node[:group]}
end script
EOH
  notifies :restart, "service[#{app_id}]"
end

service app_id do
  provider Chef::Provider::Service::Upstart
  supports :status => true, :restart => true, :reload => true
  action [ :enable, :start ]
end