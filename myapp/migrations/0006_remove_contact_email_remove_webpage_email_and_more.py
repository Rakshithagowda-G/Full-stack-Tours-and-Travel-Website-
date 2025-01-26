# Generated by Django 5.1.5 on 2025-01-19 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20190721_0207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='webpage',
            name='Email',
        ),
        migrations.AlterField(
            model_name='contact',
            name='fullname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='msg',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='package',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='package',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='package',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='repassword',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterModelTable(
            name='contact',
            table=None,
        ),
        migrations.AlterModelTable(
            name='package',
            table='package',
        ),
        migrations.AlterModelTable(
            name='webpage',
            table='web',
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='default@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='webpage',
            name='email',
            field=models.EmailField(default='default@example.com', max_length=254),
        ),
    ]
