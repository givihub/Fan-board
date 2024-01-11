import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_alter_notice_content_alter_responses_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Контент'),
        ),
    ]
