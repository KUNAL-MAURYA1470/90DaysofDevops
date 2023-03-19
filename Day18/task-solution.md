# Day 18 Task: Docker for DevOps Engineers

## Docker Compose
- Docker Compose is a tool that was developed to help define and share multi-container applications.
- With Compose, we can create a YAML file to define the services and with a single command, can spin everything up or tear it all down.
- Learn more about docker-compose [visit here](https://tecadmin.net/tutorial/docker/docker-compose/)

## What is YAML?
- YAML is a data serialization language that is often used for writing configuration files. Depending on whom you ask, YAML stands for yet another markup language or YAML ain’t markup language (a recursive acronym), which emphasizes that YAML is for data, not documents. 
- YAML is a popular programming language because it is human-readable and easy to understand.
- YAML files use a .yml or .yaml extension.
- Read more about it [here](https://www.redhat.com/en/topics/automation/what-is-yaml)

# Task-1

Learn how to use the docker-compose.yml file, to set up the environment, configure the services and links between different containers, and also to use environment variables in the docker-compose.yml file. 

## Install Docker Compose: Use the following command to install Docker Compose:

- sudo apt install docker-compose

![image](https://user-images.githubusercontent.com/83691101/226171688-98d72997-b41a-4d58-9f3d-addcf6efb86e.png)

## Step 2 : Create a docker-compose.yml file inside project folder
![image](https://user-images.githubusercontent.com/83691101/226171907-f7954599-77f5-47af-bf7b-45633280b1b6.png)

## Step 3 : Run docker-compose.yml file
![image](https://user-images.githubusercontent.com/83691101/226171999-e910e7f2-2a08-4a92-b64a-cfdbcb3ba58d.png)

## Step 4 : Verify that application is working by accessing it in a web browser
![image](https://user-images.githubusercontent.com/83691101/226172054-53ca698c-989d-4c50-ac32-9f757866a0b6.png)

## docker-compose down : 
This command stops all the services and cleans up the containers, networks, and images.
![image](https://user-images.githubusercontent.com/83691101/226172132-6716f8d0-4613-4425-b85b-0540ee273190.png)


# Task-2

## 1.Pull a pre-existing Docker image from a public repository (e.g. Docker Hub) and run it on your local machine. Run the container as a non-root user
![image](https://user-images.githubusercontent.com/83691101/226172439-6e439b8e-ef19-44ed-b83c-1b929d53cb3f.png)

## 2.Inspect the container's running processes and exposed ports using the docker inspect command.
### docker inspect <container_name or ID
![image](https://user-images.githubusercontent.com/83691101/226172514-6f28ef5f-08a4-424b-aad6-59378b767c06.png)


## 3.Use the docker logs command to view the container's log output.
### docker logs <container_name or ID>
![image](https://user-images.githubusercontent.com/83691101/226172650-c45b21de-933c-4775-a3bf-c69a652d46d3.png)


## 4.Use the docker stop and docker start commands to stop and start the container.
### docker stop : To stop one or more running Docker containers.

![image](https://user-images.githubusercontent.com/83691101/226172753-e3bbac35-a79e-489d-9dc5-3bd4fd963d61.png)

### docker start : Start one or more stopped containers
![image](https://user-images.githubusercontent.com/83691101/226172816-913e9cd0-6c93-4ad0-837c-95577d6afe6b.png)


## 5. Use the docker rm command to remove the container when you're done.

### docker rm : Remove one or more containers
### docker rm <container_name or ID>

![image](https://user-images.githubusercontent.com/83691101/226172852-a506ecfa-8ba1-44e8-83be-21fa35e70706.png)


