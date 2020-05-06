# Generated by Django 2.1.5 on 2019-02-24 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('head', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='head', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeesInDepartments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department', to='helpdesk.Department')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(default='', max_length=100)),
                ('place', models.CharField(default='', max_length=100)),
                ('priority', models.IntegerField(default='0', max_length=100)),
                ('details', models.CharField(default='', max_length=1000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('requestor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requestor', to=settings.AUTH_USER_MODEL)),
                ('targeted_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='targeted_department', to='helpdesk.Department')),
            ],
        ),
    ]