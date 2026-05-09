import schedule
import time
import logging
import sys
from claude_client import ClaudeClient
from unsplash_client import UnsplashClient
from instagram_poster import InstagramPoster
from config import POSTING_TIME

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("instagram_agent.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


def daily_post_job():
    """Main job to generate and post daily content"""
    try:
        logger.info("=== Starting daily Instagram post job ===")

        # Initialize clients
        claude = ClaudeClient()
        unsplash = UnsplashClient()
        poster = InstagramPoster()

        # 1. Generate content idea
        logger.info("Generating post idea...")
        idea = claude.generate_post_idea()
        logger.info(f"Generated idea: {idea[:100]}...")

        # 2. Create caption
        logger.info("Generating caption...")
        caption = claude.generate_caption(idea)
        logger.info(f"Generated caption ({len(caption)} chars)")

        # 3. Get relevant image
        logger.info("Searching for relevant image...")
        image_url = unsplash.search_finance_images("budget saving investing")

        if not image_url:
            logger.warning("No suitable image found from Unsplash, using fallback")
            image_url = unsplash.get_fallback_image()

        logger.info(f"Using image: {image_url}")

        # 4. Post to Instagram
        logger.info("Posting to Instagram...")
        post_id = poster.post_content(image_url, caption)

        if post_id:
            logger.info(f"✅ Successfully posted! Post ID: {post_id}")
        else:
            logger.error("❌ Failed to publish post to Instagram")

    except Exception as e:
        logger.error(f" Critical error in daily post job: {str(e)}", exc_info=True)
    finally:
        logger.info("=== Daily post job completed ===\n")


def start_scheduler():
    """Start the daily scheduling loop"""
    logger.info(f"Scheduler configured to post daily at {POSTING_TIME} UK time")
    schedule.every().day.at(POSTING_TIME).do(daily_post_job)

    # Run immediately for testing (remove in production if you don't want immediate post)
    # daily_post_job()

    logger.info("Scheduler started. Waiting for scheduled time...")
    while True:
        schedule.run_pending()
        time.sleep(30)  # Check every 30 seconds for more responsive scheduling


if __name__ == "__main__":
    try:
        start_scheduler()
    except KeyboardInterrupt:
        logger.info("Scheduler stopped by user")
    except Exception as e:
        logger.error(f"Scheduler crashed: {e}", exc_info=True)
        sys.exit(1)