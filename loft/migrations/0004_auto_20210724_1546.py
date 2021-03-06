# Generated by Django 3.2.5 on 2021-07-24 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loft', '0003_answer_correct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]
