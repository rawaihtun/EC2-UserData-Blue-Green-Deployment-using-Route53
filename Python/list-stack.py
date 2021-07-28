# Function: EvaluateOrphanedStacks
# Purpose: List out stacks based on the state and accounts
import boto3
import json
from datetime import datetime
from datetime import date
# from utils import make_cloudformation_client, load_config, get_log_level

# client = make_cloudformation_client(args.config)

stack_session = boto3.client('cloudformation')
paginator = stack_session.get_paginator('list_stacks')
response_iterator = paginator.paginate(StackStatusFilter=['CREATE_COMPLETE'])
for page in response_iterator:
    stack = page['StackSummaries']
    for output in stack:
        print(output['StackName'])
