from rest_framework import serializers 

from .models import * 



# class BranchSerializer(serializers.ModelSerializer):
#     bank_name = serializers.SerializerMethodField()

#     class Meta:
#         model = Branch
#         fields = ('name', 'address', 'branch_code',  'bank_name')
#         read_only_fields = ('id', 'bank_name')

#     def get_bank_name(self, obj):
#         return obj.bank.name if obj.bank else None
    
# bank_name = serializers.SerializerMethodField() is a line of code in the BranchSerializer class. It creates a new field called bank_name in the serialized output of the Branch model. This field is not directly mapped to any field in the Branch model; instead, it's a custom field whose value is determined by a method.

# The SerializerMethodField allows you to specify a method on the serializer class that will be used to determine the value of the field when the serializer is serialized. In this case, the method get_bank_name is used to determine the value of the bank_name field.

# Here's how it works:

# python
# Copy code
# def get_bank_name(self, obj):
#     return obj.bank.name if obj.bank else None
# get_bank_name is a method defined within the BranchSerializer class.
# It takes two parameters: self (a reference to the serializer instance) and obj (the instance of the Branch model being serialized).
# Inside the method, it checks if the obj has a related bank (obj.bank). If it does, it retrieves the name of the bank (obj.bank.name). If not, it returns None.
# The value returned by this method is then used as the value of the bank_name field in the serialized output.


# class BranchSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Branch
#         fields = ('name', 'address', 'branch_code')

class BranchSerializer(serializers.ModelSerializer):
    bank_name = serializers.CharField(source='bank.name', read_only=True)

    class Meta:
        model = Branch
        fields = ('name', 'address', 'branch_code', 'bank_name')

class BankSerializer(serializers.ModelSerializer):
    branches = BranchSerializer(many=True, read_only=True)

    class Meta:
        model = Bank 
        fields = ('name', 'branches')



class ClientManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientManager
        fields = ('__all__')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('__all__')


class AccountSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    bank = BankSerializer()
    class Meta:
        model = Account
        fields = ('__all__')



class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ('__all__')


class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields = ('__all__')


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ('__all__')