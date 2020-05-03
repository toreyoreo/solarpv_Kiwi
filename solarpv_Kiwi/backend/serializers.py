from rest_framework import serializers
from .models import Product,Certificate,Service

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('modelnumber', 'productname', 'celltechnology', 'cellmanufacturer', 'numberofcells','numberofcellsinseries', 'numberofseriesinstrings', 'numberofdiodes', 'productlength', 'productwidth', 'productweight', 'superstatetype', 'superstatemanufacturer','substratetype', 'substratemanufacturer', 'frametype', 'frameadhesive', 'encapsulatetype', 'encapsulatemanufacturer', 'junctionboxtype', 'junctionboxmanufacturer')

class CertificateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('userid', 'reportnumber', 'issuedate', 'standardid', 'locationid', 'modelnumber')

class ServiceSerializers(serializers.ModelSerializer):
    class Meta:    
        model = Service
        fields = ('servicename', 'description', 'isfirequired', 'fifrequency', 'standardid')