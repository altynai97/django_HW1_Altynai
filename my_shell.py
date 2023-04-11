# python manage.py shell
# from shop.models import *
item = Item(name = "кружка", price= "500")
item.save()
items = Item.objects.all()
items
purchase = Purchase(item_id=1, name = "Ted")
purchase.save()
purchase
purchase_2= Purchase(item=item, name = "Will")
purchase_2.save()
purchase_2
item = Item(name="тарелка")
item.save()
item
purchase = Purchase(item=item, name = "Ryan")
purchase.save()
purchase
purchase_2=Purchase.objects.create(item=item, name="Elle")
item = Item(name = "ложка", price= "1500")
item.save()
item = Item(name = "вилка", price= "5200")
item = Item(name = "бокал", price= "5300")
item.save()
item = Item(name = "нож", price= "300")
item.save()
item = Item(name = "форма", price= "5600")
item.save()
item = Item(name = "поварешка", price= "5600")
item.save()
item = Item(name = "сковородка", price= "5900")
item.save()
item = Item(name = "кастрюля", price= "5670")
item.save()
purchase_3=Purchase.objects.create(item=item, name="Jenny")
purchase_4=Purchase.objects.create(item=item, name="Ed")
purchase_5=Purchase.objects.create(item=item, name="Bella")
purchase_6=Purchase.objects.create(item=item, name="ella")
purchase_7=Purchase.objects.create(item=item, name="Inna")
purchase_8=Purchase.objects.create(item=item, name="Rima")
purchase_9=Purchase.objects.create(item=item, name="Rina")
purchase_10=Purchase.objects.create(item=item, name="Lila")

