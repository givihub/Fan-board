from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_notice_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='content',
            field=models.TextField(max_length=255, verbose_name='Контент'),
        ),
    ]
