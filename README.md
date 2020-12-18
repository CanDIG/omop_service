# OMOP service

The first prototype of the OMOP service based on the [OMOP Common Data Model](https://ohdsi.github.io/CommonDataModel/index.html)

## Installation

The service is built with:
- Python 3.7
- Django

1. Create virtual environment and install dependencies:

    ```
    pip install -r requirements.txt
    ```

2. Run migrations: the following command will generate the `sqlite` database in the root folder

    ```
    python manage.py migrate
    ```

3. Start development server at `localhost:8000`

    ```
    python manage.py runserver
    ```

4. Create admin user

    ```
    python manage.py createsuperuser
    ```

    The admin interface runs at `localhost:8000/admin`
