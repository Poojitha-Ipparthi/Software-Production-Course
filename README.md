# Calculator app in Docker

## Set up
1. Create a folder for the project in a working directory.
2. Create a file with the Python script for the calculator.
3. In the same directory, create a Dockerfile.
4. Build the Docker image using the following command: docker build -t calculator .
5. Once the Docker image is built, run the container using the command: docker run -it calculator
6. For the history to be saved, run the command: 

## Application Features
1. The application performs basic arithmetic operations such as addition, subtraction, multiplication and division
2. The calculation history is saved in a text file called history.txt
3. We are running the application in a Docker container

## Docker concepts used in this application
1. We are using a lightweight Python base image
2. Volume Mounting concept is used to save the calculation histroy.
