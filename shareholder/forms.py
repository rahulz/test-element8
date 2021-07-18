from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm, DateField, TextInput, HiddenInput
from phonenumber_field.formfields import PhoneNumberField

from shareholder.models import ShareHolder, Share


class ShareHolderForm(ModelForm):
    mobile = PhoneNumberField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = ShareHolder
        fields = '__all__'


class ShareForm(ModelForm):
    start_date = DateField(
        widget=TextInput(
            attrs={'type': 'date'}
        )
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['shareholder'] = ShareHolder.objects.get(id=self.request.path.split('/')[-2])
        return cleaned_data

    class Meta:
        model = Share
        fields = '__all__'
        widgets = {
            'shareholder': HiddenInput(),
        }
