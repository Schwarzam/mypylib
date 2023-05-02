import mypylib
import subprocess
import os

def push_to_github(commit_message, repo_path=mypylib.__path__[0], remote_name="origin", branch_name="main"):
    try:
        wd = os.getcwd()
        os.chdir(repo_path)

        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push", remote_name, branch_name], check=True)
        os.chdir(wd)
        
        print(f"Folder successfully pushed to GitHub repository: {remote_name}/{branch_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False
    return True


def pull_from_github(repo_path=mypylib.__path__[0], remote_name="origin", branch_name="main"):
    try:
        wd = os.getcwd()
        os.chdir(repo_path)
        subprocess.run(["git", "pull", remote_name, branch_name], check=True)
        os.chdir(wd)
        
        print(f"Folder successfully pulled from GitHub repository: {remote_name}/{branch_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False
    return True