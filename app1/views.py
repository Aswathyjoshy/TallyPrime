from django.shortcuts import render
from multiprocessing import context
from unicodedata import name
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import *
from datetime import datetime, date, timedelta
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'home.html')

def group(request):
    return render(request, 'groups.html')

def branch(request):
    return render(request, 'branch.html')

def ledger(request):
    return render(request, 'ledger.html')

def primary(request):
    return render(request, 'primarycost.html')

def costcat(request):
    return render(request, 'costcat.html')

def costcentr(request):
    return render(request, 'costcentr.html')

def voucher(request):
    return render(request, 'voucher.html')

def vouchpage(request):
    return render(request, 'vouchpage.html')

def currency(request):
    obj=CreateCurrency.objects.all()
    context={'cur':obj,}
    return render(request, 'currency.html',context)



# def currency_alter(request):

#     return render(request, 'currency_alter.html')

def currency_alter(request,pk):
    cur=CreateCurrency.objects.get(id=pk)
    return render(request,'currency_alter.html',{'i':cur})


def stock_grp(request):
    return render(request, 'stock_grp.html')

def stock_items(request):
    return render(request, 'stock_items.html')

def stock_cat(request):
    return render(request, 'stock_cat.html')

def units(request):
    return render(request, 'units.html')

def godwn(request):
    return render(request, 'godwn.html')

def godwn_alter(request):
    return render(request, 'godwn_alter.html')

def emp_cat(request):
    return render(request, 'emp_cat.html')

def emp_cat_alter(request):
    return render(request, 'emp_cat_alter.html')

def emp_grp(request):
    return render(request, 'emp_grp.html')

def emp(request):
    return render(request, 'emp.html')

def atndnce_list(request):
    return render(request, 'atndnce_list.html')

def pay(request):
    return render(request, 'pay.html')

def profit(request):
    return render(request, 'profit.html')


@csrf_exempt
def create_group(request):
    if request.method == 'POST':
        gname = request.POST['gname']
        alia = request.POST['alia']
        if len(gname) <= 0:
            return JsonResponse({
                'status': 00
            })

        if len(alia) <= 0:
            alia = None
        else:
            pass

        under = request.POST['und']
        gp = request.POST['subled']
        nett = request.POST['nee']
        calc = request.POST['cal']
        meth = request.POST['meth']

        mdl = GroupModel(
            name=gname,
            alias=alia,
            under=under,
            gp_behaves_like_sub_ledger=gp,
            nett_debit_credit_bal_reporting=nett,
            used_for_calculation=calc,
            method_to_allocate_usd_purchase=meth,
        )
        mdl.save()
        # return redirect('index_view')
        return JsonResponse({
            'status': 1
        })


def load_create_currency(request):
    return render(request,'load_create_currency.html')

def create_currency(request):
    if request.method == 'POST':
        symbol = request.POST['symbol']
        fname = request.POST['fname']
        if len(symbol) <= 0:
            print('XX')
            return JsonResponse({
                'status': 00
            })
        elif len(fname) <= 0:
            print('XXX')
            return JsonResponse({
                'status': 00
            })
        else:
            pass

        iso_code = request.POST['iso_code']
        n_deci_placs = request.POST['n_deci_placs']
        smt_millon = request.POST['smt_millon']
        symbol_to_amount = request.POST['symbol_to_amount']
        space_bt_sy = request.POST['space_bt_sy']
        amount_after_decimal = request.POST['amount_after_decimal']
        amount_in_words = request.POST['amount_in_words']

        mdl_obj = CreateCurrency(
            symbol=symbol,
            formal_name=fname,
            ISO_code=iso_code,
            decimal_places=n_deci_placs,
            show_in_millions=smt_millon,
            suffix_to_amount=symbol_to_amount,
            space_symbol_amount=space_bt_sy,
            word_after_decimal=amount_after_decimal,
            decimal_no_in_words=amount_in_words,
        )
        mdl_obj.save()
        return redirect('load_create_currency')

def save_currency_data(request):
    if request.method == 'POST':
        sl = request.POST['slno']
        cname = request.POST['curname']
        stdr = request.POST['stdr']
        lvr = request.POST['lvr']
        sr = request.POST['sr']
        lvr2 = request.POST['lvr2']
        sr2 = request.POST['sr2']
        
        obj = CurrencyAlter(
            slno = sl,
            currencys= cname,
            stdrate = stdr,
            lastvrate = lvr,
            specirate = sr,
            lastvrate2 = lvr2,
            specirate2 = sr2,
            
            
           
        )
        
        obj.save()
        grp = CreateCurrency.objects.all()
        obj1 = CurrencyAlter.objects.all()
        context = {'grp':grp ,'obj':obj1}
        return redirect('load_rates_of_exchange',context)

        # ********************************************************************

