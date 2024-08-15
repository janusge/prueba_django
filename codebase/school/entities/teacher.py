from django.db import models
from school.entities.subject import Subject

class Teacher(models.Model):
    name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        # return f"id:{self.id} nombre:{self.full_name}"
        return 'Id: {} - {} - {}'.format(
            self.id,
            self.name,
            self.last_name)

    class Meta:
        db_table = "teachers"
        ordering = ["last_name"]