from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)
    category = models.ForeignKey(ProductCategory, on_delete=models.RESTRICT)
    date = models.DateField(null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    test = models.TimeField(null=True, blank=True)
    boolean = models.BooleanField(default=False)
    rext = models.TextField(null=True, blank=True)
    file = models.FileField(null=True, blank=True, upload_to='files')

    def __str__(self):
        return self.name
