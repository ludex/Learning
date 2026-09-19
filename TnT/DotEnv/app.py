from dotenv import load_dotenv
import os

load_dotenv()
# loads .env variables as environment variables

print("-=-=-=-")

API_KEY = os.getenv("API_KEY")
EMAIL_ADDR = os.getenv("EMAIL_ADDR")
PASSWORD = os.getenv("PASSWORD")

if not API_KEY:
    raise RuntimeError("API_KEY must be set in the local environment")

url = "https://example.com/api/"
headers = {"Authorization": f"Bearer {API_KEY}"}
# print("URL is", url)

print("------")

login_info = {
    'email': EMAIL_ADDR,
    'pw': PASSWORD
}
# print("Login info is", login_info)

print("-=-=-=-")
