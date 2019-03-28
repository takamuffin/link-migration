[![Build Status](https://api.travis-ci.org/takamuffin/link-migration.png)](https://api.travis-ci.org/takamuffin/link-migration)

Link Migration
==============

A generic tool for schema and data migrations.

The primary inspirations for this library came from Alembic, Django, and Hibernate/Liquibase. The ultimate goal is to allow a lightweight migration framework to be deployed into any technology stack. Much of this currently relies on the user to implement, however with time more and more integrations will be added to the default set.


Version
=======

0.0.12


Installation
============

If you have pip available on your system, just type::

```pip install link-migration```

If you’ve already got an old version of link-migration, and want to upgrade, use:

```pip install --upgrade link-migration```


Usage Introduction
==================

The first thing you’ll need to define is the conf.py file and to specify its location: `link_migration -c "path_to_file/conf.py"`

Below are the minimum requirements for definitions in conf.py. The important step here is to specify where the migrations folder exists so they can be detected, and to specify where to store and fetch the versions for executed migrations.

```
import os
import requests
import json

ROOT_DIR = 'link_migration.example_migrations'
MIGRATIONS_ABS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
MIGRATIONS_DIR = 'link_migration.example_migrations'


def get_current_version():
    path = "%s/current_version.txt" % MIGRATIONS_ABS_PATH
    with open(path, "r+") as f:
        content = f.read()
    return int(content)


def set_current_version(version):
    path = "%s/current_version.txt" % MIGRATIONS_ABS_PATH
    with open(path, "w") as f:
        content = f.write(f'{version}')
    return int(content)
```

Link Migration uses the _version_ information to track the migrations schema and to 
decide the order of execution of the scripts. Link Migration will go through all .py 
files in your directory and execute all of them _version_ order.


Migrating to a specific version
===============================

If you want, you can migrate your database schema to a specific version by 
informing the --to (or -t) parameter. The attribute _version_ of the migration
file will be used as unique identifier:

    $ link-migration --to=00.00.01

If you don’t specify any version, using --up or --down, Link Migration will migrate 
the schema to the latest version available in the migrations directories 
specified in the config file.
