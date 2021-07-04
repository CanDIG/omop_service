# OMOP service

![Test Status](https://github.com/CanDIG/omop_service/workflows/Test/badge.svg)

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
             'NAME': os.environ.get('POSTGRES_DATABASE', 'omop'),
             'USER': os.environ.get('POSTGRES_USER', 'admin'),
             'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'admin'),
             'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
             'PORT': os.environ.get('POSTGRES_PORT', '5432'),
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


## API endpoints

### Data types endpoints

`api/persons` GET: list of persons

`api/persons/{id}` GET: single person

`api/conditionoccurrences` GET: list of condition occurrences

`api/conditionoccurrences/{id}` GET: single condition occurrence

`api/procedureoccurrences` GET: list of procedure occurrences

`api/procedureoccurrences/{id}` GET: single procedure occurrence

`api/measurements` GET: list of measurements

`api/measurements/{id}` GET: single measurement

`api/observations` GET: list of observations

`api/observations/{id}` GET: single observation

`api/specimens` GET: list of specimens

`api/specimens/{id}` GET: single specimen


### Data overview endpoint

`api/overview` GET: overview of data types and concepts


### Ingest endpoint

`api/ingest` POST: ingest data in csv or json

POST body example:
    
    {
    "file": "path/persons.csv",
    "data_type": "person"
    }
    
