#Created a form for CSV upload and timeframe selection
from django import forms

class UploadForm(forms.Form):
    csv_file = forms.FileField()
    timeframe = forms.IntegerField()
