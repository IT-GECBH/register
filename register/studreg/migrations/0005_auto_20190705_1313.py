# Generated by Django 2.1.5 on 2019-07-05 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studreg', '0004_auto_20190704_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='g_name',
            field=models.CharField(default='asdff', max_length=15, verbose_name="Guardian's name"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='concession',
            field=models.TextField(blank=True, null=True, verbose_name='Nature of Eligibility for fee concession (if applicable)'),
        ),
        migrations.AlterField(
            model_name='student',
            name='local_guardian_name',
            field=models.CharField(max_length=100, verbose_name='Name of Local Guardian'),
        ),
        migrations.AlterField(
            model_name='student',
            name='reservation_code',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Reservation/Special Category Code (if applicable)'),
        ),
        migrations.AlterField(
            model_name='student',
            name='reservation_rank',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Special category/Reservation Rank (if applicable)'),
        ),
        migrations.AlterField(
            model_name='student',
            name='tc_number',
            field=models.CharField(max_length=50, verbose_name='Serial Number of TC produced'),
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together={('admission_no', 'entrance_roll_no')},
        ),
    ]
