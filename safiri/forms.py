from django import forms

from safiri.models import LetCar, SelfDrive, TaxCab

class SelfDriveForm(forms.ModelForm):
    class Meta:
        model = SelfDrive
        fields = '__all__'

class LetCarForm(forms.ModelForm):
    class Meta:
        model = LetCar
        fields = '__all__'

class TaxCabForm(forms.ModelForm):
    class Meta:
        model = TaxCab
        fields = "__all__"