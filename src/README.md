
# Convin Assignment 
## Clone Repository
```
git clone https://github.com/dms24081999/Convin-Assignment.git
cd Convin-Assignment
```
***
## Install virtualenv
```
pip install virtualenv 
```
## Create virtual environment
```
virtualenv -p "path to python.exe in installation folder" venv_name
```
## Activate virtual environment
```
venv_name\scripts\activate  
```
## Install requirements.txt
```
pip install -r requirements.txt 
```
***
## Create Super User (Optional)
```
cd src
python manage.py runserver
```
### Default:
```
Username: dms
Password: 24081999
```
***
## Run Project
```
cd src
python manage.py runserver
```
***
## URL's in Project
### Admin URL:
```admin/```
### Create API URL for assignment-1 (Registration Form):

```api/register/create/```
### Update API URL for assignment-1 with API and email notifications (Registration Form):
```api/register/rud/<pk>/```
### Create API URL for assignment-2 (File hashing Form):
```api/file/create/```
### Update API URL for assignment-1 with API and email notifications (File hashing Form):
```api/file/rud/<pk>/```
***

