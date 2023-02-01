from django.contrib import admin

from safiri.models import LetCar, PostCar, SelfDrive, TaxCab

# Register your models here.
admin.site.register(SelfDrive)
admin.site.register(PostCar)
admin.site.register(LetCar)
admin.site.register(TaxCab)