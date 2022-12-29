from django.shortcuts import render


# Create your views here.
def get_todo_list(request):
    return render(request, 'todo/todo_list.html')
    #  passsing the html file in the render (import) to django,
    # to display in the browser
