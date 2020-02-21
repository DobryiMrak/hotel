from django import forms
from .models import Resedent, Nomer, Document


class ResedentForm(forms.ModelForm):
	class Meta(object):
		model = Resedent
		fields = (
			"first_name",
			"second_name",
			"father_name",
			"burn_date",
			"gender",
			"phone_number",
			"pasport_seria",
			"pasport_number"
		)


class NomerForm(forms.ModelForm):
	class Meta(object):
		model = Nomer
		fields = (
			"number",
			"square",
			"count_of_rooms",
		)


class DocumentForm(forms.ModelForm):
	class Meta:
		fields = "__all__"
		model = Document
