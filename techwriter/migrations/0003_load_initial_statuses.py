# Generated by Django 5.0.1 on 2024-01-23 11:16

from django.db import migrations


def add_status_data(apps, schema_editor):
    Status = apps.get_model('techwriter', 'Status')
    statuses = [
        'Draft',
        'Review',
        'Published'
    ]
    for status_name in statuses:
        Status.objects.create(name=status_name)


class Migration(migrations.Migration):

    dependencies = [
        ('techwriter', '0002_alter_article_options_alter_client_options_and_more'),
    ]

    operations = [
        migrations.RunPython(add_status_data),
    ]
