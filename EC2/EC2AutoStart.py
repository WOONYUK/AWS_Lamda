import boto3

region = 'リジョン名（ex:ap-northeast-1）'

instances = [
'インスタンス名'
# 複数の場合は最後,

]

ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))

    return 0
