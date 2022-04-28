from rest_framework import viewsets

from category.models import Category
from category.serializer import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """This class provides all the CRUD functionalities for Category"""

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
