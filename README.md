# Teacher Manager
is a Django CRUD app, that alllow to manage teachers

## Install packages
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
> pip install -r requirements.txt
```

## Login Database (MySQL)

```bash
> mysql -u db_user -p
```

## Create database

```sql
CREATE DATABASE teachersdb 
```

## Insert Degrees

```sql
> INSERT INTO teachapp_degree (code, name);

> VALUES
    (01, "Software Development"),
    (02, "Economy"),
    (03, "Law"),
    (04, "Mathematics"),
    (05, "Physics"),
    (06, "Music"),
    (07, "Marketing"),
    (08, "Business"); 
```

## Settings
got to teachsite/setting.py file

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': DB_HOST
    }
}

```

## Run Server
```bash
python manage.py runserver
```