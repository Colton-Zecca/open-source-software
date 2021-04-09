# Comments in Dockerfiles
FROM python:3.5

# Update and install dependencies
RUN apt-get update
RUN pip install Flask

# Add code: '.' is the source, and /opt/webapp/ is the destination
# In other words, this adds hello.py from our filesystem to the container
ADD . /opt/webapp/

# Set the working directory
WORKDIR /opt/webapp

# Set environment variables
ENV FLASK_APP=hello.py

# Expose the application's port
# Note EXPOSE doesn't make the ports of the container accessible by the host
# To do this, the -p flag is needed to publish a range of ports or -P to publish all of the exposed ports
EXPOSE 5000

# Run the application
# Can only be one of these in a Dockerfile. If there are multiple, only the last CMD takes effect
# The main purpose of CMD is to provide defaults for an executing container
CMD ["flask", "run", "--host=0.0.0.0"]
