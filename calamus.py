import os
import os.path
import subprocess

ROOT = '1.3-pre-07261249'
VERSIONS= [
[
ROOT,
'12w30e', '12w30d', '12w30c', '12w30b', '12w30a',
'12w27a',
'12w26a',
'12w25a',
'12w24a',
'12w23b', '12w23a',
'12w22a',
'12w21b', '12w21a',
'12w19a',
'12w18a',
'12w17a',
'12w16a',
'12w15a',
'1.2.5'
],
[
ROOT,
'1.3.1', '1.3.2'
]
]

def main():
	os.environ['MC_VERSION'] = ROOT
	subprocess.run("./gradlew generateCalamus --stacktrace", shell = True, check = True)
	
	for versions in VERSIONS:
		for i in range(1, len(versions)):
			os.environ['FROM_MC_VERSION'] = versions[i - 1]
			os.environ['MC_VERSION'] = versions[i]
			
			subprocess.run("./gradlew updateCalamus --stacktrace", shell = True, check = True)

if __name__ == '__main__':
	main()
