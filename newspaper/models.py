from django.db import models


class Newspaper(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    publish_date = models.DateField(unique=True)
    content = models.TextField()

    objects = models.Manager()

    class Meta:
        db_table = "newspaper"

    def __str__(self):
        return f'{self.title} - {self.publish_date}'


class EmailSubscribe(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True)

    objects = models.Manager()

    class Meta:
        db_table = "email_subscribe"

    def __str__(self):
        return self.email
