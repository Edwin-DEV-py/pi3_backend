from django.db import models
from UserApp.models import User

class CalendarModel(models.Model):
    
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    start_hour = models.TimeField()
    end_hour = models.TimeField()
    date = models.DateField()
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.start_hour >= self.end_hour:
            raise ValueError("La hora de inicio debe ser antes que la hora de fin.")
        
        super(CalendarModel, self).save(*args, **kwargs)