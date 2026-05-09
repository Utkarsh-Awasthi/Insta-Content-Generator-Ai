import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env file

# Posting time in 24-hour format (UK time) change based on your timezone
POSTING_TIME = os.getenv("POSTING_TIME", "10:00")  # Default to 10:00 AM

# Content settings
CONTENT_NICHE = os.getenv("CONTENT_NICHE", "[Content-----Niche-----Name---here]")
HASHTAGS_STR = os.getenv("HASHTAGS", "[Your------Hashtags-----here]")
HASHTAGS = [tag.strip() for tag in HASHTAGS_STR.split(",")] if HASHTAGS_STR else []

# Validation
required_vars = [
    "ANTHROPIC_API_KEY",
    "INSTAGRAM_ACCESS_TOKEN",
    "INSTAGRAM_USER_ID",
    "UNSPLASH_ACCESS_KEY"
]

missing = [var for var in required_vars if not os.getenv(var)]
if missing:
    raise EnvironmentError(
        f"Missing required environment variables: {', '.join(missing)}\n"
        f"Please check your .env file (copy from .env.example)"
    )