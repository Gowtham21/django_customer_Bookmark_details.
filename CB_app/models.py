from django.db import models
from django.urls import reverse

class customer_profile(models.Model):
    customer_fname = models.CharField(max_length = 50)
    customer_lname = models.CharField(max_length = 50)
    lat = models.CharField(max_length = 50)
    lon = models.CharField(max_length = 50)

    def __str__(self):
        return self.customer_fname +' '+ self.customer_lname
    def get_absolute_url(self):
        return reverse("CB_app:detail",kwargs={'pk':self.pk})

class Bookmark(models.Model):
    title = models.CharField(max_length = 75)
    url = models.URLField(max_length = 200)
    source_name = models.CharField(max_length = 50)
    pub_date = models.DateField()
    customer = models.ManyToManyField(customer_profile, through='customer_bookmark')

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("CB_app:b_detail",kwargs={'pk':self.pk})

class customer_bookmark(models.Model):
    cb_customer_id = models.ForeignKey(customer_profile, related_name = 'cb_customer_ids',on_delete=models.CASCADE)
    cb_bookmark_id = models.ForeignKey(Bookmark, related_name = 'cb_bookmark_ids',on_delete=models.CASCADE)
