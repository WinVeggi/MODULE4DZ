# Generated by Django 4.2.3 on 2023-07-31 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dz', '0007_alter_advertisement_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='auction',
            field=models.BooleanField(help_text='Отметьте если торг уместен.', verbose_name='возможность торга'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='description',
            field=models.TextField(verbose_name='описание объявления'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.CharField(max_length=128, verbose_name='заголовок'),
        ),
        migrations.AlterModelTable(
            name='advertisement',
            table='advertisements',
        ),
    ]
