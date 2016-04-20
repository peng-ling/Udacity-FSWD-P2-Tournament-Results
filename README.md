#Udacity Full Stack Web Developer Nanodegree P2 Tournament Results#

##How to run this project##

1 This project makes use of [vagrant](https://www.vagrantup.com/), so you first need to download and install it.
  With vagrant one can create and configure virtual development environments. It can be seen as a higher-level wrapper around virtualization software such as VirtualBox.
2 The virtualization software used for tis project is [VirtualBox](https://www.virtualbox.org/), so this needs to be
  installed, too.
3 Once this is done, cd to folder ./vagrant in a terminal and run vagrant up to start the vm.
4 Once the VM has started you can establish a ssh connection by running vagrant ssh.
5 Next is to set up the [PostgreeSQL Database](http://www.postgresql.org/). To do so cd to folder /vagrant/tournament in your
  ssh session and (/vagrant is the shared folder of the VM and the host). Run psql to start the postgree command line sql client
  and then \i tournament.sql to run the script which will first create the tournament data base and then run the ddl statements
  for the database objects necessary for this project.
6 Run python_test.py in your ssh terminal in folder /vagrant/tournament. This will test if all functions which are part of this
  project doing as supposed to.

##Additional Information##

This project is running with [Python 2.7.6](https://www.python.org/download/releases/2.7.6/) and
[psycopg](http://initd.org/psycopg/) as a PostgreeSQL adapter.

I followed the [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/), but
decided to use tabs instead of spaces for indention.
