from tortoise import fields
from tortoise.models import Model

class DBChannel(Model):
  id = fields.BigIntField(pk=True)
  active = fields.BooleanField(default=lambda:False)


class DBUser(Model):
  id = fields.BigIntField(pk=True)
  sid = fields.BigIntField(unique=True)
  auth_token = fields.TextField()