def save_ledger(request):
    if request.method == 'POST':
        # Ledger Basic
        Lname = request.POST.get('ledger_name', False)
        Lalias = request.POST.get('ledger_alias', False)
        Lunder = request.POST.get('group_under', False)
        Lopening_bal = request.POST.get('ledger_opening_bal', False)
        typ_of_ledg = request.POST.get('ledger_type', False)
        provide_banking = request.POST.get('provide_banking_details', False)

        # Banking_details
        B_od_limit = request.POST.get('od_limit', False)
        B_ac_holder_name =request.POST.get('holder_name', False)
        B_ac_no = request.POST.get('ac_number', False)
        B_ifsc = request.POST.get('ifsc', False)
        B_swift_code =request.POST.get('swift_code', False)
        B_name = request.POST.get('bank_name', False)
        B_branch = request.POST.get('branch_name', False)
        B_alter_chq_bks =request.POST.get('alter_chk_bks', False)
        B_name_enbl_chq_prtg = request.POST.get('enbl_chk_printing', False) 
        B_chqconfg= request.POST.get('chqconfg', False) 
        # Mailing_details
        Mname = request.POST.get('name', False)
        Maddress = request.POST.get('address', False)
        Mstate =request.POST.get('state', False)
        Mcountry = request.POST.get('country', False)
        Mpincode = request.POST.get('pincode', False)

        # Tax_Registration_Details
        Tgst_uin = request.POST.get('gst_uin', False)
        Treg_typ = request.POST.get('register_type', False)
        Tpan_no = request.POST.get('pan_no', False)
        T_alter_gst =request.POST.get('alter_gst_details', False)

        # Satutory Details
        assessable_calculationn = request.POST.get('assessable_calculation', False)
        Appropriate_too =request.POST.get('Appropriate_to', False)
        gst_applicablee = request.POST.get('is_gst_applicable',False)
        Set_alter_GSTT=request.POST.get('Set_alter_GST', False)
        type_of_supplyy = request.POST.get('type_of_supply',False)
        Method_of_calcc=request.POST.get('Method_of_calc', False)

        #leadger Rounding
        ledger_idd=request.POST.get('useadvc', False)
        Rounding_Methodd=request.POST.get('Rounding_Method', False)
        Round_limitt =request.POST.get('Round_limit', False)

        #ledger_tax 
        type_of_duty_or_taxx=request.POST.get('type_of_duty_or_tax', False)
        type_of_taxx=request.POST.get('type_of_tax', False)
        valuation_typee=request.POST.get('valuation_type', False)
        rate_per_unitt=request.POST.get('rate_per_unit', False)
        Persentage_of_calculationn=request.POST.get('Persentage_of_calculation', False)

        #sundry
        maintain_balance_bill_by_billl=request.POST.get('maintain_balance_bill_by_bill', False)
        Default_credit_periodd=request.POST.get('Default_credit_period', False)
        Check_for_credit_dayss=request.POST.get('Check_for_credit_days', False)

        if Ledger.objects.filter(ledger_name = Lname ).exists():
                messages.info(request,'This Name is already taken...!')
                return redirect('load_create_ledger.html')

        Lmdl = Ledger(
            ledger_name=Lname,
            ledger_alias=Lalias,
            group_under=Lunder,
            ledger_opening_bal=Lopening_bal,
            ledger_type=typ_of_ledg,
            provide_banking_details=provide_banking,
        )
        Lmdl.save()
        idd = Lmdl
        Bmdl = Ledger_Banking_Details(
        
            ledger_id=idd,
            od_limit=B_od_limit,
            holder_name=B_ac_holder_name,
            ac_number=B_ac_no,
            ifsc=B_ifsc,
            swift_code=B_swift_code,
            bank_name=B_name,
            branch_name=B_branch,
            alter_chk_bks=B_alter_chq_bks,
            enbl_chk_printing=B_name_enbl_chq_prtg,

        )
        Bmdl.save()
        M_mdl = Ledger_Mailing_Address(

            name=Mname,
            address=Maddress,
            state=Mstate,
            country=Mcountry,
            pincode=Mpincode,
        )
        M_mdl.save()
        T_mdl = Ledger_Tax_Register(
           
          
            gst_uin=Tgst_uin,
            register_type=Treg_typ,
            pan_no=Tpan_no,
            alter_gst_details=T_alter_gst,

        )
        T_mdl.save()
        LS_mdl = Ledger_Satutory(

            ledger_id=idd,
            assessable_calculation=assessable_calculationn,
            Appropriate_to =Appropriate_too ,
            gst_applicable=gst_applicablee,
            Set_alter_GST = Set_alter_GSTT,
            type_of_supply=type_of_supplyy,
            Method_of_calc = Method_of_calcc,


        )
        LS_mdl.save()

        rnd_mdl = Ledger_Rounding(
            ledger_id=idd,
            Rounding_Method=Rounding_Methodd,
            Round_limit =Round_limitt,

        )
        rnd_mdl.save()

        tax_mdl = ledger_tax(
            ledger_id=idd,
            type_of_duty_or_tax=type_of_duty_or_taxx,
            type_of_tax =type_of_taxx,
            valuation_type=valuation_typee,
            rate_per_unit=rate_per_unitt,
            Persentage_of_calculation=Persentage_of_calculationn,
        )
        tax_mdl.save()

        sndry_mdl = Ledger_sundry(
            ledger_id=idd,
            maintain_balance_bill_by_bill=maintain_balance_bill_by_billl,
            Default_credit_period=Default_credit_periodd,
            Check_for_credit_days =Check_for_credit_dayss,
        )
        sndry_mdl.save()
        messages.info(request,'LEDGER CREATED SUCCESSFULLY')
        return redirect('load_create_ledger.html')