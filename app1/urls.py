from django.urls import path,include
from.import views


urlpatterns = [

    path('',views.base,name='base'),
    path('index',views.index,name='index'),
    path('group',views.group,name='group'),
    path('branch',views.branch,name='branch'),
    path('ledger',views.ledger,name='ledger'),
    path('primary',views.primary,name='primary'),
    path('costcat',views.costcat,name='costcat'),
    path('costcentr',views.costcentr,name='costcentr'),
    path('voucher',views.voucher,name='voucher'),
    path('vouchpage',views.vouchpage,name='vouchpage'),
    path('currency',views.currency,name='currency'),
    path('currency_alter/<int:pk>',views.currency_alter,name='currency_alter'),
    path('stock_grp',views.stock_grp,name='stock_grp'),
    path('stock_items',views.stock_items,name='stock_items'),
    path('units',views.units,name='units'),
    path('stock_cat',views.stock_cat,name='stock_cat'),
    path('godwn',views.godwn,name='godwn'),
    path('godwn_alter',views.godwn_alter,name='godwn_alter'),
    path('emp_cat',views.emp_cat,name='emp_cat'),
    path('emp_cat_alter',views.emp_cat_alter,name='emp_cat_alter'),
    path('emp_grp',views.emp_grp,name='emp_grp'),
    path('emp',views.emp,name='emp'),
    path('atndnce_list',views.atndnce_list,name='atndnce_list'),
    path('pay',views.pay,name='pay'),
    path('profit',views.profit,name='profit'),

    # path('save_currency_data',views.save_currency_data,name="save_currency_data"),
    path('load_create_currency',views.load_create_currency,name='load_create_currency'),
    path('create_currency',views.create_currency,name='create_currency'),
    path('update_currency/<int:pk>',views.update_currency,name='update_currency'),





    
]