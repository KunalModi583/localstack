from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
)


class CdkLocalStackStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('cdk_local_stack'),
            handler='hello.handler',
        )