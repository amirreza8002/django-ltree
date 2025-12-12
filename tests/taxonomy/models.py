from django.db import models

from django_ltree.models import TreeModel


class Taxonomy(TreeModel):
    label_size = 2

    name = models.TextField()

    def __str__(self):
        return "{}: {}".format(self.path, self.name)


class Test(models.Model):
    abc = models.CharField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        type(self).objects.filter(id=self.id).update(abc=f"somthing-{self.id}")
