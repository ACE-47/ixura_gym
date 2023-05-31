from django.contrib import admin
from .models import Contact,Enrollment,Trainer,MemberShipPlan,Gallery,Attendance

# Register your models here.
admin.site.register(Contact)
admin.site.register(Enrollment)
admin.site.register(MemberShipPlan)
admin.site.register(Trainer)
admin.site.register(Gallery)
admin.site.register(Attendance)
