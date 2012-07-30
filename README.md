About Template
==============

このテンプレートは、以下のパッケージを利用します。

ubuntu-12.04-x86_64-5.box
-------------------------

* Ubuntu Server 12.04 TLS 64bit (3.2.0-27-virtual)
* VBoxLinuxAdditions 4.1.18
* Ruby 1.9.3
* Chef 0.10.8

Django-1.4.1-py27-1.pybundle
----------------------------

* Django==1.4.1
* MySQL-python==1.2.3
* gunicorn==0.14.6
* python-memcached==1.48
* pytz==2012d
* setproctitle==1.1.6

Required packages:

* libmysqlclient-dev

Celery-3.0.4-py27-1.pybundle
----------------------------

* celery==3.0.4
* django-celery==3.0.4

Source Layout
=============

プロジェクトには、以下のファイルが含まれます。

    README.md             このファイル
    Vagrantfile           vagrantの設定ファイル
    cookbooks/            chefの設定ファイル
    etc/                  設定ファイル
    log/                  ログファイル
    src/                  ソースコード

Djangoアプリの場合、src/には次のファイルが含まれます。

    manage.py
    myapp/                アプリケーション
      models.py
      views.py
      ...
    project/
      settings.py         共通設定
      settings_vagrant.py vagrant環境の設定
      settings_staging.py ステージング環境の設定
      urils.py
      ...
    static/               静的ファイル
    templates/            テンプレート

Runtime Layout
==============

Vagrant環境では、chefによって次のディレクトリが生成されます。

    /home/vagrant/MYAPP/  = app_dir
      bin/                実行ファイル
      env/                virtualenv
      etc/                -> /vagrant/etc/
      log/                -> /vagrant/log/
      src/                -> /vagrant/src/

etc/ や log/ ディレクトリには、実行時にファイルが生成されます。
これらのファイルは .gitignore で無視するようにします。

cookbooks
=========

myapp
-----

Djangoアプリケーションの設定サンプル。

### recipe[myapp::django]

    :myapp => {
      :owner => 'vagrant',
      :group => 'vagrant',
      :settings => 'project.settings_devel',
      :vagrant_links => ['etc', 'log', 'src'],
      :my_username => 'foo@domain',
      :my_password => '12345678',
    }

アプリケーションのディレクトリ(app_dir)を準備し、Django環境を構築する。
設定ファイルとして":settings"で指定されたモジュールが利用される。

仮想マシン内に自動生成されるスクリプト "bin/manage.py" を用いて、Djangoの
管理コマンドを実行できる。

    $ vagrant ssh
    ...
    vagrant@vagrant-ubuntu-lucid:~$ ./myapp/bin/manage.py syncdb

アプリケーションサーバとして、gunicornがインストールされる。gunicornの起動と
終了は次のようにする。(upstartを利用)

    vagrant@vagrant-ubuntu-precise:~$ sudo start myapp
    myapp start/running, process 4194
    vagrant@vagrant-ubuntu-precise:~$ sudo stop myapp
    myapp stop/waiting

python
------

opscodeによるpythonの共通レシピ。

ChangeLog
=========

* 2012-07-31
 - settings.py の構成変更。
