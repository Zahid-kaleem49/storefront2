# from django.shortcuts import render
# import datetime
from django.shortcuts import render
# from django.http import HttpResponse
# from django.core.exceptions import ObjectDoesNotExist
# from store.models import Product, Customer, Collection, Order, OrderItem
# from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
# from django.db.models.aggregates import Count, Sum, Min, Max, Avg
# from django.db import transaction, connection

#
#
def say_hello(request):
#     # query_Set = Product.objects.all()
#     # query_Set = Product.objects.get(pk=1).first() OR exists()
#     # query_set = Product.objects.filter(collection__id__gte=1)
#     # query_set = Product.objects.filter(collection__title='beauty')
#     # query_set = Product.objects.filter(Q(inventory__lt=20) & Q(unit_price__lt=10))
#     # query_set = Product.objects.filter(Q(inventory__lt=20) | Q(unit_price__lt=10))
#     # query_set = Product.objects.filter(Q(inventory__lt=20) & ~Q(unit_price__lt=10))
#     # query_set = Product.objects.filter(unit_price=F('inventory'))
#     # query_set = Product.objects.filter(unit_price__gt=10).order_by('unit_price', '-title')
#     # query_set = Product.objects.filter(unit_price__gt=10).earliest('title')
#     # query_set = Product.objects.all().latest('title')
#
#     # reverse will inverse the filter
#     # query_set = Product.objects.filter(unit_price__gt=10).order_by('unit_price', '-title').reverse()
#
#     # slicing to get data with limit and offset
#     query_set = Product.objects.all().order_by('unit_price', '-title')[5:10]
#
#
#
#
#
#
#     # SELECTINg fields to query and writing two queries
#     # query_set = OrderItem.objects.values('product_id').distinct()
#     # product_query_set = Product.objects.filter(id__in=query_set).order_by('title')
#
#     # only fields with come from db
#     # query_set = Product.objects.only('id', 'title')
#
#     # defer exclude columns loading from db
#     # query_set = Product.objects.defer('description')
#
#     # AGGREGATE
#     # result = Order.objects.aggregate(count=Count('id'))
#
#     # result = OrderItem.objects.filter(product__id=1).aggregate(total_quantity=Sum('quantity'))
#
#     # result = Order.objects.filter(customer__id=1).aggregate(total_orders=Count('id'))
#
#     # result = Product.objects.filter(collection_id=3).aggregate(
#     #     min_price=Min('unit_price'),
#     #     max_price=Max('unit_price'),
#     #     average_price=Avg('unit_price')
#     # )
#     # Annotate means adding new field to result
#     # result = Customer.objects.annotate(
#     # name = F(first_name)
#     #     )
#     # result = result.values('full_name', 'id')
#
#     # expression wrapper
#     # expression_wrapper = ExpressionWrapper(F('unit_price') * 0.9, output_field=DecimalField())
#     # result = OrderItem.objects.annotate(
#     #     discounted_price=expression_wrapper
#     #
#     # ).values('discounted_price', 'id', 'unit_price')
#
#     # Saving object two methods
#     # 1
#     # collection_object = Collection()
#     # collection_object.title = 'pizza'
#     # collection_object.featured_product_id = 1
#     # collection_object.save()
#
#     # 2
#     # object_collection = Collection.objects.create(title='pizza', featured_product_id=1)
#
#     # update 1 method
#     # obj_update = Collection.objects.filter(pk=11).update(featured_product_id=None)
#
#     # update2 method which has sometimes problem
#     # obj_update = Collection.objects.get(pk=11)
#     # obj_update.featured_product_id = None
#     # obj_update.save()
#
#     # delete
#     # obj = Collection.objects.filter(title='pizza').delete()
#
#     # ===================================================
#     # atomic transaction
#     # with transaction.atomic():
#     #     order = Order.objects.create(
#     #         customer_id=1
#     #     )
#     #     order_item = OrderItem.objects.create(
#     #         order=order,
#     #         product_id=5,
#     #         quantity=5,
#     #         unit_price=15,
#     #     )
#     # =========================================
#     # method to write raw sql
#     # raw_sql = Product.objects.raw('Select * From store_product')
#     # list(raw_sql)
#
#     # with connection.cursor() as cursor:
#     #     cursor.execute('Select * From store_product')
#     # result = Product.objects.select_related('collection').all()
#     # resukt = result.collection_id
#     # print(resukt)
#     p = list(query_set)
#     # collection = result[0].collection
#
#
    return render(request, 'hello.html', {'name': 'Mosh', })


# -------------------------------------------------
