from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse


class Company_details(models.Model):
    """docstring for Company"""
    company_name = models.CharField(
        max_length=200, help_text='Enter Company Name')
    company_moto = models.CharField(
        max_length=200, help_text='Enter Company Moto')
    company_description = HTMLField(
        blank=True, help_text='Enter Company Descriptions')
    cover_pic = models.ImageField(
        upload_to='images/', help_text='Enter Company Cover Pic(max-height:250px)')
    logo_pic = models.ImageField(
        upload_to='images/', help_text='Enter Company Logo Pic(height:220px,width:220px)')

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


class Academic(models.Model):
    dateTime = models.DateTimeField(auto_now=False, auto_now_add=True)
    project_cover_pic = models.ImageField(
        upload_to='images/', help_text='Enter Project Cover Pic max-height:250px')
    project_title = models.CharField(max_length=200,
                                     help_text="Title Of the project", blank=True)
    project_owner = models.CharField(
        max_length=200, help_text="Owner Of the project", blank=True)
    project_location = models.CharField(max_length=500,
                                        help_text="Title Of the project", blank=True)
    project_description = HTMLField(
        blank=True, help_text='Enter Project Descriptions')
    slide_image1 = models.ImageField(
        upload_to='images/', help_text='Enter Company Cover Pic(max-height:250px)', blank=True)
    slide_image2 = models.ImageField(
        upload_to='images/', help_text='Enter Company Cover Pic(max-height:250px)', blank=True)
    slide_image3 = models.ImageField(
        upload_to='images/', help_text='Enter Company Cover Pic(max-height:250px)', blank=True)
    slide_image4 = models.ImageField(
        upload_to='images/', help_text='Enter Company Cover Pic(max-height:250px)', blank=True)
    slide_image5 = models.ImageField(
        upload_to='images/', help_text='Enter Company Cover Pic(max-height:250px)', blank=True)
    external_pic_storage = models.URLField(max_length=200, blank=True)
    external_video_storage = models.URLField(max_length=200, blank=True)

    class Meta:
        ordering = ['dateTime']

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('details', kwargs={'pk': str(self.id), 'section': 'academic', })

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.project_title
