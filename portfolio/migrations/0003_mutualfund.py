# Generated by Django 2.0.5 on 2018-07-17 23:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_investment_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mutualfund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('shares', models.DecimalField(decimal_places=1, max_digits=10)),
                ('purchased_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchased_date', models.DateField(default=django.utils.timezone.now)),
                ('recent_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('recent_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mutualfunds', to='portfolio.Customer')),
            ],
        ),
    ]
