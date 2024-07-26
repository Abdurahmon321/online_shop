# Generated by Django 5.0.2 on 2024-05-15 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retailer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retailerprofile',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='retailerprofile',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='retailerprofile',
            name='firstname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='retailerprofile',
            name='img',
            field=models.ImageField(null=True, upload_to='user_profile/'),
        ),
        migrations.AlterField(
            model_name='retailerprofile',
            name='lastname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='retailerprofile',
            name='mobile_number',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='retailerprofile',
            name='phone_number',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='retailerprofile',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]