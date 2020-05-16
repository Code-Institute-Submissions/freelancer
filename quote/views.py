from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from quote.forms import  QuoteUploadForm
from quote.models import Upload, Quote, QuoteFiles
from basket.forms import AddToBasketForm
from django.core.files import File 
from datetime import datetime

def quote(request):
      return render(request, 'quote.html')


@login_required(login_url='/login/')
def quote_logged(request):
 
    upload_form = QuoteUploadForm
    context = { "price": "",
                "upload_form": upload_form, 
                "add_to_basket_form": AddToBasketForm }
    

    if request.method == "POST":
      time = datetime.now()
      

      if request.POST['form'] == "Upload":
        form = QuoteUploadForm(request.POST, request.FILES)
        if form.is_valid:
           files = request.FILES.getlist('document')
           category = request.POST.get('categories')
           title = request.POST.get('description')
           count = 0
           for eachFile in files: 
               raw = eachFile.read()
               count = count + len(raw.split())
            
      

         
           
      if count > 1000:
         price = count / 100
      else:
         price = 10
      if category != "General":
         price = price * 1.1
      price = round(price)
     
      context = { "price": price,
                "upload_form": upload_form, 
                "add_to_basket_form": AddToBasketForm }
                   
      #populate quote model intance fields:
     
      quote_instance = Quote(
                             category = category,
                             word_count = count,
                             uploaded_on = time,
                             price = price,
                             title= title)

      quote_instance.save()
      quote_ref = quote_instance.pk
      if request.POST['form'] == "Upload":
        for eachFile in files:
            file_name = str(quote_ref) + eachFile.name
        
            quote_file_instance = QuoteFiles(name = file_name,
                                             quote_ref = quote_ref)
            quote_file_instance.save()  

            eachFile.name =file_name          
            upload_file = Upload( document = eachFile )
            upload_file.save()


        current_user = request.user
        #################################################################
        file1 = Upload.objects.get(id=8)
        file1 = file1.document
        initial = {
                  'user': file1,
                # 'user': current_user.username,
                 'quote_ref': quote_ref  }
     
        context = {  "price": price, 
                     "upload_form" : upload_form,  
                     "add_to_basket_form": AddToBasketForm(initial=initial)
                   }
      

      return render(request, 'quote_logged.html', context)
    else:
      return render(request, 'quote_logged.html', context)


