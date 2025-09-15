import subprocess
import os

'''

If you have issues running the setup.py, then you 
can copy and paste this into your terminal to install 
the python dependencies and set the env vars

pip3 install -r requirements.txt

GOOGLE_CLOUD_PROJECT="replace_with_your_GCP_project_ID"
GOOGLE_CLOUD_LOCATION="us-central1"
GOOGLE_GENAI_USE_VERTEXAI="True"

'''

def install_dependencies():
    print("Installing dependencies from requirements.txt...")
    try:
        subprocess.check_call(["pip3", "install", "-r", "requirements.txt"])
        print("Dependencies installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        exit(1)

def set_gcp_environment_variables():
    print("\nSetting Google Cloud environment variables...")

    gcp_project_id = input("Please enter your Google Cloud Project ID: ")
    os.environ["GOOGLE_CLOUD_PROJECT"] = gcp_project_id
    print(f"GOOGLE_CLOUD_PROJECT set to: {gcp_project_id}")

    os.environ["GOOGLE_CLOUD_LOCATION"] = "us-central1"
    os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"
    print(f"GOOGLE_CLOUD_LOCATION set to: {os.environ['GOOGLE_CLOUD_LOCATION']}")
    print(f"GOOGLE_GENAI_USE_VERTEXAI set to: {os.environ['GOOGLE_GENAI_USE_VERTEXAI']}")
    print("Environment vars set")
    write_env_to_file(gcp_project_id)

def write_env_to_file(gcp_project_id):
    env_content = f"""GOOGLE_CLOUD_PROJECT="{gcp_project_id}"
GOOGLE_CLOUD_LOCATION="us-central1"
GOOGLE_GENAI_USE_VERTEXAI="True"
"""
    with open(".env", "w") as f:
        f.write(env_content)
    print("'.env' file created with the provided env variables")

if __name__ == "__main__":
    install_dependencies()
    set_gcp_environment_variables()
    print("\nSetup complete")
