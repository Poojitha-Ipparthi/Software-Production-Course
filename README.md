# Docker Console Application - Simple Calculator with History

## Overview
This project is a simple Python-based calculator that performs basic arithmetic operations (addition, subtraction, multiplication, division) and maintains a history of calculations. The application is containerized using Docker, ensuring consistent execution across different environments.

## Features
1. Perform basic arithmetic operations
2. Persistent calculation history stored in a text file
3. Interactive console-based user interface
4. Runs inside a Docker container with volume mounting for data persistence

# Setup Instructions
## Prerequisites
Ensure you have the following installed on your system:
- Docker (latest version)
- WSL 2 with Ubuntu (for Windows users)
- Git (optional, for cloning the repository)

## Step 1: Clone the Repository
git clone (https://github.com/Poojitha-Ipparthi/Software-Production-Course.git)

## Step 2: Build the Docker Image
docker build -t calculator .

## Step 3: Run the Application
docker run -it -v "$(pwd)/history:/history" calculator

# Usage
1. Run the container using the above command.
2. Choose an option:
- 1 for Addition
- 2 for Subtraction
- 3 for Multiplication
- 4 for Division
- 5 to Show History
- 6 to Exit
3. Enter numbers as prompted
4. View results instantly
5. Check history using option 5
6. Once done, exit the application using option 6

# Screenshots
All screenshots can be found in the [screenshots folder](Screenshots/).

# Docker Concepts Used
## Dockerfile:
- Base Image: Uses a Python base image (python:3.9-slim) for efficiency.
- Dependencies: Installs required Python packages.
- File Copying: Copies the calculator script inside the container.
- Entry Point: Runs the application when the container starts.

## Volume Mounting
- The history file is stored in '/history/history.txt'.