
#######
#Define the application configurations
#######

elasticClusterAddr = 'localhost'
elasticClusterPort= 9200
elasticCluster = {'host':elasticClusterAddr, 'port', elasticClusterPort}

summationServiceAddr = 'localhost'
summationServicePort = 6000
summationService {'host':summationServiceAddr, 'port', summationServiceAddr}

restServiceAddr = 'localhost'
restServicePort = 5000
restService = {'host':restServiceAddr, 'port':restServicePort}
