# -*- mode: ruby -*-
# vi: set ft=ruby :

BOX = "ubuntu-12.04-x86_64-5"
BOX_URL = "http://bizmo.s3-website-ap-northeast-1.amazonaws.com/boxes/ubuntu-12.04-x86_64-5.box"
COOKBOOKS_PATH = "cookbooks"

Vagrant::Config.run do |config|
  config.vm.box = BOX
  config.vm.box_url = BOX_URL
  config.vm.forward_port 8000, 8000
  config.vm.forward_port 8008, 8008
  config.vm.provision :chef_solo do |chef|
    chef.cookbooks_path = COOKBOOKS_PATH
    chef.add_recipe("myapp::django")
    chef.add_recipe("myapp::celery")
    chef.add_recipe("myapp::mysql")
    chef.json = {
      :myapp => {
        :owner => 'vagrant',
        :group => 'vagrant',
        :web_port => '8000',
        # for vagrant
        :settings => 'project.settings_devel',
        :vagrant_links => ['etc', 'log', 'src'],
        # for production
#        :settings => 'project.settings_production',
#        :settings_template => 'production.py.erb',
#        :db_host => 'localhost',
#        :db_name => 'template',
#        :db_user => 'username',
#        :db_password => 'password',
#        :my_username => 'foo@domain',
#        :my_password => '12345678',
      },
    }
  end
  config.vm.customize do |vm|
    vm.memory_size = 768
    vm.name = "ubuntu11.10-server-amd64"
  end
end
