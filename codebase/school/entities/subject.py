from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return 'Id: {} - {} '.format(
            self.id,
            self.name)

    class Meta:
        db_table = "subjects"