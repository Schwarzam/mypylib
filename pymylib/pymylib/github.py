import pymylib
import subprocess
import os

def push_to_github(commit_message, repo_path=pymylib.__path__[0], remote_name="origin", branch_name="main"):
    """Pushes the changes made in a local Git repository to a remote GitHub repository.

    Parameters
    ----------
    commit_message : str
        The commit message to use when committing the changes to Git.
    repo_path : str, optional
        The path to the local Git repository to push (default is the path to the 'pymylib' module).
    remote_name : str, optional
        The name of the remote Git repository to push to (default is 'origin').
    branch_name : str, optional
        The name of the branch to push to in the remote repository (default is 'main').

    Returns
    -------
    bool
        True if the push was successful, False otherwise.

    """
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


def pull_from_github(repo_path=pymylib.__path__[0], remote_name="origin", branch_name="main"):
    """Pulls the latest changes from a remote GitHub repository to a local Git repository.

    Parameters
    ----------
    repo_path : str, optional
        The path to the local Git repository to pull (default is the path to the 'pymylib' module).
    remote_name : str, optional
        The name of the remote Git repository to pull from (default is 'origin').
    branch_name : str, optional
        The name of the branch to pull from in the remote repository (default is 'main').

    Returns
    -------
    bool
        True if the pull was successful, False otherwise.

    """
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
