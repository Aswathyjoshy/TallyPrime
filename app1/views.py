from django.shortcuts import render
from django.contrib import messages
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
    # obj1=GroupModel.objects.filter(under ='BankAccount1')
    obj=GroupModel.objects.all().filter(under ='curntasts1')
    return render(request, 'groups.html')

def branch(request):
    context={ 'name':'Branch/Division' }
    return render(request, 'branch.html',context)

def ledger(request):
    return render(request, 'ledger.html')



def costcat(request):
    cost=CostCategory.objects.all()
    context={'cost':cost,}

    return render(request, 'costcat.html',context)

def costcentr(request):
    centr=Costcentr.objects.all()
    context={'centr':centr,}

    return render(request, 'costcentr.html',context)

def voucher(request):
    vch=VoucherModels.objects.all()
    context={'vch':vch,}
    return render(request, 'voucher.html',context)

def vouchpage(request):
    return render(request, 'vouchpage.html')

def currency(request):
    obj=CreateCurrency.objects.all()
    context={'cur':obj,}
    return render(request, 'currency.html',context)



# def currency_alter(request):

#     return render(request, 'currency_alter.html')
def primary(request,pk):
    cost=CostCategory.objects.get(id=pk)
    return render(request, 'primarycost.html',{'i':cost})

def currency_alter(request,pk):
    cur=CreateCurrency.objects.get(id=pk)
    return render(request,'currency_alter.html',{'i':cur})

def update_voucher(request,pk):
    vch=VoucherModels.objects.get(id=pk)
    return render(request,'update_voucher.html',{'i':vch})


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

def update_currency(request,pk):
    if request.method=='POST':
        cur =CreateCurrency.objects.get(id=pk)
        cur.symbol = request.POST.get('symbol')
        cur.formal_name = request.POST.get('fname')
        cur.ISO_code = request.POST.get('iso_code')
        cur.decimal_places = request.POST.get('n_deci_placs')
        cur.show_in_millions = request.POST.get('smt_millon')
        cur.suffix_to_amount = request.POST.get('symbol_to_amount')
        cur.space_symbol_amount = request.POST.get('space_bt_sy')
        cur.word_after_decimal = request.POST.get('amount_after_decimal')
        cur.decimal_no_in_words = request.POST.get('amount_in_words')
        
        cur.save()
        return redirect('currency')
    return render(request, 'currency_alter.html',)


def load_create_vouchertyp(request):
    return render(request,'load_create_vouchertyp.html')



def create_voucher(request):
    if request.method == 'POST':
        Vname = request.POST['nam']
        alias = request.POST['alias']
        vtype = request.POST['vtype']
        abbre = request.POST['abbre']
        activ_vou_typ = request.POST['avtyp']  # bool
        meth_vou_num = request.POST['meth_vou_num']
        useadv = request.POST.get('useadvc', False)
        prvtdp = request.POST.get('prvtdp', False)
        use_effct_date = request.POST['uefftdate']  # bool
        allow_zero_trans = request.POST['allow_zero_trans']  # bool
        allow_naration_in_vou = request.POST['allow_naration_in_vou']  # bool
        optional = request.POST['optional'] 
        provide_narr = request.POST['providenr']  # bool
        print = request.POST['print']  # bool

        if VoucherModels.objects.filter(voucher_name=Vname).exists():
                messages.info(request,'This Name is already taken...!')
                return render(request, 'load_create_vouchertyp')
        
        mdl = VoucherModels(

            voucher_name=Vname,
            alias=alias,
            voucher_type=vtype,
            abbreviation=abbre,
            active_this_voucher_type=activ_vou_typ,
            method_voucher_numbering=meth_vou_num,
            use_effective_date=use_effct_date,
            use_adv_conf = useadv,
            prvnt_duplictes =prvtdp,
            allow_zero_value_trns=allow_zero_trans,
            allow_naration_in_voucher=allow_naration_in_vou,
            make_optional=optional,
            provide_naration=provide_narr,
            print_voucher=print,

        )
        mdl.save()
        messages.info(request,'VOUCHER CREATED SUCCESSFULLY')
        return redirect('load_create_vouchertyp')

    return render(request, 'load_create_vouchertyp')


