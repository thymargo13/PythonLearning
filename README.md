# Python Learning
### Python -01 (21/10/2018)
introduction of Python
### Python -02 (22/10/2018)
simple variable usage and type of data 
### Python -03 (23/10/2018)
list, tuple, set, dictionary
### Python -04 (24/10/2018)
Condition (if, elif, else); Loop (for, while) --> break, continue, pass; function defind (def)
### Python -05 (25/10/2018)
Pandas - Series & DataFrame 
### Python -06 (26/10/2018)
Pandas - Merge, Join & Concat
### Python -07 (27/10/2018)
Matplotlib -line chart, bar chart, scatter, histogram, boxplot
### Python -08 (28/10/2018)
Matplotlib 
### Python -09 (29/10/2018)
apply(), map()
### Python -10 (30/10/2018)
candle chart

DjangoAPI with MongoDB
----- 

required package:

	- djangorestframework
  
	- djongo
  
	- mongoengine
  
	- pymongo
  
```bash
python -m even {environment Name}
django-admin startproject {new Project}
python manage.py startapp {app name}
```
setting.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME' : '{database name}',
        'PORT': 27017,
		}
	}	
```
```bash
python manage.py migrate
python manage.py createsuperuser
```
```python
serializers.py
	from rest_framework import serializers
	class Serializer(serializers.HyperlinkedModelSerializer):
		class Meta:
			model = {model name}
			fields = ['cols']
```
models.py : each table
```python
	from djongo import models
	# Create your models here.
	class Table(models.Model):
		fieldName = models.CharField(max_length = 8)
		#comp_id  = models.IntegerField()
```
views.py : 
```python
	class ViewSet(viewsets.ModelViewSet):
		queryset = User.objects.all()
		serializer_class = UserSerializer
```
urls.py
```python	
  from django.urls import path,include
  from .views import  CompanyView, UserView

	urlpatterns = [
		#path('{url display}', {View}.as_view({'get': 'list'}), name='company'),
		path('company', CompanyView.as_view({'get': 'list'}), name='company'),
		path('user', UserView.as_view({'get': 'list'}), name='user'),
	]
	
		path('api/', include('api.urls')) # All path within app.urls.py
 ```
