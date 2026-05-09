import anthropic
import os
from dotenv import load_dotenv

load_dotenv()


class ClaudeClient:
    def __init__(self):
        self.client = anthropic.Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )

    def generate_post_idea(self, niche=None):
        """Generate a creative Instagram post idea"""
        if niche is None:
            niche = os.getenv("CONTENT_NICHE", "UK budget hacking")

        prompt = f"""Generate a creative Instagram post idea for a {niche} page.
        Include: 
        1. A compelling hook
        2. Educational value about accessible investing for UK audience
        3. A clear call-to-action
        4. Suggested visual concept
        Keep it under 2 sentences for the idea description."""

        try:
            message = self.client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=300,
                messages=[{"role": "user", "content": prompt}]
            )
            return message.content[0].text.strip()
        except Exception as e:
            print(f"Claude API error in generate_post_idea: {e}")
            # Fallback idea if API fails
            return "Show how £5/day invested in FTSE 100 tracker fund grows over 10 years vs. keeping in savings account"

    def generate_caption(self, idea, hashtags=None):
        """Write an engaging Instagram caption based on the idea"""
        if hashtags is None:
            hashtags = os.getenv("HASHTAGS",
                                 "#UKBudgetHacking,#PersonalFinance,#Investing,#MoneySaving,#UKFinance,#StockMarketForBeginners").split(
                ",")
            hashtags = [tag.strip() for tag in hashtags if tag.strip()]

        hashtags_str = " ".join(hashtags) if hashtags else ""

        prompt = f"""Write an engaging Instagram caption based on this idea: {idea}
        Requirements:
        - Friendly, informative tone suitable for UK audience
        - Include a personal finance tip with UK-specific context (ISAs, fractional shares, etc.)
        - End with a question to boost engagement
        {"Include these hashtags: " + hashtags_str if hashtags_str else ""}
        Keep under 2,200 characters."""

        try:
            message = self.client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=500,
                messages=[{"role": "user", "content": prompt}]
            )
            return message.content[0].text.strip()
        except Exception as e:
            print(f"Claude API error in generate_caption: {e}")
            # Fallback caption
            return f"💡 {idea}\n\n{hashtags_str}"