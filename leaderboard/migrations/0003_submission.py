# Generated by Django 2.2.1 on 2019-08-31 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0002_testset_json_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        db_index=True,
                        help_text='Test set name (max 200 characters)',
                        max_length=200,
                    ),
                ),
                (
                    'test_set',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to='leaderboard.TestSet',
                    ),
                ),
            ],
        ),
    ]
