from django.shortcuts import redirect
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Product 
from django.forms import ModelForm
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

class searchForm(forms.Form):
    search_product = forms.CharField()
   

def home(request):
	
        return render_to_response('verify/base.html',{})
        
@csrf_exempt        
def search(request,term):
        search_product=request.POST.get('search_product')
        print search_product
        posts =Product.objects.filter(name__icontains= search_product)
        
    
    
    	argument = 'verify/search.html/'
    	
        t = loader.get_template(argument)
        c = Context({'posts':posts,'term':term, 'search_product':search_product})

        return HttpResponse(t.render(c))
        

        

        
  

