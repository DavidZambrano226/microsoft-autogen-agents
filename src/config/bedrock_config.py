import os

config_bedrock = [
    {
        "api_type": "bedrock",
        "model": "anthropic.claude-3-5-sonnet-20240620-v1:0",
        "aws_region": os.environ.get("REGION", "us-east-1"),
        "aws_access_key": os.environ.get("AWS_ACCESS_KEY_ID"),
        "aws_secret_key": os.environ.get("AWS_SECRET_ACCESS_KEY"),
        "price": [0.003, 0.015],
        "temperature": 0.1,
        "cache_seed": None,
    },
    {
        "model": "codellama",
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama",
    }
]
