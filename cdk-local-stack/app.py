#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_local_stack.cdk_local_stack_stack import CdkLocalStackStack


app = cdk.App()
CdkLocalStackStack(app, "cdk-local-stack")

app.synth()
