from django.db import models


# Create your models here.
class History(models.Model):
    bs1 = models.IntegerField(null=True)
    bs2 = models.IntegerField(null=True)
    bs3 = models.IntegerField(null=True)
    bs4 = models.IntegerField(null=True)
    bs5 = models.IntegerField(null=True)
    bs6 = models.IntegerField(null=True)
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "history"

    pass


class HistoryImage(models.Model):
    EmpName = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/', blank=False, null=False)
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Image"

    pass
