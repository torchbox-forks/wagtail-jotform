# Generated by Django 3.1.1 on 2020-10-07 08:49

import django.db.models.deletion
import wagtail.contrib.routable_page.models
from wagtail import VERSION as WAGTAIL_VERSION

if WAGTAIL_VERSION >= (3, 0):
    import wagtail.fields as wagtail_fields
else:
    import wagtail.core.fields as wagtail_fields

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0052_pagelogentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmbededFormPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('introduction', models.TextField(blank=True)),
                ('form', models.CharField(max_length=1000)),
                ('thank_you_text', wagtail_fields.RichTextField(blank=True, help_text='Text displayed to the user on successful submission of the form')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.routable_page.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
    ]
