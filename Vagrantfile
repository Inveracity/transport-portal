# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.define "testbox" do |dev|
    dev.vm.box = "ubuntu/xenial64"
    dev.vm.host_name = "testbox"
    dev.vm.network :private_network, ip: "10.1.1.2"
    config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--memory", "4096"]
        vb.customize ["modifyvm", :id, "--ioapic", "on"]
        vb.customize ["modifyvm", :id, "--cpus", "2"]
        vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
        vb.linked_clone = true
    config.vm.synced_folder ".", "/vagrant",
        type: "virtualbox",
        mount_options: ["dmode=775,fmode=775"]
    end
    config.vm.provision "shell", path: "scripts/vagrant.sh"
  end
end
