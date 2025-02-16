from rest_framework import views
from rest_framework.response import Response

from utils.response import ApiResponse

from apps.category.models import Group, Category, SubCategory
from apps.category.serializers.user_serializers import GroupListSerializer, CategoryListSerializer, SubCategoryListSerializer


class GroupListAPIView(views.APIView):
    def get(self, request, format=None):
        group_list = Group.objects.all()

        serializer = GroupListSerializer(
            group_list,
            many=True,
            context={"request": request},
        )

        success_response = ApiResponse(
            success=True,
            code=200,
            data=serializer.data,
            message='Data retrieved successfully'
        )

        return Response(success_response)


class CategoryListAPIView(views.APIView):
    def get(self, request, pk, format=None):
        group_obj = Group.objects.get(id=pk)
        category_list = Category.objects.filter(group=group_obj)

        serializer = CategoryListSerializer(
            category_list,
            many=True,
            context={"request": request},
        )

        success_response = ApiResponse(
            success=True,
            code=200,
            data=serializer.data,
            message='Data retrieved successfully'
        )

        return Response(success_response)


class SubCategoryListAPIView(views.APIView):
    def get(self, request, pk, format=None):
        category_obj = Category.objects.get(id=pk)
        sub_category_list = SubCategory.objects.filter(category=category_obj)

        serializer = SubCategoryListSerializer(
            sub_category_list,
            many=True,
            context={"request": request},
        )

        success_response = ApiResponse(
            success=True,
            code=200,
            data=serializer.data,
            message='Data retrieved successfully'
        )

        return Response(success_response)
