# OMOP service

The first prototype of the OMOP service based on the [OMOP Common Data Model](https://ohdsi.github.io/CommonDataModel/index.html)

## Installation

The service is built with:
- Python 3.7
- Django
- PostgreSQL >= 11

1. Create virtual environment and install dependencies:

    ```
    pip install -r requirements.txt
    ```

2. The service uses PostgreSQL database for data storage.
    Configue the database in `settings.py`:

    ```
    # default PostgreSQL settings
    DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'omop',
             'USER': 'admin',
             'PASSWORD': 'admin',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
    ```
   
   If using `sqlite` database then skip this step.

3. Run migrations:

    ```
    python manage.py migrate
    ```
   
   If using `sqlite` database the above command will generate the `sqlite` database file in the project's root directory.

4. Start development server:

    ```
    python manage.py runserver
    ```
   
   The service should be accessible now at `localhost:8000`

5. Create admin user:

    ```
    python manage.py createsuperuser
    ```

    The admin interface runs at `localhost:8000/admin`
    
    
The OMOP Standardized Vocabularies need to be downloaded independently and can be imported using django commands in `data_tables/management/commands` directory.
