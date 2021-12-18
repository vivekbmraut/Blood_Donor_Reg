# Generated by Django 3.2.9 on 2021-12-12 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doc_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('doc_name', models.CharField(max_length=50)),
                ('contact_no', models.BigIntegerField(max_length=10)),
                ('doc_hospital', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('donor_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('donor_name', models.CharField(max_length=40)),
                ('blood_group', models.CharField(max_length=3)),
                ('contact_no', models.BigIntegerField(max_length=10)),
                ('last_doantion', models.DateField()),
                ('location_donation', models.CharField(max_length=40)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BloodPlus.doctor')),
            ],
        ),
    ]
