# Docker Project

## Overview
This project demonstrates how to create a Docker image for an application and run it as a Docker container. The project includes a `Dockerfile` which contains all the necessary instructions to build the image.

## Prerequisites
- Docker installed on your machine
- Follow the Docker official documentation for [Docker Installation](https://docs.docker.com/engine/install/).

## Getting Started

Clone the project to any directory where you do development work.

```
git clone https://github.com/praks7v/BloggersUnity.git
cd BloggersUnity
```

### Building the Docker Image
To build the Docker image, navigate to the directory containing the `Dockerfile` and run the following command:

```bash
docker build . -t bloggersunity:latest -f docker/Dockerfile
```
To build the Docker image using docker compose:
```
docker compose -f docker/docker-compose.yaml build
```

This command builds the Docker image and tags it as `latest`.

## Running the Docker Container
To run the Docker container, use the following command:

```bash
docker run -p 8000:8000 bloggersunity:latest
```
To run the Docker container using docker compose, use the following command:
```
docker compose -f docker/docker-compose.yaml up
```

This command maps port 8000 in the container to port 8000 on your host machine. You can access the application by navigating to `http://localhost:8000`.

## Pushing the Docker Image to Docker Hub
To push images to Docker Hub, you need to authenticate with your Docker Hub account. Use the `docker login` command:

```bash
docker login
```

To share your Docker image, you can push it to Docker Hub. First, tag your image with your Docker Hub repository name:

```bash
docker tag bloggersunity <your-dockerhub-username>/bloggersunity:latest
```

Then, push the image to Docker Hub:

```bash
docker push <your-dockerhub-username>/bloggersunity:latest
```

## Pulling the Docker Image from Docker Hub
If you want to pull and run the Docker image from Docker Hub, use the following commands:

```bash
docker pull <your-dockerhub-username>/bloggersunity:latest
docker run -p 8000:8000 <your-dockerhub-username>/bloggersunity:latest
```

## Docker Commands Summary Example
- **Build an image**:
    ```bash
    docker build -t myapp .
    ```
- **Run a container**:
    ```bash
    docker run -p 4000:80 myapp
    ```
- **Tag an image**:
    ```bash
    docker tag myapp your-dockerhub-username/myapp
    ```
- **Push an image to Docker Hub**:
    ```bash
    docker push your-dockerhub-username/myapp
    ```
- **Pull an image from Docker Hub**:
    ```bash
    docker pull your-dockerhub-username/myapp
    ```
- **List Docker images**:
    ```bash
    docker images
    ```
- **List running containers**:
    ```bash
    docker ps
    ```
- **Stop a running container**:
    ```bash
    docker stop <container_id>
    ```
- **Remove a Docker image**:
    ```bash
    docker rmi myapp
    ```

## Troubleshooting
- Ensure Docker is installed and running on your machine.
- Check that the Dockerfile and application files are correctly set up.
- Use `docker logs <container_id>` to view the logs if the container is not running as expected.

## Contributions
Feel free to submit pull requests or open issues if you encounter any problems or have suggestions for improvements.

## License
This project is licensed under the MIT License.
