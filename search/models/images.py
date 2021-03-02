from datetime import datetime

from tortoise import fields, models


class Images(models.Model):
    """Image Model"""

    id = fields.IntField(pk=True)
    filename = fields.CharField(null=False, max_length=120)
    storename = fields.CharField(null=False, max_length=120)
    content_type = fields.CharField(null=False, max_length=50)
    hash = fields.CharField(null=False, index=True, unique=True, max_length=120)
    path = fields.CharField(null=False, max_length=120)
    created_at = fields.DatetimeField(auto_now_add=True)

    class PydanticMeta:
        exclude = ["created_at"]
