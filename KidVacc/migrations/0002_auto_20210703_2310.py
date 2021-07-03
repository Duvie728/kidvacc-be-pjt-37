# Generated by Django 3.1.4 on 2021-07-03 22:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('KidVacc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100)),
                ('Middle_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('Gender', models.TextField(max_length=25)),
                ('Date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('Blood_group', models.CharField(max_length=25)),
                ('Genotype', models.TextField()),
                ('Vaccination_history', models.TextField(max_length=250)),
                ('images', models.ImageField(upload_to='', verbose_name='images')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('First_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('Gender', models.TextField(max_length=25)),
                ('Email_address', models.EmailField(max_length=250)),
                ('Password', models.TextField()),
                ('Phone_number', models.IntegerField()),
                ('images', models.ImageField(upload_to='', verbose_name='images')),
            ],
        ),
        migrations.DeleteModel(
            name='child_details',
        ),
        migrations.DeleteModel(
            name='parent_details',
        ),
        migrations.AddField(
            model_name='hospital_details',
            name='address',
            field=models.CharField(default='', max_length=1024, verbose_name='Address line 1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hospital_details',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='hospital_type',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KidVacc.parent'),
        ),
    ]
