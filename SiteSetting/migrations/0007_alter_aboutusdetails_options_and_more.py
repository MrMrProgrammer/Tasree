# Generated by Django 4.2.6 on 2023-10-22 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SiteSetting', '0006_sliderimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutusdetails',
            options={'verbose_name': 'About Us', 'verbose_name_plural': 'About Us'},
        ),
        migrations.AlterModelOptions(
            name='homedetails',
            options={'verbose_name': 'Home Setting', 'verbose_name_plural': 'Home Settings'},
        ),
        migrations.AlterModelOptions(
            name='ourservicesdetails',
            options={'verbose_name': 'Our Service', 'verbose_name_plural': 'Our Services'},
        ),
    ]