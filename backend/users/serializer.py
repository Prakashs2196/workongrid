from .models import *
from rest_framework.serializers import *

class UserSerialize(ModelSerializer):
    # name=CharField(max_length=32,default=None,null=True)
    # username=CharField(max_length=256,default=None,null=True)
    # email=EmailField(max_length=256,default=None,null=True)
    # website=CharField(max_length=256,default=None,null=True)

    class Meta:
        model=Users
        fields = '__all__'
        # fields=('pk','name','username','email','website')


