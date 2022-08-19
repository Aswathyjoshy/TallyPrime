from django.urls import path,include
from.import views


urlpatterns = [

    path('',views.base,name='base'),
    path('index',views.index,name='index'),
    path('group',views.group,name='group'),
    path('branch',views.branch,name='branch'),
    path('ledger',views.ledger,name='ledger'),
    path('primary/<int:pk>',views.primary,name='primary'),
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
    path('load_create_vouchertyp',views.load_create_vouchertyp,name='load_create_vouchertyp'),
    path('create_voucher',views.create_voucher,name="create_voucher"),
    path('update_voucher/<int:pk>',views.update_voucher,name="update_voucher"),
    path('save_voucher/<int:pk>',views.save_voucher,name="save_voucher"),
    # path('load_create_groups',views.load_create_groups,name="load_create_groups"),
    # path('create_group',views.create_group,name="create_group"),
    # path('update_grp/<int:pk>',views.update_grp,name="update_grp"),
    path('update_cost/<int:pk>',views.update_cost,name="update_cost"),
    path('update_centr/<int:pk>',views.update_centr,name='update_centr'),
    path('centr/<int:pk>',views.centr,name='centr'),
    path('grp_alter/<int:pk>',views.grp_alter,name="grp_alter"),
    path('grp/<int:pk>',views.grp,name='grp'),
    path('load_ledger',views.load_ledger,name='load_ledger'),
    path('save_ledger',views.save_ledger,name='save_ledger'),
    






    
]