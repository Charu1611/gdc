from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile,RegularUpdate,Withdraw, ContactUs, Event, Review, PastEvent
from django.forms.widgets import DateInput

class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)
    class Meta:
        model = User
        fields = ('username','email','first_name', 'last_name','password1','password2')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('plantype','profession','mobile','user_commission','fixed_rate','profilephoto','pancard')
class RegularUpdateForm(forms.ModelForm):
    class Meta:
        model = RegularUpdate
        fields = ('initial_value','final_value')
        labels = {
            'initial_value': 'Initial Value',
            'final_value': 'Final Value',
        }
class WithdrawForm(forms.ModelForm):
    class Meta:
        model = Withdraw
        fields = ('requested_by','amount','status','status_updated_by','status_updated_on','present_balance','plantype','user_commission','invested_balance')
        labels = {
            'requested_by': 'Requested by',
            'amount': 'Withdrawal Amount',
            'status': 'Status (Type A/R)',
            'status_updated_by': 'Status updated by',
            'present_balance': 'Present Balance',
            'plantype': 'Plantype',
            'user_commission': 'User Commission',
            'invested_balance': 'Invested Balance'
        }
        widgets = {
        'requested_by':forms.TextInput(attrs={'readonly':True}),
        'status_updated_by':forms.TextInput(attrs={'readonly':True}),
        'plantype':forms.TextInput(attrs={'readonly':True}),
        }
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name','email','mobile','address','message')
        labels = {
            'name': 'Name',
            'email': 'Email Address',
            'mobile': 'Mobile No.',
            'address': 'Address',
            'message': 'Message',
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title','description','date')
        labels = {
            'title': 'Title of Event',
            'description': 'Description',
            'date': 'Date of Events',
        }
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
        }
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name','review','display')
        labels = {
            'name': 'Your name',
            'review': 'Write Review',
            'display': 'Show on homepage',
        }
class PastEventForm(forms.ModelForm):
    class Meta:
        model = PastEvent
        fields = ('event_name','event_date','star_client_image','star_client_name','client1_image','client2_image','client3_image','client4_image','client5_image','client6_image','client7_image','client8_image','client9_image','client10_image','client1_name','client2_name','client3_name','client4_name','client5_name','client6_name','client7_name','client8_name','client9_name','client10_name')
        labels = {
            'event_name': 'Event Name',
            'event_date': 'Event Date',
            'star_client_image': 'Upload Star Client Image',
            'star_client_name': 'Star Client Name',

            'client1_image': 'Upload Client 1 Image',
            'client1_name': 'Client 1 Name',

            'client2_image': 'Upload Client 2 Image',
            'client2_name': 'Client 2 Name',

            'client3_image': 'Upload Client 3 Image',
            'client3_name': 'Client 3 Name',

            'client4_image': 'Upload Client 4 Image',
            'client4_name': 'Client 4 Name',

            'client5_image': 'Upload Client 5 Image',
            'client5_name': 'Client 5 Name',

            'client6_image': 'Upload Client 6 Image',
            'client6_name': 'Client 6 Name',

            'client7_image': 'Upload Client 7 Image',
            'client7_name': 'Client 7 Name',

            'client8_image': 'Upload Client 8 Image',
            'client8_name': 'Client 8 Name',

            'client9_image': 'Upload Client 9 Image',
            'client9_name': 'Client 9 Name',

            'client10_image': 'Upload Client 10 Image',
            'client10_name': 'Client 10 Name',
        }
        widgets = {
            'event_date': DateInput(attrs={'type': 'date'}),
        }