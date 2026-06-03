from django import forms
from django.core import validators
# widgets == field to html input

class contactForm(forms.Form):
    name = forms.CharField(label ="USER NAME:",initial='Hridoy kumar bala',help_text='total lenth must be 15 charater',required=False, widget = forms.Textarea(attrs={'id':'text_area'}))
    # email =forms.EmailField(label ="USER EMAIL")
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance =forms.DecimalField()
    # check = forms.BooleanField()
    # Image = forms.ImageField(label= "Image")
    birthday =forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    # appointment = forms.DateTimeField()
    CHOICES=[{'S',"Small"},{'M',"Medium"},{'L',"Large"}]
    size =forms.ChoiceField(choices=CHOICES, widget =forms.RadioSelect,required=False)
    MEAL =[{'P',"Pepperonl"},{'M',"Mashroom"},{'R',"Rice"}]
    kpizza =forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)
    # files =forms.FileField()
    # if you can't remember any tag you can use forms.CharField tag

# class studentData(forms.Form):
#     name= forms.CharField(label ="Student Name:",widget=forms.TextInput)
#     email=forms.CharField(label="Enter your Email", widget=forms.EmailInput)
#     # def clean_name(self):
#     #     valname= self.cleaned_data['name']
#     #     if len(valname) <10:
#     #         raise forms.ValidationError("Enter a name With at least 10 character.")
#     #     return valname
#     # def clean_email(self):
#     #     valemail =self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("your email is not valid")
#     #     return valemail
#     def clean(self):
#         clean_data =super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname)>10:
#             raise forms.ValidationError('Enter a name With at least 10 character.')
#         if '.com' not in valemail:
#             raise forms.ValidationError("your email is not valid")
def len_check(value):
    if len(value)<10:
        raise forms.ValidationError("enter a value at least 10 chars")

class studentData(forms.Form):
    name= forms.CharField(label ="Student Name:",widget=forms.TextInput, validators=[validators.MinLengthValidator(10,message='Enter a name With at least 10 character.')])
    text =forms.CharField(widget=forms.TextInput,validators=[len_check])
    email=forms.CharField(label="Enter your Email", widget=forms.EmailInput, validators=[validators.EmailValidator(message='your email is not valid')])

    age =forms.IntegerField(validators=[validators.MaxValueValidator(100, message='not exits'),validators.MinValueValidator(10, message="you are kids") ])
    files =forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'], message="message index must be pdf")])

class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        clean_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        val_name =self.cleaned_data['name']
        if val_conpass != val_pass:
            raise forms.ValidationError("password don't match")
        if len(val_name)< 10:
            raise forms.ValidationError("name must be at least 10 chars")


