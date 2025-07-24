from langchain.tools import tool
import requests
import os
from dotenv import load_dotenv
from mcp_server.agents.post_writer_agent import run_post_writer

# Load environment variables
load_dotenv()

LINKEDIN_ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")
LINKEDIN_URN = os.getenv("LINKEDIN_URN")
LINKEDIN_ENDPOINT = "https://api.linkedin.com/v2/ugcPosts"

HEADERS = {
    "Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}",
    "X-Restli-Protocol-Version": "2.0.0",
    "Content-Type": "application/json"
}

@tool
def post_to_linkedin(prompt: str) -> str:
    """
    Generates and posts a professional LinkedIn post from a given idea.
    
    Args:
        prompt (str): User's idea or topic.
    
    Returns:
        str: Status message or post link.
    """
    try:
        # 1. Generate post content
        final_post = run_post_writer(prompt)

        # 2. Post to LinkedIn
        payload = {
            "author": LINKEDIN_URN,
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {"text": final_post},
                    "shareMediaCategory": "NONE"
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }

        response = requests.post(LINKEDIN_ENDPOINT, json=payload, headers=HEADERS)
        if response.status_code == 201:
            return "✅ Post published successfully: https://www.linkedin.com/in/<your-linkedin-username>"
        else:
            return f"❌ Failed to publish: {response.text}"

    except Exception as e:
        return f"❌ Error: {str(e)}"
