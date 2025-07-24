import os
from dotenv import load_dotenv

load_dotenv()

def get_headers():
    return {
        "Authorization": f"Bearer {os.getenv('LINKEDIN_ACCESS_TOKEN')}",
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json"
    }

def get_urn():
    return os.getenv("LINKEDIN_URN")

def get_endpoint():
    return "https://api.linkedin.com/v2/ugcPosts"
