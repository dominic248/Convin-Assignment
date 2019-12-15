

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
virtualenv -p "path to python.exe (eg.: 'C:\Program Files\Python38\python.exe')" venv_name
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

### Examples via curl
```
curl dms.com:8000/api/register/create/ -X POST -i --form name=Dominic -F email=dms24081999@gmail.com -F photo=@E:\Projects\Python\Django\Convin\src\test\1.jpg
```

```
curl dms.com:8000/api/register/create/ -X POST -i --form name=Dominic2 -F email=dominicsilveira289@gmail.com -F photo=@E:\Projects\Python\Django\Convin\src\test\1.jpg -F cv=@E:\Projects\Python\Django\Convin\src\test\1.pdf
```

```
curl dms.com:8000/api/register/rud/109/ -X PUT -i --form name=Dominic2 -F email=dms24081999@gmail.com -F photo=@E:\Projects\Python\Django\Convin\src\test\1.jpg -F cv=@E:\Projects\Python\Django\Convin\src\test\2.pdf -F id=109
```

```
curl dms.com:8000/api/register/rud/110/ -X PUT -i --form name=Vincent -F email=dominicsilveira289@gmail.com -F blog_url=https://github.com/dms24081999 -F photo=@E:\Projects\Python\Django\Convin\src\test\1.jpg -F id=110
```

```
curl dms.com:8000/api/file/create/ -X POST -i -F email=dominicsilveira289@gmail.com -F document=@E:\Projects\Python\Django\Convin\src\test\1.jpg
```

```
curl dms.com:8000/api/file/create/ -X POST -i -F email=dominicsilveira289@gmail.com -F document=@E:\Projects\Python\Django\Convin\src\test\2.pdf
```

```
curl dms.com:8000/api/file/rud/8/ -X PUT -i -F email=dominicsilveira289@gmail.com -F document=@E:\Projects\Python\Django\Convin\src\test\3.pdf
```

```
curl dms.com:8000/api/file/rud/9/ -X PUT -i -F email=dms24081999@gmail.com -F document=@E:\Projects\Python\Django\Convin\src\test\4.jpg
```