from django.shortcuts import render
# creating class based views
from django.views import generic
from .models import Item


# this class displays the list of menu items
class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_created")  # orders the object by the query
    template_name = "index.html"  # returns the template as requested

    def get_context_data(self):
        context = {"meals": "Pizza"}
        return context


# this class displays detail of each item
class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"
