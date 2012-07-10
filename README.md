basebox
=======

- ubuntu-12.04-x86_64-4.box

Ubuntu Server 12.04 TLS 64bit (3.2.0-24-virtual)
VBoxLinuxAdditions 4.1.16
Ruby 1.9.3-p0
Chef 0.10.8

pybundle
========

- Django-1.4-py27-1.pybundle

Django==1.4
MySQL-python==1.2.3
gunicorn==0.14.3
pytz==2012c
setproctitle==1.1.6

Required packages:
libmysqlclient-dev

- Celery-2.5-py27-1.pybundle

celery==2.5.5
django-celery==2.5.5

Vagrant
=======

仮想マシンを起動。

  $ vagrant up

SSHでログイン。

  $ vagrant ssh

起動後に chef だけ再度実行。

  $ vagrant provision

シャットダウン。

  $ vagrant halt

halt してから up を実行。

  $ vagrant reload

仮想マシンを削除。

  $ vagrant destroy

Source Layout
=============

各プロジェクトは以下のファイルを含みます。

README                  このファイル
Vagrantfile             vagrantの設定ファイル
cookbooks/              chefの設定ファイル
data_bags/              プロジェクトの共通設定やファイルなど

Djangoアプリでは、更に次のようなファイルを含みます。

project/                サイト設定
  settings.py
  urils.py
  ...
manage.py
myapp/                  アプリケーション
static/                 静的ファイル
templates/              共通テンプレート

Runtime Layout
==============

Vagrant環境では、Vagrantfileで指定したファイルが次の場所にバインドされます。

/home/vagrant/MYAPP/

仮想マシン内部では、更にchefによって以下のディレクトリが生成されます。

/home/vagrant/MYAPP/    = app_dir
  bin/                  実行ファイル
  env/                  virtualenv

chef、または実行時に生成されるいくつかのファイルは、Vagrant環境ではホストPCから
参照できるようになります。(例えば、設定ファイルやログファイルなど)

このテンプレートでは、以下のファイルが実行時に生成されます。

log/access.log
log/error.log
project/gunicorn.py
project/settings_local.py

こうしたファイルは .gitignore で無視するようにします。

cookbooks
=========

myapp
-----

Djangoアプリケーションの設定サンプル。

- recipe[myapp::default]

  :myapp => {
    :owner => 'vagrant',
    :group => 'vagrant',
    :vagrant_links => ['log', 'manage.py', 'myapp', 'project'],
    :settings_local => 'settings_devel.py.erb',
    :my_username => 'foo@domain',
    :my_password => '12345678',
  }

アプリケーションのディレクトリをセットアップし、設定ファイルを自動生成します。

:vagrant_links で指定したファイルに対してシンボリックリンクが生成され、ホストPCの
ファイルが仮想マシンから直接参照されるようになります。

:settings_local で指定したテンプレート(cookbooks/myapp/templates/default/*)
に値を埋めて、"project/settings_local.py" を生成します。

生成された settings_local.py は開発中に直接編集しても構いませんが、chefによって
上書きされるので、テンプレートの更新を忘れないようにします。

- recipe[myapp::django]

Djangoスタック。data_bagsで指定したpackages、pybundles、pipsをインストールし、
gunicornをセットアップします。(supervisordにより起動)

gunicornのログは、プロジェクトの log/ に生成されます。gnucornの状態確認、及び起動、
終了は次のようにします。

vagrant@vagrant-ubuntu-lucid:~$ sudo supervisorctl status
myapp                            RUNNING    pid 4901, uptime 0:09:15
vagrant@vagrant-ubuntu-lucid:~$ sudo supervisorctl stop myapp
myapp: stopped
vagrant@vagrant-ubuntu-lucid:~$ sudo supervisorctl start myapp
myapp: started

manage.pyをvirtualenv環境で実行するスクリプト "bin/manage.py" が生成されます。
次のようにして実行できます。

$ vagrant ssh
...
vagrant@vagrant-ubuntu-lucid:~$ ./myapp/bin/manage.py syncdb

data_bags
=========

- apps/myapp.json

myappの構成定義。

ChangeLog
=========

* 2012-04-13

** レイアウト変更。src以下としていたファイルをトップレベルに移動。
