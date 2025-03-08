from rest_framework import views, status, permissions
from rest_framework.response import Response
from utils.response import ApiResponse
from apps.market.models import Market
from apps.market.serializers.user_serializers import MarketListSerializer
from apps.product.models import Product
from apps.product.serializers.owner_serializers import ProductDetailSerializer
# Create your views here.


class MarketDetailView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        market_id = request.GET.get('id')
        if not market_id:
            return Response(
                ApiResponse(
                    success=False,
                    code=400,
                    error="Market Id Not Provided"
                ),
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            market = Market.objects.get(id=market_id)
        except Market.DoesNotExist:
            return Response(
                ApiResponse(
                    success=False,
                    code=404,
                    error="Market Not Found"
                ),
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = MarketListSerializer(market)

        return Response(
            ApiResponse(
                success=True,
                code=200,
                data=serializer.data
            )
        )
        

class ProductDetailView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        product_id = request.GET.get('id')
        if not product_id:
            return Response(
                ApiResponse(
                    success=False,
                    code=400,
                    error="Product Id Not Provided"
                ),
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(
                ApiResponse(
                    success=False,
                    code=404,
                    error="Product Not Found"
                ),
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = ProductDetailSerializer(product)

        return Response(
            ApiResponse(
                success=True,
                code=200,
                data=serializer.data
            )
        )


class AdvertizeDetailView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        pass