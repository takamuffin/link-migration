# -*- coding: utf-8 -*-
import os
import requests

abs_path = os.path.abspath('')

folder = "%s/example_migrations" % abs_path.replace('/framework', '')

ROOT_DIR = 'link_migration.example_migrations'
MIGRATIONS_DIR = 'link_migration.example_migrations'


NEO_HOST = 'localhost'
NEO_PORT = '7474'
NEO_USER = 'neo4j'
NEO_PASSWORD = 'password'
NEO_TRANSACTION_URL = f"http://{NEO_HOST}:{NEO_PORT}/db/data/transaction/commit"

NEO_GRAPH = requests.Session()
NEO_GRAPH.headers = {'Content-Type': "application/json"}
NEO_GRAPH.auth = requests.auth.HTTPBasicAuth(NEO_USER, NEO_PASSWORD)


def get_current_version():
    path = "%s/current_version.txt" % folder
    with open(path, "r+") as f:
        content = f.read()
    return int(content)


def set_current_version(version):
    path = "%s/current_version.txt" % folder
    with open(path, "w") as f:
        content = f.write(f'{version}')
    return int(content)