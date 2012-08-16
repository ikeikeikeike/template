package "mysql-server"
package "mysql-client"

# create a mysql database
mysql_database 'template' do
  connection ({:host => "localhost", :username => 'root', :password => ""})
  action :create
end
