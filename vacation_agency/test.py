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

all_users = User.objects.all()

all_users.filter(Q(name="Vlad") | Q(name="David"))
# __ в скл то же самое шо точка

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

all_acoms = Accomodation.objects.all()
all_acoms.filter(Q(square__gte=100) , Q(price__lte=150))


