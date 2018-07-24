import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


# check if MongoDB is installed and version is right
def test_mongo_is_installed(host):
    mongo = host.package("mongodb-org")
    assert mongo.is_installed
    assert mongo.version.startswith("3.2")


# check if MongoDB is enabled and running
def test_mongo_running_and_enabled(host):
    mongo = host.service("mongod")
    assert mongo.is_running
    assert mongo.is_enabled


# check if configuration file contains the required line
def test_config_file(host):
    config_file = host.file('/etc/mongod.conf')
    assert config_file.contains('bindIp: 127.0.0.1')
    assert config_file.is_file


# check if MongoDB is listening port
def test_mongo_listening_port(host):
    mongo = host.socket("tcp://127.0.0.1:27017")
    assert mongo.is_listening
