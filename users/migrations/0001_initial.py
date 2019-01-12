# Generated by Django 2.1.5 on 2019-01-12 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trips', '0001_initial'),
        ('rewards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
                ('weight', models.IntegerField(default=60)),
                ('rose', models.IntegerField(default=0)),
                ('gear', models.IntegerField(default=0)),
                ('coin', models.IntegerField(default=0)),
                ('reg_time', models.DateField(auto_now_add=True)),
                ('favorites', models.ManyToManyField(related_name='favorite_places', to='trips.Location')),
                ('title_equipped', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='title_euipped', to='rewards.Title')),
                ('titles_had', models.ManyToManyField(related_name='titles_had', to='rewards.Title')),
            ],
        ),
    ]