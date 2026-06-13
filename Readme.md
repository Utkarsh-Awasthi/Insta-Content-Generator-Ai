# 🤖 Instagram Content Agent 

An automated Python system that generates and posts daily financial content to Instagram using:
- **Anthropic Claude API** for content ideation and caption writing
- **Unsplash API** for sourcing relevant, high-quality images
- **Instagram Basic Display API** for publishing posts
- **Schedule library** for daily automation

Perfect for running a personal finance page like "Your-insta-page" with minimal manual effort.

## ✨ Features

- 💡 **AI-Generated Content**: Fresh post ideas and engaging captions tailored to your niche
- 🖼️ **Smart Image Sourcing**: Automatic retrieval of relevant finance/budgeting images from Unsplash
- ⏰ **Daily Automation**: Posts automatically at your specified time each day
- 📊 **Error Handling**: Comprehensive logging and graceful fallbacks for API failures
- 🔧 **Easy Configuration**: All settings via environment variables
- 📱 **Platform Optimized**: Creates vertical-friendly content ideal for Instagram

## 🚀 Setup Instructions

### 1. Get Required API Keys
- **[Anthropic Claude API](https://console.anthropic.com/)** → Create account → Get API key
- **[Instagram Basic Display API](https://developers.facebook.com/docs/instagram-basic-display-api)** → 
  1. Create Facebook Developer account
  2. Create App → Add Instagram Basic Display
  3. Generate User Token (requires logging into your Instagram account)
  4. Get your Instagram Business Account ID
- **[Unsplash API](https://unsplash.com/developers)** → Create account → Get access key

### 2. Configure Environment
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your actual API keys:
# - ANTHROPIC_API_KEY=your_actual_claude_key
# - INSTAGRAM_ACCESS_TOKEN=your_actual_instagram_token
# - INSTAGRAM_USER_ID=your_actual_instagram_business_id
# - UNSPLASH_ACCESS_KEY=your_actual_unsplash_key
# - POSTING_TIME=10:00 (optional - defaults to 10:00 AM UK time)
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Agent
```bash
# For immediate testing (will post once then wait for schedule):
python main.py

# For background execution (recommended for production):
# Using nohup:
nohup python main.py &

# Or using screen/tmux for persistent session:
screen
python main.py
# Press Ctrl+A then D to detach
```

## 📝 How It Works

1. **Daily at Scheduled Time** (default 10:00 AM UK time):
   - Claude generates a fresh post idea for your niche
   - Creates an engaging caption with personal finance tips (ISAs, fractional shares, etc.)
   - Searches Unsplash for relevant content for example- finance imagery (saving, investing, budgeting)
   - Posts the image + caption to Instagram via Basic Display API

2. **Content Focus**:
   - Accessible investing for beginners (small amounts, simple apps)
   - Actionable advice with clear calls-to-action
   - Engagement-boosting questions in captions
   - Strategic hashtags for UK personal finance community

## ⚙️ Customization

| What to Change | Where to Change | Example                                                     |
|----------------|----------------|-------------------------------------------------------------|
| **Posting Time** | `.env` → `POSTING_TIME` | `"18:30"` for 6:30 PM                                       |
| **Content Niche** | `.env` → `CONTENT_NICHE` | `"Your Niche"`                                              |
| **Hashtags** | `.env` → `HASHTAGS` | `----Hashtags----`                                          |
| **Image Search Terms** | `unsplash_client.py` → `search_finance_images()` | Change `"budget saving investing"` to `"student budget uk"` | (Example)

## ⚠️ Important Notes

### Instagram API Limitations
- The Basic Display API allows posting to **personal accounts only**
- For business accounts with advanced features (insights, promotion), consider:
  - Facebook Graph API (requires Facebook Page connection)
  - Third-party tools like Buffer, Later, or Hootsuite
  - Instagram's newer Content Publishing API (requires Instagram Business/Creator account)

### Content Responsibility
- AI-generated financial advice should be reviewed for accuracy
- Consider adding disclaimer: " For educational purposes only."

### Troubleshooting
- **"Authentication failed"**: Verify API keys in `.env` have correct permissions
- **"No image found"**: Try broader search terms or check Unsplash API limits
- **"Post failed"**: Check Instagram token validity (tokens expire ~60 days)
- **Scheduler not running**: Ensure script stays active (use screen/tmux or systemd service)
- **Check logs**: See `instagram_agent.log` for detailed error information

## 📋 Example Output

**Generated Idea**: 
"Show how £5/day invested in FTSE 100 tracker fund grows over 10 years vs. keeping in savings account - with real UK numbers accounting for inflation."

**Generated Caption**:
"💰 Let's talk about the power of starting small with investing in the UK!

Did you know that investing just £5 per day (that's less than your daily coffee!) in a low-cost FTSE 100 index fund could grow to over £23,000 in 10 years? 

Meanwhile, keeping that same £1,825 per year in a standard savings account earning 0.5% interest would only grow to about £19,500 - and that's BEFORE accounting for inflation eating away at your purchasing power.

The key isn't timing the market - it's TIME IN the market. Start with what you can afford, be consistent, and let compound growth work its magic.

What's one small change you could make today to start investing your spare change? 👇

#UKBudgetHacking #PersonalFinance #Investing #MoneySaving #UKFinance #StockMarketForBeginners #FTSE100 #ISAAccount"

## 🛡️ Security Notes

- **Never commit your `.env` file** to version control (it's already in `.gitignore` if using Git)
- Consider using a secrets manager for production deployments
- Regularly rotate your API keys, especially Instagram tokens
- Monitor usage to avoid unexpected API charges

## 📜 License

MIT License - feel free to modify and use for your personal page!

## 💡 Next Steps

1. Test with a personal Instagram account first
2. Monitor engagement and refine your content strategy
3. Consider adding:
   - Comment auto-responses for common questions
   - Weekly performance analytics email
   - Story generation for behind-the-scenes content
   - Reel/video generation using similar principles

Happy posting! 
