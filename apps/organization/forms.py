from django import forms
from operation.models import UserAsk
import re

class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

        def clean_mobile(self):
            mobile = self.cleaned_data['mobile']
            REGEX_MOBILE = "^1[358]\d"