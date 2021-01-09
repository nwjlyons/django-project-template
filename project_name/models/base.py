import uuid

from django.db import models


class AbstractBaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id}>"
