# Modernizing Cosmetic Retail: Reinventing E-commerce for Beauty Products

By using Amazon Web Services (AWS) cloud computing resources, my project aims to build a robust cosmetics e-commerce website.

# Instructions for installation

`git clone https://github.com/Annurag99/CPP-Cosmetic-Retail.git`

`cd CPP-Cosmetic-Retail`

`pip install virtualenv`

`virtualenv env` or `python -m venv env`

# Mac/Linux

`source env/bin/activate`

'New Version will throw an error due to version conflicts'

```python

pip install Django==2.2.4
python3 -m pip install django-allauth==0.40.0
pip install django-crispy-forms==1.7.2
pip install django-countries==5.5
pip install stripe==2.37.1
pip install Pillow

```
`python3 manage.py makemigrations`

`python3 manage.py migrate`

`python3 manage.py runserver 8080`

To resolve the Invalid HTTP_HOST header error. You may need to add a host header 
example - 'd003a56484c942d88af2e1fc366a3f01.vfs.cloud9.eu-west-1.amazonaws.com'
to ALLOWED_HOSTS inside the demo folder in the settings.py file.

# Admin Login

```python
python3 manage.py createsuperuser
Username: add
Password: add
```
# Demo & Static Pages




