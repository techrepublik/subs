import datetime
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser
from django.db.models import Prefetch, Q
from home.models import User, Region, Province, Municipality, Barangay, Plan, Modem, \
    Subscription, Billing, Payment, Issue, Ticket
from accounts.models import User, Subscriber, Employee
from .serializers import RegionSerializer, ProvinceSerializer, MunicipalitySerializer, BarangaySerializer, \
    PlanSerializer, ModemSerializer, SubscriptionSerializer, BillingSerializer, PaymentSerializer, IssueSerializer, TicketSerializer, \
    UserSerializer, SubscriberSerializer

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    filter_backends = [SearchFilter]
    search_fields = [
        'last_name',
        'first_name',
        'id_no',
    ]


class SubscriberChoicesView(APIView):
    def get(self, request, *args, **kwargs):
        choices = {
            "marital_status": [{'value': choice[0], 'display': choice[1]} for choice in Subscriber._meta.get_field('marital_status').choices],
            "gender": [{'value': choice[0], 'display': choice[1]} for choice in Subscriber._meta.get_field('gender').choices],
        }
        return Response(choices)


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    @swagger_auto_schema(
        method='get',
        operation_description="Retrieve a custom greeting message for regions.",
        responses={
            200: openapi.Response(
                description="A greeting message",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'message': openapi.Schema(type=openapi.TYPE_STRING, description='Greeting message'),
                    },
                )
            )
        }
    )
    @action(detail=False, methods=['get'], url_path='greeting', url_name='greeting')
    def custom_greeting(self, request):
        """
        Custom action to return a greeting message for the region endpoint.
        """
        return Response({"message": "Hello from the Region API!"}, status=status.HTTP_200_OK)


class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

    def get_queryset(self):
        region_id = self.request.query_params.get("region_id")
        if region_id:
            query = self.queryset.filter(region=region_id)

            return query
        else:
            return self.queryset 
    
class MunicipalityViewSet(viewsets.ModelViewSet):
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer

    def get_queryset(self):
        province_id = self.request.query_params.get("province_id")
        if province_id:
            queryset = self.queryset.filter(province=province_id)

            return queryset

        else:
            return self.queryset


class BarangayViewSet(viewsets.ModelViewSet):
    queryset = Barangay.objects.all()
    serializer_class = BarangaySerializer

    def get_queryset(self):
        municipality_id = self.request.query_params.get("municipality_id")
        if municipality_id:
            queryset = self.queryset.filter(municipality=municipality_id)

            return queryset
        else:
            return self.queryset

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class ModemViewSets(viewsets.ModelViewSet):
    queryset = Modem.objects.all()
    serializer_class = ModemSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.select_related(
            'subscriber', 'region', 'province', 'municipality', 'barangay', 'plan', 'modem'
        )
    serializer_class = SubscriptionSerializer
    filter_backends = [SearchFilter]
    search_fields = [
        'no',
        'alias',
        'purok',
        'bill_schedule',
        'subscriber__id_no',
        'subscriber__last_name',
        'barangay__name',
        'municipality__name',
        'plan__plan_name',
        'modem__modem_brand',
    ]

    def get_queryset(self):
        queryset = Subscription.objects.all()
        id = self.request.query_params.get('id')
        print(id)

        if id:
            queryset = queryset.filter(subscriber=id)

        return queryset

class BillingViewSet(viewsets.ModelViewSet):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer

    def get_queryset(self):
        queryset = Billing.objects.all()
        id = self.request.query_params.get("id")
        if id:
            queryset = queryset.filter(subscription=id)
            
        return queryset

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        # queryset = Payment.objects.all()
        # Fetch all Billing records and prefetch Payment records (LEFT JOIN behavior)
        queryset = Billing.objects.prefetch_related(
            Prefetch(
                'payments',  # Reverse relation from Payment to Billing
                queryset=Payment.objects.select_related('subscription', 'subscription__subscriber__user')
            )
        )

        # filter by id
        id = self.request.query_params.get("id")

        # filter by id
        user_id = self.request.query_params.get("user_id")
        # if user_id:
        #     queryset = queryset.filter(user_id=user_id)

        # filter by payment_date
        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get('end_date')

        # get the user_id
        user_id = self.request.query_params.get('user_id')

        # Convert start_date and end_date to datetime
        try:
            if start_date:
                start_date = datetime.strptime(start_date, "%Y-%m-%d")
            if end_date:
                end_date = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            return Billing.objects.none()  # Return empty queryset if date format is incorrect

        # Apply date range filtering for payments all
        payment_filters = Q()
        if start_date and end_date:
            payment_filters &= Q(payments__payment_date__date__range=(start_date, end_date))
        elif start_date:
            payment_filters &= Q(payments__payment_date__date__gte=start_date)
        elif end_date:
            payment_filters &= Q(payments__payment_date__date__lte=end_date)

        if user_id:
            # payment_filters &= Q(payment_set__received_by=user_id)

            if id:
                queryset = queryset.filter(bill_no=id)

        # Ensure we include Billing records even if they have no payments
        queryset = queryset.filter(payment_filters | Q(payments__isnull=True))

        return queryset
    
    def create(self, request, *args, **kwargs):
        data = request.data.copy()

        # Remove `reference_picture` from the request if it is empty
        if 'reference_picture' in data and not data['reference_picture']:
            data.pop('reference_picture')

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)  # Handle both PUT and PATCH
        instance = self.get_object()
        data = request.data.copy()

        # Remove `reference_picture` from the request if it is empty
        if 'reference_picture' in data and not data['reference_picture']:
            data.pop('reference_picture')

        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get_queryset(self):
        queryset = Ticket.objects.all()
        id = self.request.query_params.get("id")
        print(id)
        if id:
            queryset = queryset.filter(subscription=id)

        return queryset