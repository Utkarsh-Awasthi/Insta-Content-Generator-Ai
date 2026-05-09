import requests
import os
from dotenv import load_dotenv

load_dotenv()


class InstagramPoster:
    def __init__(self):
        self.access_token = os.getenv("INSTAGRAM_ACCESS_TOKEN")
        self.user_id = os.getenv("INSTAGRAM_USER_ID")
        self.base_url = "https://graph.instagram.com/v18.0"  # Using v18.0

    def create_media_container(self, image_url, caption):
        """Create a media container for Instagram post"""
        if not all([self.access_token, self.user_id]):
            print("Error: Instagram credentials not configured")
            return None

        endpoint = f"{self.base_url}/{self.user_id}/media"
        params = {
            "image_url": image_url,
            "caption": caption,
            "access_token": self.access_token
        }

        try:
            response = requests.post(endpoint, params=params, timeout=15)
            response.raise_for_status()
            result = response.json()
            return result.get("id")
        except Exception as e:
            print(f"Instagram API error creating media container: {e}")
            print(f"Response: {response.text if 'response' in locals() else 'No response'}")
            return None

    def publish_media(self, creation_id):
        """Publish the media container"""
        if not self.access_token:
            print("Error: Instagram access token not configured")
            return None

        endpoint = f"{self.base_url}/{self.user_id}/media_publish"
        params = {
            "creation_id": creation_id,
            "access_token": self.access_token
        }

        try:
            response = requests.post(endpoint, params=params, timeout=15)
            response.raise_for_status()
            result = response.json()
            return result.get("id")
        except Exception as e:
            print(f"Instagram API error publishing media: {e}")
            print(f"Response: {response.text if 'response' in locals() else 'No response'}")
            return None

    def post_content(self, image_url, caption):
        """Full posting workflow"""
        print(f"Attempting to post image: {image_url[:50]}...")
        creation_id = self.create_media_container(image_url, caption)
        if creation_id:
            print(f"Media container created: {creation_id}")
            post_id = self.publish_media(creation_id)
            if post_id:
                print(f"Successfully published! Post ID: {post_id}")
                return post_id
            else:
                print("Failed to publish media container")
        else:
            print("Failed to create media container")
        return None