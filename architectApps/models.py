from django.db import models
from tinymce.models import HTMLField


class Company_details(models.Model):
    """docstring for Company"""
    company_name = models.CharField(max_length=200)
    company_moto = models.CharField(max_length=200)
    company_description = HTMLField()

    def __str__(self):
        return self.company_name

    def save(self):
        # count will have all of the objects from the Company_details model
        count = Company_details.objects.all().count()
        # this will check if the variable exist so we can update the existing
        # ones
        save_permission = Company_details.has_add_permission(self)

        # if there's more than two objects it will not save them in the
        # database
        if count < 2:
            super(Company_details, self).save()
        elif save_permission:
            super(Company_details, self).save()

    def has_add_permission(self):
        return Company_details.objects.filter(id=self.id).exists()
