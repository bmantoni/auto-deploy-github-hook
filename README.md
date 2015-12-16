# auto-deploy-github-hook
Automatically pull and deploy latest code on push to github.

I'm running this on a Raspberry Pi. Whenever code is pushed to a repo on github, I want it to be automtically deployed down to my Pi.

Github Webhooks make this possible. I run a little server on the pi that exposes and HTTP endpoint.

Github makes a POST to this URL whenever a push occurs.

I can then do a pull and deploy the latest code.

# Setting it up

I'm using Flask to host this lightweight web server.

I listen on a high port number, and run the Flask as a non-root restricted user using a daemon.

This user only has the minimum rights to do what it needs to do.

# What I'm using it for

I'm using this with my hue-motion project, which also runs on the Pi as a daemon.

I give the user running this server sudo rights only to stop and start the hue-motion service.