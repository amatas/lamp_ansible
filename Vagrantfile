# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.define "dbserver" do |dbserver|

    dbserver.vm.box = "centos65"
    dbserver.vm.box_url = "https://github.com/2creatives/vagrant-centos/releases/download/v6.5.1/centos65-x86_64-20131205.box"

    dbserver.vm.hostname = 'dbserver'
    dbserver.vm.network "private_network", ip: "192.168.50.12"

  end  

  config.vm.define "lampserver" do |lampserver|

    lampserver.vm.box = "centos65"
    lampserver.vm.box_url = "https://github.com/2creatives/vagrant-centos/releases/download/v6.5.1/centos65-x86_64-20131205.box"

    lampserver.vm.hostname = 'lampserver'
    lampserver.vm.network "private_network", ip: "192.168.50.11"

    lampserver.vm.provision "ansible" do |ansible|

      ansible.host_key_checking = false
      ansible.sudo = true
      ansible.extra_vars = { 
        ansible_ssh_user: 'vagrant',
      } 
            
      ansible.playbook = "lamp/mediawiki.yml"
      ansible.groups = {
        "webservers" => ["lampserver"],
        "dbservers" => ["dbserver"],
        "all_groups:children" => ["webservers", "dbservers"]
      }
      ansible.limit = 'all'
      ansible.raw_arguments  = "--ask-vault-pass"
#     Debug option
#      ansible.raw_arguments  = "--vault-password-file=secret_file_plain_pass"
#      ansible.verbose = 'vvvv'
    end
  end
end
