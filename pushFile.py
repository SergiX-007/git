#!/usr/bin/env python3
import subprocess

subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "'init'"])
subprocess.run(["git", "push"])
subprocess.run(["git", "status"])
