import boto3


def lambda_handler(event, context):
    dbcluster ='snadbs001-cluster-1'
    client = boto3.client('rds')
    response = client.start_db_cluster(DBClusterIdentifier=dbcluster)
    print(response)
    return 
