from django.db import models
from school.entities.subject import Subject

class Student(models.Model):
    name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    subjects = models.ManyToManyField(Subject)
    
    def __str__(self):
        
        return 'id: {} - {} - {}'.format(
            self.id,
            self.name,
            self.last_name)

    class Meta:
        db_table = "students"
        ordering = ["last_name"]