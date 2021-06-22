# Generated by Django 3.2.4 on 2021-06-22 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0014_auto_20210622_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='graphics',
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='items.product')),
                ('cores', models.FloatField()),
                ('clockspeed', models.FloatField()),
                ('graphics', models.CharField(max_length=200, null=True)),
            ],
            bases=('items.product',),
        ),
    ]
