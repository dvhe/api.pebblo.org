# http://docs.peewee-orm.com/en/latest/peewee/database.html

from peewee import *
import os

from playhouse.postgres_ext import *

db = PostgresqlExtDatabase(os.getenv('DB_NAME'), user=os.getenv('DB_USERNAME'), password=os.getenv('DB_PASSWORD'), host='localhost', port='5432')

class BaseModel(Model):
    class Meta:
        database = db

class Post(BaseModel):
    id = BigIntegerField(primary_key=True)
    author = BigIntegerField(unique=False, null=False)
    content = CharField(2000, unique=False, null=False)
    likes = ArrayField(CharField, unique=False, null=False)
    created_at = DateTimeField(unique=False, null=False)
    updated_at = DateTimeField(unique=False, null=True) 