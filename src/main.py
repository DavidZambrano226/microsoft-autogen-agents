from autogen import AssistantAgent, GroupChat, GroupChatManager
from config.bedrock_config import ollama_config

llm_config = {"config_list": ollama_config}

content_analist = AssistantAgent(
    "content_analist",
    system_message="""You are an AI assistant specialized medical content analyst,
    your task is get relevant medical information and look for trends.""",
    llm_config=llm_config,
)

post_generator = AssistantAgent(
    "post_generator",
    system_message="""You are an AI assistant specialized in creating social media content.
    Your task is to generate posts for various platforms like Twitter, Instagram, and LinkedIn.""",
    llm_config=llm_config,
)

agents = [content_analist, post_generator]
group_chat = GroupChat(
    agents=agents, allow_repeat_speaker=False, messages=[], max_round=2)
manager = GroupChatManager(
    groupchat=group_chat, llm_config=llm_config)

manager.initiate_chat(
    content_analist,
    message="""Generate a social media post about Artificial Intelligence in
    Healthcare. Make it engaging and appropriate for LinkedIn.""",
)
