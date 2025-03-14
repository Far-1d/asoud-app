from rest_framework import views, status
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _

from utils.response import ApiResponse

from apps.product.serializers.owner_serializers import (
    ProductCreateSerializer,
    ProductDiscountCreateSerializer,
    ProductDetailSerializer,
    ProductThemeListSerializer,
    ProductThemeCreateSerializer,
    ProductThemeListSerializer,
)
from apps.product.models import Product, ProductTheme
from apps.market.models import Market
from apps.advertise.core  import AdvertisementCore

# affiliate products
from apps.affiliate.models import (
    AffiliateProduct, 
    AffiliateProductTheme
)
from apps.affiliate.serializers.user import AffiliateProductThemeListSerializer


class ProductCreateAPIView(views.APIView):
    def post(self, request):
        serializer = ProductCreateSerializer(
            data=request.data,
            context={'request': request},
        )

        if serializer.is_valid(raise_exception=True):
            product = serializer.save()

            product_id = product.id

            if product.is_requirement:
                ad_data = AdvertisementCore.create_advertisement_for_product(product)

            success_response = ApiResponse(
                success=True,
                code=200,
                data={
                    'product': product_id,
                    **serializer.data,
                },
                message='Product created successfully.',
            )

            return Response(success_response, status=status.HTTP_201_CREATED)


class ProductDiscountCreateAPIView(views.APIView):
    def post(self, request, pk):
        product = Product.objects.get(id=pk)

        serializer = ProductDiscountCreateSerializer(
            data=request.data,
            context={'request': request},
        )

        if serializer.is_valid():
            serializer.save(
                product=product,
            )

            success_response = ApiResponse(
                success=True,
                code=200,
                data={
                    **serializer.data,
                },
                message='ProductDiscount created successfully.',
            )

            return Response(success_response, status=status.HTTP_201_CREATED)


class ProductListAPIView(views.APIView):
    def get(self, request, pk):
        product_market_theme_list = ProductTheme.objects.filter(
            market_id=pk
        ).prefetch_related('products')

        serializer = ProductThemeListSerializer(
            product_market_theme_list,
            many=True,
            context={"request": request},
        )

        affiliate_product_theme_list = AffiliateProductTheme.objects.filter(
            market=pk
        ).prefetch_related('affiliate_products')
        
        aff_serializer = AffiliateProductThemeListSerializer(
            affiliate_product_theme_list,
            many=True,
            context={"request": request},
        )

        success_response = ApiResponse(
            success=True,
            code=200,
            data=serializer.data + aff_serializer.data,
            message='Data retrieved successfully'
        )

        return Response(success_response)


class ProductDetailAPIView(views.APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
        except:
            return Response(
                ApiResponse(
                    success=False,
                    code=404,
                    error="Product Not Found"
                )
            )
        
        serializer = ProductDetailSerializer(
            product,
            context={"request": request},
        )

        success_response = ApiResponse(
            success=True,
            code=200,
            data=serializer.data,
            message='Data retrieved successfully',
        )

        return Response(success_response)


class ProductThemeCreateAPIView(views.APIView):
    def post(self, request, pk):
        try:
            market = Market.objects.get(id=pk)
        except:
            return Response(
                ApiResponse(
                    success=False,
                    code=404,
                    error="Market Not Found"
                )
            )
        
        serializer = ProductThemeCreateSerializer(
            data=request.data,
            context={'request': request},
        )

        if serializer.is_valid(raise_exception=True):
            serializer.save(
                market=market,
            )

            success_response = ApiResponse(
                success=True,
                code=200,
                data={
                    **serializer.data,
                },
                message='Product theme created successfully.',
            )

            return Response(success_response, status=status.HTTP_201_CREATED)


class ProductThemeListAPIView(views.APIView):
    def get(self, request, pk):
        try:
            market = Market.objects.get(id=pk)
        except:
            return Response(
                ApiResponse(
                    success=False,
                    code=404,
                    error="Market Not Found"
                )
            )
    
        product_theme_list = ProductTheme.objects.filter(market=market)

        serializer = ProductThemeListSerializer(
            product_theme_list,
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


class ProductThemeUpdateAPIView(views.APIView):
    def put(self, request, pk):
        try:
            product_theme = ProductTheme.objects.get(id=pk)
        except:
            return Response(
                ApiResponse(
                    success=False,
                    code=404,
                    error="Product Theme Not Found"
                )
            )
        products = request.data.get("products", [])

        if not isinstance(products, list):
            response = ApiResponse(
                success=False,
                code=400,
                error={
                    'code': 'bad_request',
                    'detail': 'Invalid format. "products" should be a list.',
                }
            )
            return Response(response)

        for product_id in products:
            try:
                product = Product.objects.get(id=product_id)
                product.theme = product_theme
                product.save()
            except:
                pass
            
        success_response = ApiResponse(
            success=True,
            code=200,
            data={},
            message='Product theme updated successfully.',
        )
        return Response(success_response, status=status.HTTP_200_OK)
