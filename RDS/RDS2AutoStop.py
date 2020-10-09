import boto3


def lambda_handler(event, context):
    dbcluster ='DB クラスター ID'
    client = boto3.client('rds')
    response = client.stop_db_cluster(DBClusterIdentifier=dbcluster)
    print(response)
    return 
