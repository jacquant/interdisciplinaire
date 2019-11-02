from django.db import models


class ReportingAuthority(models.Model):
    name_authority = models.CharField(max_length=100)


# Create your models here.
class Action(models.Model):
    organization = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    reporting_authority = models.ManyToManyField(ReportingAuthority)
    access = models.CharField(max_length=100)
    reporting_year = models.CharField(max_length=100)
    climate_hazard = models.CharField(max_length=100)
    adaptation_action = models.CharField(max_length=100)
    action_title = models.CharField(max_length=100)
    action_status = models.CharField(max_length=100)
    co_benefit_area = models.CharField(max_length=100)
    action_description = models.TextField()
    finance_status = models.CharField(max_length=100)
    total_cost_project = models.CharField(max_length=100)
    total_cost_provided_government = models.CharField(max_length=100)
    web_link = models.URLField()
    population = models.IntegerField()
    population_year = models.IntegerField()
    city_location = models.CharField(max_length=100)
    country_location = models.CharField(max_length=100)
