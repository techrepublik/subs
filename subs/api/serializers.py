from rest_framework import serializers

from home.models import Region, Province, Municipality, Barangay, Plan, Modem, \
    Subscription, Billing, Payment, Issue, Ticket, User
from accounts.models import User, Employee, Subscriber

from djoser.serializers import UserSerializer as BaseUserSerializer


class CustomUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = BaseUserSerializer.Meta.fields + (
            'sub_no',
            'first_name',
            'last_name',
            'middle_name',
            'ext_name',
            'email',
            'user_type',
            'added_on',
            'updated_on',
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['full_name'] = f"{instance.first_name} {instance.last_name}"
        return representation


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name', 'last_name', 'middle_name', 'ext_name',
            'user_type', 'sub_no', 'password1', 'password2', 'is_active', 'is_staff'
        ]
        read_only_fields = ['id', 'is_active', 'is_staff']
        ref_name = "CustomUserSerializer" 

    def validate(self, data):
        # Ensure passwords match
        if data['password1'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match"})
        return data

    def create(self, validated_data):
        # Extract passwords
        password = validated_data.pop('password1')
        validated_data.pop('password2')

        # Create the user using the custom manager
        user = User.objects.create_user(password=password, **validated_data)
        return user

    def update(self, instance, validated_data):
        # Handle password update
        password1 = validated_data.pop('password1', None)
        password2 = validated_data.pop('password2', None)

        if password1 and password2:
            if password1 != password2:
                raise serializers.ValidationError({"password": "Passwords do not match"})
            instance.set_password(password1)

        # Update other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
    

class SubscriberSerializer(serializers.ModelSerializer):
    marital_status_choices = serializers.SerializerMethodField()
    gender_choices = serializers.SerializerMethodField()

    class Meta:
        model = Subscriber
        fields = '__all__'  # Include all fields or explicitly list them
        extra_fields = ['marital_status_choices', 'gender_choices']

    def get_marital_status_choices(self, obj):
        # Return choices as a list of dictionaries
        return [{'value': choice[0], 'display': choice[1]} for choice in Subscriber._meta.get_field('marital_status').choices]

    def get_gender_choices(self, obj):
        return [{'value': choice[0], 'display': choice[1]} for choice in Subscriber._meta.get_field('gender').choices]




class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'
    
class MunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = '__all__'

class BarangaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Barangay
        fields = '__all__'

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class ModemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modem
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    # Related fields from Subscriber
    id_no = serializers.CharField(source='subscriber.id_no', read_only=True)
    last_name = serializers.CharField(source='subscriber.last_name', read_only=True)
    first_name = serializers.CharField(source='subscriber.first_name', read_only=True)
    ext_name = serializers.CharField(source='subscriber.ext_name', read_only=True)
    gender = serializers.CharField(source='subscriber.gender', read_only=True)
    
    # Related fields from Subscription
    region_name = serializers.CharField(source='region.name', read_only=True)
    province_name = serializers.CharField(source='province.name', read_only=True)
    municipality_name = serializers.CharField(source='municipality.name', read_only=True)
    barangay_name = serializers.CharField(source='barangay.name', read_only=True)
    plan_name = serializers.CharField(source='plan.plan_name', read_only=True)
    plan_amount = serializers.CharField(source='plan.price', read_only=True)
    modem_name = serializers.CharField(source='modem.modem_brand', read_only=True)

    class Meta:
        model = Subscription
        # fields = [
        #     'id_no', 'last_name', 'first_name', 'ext_name', 'gender',  # Subscriber fields
        #     'account_no','alias', 'region', 'province', 'municipality', 'barangay', 'purok', 'plan', 'note', 'modem', 'modem_serial', 'pon_no', 'nap_no', 'referred_by', # Writable fields
        #     'region_name', 'province_name', 'municipality_name', 'barangay_name', 'plan_name',  'modem_name',# Read-only related names
        #     'sub_status', 'sub_type', 'date_activated', 'date_terminated', 'date_suspended', 'modem_username', 'modem_password'
        # ]
        fields = '__all__'


class BillingSerializer(serializers.ModelSerializer):
    last_name = serializers.CharField(source='billed_by.last_name', read_only=True)
    first_name = serializers.CharField(source='billed_by.first_name', read_only=True)

    collector_last_name = serializers.CharField(source='collector.last_name', read_only=True)
    collector_first_name = serializers.CharField(source='collector.first_name', read_only=True)

    class Meta:
        model = Billing
        # read_only_fields = ['created_on','updated_on', 'billing_no']
        # fields = ['billed_by','subscription','amount_due','billing_date','is_paid','is_partial',
        #           'bill_type','notice','remarks']
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    last_name = serializers.CharField(source='received_by.last_name', read_only=True)
    first_name = serializers.CharField(source='received_by.first_name', read_only=True)
    user_id = serializers.IntegerField(source='received_by.id', read_only=True)

    subscriber_last_name = serializers.CharField(source='subscription.subscriber.user.last_name', read_only=True)
    subscriber_first_name = serializers.CharField(source='subscription.subscriber.user.first_name', read_only=True)
    account_no = serializers.CharField(source='subscription.alias', read_only=True)
    billing_no = serializers.CharField(source='billing_no.billing_no', read_only=True)

    class Meta:
        model = Payment
        read_only_fields = ['created_on','updated_on', 'or_no']
        # fields = ['received_by','subscription', 'bill_no','amount_paid','payment_date','is_paid', 
        #           'is_partial','is_cancelled','remarks','or_ref_no','payment_type','cheque_no',
        #           'reference_no']
        fields = '__all__'

    # Make reference_picture optional
    reference_picture = serializers.ImageField(required=False, allow_null=True)

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        read_only_fields = ['created_on','updated_on']
        fields = ['name','description']


class TicketSerializer(serializers.ModelSerializer):
    last_name = serializers.CharField(source='prepared_by.last_name', read_only=True)
    first_name = serializers.CharField(source='prepared_by.first_name', read_only=True)

    last_name_to = serializers.CharField(source='assigned_to.last_name', read_only=True)
    first_name_to = serializers.CharField(source='assigned_to.first_name', read_only=True)

    class Meta:
        model = Ticket
        read_only_fields = ['created_on','updated_on']
        # fields = ['prepared_by','subscription','subject','description','issue','ticket_no',
        #           'priority','status','remarks']4
        fields = '__all__'
