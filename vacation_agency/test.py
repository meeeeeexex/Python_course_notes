'''
I tried to write script which tests my app, but it even didn't set up
'''

from agency.models import User, Accomodation, Excursion

v = User(name="Vlad", surname="Dolgopolov")
v.save()
v = User(name="David", surname="Dolgopolov")
v.save()
v = User(name="Alex", surname="Corwell")
v.save()
v = User(name="Zhen", surname="Abdellasem")
v.save()
v = User(name="Zack", surname="Phoden")
v.save()
v = User(name="Kylie", surname="Corwell")
v.save()
v = User(name="Max", surname="Schulenberg")
v.save()
v = User(name="Sam", surname="Rotenbach")
v.save()
v = User(name="Leo", surname="Straightgoing")
v.save()
v = User(name="Nick", surname="McKinsey")
v.save()
v = User(name="George", surname="Pavard")
v.save()
v = User(name="Maron", surname="Mason")
v.save()

acom = Accomodation(name='Hilton', square=150, price=200)
acom.save()
acom = Accomodation(name='Radison', square=100, price=100)
acom.save()
acom = Accomodation(name='Book', square=70, price=90)
acom.save()
acom = Accomodation(name='Hostel', square=20, price=20)
acom.save()
acom = Accomodation(name='Zirka', square=10, price=10)
acom.save()

exc = Excursion(city='London', price=10)
exc.save()

exc = Excursion(city='Berlin', duration=100, price=120)
exc.save()

exc = Excursion(city='Paris', duration=120, price=20)
exc.save()

exc = Excursion(city='Lisbon', duration=140, price=50)
exc.save()

exc = Excursion(city='Lisbon', duration=100, price=30)
exc.save()

exc = Excursion(city='Paris', duration=99, price=25)
exc.save()
exc = Excursion(city='London', duration=85, price=67)
exc.save()
exc = Excursion(city='Lisbon', duration=90, price=100)
exc.save()

exc = Excursion(city='Lisbon', duration=240, price=250)
exc.save()
exc = Excursion(city='Paris', duration=150, price=90)
exc.save()
exc = Excursion(city='London', price=10)
exc.save()

all_users = User.objects.all()

all_users.filter(Q(name="Vlad") | Q(name="David"))
all_acoms = Accomodation.objects.all()

all_acoms.filter(Q(square__gte=100), Q(price__lte=150))

exc_all = Excursion.objects.all()

exc_all.filter(Q(city='Paris'), (Q(duration__lte=100) | Q(price__lte=100)))
exc_all.order_by('price')[0]

acc_for_price_enlarge = all_acoms.get(name='Zirka')
min_price_acc_price = all_acoms.order_by('price')[0]
acc_for_price_enlarge.price = acc_for_price_enlarge.price + min_price_acc_price.price