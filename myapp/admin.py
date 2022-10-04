from django.contrib import admin
from .models import UserProfile,RegularUpdate,Transaction,Withdraw,CompanyCapital, ContactUs


admin.site.register(UserProfile)
admin.site.register(Transaction)
admin.site.register(RegularUpdate)
admin.site.register(Withdraw)
admin.site.register(CompanyCapital)
admin.site.register(ContactUs)