def save_voucher(request,pk):
    if request.method=='POST':
        vch =VoucherModels.objects.get(id=pk)
        vch.voucher_name = request.POST.get('nam')
        vch.alias = request.POST.get('alias')
        vch.voucher_type = request.POST.get('vtype')
        vch.abbreviation = request.POST.get('abbre')
        vch.active_this_voucher_type = request.POST.get('avtyp')
        vch.method_voucher_numbering = request.POST.get('meth_vou_num')
        vch.use_effective_date = request.POST.get('uefftdate')
        vch.allow_zero_value_trns = request.POST.get('allow_zero_trans')
        vch.make_optional = request.POST.get('optional')
        vch.allow_naration_in_voucher = request.POST.get('allow_naration_in_vou')
        vch.provide_naration = request.POST.get('providenr')
        vch.print_voucher = request.POST.get('print')
        
        vch.save()
        return redirect('voucher')
    return render(request, 'update_voucher.html',)

def load_create_groups(request):
    grp = GroupModel.objects.all()
    context={'grp':grp}
    return render(request,'load_create_groups.html',context)

def create_group(request):
    if request.method == 'POST':
        gname = request.POST['gname']
        alia = request.POST['alia']
        under = request.POST['und']
        gp = request.POST['subled']
        naturee = request.POST['nature']
        gross_profitt = request.POST['gross_profit']
        nett = request.POST['nee'] 
        calc = request.POST['cal']
        meth = request.POST['meth']

        grp = GroupModel.objects.all()
        context={'grp':grp}

        if GroupModel.objects.filter(name=gname).exists():
                messages.info(request,'This Name is already taken...!')
                return render(request,'load_create_groups.html',context)

        mdl = GroupModel(
            name=gname,
            alias=alia,
            under=under,
            nature_of_group=naturee,
            does_it_affect=gross_profitt,
            gp_behaves_like_sub_ledger=gp,
            nett_debit_credit_bal_reporting=nett,
            used_for_calculation=calc,
            method_to_allocate_usd_purchase=meth,
        )
        mdl.save()
        grp = GroupModel.objects.all()
        context={'grp':grp}
        messages.info(request,'GROUP CREATED SUCCESSFULLY')
        return render(request,'load_create_groups.html',context)


def update_grp(request,pk):
    if request.method=='POST':
        grp =GroupModel.objects.get(id=pk)
        grp.name = request.POST.get('gname')
        grp.alias = request.POST.get('alia')
        grp.under = request.POST.get('under')
        grp.nature_of_group = request.POST.get('nature')
        grp.does_it_affect = request.POST.get('gross_profit')
        grp.gp_behaves_like_sub_ledger = request.POST.get('subled')
        grp.nett_debit_credit_bal_reporting = request.POST.get('nee')
        grp.used_for_calculation = request.POST.get('cal')
        grp.method_to_allocate_usd_purchase = request.POST.get('meth')
        
        grp.save()
        return redirect('groups')
    return render(request, 'update_grp.html',)

# **********************************************************************************

def update_cost(request,pk):
    if request.method=='POST':
        cost =CostCategory.objects.get(id=pk)
        cost.name = request.POST.get('a')
        cost.alias = request.POST.get('b')
        cost.revenue = request.POST.get('c')
        cost.nonrevenue = request.POST.get('d')
        
        
        cost.save()
        return redirect('base')
    return render(request, 'primarycost.html',)


def centr(request,pk):
    centr=Costcentr.objects.get(id=pk)
    return render(request, 'update_costcentr.html',{'i':centr})


def update_centr(request,pk):
    if request.method=='POST':
        centr =Costcentr.objects.get(id=pk)
        centr.name = request.POST.get('a')
        centr.alias = request.POST.get('b')
        centr.under = request.POST.get('c')
        centr.emply = request.POST.get('d')
        
        
        centr.save()
        return redirect('base')
    return render(request, 'update_costcentr.html',)




