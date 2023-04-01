# Generated by Django 4.0 on 2021-12-29 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_video_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='category',
            field=models.CharField(choices=[('Algorithm', 'Algorithm'), ('Data Structures', 'Data Structures'), ('Dynamic Programming', 'Dynamic Programming'), ('Mathematics', 'Mathematics'), ('Implementation', 'Implementation'), ('String', 'String'), ('Searching and Sortings', 'Searching and Sortings'), ('Graph', 'Graph'), ('Geometry', 'Geometry'), ('Miscellaneous', 'Miscellaneous'), ('Live Contests', 'Live Contests')], default='Live Contest', max_length=255),
        ),
    ]
