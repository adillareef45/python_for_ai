import os
from dotenv import load_dotenv

load_dotenv()

# Read from environment
api_key = os.environ.get('API_KEY')
database = os.environ.get('DATABASE_URL', 'default.db')

print(f"Using database: {api_key}")
print(f"Using database: {database}")