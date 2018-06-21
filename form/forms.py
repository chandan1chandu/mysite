class CemeteryForm(forms.ModelForm):
     class Meta:
        model=Cemetery
        fields=('name','city','zipcode',)