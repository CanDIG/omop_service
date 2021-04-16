## Notes on standardized vocabularies import

Standardized vocabularies must be downloaded in advance from the [Athena vocabularies server](https://athena.ohdsi.org/).

More about CDM and Vocabularies import can be found here https://github.com/OHDSI/CommonDataModel

There are two options to import vocabularies:

1. Import vocabularies with django command (recommended if using Postgres):

```
   python manage.py import_postgres 
```

This command based on the script that uses raw SQL COPY statements to copy data from the csv files into Postgres database.
By default all vocabularies are imported otherwise the SQL statements can be edited.
By default it expects the vocabularies to be located in `C:\CDMV6VOCAB\`  directory.
The directory path can be changed in `omop_service.management.commands._utils.import_postgres` function.


2. Not recommended, only for small vocabularies.
Import vocabularies with django command (can be used for import into Sqlite database, significantly slower than option 1):

```
   python manage.py import_all_vocabularies 
```

By default only Vocabulary, Domain, Concept_class, Concept vocabularies are required.
The vocabulary files must be placed in the directory where `manage.py` file is located (root directory of the project).
