from django.forms import ModelForm
from django import forms
from .models import User, StudentProfile, AcademicInfo, JobNotifications, Suggestions
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class StudentRegistrationForm(UserCreationForm):
    address = forms.CharField(widget=forms.Textarea)
    mobile = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password1','password2', 'first_name', 'last_name', 'email', 'address', 'mobile' )

    def save(self,commit = False):
        user = super(MyRegistrationForm, self).save(commit = False)
        user.address = self.cleaned_data['address']
        user.email = self.cleaned_data['email']
        user.mobile = self.cleaned_data['mobile']
        user.userRole = "student"
        user.set_password(self.cleaned_data["password1"])

        user_default = User.objects.create_user(self.cleaned_data['username'],
                                                self.cleaned_data['email'],
                                                self.cleaned_data['password1'])
        user_default.save()
        if commit:
             user.save()
        return user

class StudentProfileForm(ModelForm):
    class Meta:
        model = StudentProfile
        exclude = ['user']

class AcademicInfoForm(ModelForm):
    class Meta:
        model = AcademicInfo
        exclude = ['student']

class JobNotificationsForm(ModelForm):
    class Meta:
        model = JobNotifications
        fields = '__all__'
