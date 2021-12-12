# Big-Eng-Project
### TRAN Jean-PIerre
### LOUKILI Bilal
### KHLIJ Nadhem


This project was made as a part of the curriculum of the Master 2 course entitled "Data Engineering II".
In a group of 3, we worked toward creating a solid example of real-life application development in a DevOps environment.
The application is a sentiment analysis application, which analyses a piece of text and responds with the sentiment detected : either positive, negative or neutral.
<br/><br/>
The application is composed of two parts :
1. The web Interface.
2. The ML model and notebook deployed on docker.

The final application deliverable is a Docker image, that contains the pre-trained model as well as the application web interface.

Vader api was used in the model.
## Project Start:
The application should have a web interface with an input form and a submit button, where users can input their sentences, and hit submit, and the sentiment of their sentence will be presented.
<br/><br/>
The image of the application:
<img src="https://github.com/jeanpierre8/Big-Eng-Project/blob/main/index.PNG"/>
<br/><br/>
The output of the application:
<img src="https://github.com/jeanpierre8/Big-Eng-Project/blob/main/output.PNG"/>
<br/><br/>

The docker installation on linux:

    sudo apt install docker.io
    docker --version

The docker-compose installation on linux:

    sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
    docker-compose --version

The docker-compose start and down:

    sudo docker-compose up
    sudo docker-compose down
    sudo docker image rm -f big-eng-project_web

The docker images:

    sudo docker images

    REPOSITORY            TAG       IMAGE ID       CREATED          SIZE
    big-eng-project_web   latest    e1b0e9aedeee   18 minutes ago   935MB
    python                3.8       f746089c9d02   9 days ago       909MB

The requirements of the application:

    flask
    vaderSentiment


## Project Management:
## Jira
    https://efrei22.atlassian.net/jira/software/projects/DEP/boards/1

We have four main parts to do:

    The Ml Model
    The Web interface
    The Application Package
    the Testing

## Step of the project:

First, we need a base to start the project, we base on the python website, using flask, <br/>
that calculates the mean of GET requests containing a list of numbers of the classes.<br/>
We change it for have the input of the user of POST requests with a form.

<br/>

Second, we increment the Ml model VaderSentiment to analyse the input of the user, and detected the sentiment is either positive, negative or neutral.

<br/>

Third, we do the html and css of the Web interface.

<br/>

Finally, we do units tests.

<br/>

## Tests:
