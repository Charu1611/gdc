# Generated by Django 4.1.1 on 2022-10-09 11:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('review', models.TextField(blank=True, max_length=500, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('display', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='no', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
