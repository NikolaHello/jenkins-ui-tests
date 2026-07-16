from dotenv import load_dotenv
import os

load_dotenv()

JENKINS_URL = os.getenv("JENKINS_URL")
JENKINS_USER = os.getenv("JENKINS_USER")
JENKINS_PASSWORD = os.getenv("JENKINS_PASSWORD")

print("URL:", JENKINS_URL)
print("USER:", JENKINS_USER)
print("PASSWORD:", JENKINS_PASSWORD)