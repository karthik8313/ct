from django import forms
from django.contrib.auth import(
	authenticate,
	get_user_model,
	login,
	logout,
	)
user = get_user_model()

class userloginform(forms.Form):
	username=forms.CharField(max_length=30)
	password=forms.CharField(widget=forms.PasswordInput)

	def clean(self,*args,**kwargs):
		username= self.cleaned_data.get("username")
		password= self.cleaned_data.get("password")

		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("This User Does Not Exist")
			if not user.check_password(password):
				raise forms.ValidationError("Incorrect Password")
			if not user.is_active:
				raise forms.ValidationError("User is Inactive")
		return super(userloginform,self).clean(*args,**kwargs)

class newuserform(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = user
		fields=[
		'username',
		'password',
		'email',
		]