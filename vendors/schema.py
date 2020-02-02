import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import django_filters
import maintdx.vendors.models as vendors

class VendorTypeNode(DjangoObjectType):
    class Meta:
        model = vendors.VendorType
        filter_fields = {
            'vendor_type': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (graphene.relay.Node, )

class VendorNode(DjangoObjectType):
    class Meta:
        model = vendors.Vendor
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'vendor_type__id': ['exact'],
            'vendor_type__vendor_type': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (graphene.relay.Node, )

class VendorContactNode(DjangoObjectType):
    class Meta:
        model = vendors.VendorContact
        filter_fields = {
            'first_name': ['exact', 'icontains', 'istartswith'],
            'last_name': ['exact', 'icontains', 'istartswith'],
            'title': ['exact', 'icontains', 'istartswith'],
            'email': ['exact', 'icontains', 'istartswith'],
            'vendor__id': ['exact'],
            'vendor__name': ['exact', 'istartswith', 'icontains']
        }
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    all_vendor_types = DjangoFilterConnectionField(VendorTypeNode)
    all_vendors = DjangoFilterConnectionField(VendorNode)
    all_vendor_contacts = DjangoFilterConnectionField(VendorContactNode)

    vendor_type = graphene.Node.Field(VendorTypeNode)
    vendor = graphene.Node.Field(VendorNode)
    vendor_contact = graphene.Node.Field(VendorContactNode)
