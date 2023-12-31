# Generated by Django 4.2.6 on 2023-10-12 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text_image', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='hadiths',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hadith_number', models.IntegerField()),
                ('text', models.TextField()),
                ('hadith_status', models.CharField(choices=[('Sahih', 'Sahih'), ('Zaif', 'Zaif'), ('Hasan', 'Hasan')], max_length=5)),
            ],
        ),
        migrations.DeleteModel(
            name='ImageWithText',
        ),
    ]
