from django.db import models

# Create your models here.
class Idea(models.Model):
    name = models.CharField(max_length=30)
    long_description = models.TextField(blank=True)

    market_population = models.PositiveIntegerField(default=0, help_text='Total Market population')
    market_percentage = models.PositiveSmallIntegerField(default=2, verbose_name= 'Market %', help_text='% of Market population that we expect to cover')

    monthly_sales = models.PositiveIntegerField(default=0, help_text='Number(avg) of sales we expect to do monthly')

    initial_cost = models.PositiveIntegerField(default=0, help_text='How much is going to cost us to create this piece of software')
    monthly_cost = models.PositiveIntegerField(default=0, help_text='Monthly cost for having the service up and running')

    sale_price = models.PositiveIntegerField(default=0, help_text='Price of one copy of the app')
    subscription_fee = models.PositiveIntegerField(default=0, help_text='monthly price for using this product or service')

    years = models.PositiveSmallIntegerField(default=1, help_text="Number of years we want to use for guessing how much profits we will get")
    expectation_x_years = models.PositiveIntegerField(default=0, help_text='How much do we expect to earn in x years', editable=True)

    class Meta:
        ordering = ('-expectation_x_years',)

    @property
    def max_number_of_sales(self):
        """
        we can only cover certain percentange of the market no matter how good we are
        """
        return self.market_population*self.market_percentage/100

    def total_number_of_sales(self, years=1):
        max_number_of_sales = self.max_number_of_sales
        if self.monthly_sales*12*years < max_number_of_sales:
            return self.monthly_sales*12*years
        else:
            return max_number_of_sales

    def expection_in_years(self, years = 1):
        total_number_of_sales = self.total_number_of_sales(years)
        cost = self.initial_cost + self.monthly_cost*12*years
        earnings = total_number_of_sales*(self.sale_price + self.subscription_fee*12*years)
        return earnings - cost


    @property
    def expectation(self):
        """
        it will return the expectation in one year
        """
        return self.expection_in_years(1)

    def save(self, *args, **kwargs):
        self.expectation_x_years = self.expection_in_years(self.years)

        super(Idea, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
