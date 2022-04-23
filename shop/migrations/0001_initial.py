# Generated by Django 4.0.4 on 2022-04-22 11:03

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_image', models.ImageField(help_text='Image to show in list', upload_to='img')),
                ('title', models.CharField(help_text='News title e.g. Deal title or Update title', max_length=256)),
                ('poster', models.ImageField(help_text='Image to show in content page', upload_to='img')),
                ('content', models.TextField(help_text='News Contents')),
                ('published_by', models.DateTimeField(default=django.utils.timezone.now, help_text='Published date')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_image', models.ImageField(help_text='Image to show in list', upload_to='img')),
                ('title', models.CharField(help_text='article title', max_length=256)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('published_by', models.DateTimeField(default=django.utils.timezone.now, help_text='Published date')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=256)),
                ('event_start', models.DateField(default=django.utils.timezone.now, help_text='Event starting date')),
                ('event_end', models.DateField(default=django.utils.timezone.now, help_text='Event ending date')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(help_text='This is Logo image', upload_to='img')),
                ('name', models.CharField(help_text='Store name', max_length=256)),
                ('store_type', models.CharField(choices=[('BNK', 'Bank'), ('BUT', 'Beauty'), ('ECT', 'Electrical'), ('ENT', 'Entertainment'), ('FSH', 'Fashion'), ('FOD', 'Food'), ('FUN', 'Furniture'), ('JEW', 'JEWELLERY'), ('SVC', 'Services'), ('SPT', 'Sport'), ('TOY', 'Toy')], default='FOD', help_text='Store Type', max_length=3)),
                ('location', models.CharField(help_text='Store location', max_length=256)),
                ('contact', models.CharField(help_text='Store contact', max_length=256)),
                ('opening', models.CharField(help_text='Opening Time', max_length=256)),
                ('description', models.TextField(help_text='Store description')),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_image', models.ImageField(help_text='Image to show in list', upload_to='img')),
                ('title', models.CharField(help_text='News title e.g. Deal title or Update title', max_length=256)),
                ('poster', models.ImageField(help_text='Image to show in content page', upload_to='img')),
                ('content', models.TextField(help_text='News Contents')),
                ('published_by', models.DateTimeField(default=django.utils.timezone.now, help_text='Published date')),
                ('event', models.ForeignKey(help_text='Event Schedule', on_delete=django.db.models.deletion.CASCADE, to='shop.event')),
                ('related_store_id', models.ForeignKey(help_text='Event Store', on_delete=django.db.models.deletion.DO_NOTHING, to='shop.store')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
