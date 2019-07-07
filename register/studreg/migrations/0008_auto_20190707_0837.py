# Generated by Django 2.1.5 on 2019-07-07 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studreg', '0007_auto_20190707_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='alloted_course_code',
            field=models.CharField(choices=[('BTech', 'BTech'), ('MTech', 'MTech'), ('PhD', 'PhD')], default='BTech', max_length=10, verbose_name='Alloted Course Code'),
        ),
        migrations.AlterField(
            model_name='student',
            name='concession',
            field=models.CharField(choices=[('No eligibility', 'No eligibility'), ('SC', 'SC'), ('ST', 'ST'), ('OEC', 'OEC')], default='No eligibility', max_length=20, verbose_name='Nature of Eligibility for fee concession'),
        ),
        migrations.AlterField(
            model_name='student',
            name='fee_concession',
            field=models.BooleanField(default=False, help_text='Tick if eligible', verbose_name='Fee Concession'),
        ),
    ]
