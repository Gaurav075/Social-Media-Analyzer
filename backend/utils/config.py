"""
Configuration settings for the application
"""
import os
from dotenv import load_dotenv

load_dotenv()

# API Settings
DEBUG = os.getenv("DEBUG", "True") == "True"
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))

# Database
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./social_analyzer.db")

# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN", "")

# Scraping
MAX_TWEETS = int(os.getenv("MAX_TWEETS", 100))
MAX_LINKEDIN_POSTS = int(os.getenv("MAX_LINKEDIN_POSTS", 50))

print("✅ Config loaded successfully")
