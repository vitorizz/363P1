import os
from dotenv import load_dotenv

load_dotenv()  
DATABASES = {
    'ENGINE': os.getenv('DATABASE_ENGINE', 'psycopg2'),
    'HOST': os.getenv('DATABASE_HOST', 'localhost'),
    'USER': os.getenv('DATABASE_USER', 'postgres'),
    'PASSWORD': os.getenv('DATABASE_PASSWORD', ''),
    'NAME': os.getenv('DATABASE_NAME', 'stocks'),
    'PORT': int(os.getenv('DATABASE_PORT', 5432))
}
