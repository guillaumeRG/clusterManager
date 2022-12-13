# clusterManager
for Linux Debian
to run this with python V2:
python run.py

in cfg/
to configure dependencies build a file with the name of the service like this :
is_install;hostname1,hostname2,...;service1,service2...
started;hostname1,hostname2,...;service1,service2...

the line is_install -> the nodes and services needed to be installed
the line started -> the nodes and services needed to be started

to setup a configuration chain build a file like this :
target;hostname1,hostname2,...
services;service1,service2,...
link;[link to another configuration file]
