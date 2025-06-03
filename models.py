from tortoise import fields
from tortoise.models import Model

class DBChannel(Model):
  id = fields.BigIntField(pk=True)
  active = fields.BooleanField(default=lambda:False)

  def toggle_active(self):
    return self.update(active=not self.active)

class DBUser(Model):
  id = fields.BigIntField(pk=True)
  sid = fields.CharField(unique=True, max_length=50)
  auth_token = fields.TextField(null=True)

