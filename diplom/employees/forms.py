from django import forms

from .models import Emolyees


class CreateEmployeeForm(forms.ModelForm):

    class Meta:
        model = Emolyees
        fields = ['last_name',
                  'first_name',
                  'patronymic',
                  'login',
                  'password',
                  'legal_adress',
                  'physical_adress',
                  'position',
                  'subdivision',
                  'role',
                  'inn',
                  'snils',
                  'phone',
                  'email',
                  'date_of_birth',
                  'passports_series',
                  'passports_number',
                  'date_of_employment',
                  'education',
                  'salary',
                  ]