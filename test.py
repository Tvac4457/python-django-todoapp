import os
import subprocess

print("Installing Chrome Remote Desktop")
subprocess.run(['wget', 'https://github.com/thoeb292/thoeb292/raw/main/rocky.sh'], stdout=subprocess.PIPE)
subprocess.run(['chmod 777 rocky.sh'], stdout=subprocess.PIPE)
subprocess.run(['bash rocky.sh'], stdout=subprocess.PIPE)
