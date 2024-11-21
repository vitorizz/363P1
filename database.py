import config
from peewee import PostgresqlDatabase

database = PostgresqlDatabase(
    database=config.DATABASES['NAME'],
    user=config.DATABASES['USER'],
    password=config.DATABASES['PASSWORD'],
    host=config.DATABASES['HOST'],
    port=config.DATABASES['PORT']
    )

database.connect()