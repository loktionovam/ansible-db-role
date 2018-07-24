db
=========

[![Build Status](https://travis-ci.org/loktionovam/db.svg?branch=master)](https://travis-ci.org/loktionovam/db)

Simple mongodb role

Requirements
------------

Install requirements:

```bash
pip install 'ansible>=2.4' 'molecule>=2.6' 'testinfra>=1.10' 'python-vagrant>=0.5.15' 'ansible-lint==3.4.20'
```

Role Variables
--------------

```yaml
# Mongo database version
# For example:
mongo_version: 3.2
```

```yaml
# MongoDB repo url
# For example:
mongo_repo: "deb http://repo.mongodb.org/apt/ubuntu {{ ansible_distribution_release }}/mongodb-org/{{ mongo_version }} multiverse"
```

```yaml
# MongoDB packages list
# For example:
mongo_packages:
  - mongodb-org
```

```yaml
# MongoDB listening port
# For example:
mongo_port: 27017
```

```yaml
# MongoDB bind IP address
# For example:
mongo_bind_ip: 127.0.0.1
```

```yaml
# Role execution environment (local, stage, prod)
# For example:
env: local
```

Dependencies
------------

none

Example Playbook
----------------

```yaml
---
- name: Configure MongoDB
  hosts:
    - db

  roles:
    - role: db
      mongo_bind_ip: 0.0.0.0
```

License
-------

BSD

Author Information
------------------

Aleksandr Loktionov
