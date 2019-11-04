from django.db import models


# Create your models here.
class AdaptationAction(models.Model):
    year_reported_to_cdp = models.CharField(max_length=100)
    account_number = models.IntegerField()
    organization = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    cdp_region = models.CharField(max_length=100)
    reporting_authority = models.CharField(max_length=200)
    access = models.CharField(max_length=100)
    climate_hazard = models.CharField(max_length=100)
    adaptation_action = models.CharField(max_length=100)
    action_title = models.CharField(max_length=100)
    status_of_action = models.CharField(max_length=100)
    co_benefit_area = models.CharField(max_length=100)
    action_description_and_implementation_progress = models.TextField()
    finance_status = models.CharField(max_length=100)
    total_cost_of_project = models.CharField(max_length=30, null=True)
    total_cost_provided_by_the_local_government = models.CharField(max_length=30, null=True)
    primary_source_fund = models.CharField(max_length=100)
    web_link = models.CharField(max_length=100)
    population = models.CharField(max_length=30, null=True)
    population_year = models.CharField(max_length=10, null=True)
    city_location = models.CharField(max_length=100)
    last_update = models.CharField(max_length=50)
