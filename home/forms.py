from django import forms
from django.core.exceptions import ValidationError
from PIL import Image

class PhotoUploadForm(forms.Form):
    photo = forms.ImageField()

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if photo:
            img = Image.open(photo)
            width, height = img.size
            # Example dimension check: width and height must be at least 300px
            if width < 300 or height < 300:
                raise ValidationError("Image dimensions are too small. Minimum size is 300x300 pixels.")
        return photo
