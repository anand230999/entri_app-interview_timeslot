# Generated by Django 3.1.6 on 2021-02-05 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('I', 'Interviewer'), ('C', 'Candidate')], max_length=1)),
                ('user_id', models.CharField(max_length=100)),
                ('available_from_time', models.TimeField()),
                ('available_to_time', models.TimeField()),
            ],
        ),
    ]