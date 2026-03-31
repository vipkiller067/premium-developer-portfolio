import os
import shutil
import subprocess

root_dir = r"c:\Users\ADMIN\Desktop\portfolio website"

to_remove = [
    os.path.join(root_dir, "front"),
    os.path.join(root_dir, "templates"),
    os.path.join(root_dir, "main.py"),
    os.path.join(root_dir, "requirements.txt"),
    os.path.join(root_dir, "__pycache__")
]

for item in to_remove:
    # Remove from Git index
    if os.path.exists(item):
        try:
            subprocess.run(["git", "rm", "-r", "-f", item], cwd=root_dir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            pass
        
        # Remove from disk
        if os.path.isdir(item):
            try:
                shutil.rmtree(item, ignore_errors=True)
            except:
                pass
        else:
            try:
                os.remove(item)
            except:
                pass

print("Git synced and purged.")
