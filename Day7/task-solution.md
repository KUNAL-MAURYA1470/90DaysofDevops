# Day 7 Task: Understanding package manager and systemctl
# Tasks
## 1. You have to install docker and jenkins in your system from your terminal using package managers

![image](https://user-images.githubusercontent.com/83691101/222152079-cbccbb3b-1b4c-41a8-9e83-1d196b096af4.png)

![image](https://user-images.githubusercontent.com/83691101/222152164-78c25e43-c38e-4668-8505-9095a93b9e32.png)

## 2. check the status of docker service in your system 
-> sudo systemctl status docker

## 3. stop the service jenkins and post before and after screenshots

![image](https://user-images.githubusercontent.com/83691101/222152619-9db2094c-cbee-46bf-a022-f6f6cef7bc34.png)

after stop

![image](https://user-images.githubusercontent.com/83691101/222152692-8d856488-d4f9-4f00-a058-d30bfa1141ed.png)

## 4. read about the commands systemctl vs service

## systemctl commands 
systemctl start <service>: Starts a service

systemctl stop <service>: Stops a service

systemctl restart <service>: Restarts a service

systemctl enable <service>: Enables a service to start automatically at boot

systemctl disable <service>: Disables a service from starting automatically at boot

systemctl status <service>: Displays the status of a service
  
## service commands 
  
`service <service-name> <action>`

start: Starts a service

stop: Stops a service

restart: Restarts a service

reload: Reloads the configuration of a service

status: Displays the status of a service

enable: Enables a service to start automatically at boot

disable: Disables a service from starting automatically at boot
