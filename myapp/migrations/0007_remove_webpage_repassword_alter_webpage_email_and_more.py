# Generated by Django 5.1.5 on 2025-01-19 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_contact_email_remove_webpage_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webpage',
            name='repassword',
        ),
        migrations.AlterField(
            model_name='webpage',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='password',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterModelTable(
            name='webpage',
            table=None,
        ),
    ]
