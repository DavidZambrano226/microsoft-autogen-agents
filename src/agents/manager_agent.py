from config.bedrock_config import config_bedrock
from autogen import AssistantAgent, UserProxyAgent


def create_social_media_agent():
    return AssistantAgent(
        name="SocialMediaAgent",
        system_message="""You are an AI assistant specialized in creating 
        engaging social media content. Your task is to generate posts for 
        various platforms like Twitter, Instagram, and LinkedIn.""",
        llm_config={
            "config_list": config_bedrock,
        },
    )


def generate_social_media_post(topic, platform):
    social_media_agent = create_social_media_agent()
    user_proxy = UserProxyAgent(
        name="UserProxy",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=1,
    )

    user_proxy.initiate_chat(
        social_media_agent,
        message=f"""Generate a {platform} post 
        about {topic}. Make it engaging and 
        appropriate for the platform.""",
    )

    # Extract the generated post from the conversation
    conversation = user_proxy.chat_messages[social_media_agent]
    generated_post = conversation[-1]["content"]

    return generated_post


# Example usage
if __name__ == "__main__":
    topic = "Artificial Intelligence in Healthcare"
    platform = "LinkedIn"
    post = generate_social_media_post(topic, platform)
    print(f"Generated {platform} post about {topic}:")
    print(post)
