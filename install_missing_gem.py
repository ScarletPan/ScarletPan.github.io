import subprocess
import re
while True:
    msg = subprocess.getoutput("jekyll serve")
    package = re.findall("Could not find (.*) in any of the sources", msg)[0]
    version = package.split("-")[-1]
    pstr = "-".join(package.split("-")[:-1])
    cmd = "gem install " + pstr + " -v" + version
    print(cmd)
    subprocess.getoutput(cmd)
