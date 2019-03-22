Tests using jenkins blue ocean and python

## run container
```sh
docker build -t jenkinsbo .
docker run -p 8888:8080 --name=jenkinsbo -v $HOME/Desktop/jenkins:/var/jenkins_home jenkinsbo
```
