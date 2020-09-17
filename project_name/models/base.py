from django.db import models
from django_smalluuid.models import SmallUUIDField, uuid_default


class AbstractBaseModel(models.Model):
    id = SmallUUIDField(default=uuid_default(), primary_key=True, editable=False)

    class Meta:
        abstract = True

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id}>"
