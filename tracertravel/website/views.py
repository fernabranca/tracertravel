from django.shortcuts import render
from .forms import CustomerForm
from django.shortcuts import render_to_response

#registro de usuarios
def create_customer(request):

	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = CustomerForm()
	
	return render_to_response('register.html', 
		{'form': form},
		context_instance=RequestContext(request))