import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_remove_responses_author_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='responses',
            name='accepted',
            field=models.BooleanField(default=False, verbose_name='Принято/Отклонено'),
        ),
    ]
