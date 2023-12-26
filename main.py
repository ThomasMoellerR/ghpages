import subprocess
result = subprocess.run(['sh', 'git.sh'], stdout=subprocess.PIPE)
a = result.stdout

print(a)