# Employee Dashboard

## Dependencies

- **Django**  
  You can install it by running the following command:

  ```bash
  pip install django
  ```

- **MySQL Database**  
  After setting up MySQL on your machine, create a new database and modify the following in `settings.py` according to your database setup:

  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'emp_db',
          'USER': 'root',
          'PASSWORD': 'test',
          'HOST': 'localhost',
          'PORT': '3306',
      }
  }
  ```

## Starting the App

In the terminal, run the following command to start the Django server:

```bash
python manage.py runserver
```

> **Note**: Nothing will show up on the dashboard if the database is empty.

## Views

You can use the following URLs to interact with the application:

- `/create`  
  This URL creates dummy employees and stores them in the database. At this point, the dashboard will only show one pie chart, marking all employees as **absent** since they haven't checked in for the day.

- `/create2`  
  This URL checks the employees in and out randomly for the day, updating their attendance status.

You can also access the Django Admin panel using the `/admin` URL with the default credentials:

- **Username**: `admin`
- **Password**: `admin`

The admin interface allows you to:

- Add or remove employees
- Manually check employees in or out

## Screenshot

![Dasboard1](https://github.com/user-attachments/assets/69abc774-f722-4350-9ca4-db99ddb5011e)
```
