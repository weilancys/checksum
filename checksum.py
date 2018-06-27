import hashlib
import sys
import os

usageInfo = "usage: checksum md5|sha256 filename."

if len(sys.argv) != 3:
    print(usageInfo)
    sys.exit()

methodName = sys.argv[1]
fileName = sys.argv[2]

if methodName not in ['md5', 'sha256']:
    print(usageInfo)
    sys.exit()

if not os.path.exists(fileName):
    print("invalid filename.")
    sys.exit()

if methodName == 'md5':
    parser = hashlib.md5()
else:
    parser = hashlib.sha256()

try:
    with open(fileName, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            parser.update(data)
    print(parser.hexdigest())
except:
    print("checksum failure")
