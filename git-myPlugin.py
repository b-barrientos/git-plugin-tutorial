#!/urs/bin/env python3

import click
import os
import subprocess

def _walk_dir(dir):
    """Walk through dir and return true if we find a directory labelled .git, 
    otherwise return false"""
    for filename in os.listdir(dir):
        f = os.path.join(dir, filename)
        if os.path.isdir(dir) == True:
            print("Filename: " + filename)
            if filename == ".git":
                return True
    return False

def _run_git_commands(repo_dir):
    """Runs the following commands in order on the repo given"""
    subprocess.run(["git", "pull"])
    subprocess.run(["git", "push"])
    subprocess.run(["git", "push", "--tags"])
    

@click.command()
@click.option('-d', '--dir', default=".", type=str, help="Target path to scan")
def run(dir):
    is_git = _walk_dir(dir)
    if is_git is True:
        _run_git_commands(dir)

if __name__ == '__main__':
    run()