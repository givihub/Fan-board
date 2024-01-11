from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_responses_accepted_alter_notice_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='category_notice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.category', verbose_name='Категории'),
        ),
    ]
