# Generated by Django 4.2.1 on 2023-05-19 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_tag_post_is_advertising_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='language',
            field=models.CharField(choices=[('uz_latin', 'uz_latin'), ('uz_kirill', 'uz_kirill'), ('rus', 'rus'), ('eng', 'eng')], default='uz_latin', max_length=10),
        ),
    ]
