Tests using jenkins blue ocean and python


## Start Jenkins container
```sh
docker build -t jenkinsbo -f Dockerfile_JBO .
docker run -p 8888:8080 --name=jenkinsbo -v /var/run/docker.sock:/var/run/docker.sock -v $HOME/Desktop/jenkins:/var/jenkins_home jenkinsbo
```
