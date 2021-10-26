from aws_cdk import core as cdk

from aws_cdk import core

""" 
ATENCAO: Cada recurso contido aqui (https://docs.aws.amazon.com/cdk/api/latest/python/index.html) você deve instalar o pacote dele. No caso abaixo vamos
instalar o EC2 (VPC faz parte da EC2) e criar um user IAM
pip install aws_cdk.aws_ec2
pip install aws_cdk.aws_iam
"""
import aws_cdk.aws_ec2 as ec2 
import aws_cdk.aws_iam as iam

class CdkStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Aqui vamos escrever o código da nossa stack
        # Todos os resources estão aqui https://docs.aws.amazon.com/cdk/api/latest/python/index.html


        # Esta VPC será criada com um CIDR 10.0.0.0/16, 
        # todos os parametros estão aqui https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_ec2/Vpc.html
        # NOTA: Por padrão a AWS vai criar subnets nessa sua VPC, por questões de boas praticas. Rodee um "cdk synth" e veja

        # O primeiro parametro sempre será o escopo do seu stack, neste caso é self pq ele é parte do mesmo constructor.
        # Mas se você tiver outro constructor vc pode herdar o objeto e instanciar a partir dele
        # O segundo parametro é SEMPRE o id do seu objeto, o cdk usa isso para manter o estado
        # Os demais parametros estão no link acima
        vpc = ec2.Vpc(self, "MINHAVPC", cidr="10.0.0.0/16")


        # Mesmo conceito da VPC.. 
        meuuser = iam.User(self, "MEUUSER", user_name="leandro")


        # Rode "cdk synth" e veja o que acontece.




