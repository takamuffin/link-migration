# -*- coding: utf-8 -*-
"""
    Neo4j Match Query

    This is a simple match query run against a local Neo4j instance.

"""

import json

version = 0


def up(self):
    """
        Get a count of the total nodes in the graph.

        MATCH (n) RETURN count(n)
    """
    payload = "{\"statements\" : [ {\"statement\" : \"MATCH (n) RETURN count(n)\"} ]}"

    response = self.config.NEO_GRAPH.request(
        "POST",
        self.config.NEO_TRANSACTION_URL,
        data=payload,
        timeout=5
    )
    response_data = json.loads(response.text)

    if response_data.get('errors'):
        print("Neo4j sent an error:", response)
        raise Exception("Encountered Neo4j Error")

    # get count from neo
    total_nodes = response_data['results'][0]['data'][0]['row'][0]
    print("Total count queried from Neo: %s" % total_nodes)


def down(self):
    """
        Get a count of the total nodes in the graph.

        MATCH ()-->() RETURN count(*)
    """
    payload = "{\"statements\" : [ {\"statement\" : \"MATCH ()-->() RETURN count(*)\"} ]}"

    response = self.config.NEO_GRAPH.request(
        "POST",
        self.config.NEO_TRANSACTION_URL,
        data=payload,
        timeout=5
    )
    response_data = json.loads(response.text)

    if response_data.get('errors'):
        print("Neo4j sent an error:", response)
        raise Exception("Encountered Neo4j Error")

    # get count from neo
    total_nodes = response_data['results'][0]['data'][0]['row'][0]
    print("Total count queried from Neo: %s" % total_nodes)
