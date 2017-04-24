## CDH 5 INSTALLATION

 Assuming you have basic knowledge of hadoop we are going ahead with the `cdh 5` installation on `google console`. We created two instances namenode and datanode both having `RHEL 7`.

### Login as root and set password
```vim
sudo su root
```
```vim
Passwd
```
```
Enter password ********
Reenter password ********
```
### Disable firewall
```
systemctl stop firewalld
Service firewalld start
chkconfig firewalld off
```


### To stop iptables and even after the reboot:

```
systemctl stop iptables && chkconfig iptables off
systemctl stop ip6tables && chkconfig ip6tables off
```

### Disable SELINUX
```sh
vi /etc/selinux/config
```
open the above file and change the attribute of SELINUX to `disabled`
##### SELINUX=disabled
System is to be rebooted for the changes to take effect

### SSH Passwordless Keygen

```
ssh-keygen -t rsa 
```
or
```
ssh -keygen 
```
* Now that we generated ssh-keygen, we go to sshd_config and change `permitrootlogin` to `yes`
And  `passwordauthentication` to `yes`
```
vi /etc/ssh/sshd_config
```
* After setting above attributes we must Restart sshd 
```
service sshd restart
```
* Create a file named authorized_keys in namenode as well as datanode
* Copy public key which is in id_rsa.pub to authorized_keys
```
cat id_rsa.pub > authorized_keys
```
* Secure copy the authorized_keys to all other nodes
```
scp authorized_keys datanode:/root/.ssh/test
```
##### Try
```
Ssh datanode
```
##### Do this to all other nodes and you’ll be able to login to other nodes without any prompt for password



### Install web Server in all the servers:

```
yum install -y httpd
```
```
service httpd start && chkconfig httpd on
```

### Got to netwroking/Firewall rules and create firewall rule. Make sure you add the below rule in networking/firewall_rules

name: my_rule
source_tag: 0.0.0.0/0
allowed protocols/ports: tcp:0-65000
network: default


### CDH INSTALLATION
*CDH must be installed in namenode
#### Install wget 

```
yum install wget
```

#### Get the bin file from cloudera 
```
wget http://archive.cloudera.com/cm5/installer/latest/cloudera-manager-installer.bin
```
* The above command downloads the latest installer
chmod u+x cloudera-manager-installer.bin
* After that run the following to install cloudera manager using local repo
```
sudo ./cloudera-manager-installer.bin
```

#### Cloudera Wizard will take you through the following steps if above all of the prerequisites are set properly


#### Login Screen

![GitHub Logo](https://github.com/kaushikamaravadi/Hadoop/blob/master/cdh5_pics/Login.png)

#### Login

![GitHub Logo](https://github.com/kaushikamaravadi/Hadoop/blob/master/cdh5_pics/Login.png)

#### Welcome to Cloudera manager and CDH

![GitHub Logo](https://github.com/kaushikamaravadi/Hadoop/blob/master/cdh5_pics/cdh.png)

#### Hosts

![GitHub Logo](https://github.com/kaushikamaravadi/Hadoop/blob/master/cdh5_pics/hosts.png)

#### JDK Installation

![GitHub Logo](https://github.com/kaushikamaravadi/Hadoop/blob/master/cdh5_pics/jdk.png)

#### Single User

![GitHub Logo](https://github.com/kaushikamaravadi/Hadoop/blob/master/cdh5_pics/single_user.png)

#### SSH Login Credentials

![GitHub Logo](https://github.com/kaushikamaravadi/Hadoop/blob/master/cdh5_pics/ssh_login_credentials.png)

#### Cluster Installation 

![GitHub Logo](https://github.com/kaushikamaravadi/Hadoop/blob/master/cdh5_pics/cluster_installation.png)

#### Cluster Installation

![GitHub Logo](https://github.com/kaushikamaravadi/Hadoop/blob/master/cdh5_pics/cluster_installation1.png)

#### Cluster Installation Completed Successfully 

![GitHub Logo](https://github.com/kaushikamaravadi/Hadoop/blob/master/cdh5_pics/complete.png)

#### Installing Selected Parcels

![GitHub Logo](https://github.com/kaushikamaravadi/Hadoop/blob/master/cdh5_pics/parcels.png)

#### Cluster Setup

![GitHub Logo](https://github.com/kaushikamaravadi/Hadoop/blob/master/cdh5_pics/setup.png)

#### Database Setup

![GitHub Logo](https://github.com/kaushikamaravadi/Hadoop/blob/master/cdh5_pics/setup2.png)

#### First Run

![GitHub Logo](https://github.com/kaushikamaravadi/Hadoop/blob/master/cdh5_pics/first_run.png)

#### Inspect Hosts for Connection

![GitHub Logo](https://github.com/kaushikamaravadi/Hadoop/blob/master/cdh5_pics/inspect1.png)

#### Congrats

![GitHub Logo](https://github.com/kaushikamaravadi/Hadoop/blob/master/cdh5_pics/congrats.png)



