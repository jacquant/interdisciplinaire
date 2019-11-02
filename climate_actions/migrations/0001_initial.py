# Generated by Django 3.0b1 on 2019-11-02 13:14

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReportingAuthority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_authority', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('access', models.CharField(max_length=100)),
                ('reporting_year', models.CharField(max_length=100)),
                ('climate_hazard', models.CharField(max_length=100)),
                ('adaptation_action', models.CharField(max_length=100)),
                ('action_title', models.CharField(max_length=100)),
                ('action_status', models.CharField(max_length=100)),
                ('co_benefit_area', models.CharField(max_length=100)),
                ('action_description', models.TextField()),
                ('finance_status', models.CharField(max_length=100)),
                ('total_cost_project', models.CharField(max_length=100)),
                ('total_cost_provided_government', models.CharField(max_length=100)),
                ('web_link', models.URLField()),
                ('population', models.IntegerField()),
                ('population_year', models.IntegerField()),
                ('city_location', models.CharField(max_length=100)),
                ('country_location', models.CharField(max_length=100)),
                ('reporting_authority', models.ManyToManyField(to='climate_actions.ReportingAuthority')),
            ],
        ),
    ]