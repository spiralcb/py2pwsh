import subprocess
import sys

'''p = subprocess.Popen(["powershell.exe", ".\\run.ps1"], stdout=sys.stdout)
p.communicate()
'''

script_path = ".\\run.ps1"

result = subprocess.run(["powershell.exe", "-File", script_path], shell=True, capture_output=True, text=True)

print(result.returncode)
print(result.stdout)