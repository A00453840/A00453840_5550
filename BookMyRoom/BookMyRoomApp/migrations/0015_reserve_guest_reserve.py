# Generated by Django 4.0.3 on 2022-03-14 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookMyRoomApp', '0014_remove_guest_reserve_delete_reserve'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=200)),
                ('checkin', models.CharField(max_length=200)),
                ('checkout', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='guest',
            name='reserve',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='BookMyRoomApp.reserve'),
        ),
    ]
