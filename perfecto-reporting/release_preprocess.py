import os

release_version = os.environ['RELEASE_VERSION']
FileName = 'setup.py'
with open(FileName) as f:
    newText = f.read().replace('<PLACE_HOLDER_RELEASE_VERSION>', release_version)

with open(FileName, "w") as f:
    f.write(newText)
