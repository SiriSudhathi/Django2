from django.contrib import admin
from .models import User, StudentProfile, AcademicInfo, Suggestions, JobNotifications
# Register your models here.

from django.contrib.auth.admin import UserAdmin


class MyUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('mobile', 'address', 'userRole')}),
    )

class StudentProfileAdmin(admin.ModelAdmin):
    def render_change_form(self, request, context, *args, **kwargs):
         context['adminform'].form.fields['user'].queryset = User.objects.filter(userRole="student")
         return super(StudentProfileAdmin, self).render_change_form(request, context, args, kwargs)


class AcademicInfoAdmin(admin.ModelAdmin):
    def render_change_form(self, request, context, *args, **kwargs):
         context['adminform'].form.fields['student'].queryset = StudentProfile.objects.all()
         return super(AcademicInfoAdmin, self).render_change_form(request, context, args, kwargs)


admin.site.register(User, MyUserAdmin)
admin.site.register(StudentProfile, StudentProfileAdmin)
admin.site.register(AcademicInfo, AcademicInfoAdmin)
admin.site.register(Suggestions)
admin.site.register(JobNotifications)
