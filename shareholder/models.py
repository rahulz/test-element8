from datetime import timedelta

from django.db import models
from django.utils.functional import cached_property
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class ShareHolder(models.Model):
    name = models.CharField(max_length=255, help_text='First Name')
    mobile = PhoneNumberField(help_text='Mobile Number', verbose_name='Mobile Number')
    email = models.EmailField()
    country = CountryField(default='IN')

    class Meta:
        ordering = ('-id',)


class Share(models.Model):
    """
    a) The duration of shares is set
    b) The annual amount is set
    c) The installment type (Monthly, Quarterly, Annual, Custom)
    d) A Start date decides from what date the money should be collected
    """
    shareholder = models.OneToOneField(ShareHolder, on_delete=models.CASCADE, blank=True)
    duration = models.PositiveIntegerField(help_text='Duration in years')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    installment_type = models.IntegerField(choices=((12, 'Monthly'), (4, 'Quarterly'), (1, 'Annual')))
    start_date = models.DateField()

    @cached_property
    def no_of_installments(self):
        return self.duration * self.installment_type

    @cached_property
    def installment_amount(self):
        return self.total_amount / self.no_of_installments

    def save(self, *args, **kwrgs):
        if self._state.adding:
            super().save(*args, **kwrgs)
            installments = []
            for i in range(self.no_of_installments):
                obj = Installment(
                    share=self,
                    date=self.start_date + timedelta(i * (12 / self.installment_type * 30)),
                    amount=self.installment_amount
                )
                installments.append(obj)
            Installment.objects.bulk_create(installments)
        else:
            super().save(*args, **kwrgs)

    class Meta:
        ordering = ('-id',)


class Installment(models.Model):
    share = models.ForeignKey(Share, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)

    def toggle_paid(self):
        self.paid = not self.paid
        self.save()

    class Meta:
        ordering = ('id',)
