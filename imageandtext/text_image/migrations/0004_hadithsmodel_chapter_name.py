# Generated by Django 4.2.6 on 2023-10-12 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text_image', '0003_rename_hadiths_hadithsmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='hadithsmodel',
            name='chapter_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
