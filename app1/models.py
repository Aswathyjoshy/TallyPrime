# from django.db import models

# # Create your models here.
# from django.db import models

# class GroupModel(models.Model):
#     name = models.CharField(max_length=225)
#     alias = models.CharField(max_length=225,null=True)
#     under = models.CharField(max_length=225)
#     gp_behaves_like_sub_ledger = models.BooleanField(default=False)
#     nett_debit_credit_bal_reporting = models.BooleanField(default=False)
#     used_for_calculation = models.BooleanField(default=False)
#     method_to_allocate_usd_purchase = models.CharField(max_length=225,null=True,blank=True)

#     def __str__(self):
#         return self.name
from decimal import Decimal
from locale import currency
from unicodedata import decimal
from django.db import models

# Create your models here.
class GroupModel(models.Model):
    name = models.CharField(max_length=225)
    alias = models.CharField(max_length=225,null=True)
    under = models.CharField(max_length=225)
    gp_behaves_like_sub_ledger = models.BooleanField(default=False)
    nett_debit_credit_bal_reporting = models.BooleanField(default=False)
    used_for_calculation = models.BooleanField(default=False)
    method_to_allocate_usd_purchase = models.CharField(max_length=225,null=True,blank=True)

    def _str_(self):
        return self.name
    
class CreateCurrency(models.Model):
    symbol =models.CharField(max_length=225)
    formal_name=models.CharField(max_length=225)
    ISO_code=models.CharField(max_length=225)
    decimal_places= models.CharField(max_length=225,default=2)
    show_in_millions =  models.CharField(max_length=225)
    suffix_to_amount=  models.CharField(max_length=225)
    space_symbol_amount = models.CharField(max_length=225)
    word_after_decimal = models.CharField(max_length=225)
    decimal_no_in_words = models.CharField(max_length=225)

# class CreateEmployeeCategory(models.Model):
#     name =models.CharField(max_length=225)
#     alias=models.CharField(max_length=225)
#     allocate_revenue=models.CharField(max_length=225)
#     allocate_nonrevenue=models.CharField(max_length=225)



# class VoucherModel(models.Model):
#     voucher_name = models.CharField(max_length=225)
#     alias = models.CharField(max_length=225)
#     voucher_type = models.CharField(max_length=225)
#     abbreviation = models.CharField(max_length=225)
#     active_this_voucher_type = models.BooleanField()
#     method_voucher_numbering = models.CharField(max_length=225)
#     use_effective_date = models.BooleanField()
#     allow_zero_value_trns = models.BooleanField()
#     allow_naration_in_voucher = models.BooleanField()
#     enable_default_ac_allocation = models.BooleanField()
#     track_additional_cost_purchase = models.BooleanField()
#     use_as_manf_journal = models.BooleanField()
#     print_voucher_af_save = models.BooleanField()
#     print_formal_recept = models.BooleanField()
#     default_juridiction = models.CharField(max_length=225)
#     default_title = models.CharField(max_length=225)
#     alter_decalaration = models.BooleanField()


# class CurrencyAlter(models.Model):
#     cname= models.ForeignKey( CreateCurrency,on_delete=models.CASCADE,default=1)
#     slno = models.CharField(max_length=225)
#     currencys = models.CharField(max_length=225)
#     stdrate =models.CharField(max_length=225)
#     lastvrate =models.CharField(max_length=225)
#     specirate =models.CharField(max_length=225)
#     lastvrate2 =models.CharField(max_length=225)
#     specirate2 =models.CharField(max_length=225)
class VoucherModel(models.Model):
    voucher_name = models.CharField(max_length=225)
    alias = models.CharField(max_length=225)
    voucher_type = models.CharField(max_length=225)
    abbreviation = models.CharField(max_length=225)
    active_this_voucher_type = models.BooleanField()
    method_voucher_numbering = models.CharField(max_length=225)
    use_effective_date = models.BooleanField()
    allow_zero_value_trns = models.BooleanField()
    allow_naration_in_voucher = models.BooleanField()
    enable_default_ac_allocation = models.BooleanField()
    track_additional_cost_purchase = models.BooleanField()
    use_as_manf_journal = models.BooleanField()
    print_voucher_af_save = models.BooleanField()
    print_formal_recept = models.BooleanField()
    default_juridiction = models.CharField(max_length=225)
    default_title = models.CharField(max_length=225)
    alter_decalaration = models.BooleanField()


# class CurrencyAlter(models.Model):
#     cname= models.ForeignKey( CreateCurrency,on_delete=models.CASCADE,default=1)
#     slno = models.CharField(max_length=225)
#     currencys = models.CharField(max_length=225)
#     stdrate =models.CharField(max_length=225)
#     lastvrate =models.CharField(max_length=225)
#     specirate =models.CharField(max_length=225)
#     lastvrate2 =models.CharField(max_length=225)
#     specirate2 =models.CharField(max_length=225)
