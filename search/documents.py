from django_elasticsearch_dsl import DocType, Index
from campusbuy.models import  Advert

adverts = Index('adverts')


@adverts.doc_type
class PostDocument(DocType):
    class Meta:
        model = Advert

        fields = [
            'Seller_Name',
            'Phone_Number',
            'Location',
            'Item',
            'id',
            'Description',
            'Asking_Price',
            'published_date',
            'image',
        ]