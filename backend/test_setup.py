"""
Test if all dependencies are installed correctly
"""

print("Testing imports...")

try:
    import fastapi
    print("✅ FastAPI installed")
except ImportError:
    print("❌ FastAPI not installed")

try:
    import pandas
    print("✅ Pandas installed")
except ImportError:
    print("❌ Pandas not installed")

try:
    import sklearn
    print("✅ Scikit-learn installed")
except ImportError:
    print("❌ Scikit-learn not installed")

try:
    import nltk
    print("✅ NLTK installed")
except ImportError:
    print("❌ NLTK not installed")

try:
    import requests
    print("✅ Requests installed")
except ImportError:
    print("❌ Requests not installed")

try:
    from dotenv import load_dotenv
    print("✅ python-dotenv installed")
except ImportError:
    print("❌ python-dotenv not installed")

print("\n🎉 All dependencies ready!")
