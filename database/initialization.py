import os
from dotenv import load_dotenv
from supabase import create_client
load_dotenv()

db_client = create_client(os.getenv("SUSUPABASE_URL"), os.getenv("SUPABASE_API_KEY"))