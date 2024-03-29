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
    name =  models.CharField(max_length=225,default="Null",blank=True)
    alias =  models.CharField(max_length=225,default="Null",blank=True)
    under =models.CharField(max_length=225,default="Null",blank=True)
    nature_of_group = models.CharField(max_length=225,default="Null",blank=True)
    does_it_affect =models.CharField(max_length=225,default="Null",blank=True)
    gp_behaves_like_sub_ledger =  models.CharField(max_length=225,default="Null",blank=True)
    nett_debit_credit_bal_reporting =  models.CharField(max_length=225,default="Null",blank=True)
    used_for_calculation =  models.CharField(max_length=225,default="Null",blank=True)
    method_to_allocate_usd_purchase =  models.CharField(max_length=225,default="Null",blank=True)

    def __str__(self):
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
class VoucherModels(models.Model):
    voucher_name = models.CharField(max_length=225)
    alias = models.CharField(max_length=225)
    voucher_type = models.CharField(max_length=225)
    abbreviation = models.CharField(max_length=225)
    active_this_voucher_type =  models.CharField(max_length=225)
    method_voucher_numbering = models.CharField(max_length=225)
    use_adv_conf = models.CharField(max_length=225,blank=True)
    prvnt_duplictes = models.CharField(max_length=225,default="Null",blank=True)
    use_effective_date =  models.CharField(max_length=225,default="Null")
    allow_zero_value_trns =  models.CharField(max_length=225)
    allow_naration_in_voucher =  models.CharField(max_length=225)
    make_optional =  models.CharField(max_length=225)
    provide_naration =  models.CharField(max_length=225)
    print_voucher = models.CharField(max_length=225)


class CurrencyAlter(models.Model):
    cname= models.ForeignKey( CreateCurrency,on_delete=models.CASCADE,default=1)
    slno = models.CharField(max_length=225)
    currencys = models.CharField(max_length=225)
    stdrate =models.CharField(max_length=225)
    lastvrate =models.CharField(max_length=225)
    specirate =models.CharField(max_length=225)
    lastvrate2 =models.CharField(max_length=225)
    specirate2 =models.CharField(max_length=225)


# *********************************************************************

class CostCategory(models.Model):
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    revenue=models.CharField(max_length=225)
    nonrevenue=models.CharField(max_length=225)

class Costcentr(models.Model):
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    emply=models.CharField(max_length=225)

class GrpAlter(models.Model):
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    nature=models.CharField(max_length=225)
    grp=models.CharField(max_length=225)
    nett=models.CharField(max_length=225)
    used=models.CharField(max_length=225)
    method=models.CharField(max_length=225)




class Ledger(models.Model):
    ledger_name = models.CharField(max_length=225,default="Null",blank=True)
    ledger_alias = models.CharField(max_length=225,default="Null",blank=True)
    group_under =  models.CharField(max_length=225,default="Null",blank=True)
    ledger_opening_bal = models.CharField(max_length=225,default="Null",blank=True)
    ledger_type = models.CharField(max_length=225,default="Null",blank=True)
    provide_banking_details =  models.CharField(max_length=225,default="Null",blank=True)

    def __str__(self):
        return self.ledger_name


class Ledger_Banking_Details(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    od_limit = models.CharField(max_length=225,default="Null",blank=True)
    holder_name =models.CharField(max_length=225,default="Null",blank=True)
    ac_number =models.CharField(max_length=225,default="Null",blank=True)
    ifsc =models.CharField(max_length=225,default="Null",blank=True)
    swift_code =models.CharField(max_length=225,default="Null",blank=True)
    bank_name = models.CharField(max_length=225,default="Null",blank=True)
    branch_name = models.CharField(max_length=225,default="Null",blank=True)
    alter_chk_bks =  models.CharField(max_length=225,default="Null",blank=True)
    enbl_chk_printing =  models.CharField(max_length=225,default="Null",blank=True)
    chqconfg= models.CharField(max_length=225,default="Null",blank=True)

class Ledger_Mailing_Address(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=225,default="Null",blank=True)
    address = models.CharField(max_length=225,default="Null",blank=True)
    state = models.CharField(max_length=225,default="Null",blank=True)
    country =models.CharField(max_length=225,default="Null",blank=True)
    pincode =models.CharField(max_length=225,default="Null",blank=True)


class Ledger_Tax_Register(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    gst_uin = models.CharField(max_length=225,default="Null",blank=True)
    register_type =models.CharField(max_length=225,default="Null",blank=True)
    pan_no = models.CharField(max_length=225,default="Null",blank=True)
    alter_gst_details = models.CharField(max_length=225,default="Null",blank=True)


class Ledger_Satutory(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    assessable_calculation = models.CharField(max_length=225,default="Null",blank=True)
    Appropriate_to =models.CharField(max_length=225,default="Null",blank=True)
    gst_applicable = models.CharField(max_length=225,default="Null",blank=True)
    Set_alter_GST =models.CharField(max_length=225,default="Null",blank=True)
    type_of_supply = models.CharField(max_length=225,default="Null",blank=True)
    Method_of_calc=models.CharField(max_length=225,default="Null",blank=True)

class Ledger_Rounding(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    Rounding_Method =models.CharField(max_length=225,default="Null",blank=True)
    Round_limit = models.CharField(max_length=22,default="Null",blank=True)

class ledger_tax(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    type_of_duty_or_tax =models.CharField(max_length=225,default="Null",blank=True)
    type_of_tax =models.CharField(max_length=225,default="Null",blank=True)
    valuation_type=models.CharField(max_length=225,default="Null",blank=True)
    rate_per_unit =models.CharField(max_length=225,default="Null",blank=True)
    Persentage_of_calculation=models.CharField(max_length=225,default="Null",blank=True)
   

class Ledger_sundry(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    maintain_balance_bill_by_bill =models.CharField(max_length=225,default="Null",blank=True)
    Default_credit_period=models.CharField(max_length=225,default="Null",blank=True)
    Check_for_credit_days=models.CharField(max_length=225,default="Null",blank=True)
    


    





