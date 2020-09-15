# Generated by Django 3.1.1 on 2020-09-15 05:39

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('architectApps', '0008_auto_20200914_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
                ('project_cover_pic', models.ImageField(help_text='Enter Project Cover Pic max-height:250px', upload_to='images/')),
                ('project_title', models.CharField(blank=True, help_text='Title Of the project', max_length=200)),
                ('project_owner', models.CharField(blank=True, help_text='Owner Of the project', max_length=200)),
                ('project_location', models.CharField(blank=True, help_text='Title Of the project', max_length=500)),
                ('project_description', tinymce.models.HTMLField(blank=True, help_text='Enter Project Descriptions')),
                ('slide_image1', models.ImageField(blank=True, help_text='Enter Company Cover Pic(max-height:250px)', upload_to='images/')),
                ('slide_image2', models.ImageField(blank=True, help_text='Enter Company Cover Pic(max-height:250px)', upload_to='images/')),
                ('slide_image3', models.ImageField(blank=True, help_text='Enter Company Cover Pic(max-height:250px)', upload_to='images/')),
                ('slide_image4', models.ImageField(blank=True, help_text='Enter Company Cover Pic(max-height:250px)', upload_to='images/')),
                ('slide_image5', models.ImageField(blank=True, help_text='Enter Company Cover Pic(max-height:250px)', upload_to='images/')),
                ('external_pic_storage', models.URLField(blank=True)),
                ('external_video_storage', models.URLField(blank=True)),
            ],
            options={
                'ordering': ['dateTime'],
            },
        ),
    ]
