from django.forms import ModelForm
from contact.models import ContactModel

class contactForm(ModelForm):
    class Meta:
        model: ContactModel
        fields='__all__'