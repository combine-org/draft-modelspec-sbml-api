# -*- mode: ruby -*-
# vi: set ft=ruby :

#
# configure a linux vm using virtual box
#

# usage: vagrant up [--provision]
#        vagrant ssh
#        vagrant halt
#        vagrant destroy

Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/jammy64"
  config.vm.synced_folder ".", "/vagrant"   #for ansible_local provisioning

  config.vm.provider "virtualbox" do |vb|
    vb.cpus = "2"
    vb.memory = "2048"
    vb.customize ["modifyvm", :id, "--vram", "256"]
    vb.gui = true
  end

  config.vm.provision "ansible_local" do |ansible|
    ansible.provisioning_path = "/vagrant/ansible_local"
    ansible.playbook = "playbook.yaml"
    ansible.install = "true"
  end

  config.vm.provision :shell do |shell|
    shell.privileged = true
    shell.inline = 'echo rebooting'
    shell.reboot = true
  end
  
end
