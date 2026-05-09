import requests
import os
from dotenv import load_dotenv

load_dotenv()


class UnsplashClient:
    def __init__(self):
        self.access_key = os.getenv("UNSPLASH_ACCESS_KEY")
        self.base_url = "https://api.unsplash.com"

    def search_finance_images(self, query, count=1):
        """Search for UK-relevant finance images"""
        if not self.access_key:
            print("Warning: Unsplash API key not configured")
            return None

        headers = {"Authorization": f"Client-ID {self.access_key}"}
        params = {
            "query": f"{query} [Content----Niche-----Name-here]",
            "per_page": count,
            "orientation": "landscape"
        }

        try:
            response = requests.get(
                f"{self.base_url}/search/photos",
                headers=headers,
                params=params,
                timeout=10
            )
            response.raise_for_status()
            results = response.json().get("results", [])
            return results[0]["urls"]["regular"] if results else None
        except Exception as e:
            print(f"Unsplash API error: {e}")
            return None

    def get_fallback_image(self):
        """Return a reliable fallback image URL"""
        return "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e"  # Generic  image