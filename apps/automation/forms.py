from django import forms
from .models import Automation


class AutomationForm(forms.ModelForm):
    class Meta:
        model = Automation
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(AutomationForm, self).__init__(*args, **kwargs)
        self.fields['gitrepo'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Repo...'})
        self.fields['gitbranch'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Branch...'})
        self.fields['env'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Env...'})
        self.fields['tags'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Tags...'})
        self.fields['processes'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Processes...'})
        self.fields['googlechaturl'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'GoogleChatUrl...'})
        self.fields['reportpath'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Report...'})
