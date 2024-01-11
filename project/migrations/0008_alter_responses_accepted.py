from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_alter_category_name_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responses',
            name='accepted',
            field=models.BooleanField(),
        ),
    ]
