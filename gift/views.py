from django.shortcuts import render
from django.views import View

from gift.models import TypesGift,Gifts


class HomePageView(View):
    def get(self,request):
        return render(request,'index.html')
    
class AboutView(View):
    def get(self,request):
        return render(request, 'about.html')
    
class GiftsView(View):
    def get(self,request):
        gifts=TypesGift.objects.all()
        return render(request,'all_gift.html',{'gifts':gifts})
    
class Giftsdetail(View):
    def get(self,request,id):
         gifts=Gifts.objects.filter(turi=id)
         return render(request,'detail.html',{'gifts':gifts})
    
class ContactView(View):
    def get(self,request):
        return render(request,'contact.html')