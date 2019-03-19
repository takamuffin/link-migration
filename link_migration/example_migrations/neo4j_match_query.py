# -*- coding: utf-8 -*-
"""
    Neo4j Match Query

    This is a simple match query run against a local Neo4j instance.

"""

version = 0.5


def up(self):
    """
        Get a count of the total nodes in the graph.

        MATCH (n) RETURN count(n)
    """
    payload = "{\"statements\" : [ {\"statement\" : \"MATCH (n) RETURN count(n)\"} ]}"

    response_data = self.config.post_neo(data=payload)

    # get count from neo
    total_nodes = response_data['results'][0]['data'][0]['row'][0]
    print("Total count queried from Neo: %s" % total_nodes)


def down(self):
    """
        Get a count of the total nodes in the graph.

        MATCH ()-->() RETURN count(*)
    """
    payload = "{\"statements\" : [ {\"statement\" : \"MATCH ()-->() RETURN count(*)\"} ]}"

    response_data = self.config.post_neo(data=payload)

    # get count from neo
    total_nodes = response_data['results'][0]['data'][0]['row'][0]
    print("Total count queried from Neo: %s" % total_nodes)
