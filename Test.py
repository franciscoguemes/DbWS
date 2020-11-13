#!/usr/bin/python3
import subprocess

full_command = [
    '/home/francisco/git/Francisco/github/chrome_bookmarks/chrome_bookmarks.py',
    '--config=/home/francisco/conf/chrome_bookmarks/chrome_bookmarks.conf',
    '/Personal/Login screen']

application = subprocess.Popen(full_command, stdout=subprocess.PIPE)
application.wait()
result = application.communicate()[0]
print(type(result))
result = result.decode("utf-8")
print(result)
print(type(result))
print(len(result))
# This is very important, to remove the spaces at the end...
result = result.strip()
print(len(result))
if result[0:2] == "['":
    print(result[0:2])
if result[-2:] == "']":
    print(result[-3:])
# for x in result:
#     print(x)

# result = result.replace("[", "", 1)
# result = result[:-1]
# urls = result.split(", ")
# for url in urls:
#     print(url)

if result[0:2] == "['" and result[-2:] == "']":
    result = result[1:-1]
    urls = result.split(", ")
    for url in urls:
        print(url[1:-1])