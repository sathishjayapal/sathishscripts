# sathishscripts
Some utility scripts for spinning EC2s


### Running
Project requires Python 3 and requests package

### Pipenv world

Install pipenv for the scripts
Install Boto3 for the scripting

For a sample run make sure all things are working
```
pipenv install
pipenv run python mydefault/myterster.py
```

##Matty application

Matty scripter uses aws cli for its profile lookup

`aws configure --profile matty`

##Running Matty

`pipenv run python matty/matty.py`