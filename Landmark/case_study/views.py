from django.shortcuts import render
from django.db.models import Q
from django.db.models import Sum
from django.views import View

from .models import CaseStudy
# Create your views here.
from django.contrib import messages


class Case_study(View):
    context = {}

    def get(self, request):
        warehouse_stock = CaseStudy.objects.aggregate(total_warehouse_stock=Sum('warehouse_stock'),
                                                      total_store_stock=Sum('store_stock'),
                                                      total_transit_stock=Sum('transit_stock'))
        Overall_Stock = warehouse_stock['total_warehouse_stock'] + warehouse_stock['total_store_stock'] + \
                        warehouse_stock['total_transit_stock']
        territory_list = CaseStudy.objects.order_by('territory').values_list('territory', flat=True).distinct()
        self.context['overall_stock'] = Overall_Stock
        self.context['territory_list'] = territory_list

        return render(request, 'Case_Study.html', self.context)

    def post(self, request):
        if request.method == 'POST':
            selected_territory = request.POST.get('tritry')
            selected_territory_id = request.POST.get('territary_id')
            if selected_territory == None and selected_territory_id==None:
                territory_wise_overall_stock = '--'
                warehouse_stock = '--'
                store_stock = '--'
                price_value = '--'
                messages.warning(request, "Please select Territory")

            else:
                territory_wise_total_stock = CaseStudy.objects.filter(Q(territory=selected_territory) & Q(item_id=selected_territory_id)).aggregate(
                    total_warehouse_stock=Sum('warehouse_stock'), total_store_stock=Sum('store_stock'),
                    total_transit_stock=Sum('transit_stock'))
                price = CaseStudy.objects.filter(Q(territory=selected_territory) & Q(item_id=selected_territory_id)).values_list('price', flat=True)
                territory_wise_overall_stock = territory_wise_total_stock['total_warehouse_stock'] + \
                                               territory_wise_total_stock['total_store_stock'] + \
                                               territory_wise_total_stock['total_transit_stock']
                warehouse_stock = territory_wise_total_stock['total_warehouse_stock']
                store_stock = territory_wise_total_stock['total_store_stock']
                price_value = territory_wise_overall_stock * price[0]

        self.context['territory_wise_overall_stock'] = territory_wise_overall_stock
        self.context['warehouse_stock'] = warehouse_stock
        self.context['store_stock'] = store_stock
        self.context['price_value'] = price_value

        return render(request, 'Case_Study.html', self.context)


def load_item_id(request):
    territory_name = request.GET.get('territory_name')
    item_id = CaseStudy.objects.filter(territory = territory_name)
    return render(request, 'case_id_dropdown.html', {'item_id': item_id})