from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from heritagesites.models import HeritageSite

class HeritageSiteForm(forms.ModelForm):
	justification = forms.CharField(required=False)
	date_inscribed = forms.IntegerField(required=False)
	longitude = forms.DecimalField(required=False)
	latitude = forms.DecimalField(required=False)
	area_hectares = forms.DecimalField(required=False)


	class Meta:
		model = HeritageSite
		fields = '__all__'


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'submit'))





