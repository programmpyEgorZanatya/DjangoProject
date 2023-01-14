from django.shortcuts import render, HttpResponse, Http404
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist

def home(request):
    # text = f""" <h1>"Изучаем django"</h1> <strong>Автор</strong>: <i>Лазуренко Н.С.</i>"""
    # return HttpResponse(text)
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

# items = [
#    {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
#    {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
#    {"id": 3, "name": "Coca-cola 1 литр" ,"quantity":12},
#    {"id": 4, "name": "Картофель фри" ,"quantity":0},
#    {"id": 5, "name": "Кепка" ,"quantity":124},
# ]
def items_list(request):
    items = Item.objects.all()
    # items_result = "<ol>"
    # for item in items:
    #     items_result += "<li>" + f"<a href ='/item/{item['id']}'> " + item['name'] + "</a>" + "</li>"
    # items_result += "</ol>"
    # return HttpResponse(items_result)
    context = {
        "items": items
    }
    return render(request,"items.html",context)
def item_page(request,id):
    try:
        item = Item.objects.get(pk=id)
        return render(request,"item_page.html", {"item":item})
    except ObjectDoesNotExist:
        raise Http404(f"Товар с id = {id} не найден")