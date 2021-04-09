# Lab 9 Report - Virtualization and Docker

## Example 0: Installing Docker
### `docker run docker/whalesay cowsay boo`
![Example 0 Screenshot](./screenshots/00-RunWhalesay.png)

---
## Example 1: Creating Ubuntu in a Container
### Starting a Docker Container with an Interactive Ubuntu Terminal
![Example 1 Screenshot A](./screenshots/01a-RunUbuntuBash.png)

### Using VIM in the Container to Create a Text File
![Example 1 Screenshot B](./screenshots/01b.png)

### Installing and Running `cowsay` in our Ubuntu Container
![Example 1 Screenshot C](./screenshots/01c.png)

---
## Example 2: Docker in Large Projects
### Running Mongo and RocketChat, Then `docker ps` to Show Running Containers
![Example 2 Screenshot A](./screenshots/02a.png)

### Showing I Have RocketChat Successfully Up and Running
![Example 2 Screenshot B](./screenshots/02b.png)

### Practicing with `docker stop`, `docker rm`, and `docker rmi`
![Example 2 Screenshot C](./screenshots/02c.png)

---
## Example 3: Python Hello World Server with a Dockerfile
[Link to associated Dockerfile](example03/Dockerfile)

### Building and Running the Dockerfile I Just Made
![Example 3 Screenshot A](./screenshots/03a.png)

### Showing I Have the Hello World Python Server Successfully Up and Running
![Example 3 Screenshot B](./screenshots/03b.png)

---
## Example 4: Simple Docker Compose

### Using a `Dockerfile` to Try and Set Up MessageApp
[Link to associated Dockerfile.](example04/messageApp/Dockerfile) Because we didn't set up a MongoDB database or container for our message-app to use, trying to do `docker run message-app` doesn't work. See the next part for the solution, where a `docker-compose.yml` file is used to launch a MongoDB service alongside the message-app container.

__Message-App Being Built, But Failing Upon `docker run`:__
![Example 4 Screenshot A](./screenshots/04a.png)

### Using `docker-compose.yml` to Launch Both MessageApp _AND_ MongoDB
[Link to associated docker-compose.yml.](example04/messageApp/docker-compose.yml) Since message-app now has an actual database to use, it successfully builds and runs. This is done by first building the images, setting up our volumes, etc. with `docker compose build` and then running the services using `docker compose up`. Note that since `docker-compose` is now bundled with `docker` as of recent updates, the hyphen in between _docker_ and _compose_ is no longer necessary.

__Playing Around With Message-App Since It's Now Working:__
![Example 4 Screenshot B](./screenshots/04b.png)

---
## Licensing
The example code used in this lab comes from the [rcos/docker-examples](https://github.com/rcos/docker-examples) repository, which uses the MIT License. For more information about licensing for the example code, click [here](https://github.com/rcos/docker-examples/blob/73a1c960f305d3d7c435f5f75cdad7343fddd610/LICENSE).