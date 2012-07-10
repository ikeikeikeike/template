# Sample recipe

app_id = 'myapp'
app_node = node[:myapp]
app_data = data_bag_item('apps', app_id)
app_dir = app_node['deploy_to'] || "/home/#{app_node[:owner]}/#{app_id}"

# application directories
["#{app_dir}", "#{app_dir}/bin"].each do |dir|
  directory dir do
    owner app_node[:owner]
    group app_node[:group]
    mode '0755'
    recursive true
  end
end

# symbolic links
if app_node[:vagrant_links]
  app_node[:vagrant_links].each do |name|
    link "#{app_dir}/#{name}" do
      to "/vagrant/#{name}"
      owner app_node[:owner]
      group app_node[:group]
    end
  end
end

# local_settings.py
if app_node[:local_settings]
  template "#{app_dir}/etc/local_settings.py" do
    source app_node[:local_settings]
    owner app_node[:owner]
    group app_node[:group]
    mode "0644"
  end
end

# install the Django stack
include_recipe "#{app_id}::django"
