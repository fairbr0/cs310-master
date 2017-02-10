#!/bin/sh
elasticdir=elasticSearch
#$elasticdir/bin/elasticsearch -E node.data=false -E node.master=true -E node.name=NoData
$elasticdir/bin/elasticsearch -E node.name=DataOne
