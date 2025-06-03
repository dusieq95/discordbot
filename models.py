from tortoise import fields
from tortoise.models import Model

class DBChannel(Model):
  id = fields.BigIntField(pk=True)
  active = fields.BooleanField(default=lambda:False)

  def toggle_active(self):
    return self.update(active=not self.active)

class DBUser(Model):
  id = fields.BigIntField(pk=True)
  sid = fields.TextField(unique=True)
  auth_token = fields.TextField(null=True)

