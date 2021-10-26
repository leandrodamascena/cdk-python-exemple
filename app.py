#!/usr/bin/env python3
import os

from aws_cdk import core as cdk

from aws_cdk import core

from cdk.cdk_stack import CdkStack


# Isso aqui é a instância do construtor da sua Stack.. Quando evoluir mais você pode cria os seus, mas por enquanto vamos fazer tudo dentro do Stack padrão.

# Esta stack fica dentro da pasta cdk

app = core.App()
CdkStack(app, "CdkStack")

app.synth()
