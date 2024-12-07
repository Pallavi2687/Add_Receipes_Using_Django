"""if we delete the migration file then what happend?
   django ko pata chal jaye ki migration file delete ho gyi h
   kyoki django apne data base me migration file rakhta h 
   and show error
CRUD = 'create' , 'read' , 'update' , 'delete',

"""





from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
  peoples=[
     {'name' : 'abhijeet ' , 'age' : 32},
     {'name' : 'Roshan ' , 'age' : 22},
     {'name' : 'Aman ' , 'age' : 25},
     {'name' : 'Vicky ' , 'age' : 23},
     {'name' : 'Sam ' , 'age' : 29},
     {'name' : 'abhi ' , 'age' : 20},
  ]
 
  vegetables = ['Pumpkin' 'Tomato' 'Patato']

  
  return render(request , "index.html" , context ={'peoples' : peoples , 'vegetables': vegetables})

def about(request):
      return render(request , "about.html")

def contact(request):
  return render(request , "contact.html" )

def success_page(request):
    return HttpResponse("<h1>hey, this is success page<h1>")