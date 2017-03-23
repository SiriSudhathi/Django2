from django.forms import ModelForm
from polls.models import PersonInfo
from polls.models import AcedamicInfo
from polls.models import AdditionalInfo

class PersonInfoForm(ModelForm):
    class Meta:
        model = PersonInfo
        fields = '__all__'

class AcedemicInfoForm(ModelForm):
    class Meta:
        model = AcedamicInfo
        fields = ('yearOfJoining','aggregate','upperSecondaryInstitution',
            'upperSecondaryBoard','upperSecondaryPercentage','SecondaryPercentage',
                'SecondaryInstitution','SecondaryBoard')

class AdditionalInfoForm(ModelForm):
    class Meta:
        model = AdditionalInfo
        fields = ('coAcademicActivities','details','coCurriculars','hobbies')
