from django.shortcuts import render 
def home_page(request): 

    if request.method == 'POST':
        time = request.POST.get('time')   
        customer_name=request.POST.get("customer_name")
        
        return render(request, 'haircut/home_page.html', {'time': time, ' ': customer_name})
        
    return render(request,'haircut/home_page.html')