import autogen
import os

config_list_bedrock = [
    {
        "api_type": "bedrock",
        "model": "amazon.titan-text-express-v1",
        "aws_region": os.environ.get("REGION", "us-east-1"),
        "aws_access_key": os.environ.get("AWS_ACCESS_KEY_ID"),
        "aws_secret_key": os.environ.get("AWS_SECRET_ACCESS_KEY"),
        "price": [0.003, 0.015],
        "temperature": 0.1,
        "cache_seed": None,
    }
]

assistant = autogen.AssistantAgent(
    "assistant",
    llm_config={
        "config_list": config_list_bedrock,
    },
)

user_proxy = autogen.UserProxyAgent(
    "user_proxy",
    human_input_mode="NEVER",
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False,
    },
    is_termination_msg=lambda x: x.get(
        "content", "") and "TERMINATE" in x.get("content", ""),
    max_consecutive_auto_reply=1,
)

user_proxy.initiate_chat(
    assistant,
    message="""Write a python program to print the first
    10 numbers of the Fibonacci sequence. Just output the python code, 
    no additional information.""",
)