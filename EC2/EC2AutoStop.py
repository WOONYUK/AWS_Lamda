import boto3

region = 'リジョン名（ex:ap-northeast-1）'

instances = [
'インスタンス名'
# 複数の場合は最後,

]

ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))

    return 0
