#!/usr/bin/env python

from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/pullLatestHueMotion", methods=['POST'])
def hello():
    #cmd = ["ls","-l"]
    p = subprocess.Popen('sudo /etc/init.d/hue-motion stop', shell=True)
    p.wait()

    p = subprocess.Popen(['git','pull'], cwd='/home/pi/pi-hue-motion')
    #out,err = p.communicate()
    p.wait()

    p = subprocess.Popen('sudo /etc/init.d/hue-motion start', shell=True)
    p.wait()

    return "Done!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
