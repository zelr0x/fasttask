from uuid import uuid4

from tortoise import fields, models


class IdMixin(models.Model):
    id = fields.UUIDField(pk=True, default=uuid4)

    class Meta:
        abstract = True


class TimestampMixin(models.Model):
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseModel(IdMixin, TimestampMixin):
    class Meta:
        abstract = True


class Task(BaseModel):
    name = fields.CharField(max_length=255, unique=True)
    description = fields.TextField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        table = "task"


class User(BaseModel):
    name = fields.CharField(max_length=255, unique=True)
    description = fields.TextField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        table = "user"
