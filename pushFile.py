#!/usr/bin/env python3
import subprocess
import os


subprocess.Popen(
    ["gnome-terminal"],
    cwd=os.path.expanduser("~/Desktop")
)
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "'init'"])
subprocess.run(["git", "push"])
subprocess.run(["git", "status"])
