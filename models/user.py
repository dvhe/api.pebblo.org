from peewee import *
import os

from playhouse.postgres_ext import *

db = PostgresqlExtDatabase(os.getenv('DB_NAME'), user=os.getenv('DB_USERNAME'), password=os.getenv('DB_PASSWORD'), host='localhost', port='5432')

class BaseModel(Model):
    class Meta:
        database = db


class Users(BaseModel):
    id = BigIntegerField(primary_key=True)
    username = CharField(16, unique=True, null=False)
    name = CharField(40, unique=False, null=True)
    avatar = CharField(80, unique=False, null=True)
    password = BlobField(500, unique=False)
    vanity = CharField(80, unique=True, null=True)
    verified = BooleanField(unique=False, null=True)
    email = CharField(80, unique=True, null=True)
    verified_email = BooleanField(unique=False, null=True)
    bio = CharField(2000, unique=False, null=True)
    email_code = CharField(80, unique=False, null=True)
    created_at = DateTimeField(unique=False, null=True)
    updated_at = DateTimeField(unique=False, null=True)
    verified_at = DateTimeField(unique=False, null=True)
    admin = BooleanField(unique=False, null=True)
    mod = BooleanField(unique=False, null=True)
    suspended = BooleanField(unique=False, null=True)
    suspended_date = DateTimeField(unique=False, null=True)
    following = ArrayField(CharField, unique=False, default=[])
    followers = ArrayField(CharField, unique=False, default=[])
    blocked = ArrayField(CharField, unique=False, default=[])
    mfa = BooleanField(unique=False, null=True)
    mfa_backup = CharField(80, unique=True, null=True)

