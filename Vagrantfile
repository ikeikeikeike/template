# -*- mode: ruby -*-
# vi: set ft=ruby :

BOX = "ubuntu-12.04-x86_64-4"
BOX_URL = "http://bizmo.s3-website-ap-northeast-1.amazonaws.com/boxes/ubuntu-12.04-x86_64-4.box"
COOKBOOKS_PATH = "cookbooks"
DATA_BAGS_PATH = "data_bags"

Vagrant::Config.run do |config|
  config.vm.box = BOX
  config.vm.box_url = BOX_URL
  config.vm.provision :chef_solo do |chef|
    chef.cookbooks_path = COOKBOOKS_PATH
    chef.data_bags_path = DATA_BAGS_PATH
    chef.add_recipe("myapp")
    chef.json = {
      :myapp => {
        :owner => 'vagrant',
        :group => 'vagrant',
        :web_port => '8000',
        # for vagrant
        :vagrant_links => ['etc', 'log', 'src'],
        # for production
#        :local_settings => 'production.py.erb',
#        :db_host => 'localhost',
#        :db_name => 'template',
#        :db_user => 'username',
#        :db_password => 'password',
#        :my_username => 'foo@domain',
#        :my_password => '12345678',
      },
    }
  end
end
