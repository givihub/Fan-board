from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_responses_author_names_alter_responses_accepted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responses',
            name='author_names',
        ),
    ]
