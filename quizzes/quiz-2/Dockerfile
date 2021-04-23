FROM python:latest

# Update and install dependencies
RUN apt-get update
RUN apt-get install git
RUN apt-get install emacs

RUN pip install tensorflow
RUN pip install matplotlib

# WORKDIR runs mkdir and cd implicity, then sets the working directory to /home/turner
WORKDIR /home/turner

# Run the application
# Can only be one of these in a Dockerfile. If there are multiple, only the last CMD takes effect
# The main purpose of CMD is to provide defaults for an executing container
CMD bash
