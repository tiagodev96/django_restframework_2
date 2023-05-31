from rest_framework import serializers
from clients.models import Client, Case
from clients.validators import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

    def validate(self, data):
        if not name_is_valid(data["name"]):
            raise serializers.ValidationError(
                {"name": "This Field doesn't allow numbers."}
            )
        if not document_is_valid(data["document"]):
            raise serializers.ValidationError(
                {"document": "Invalid document. Please insert a valid CPF."}
            )
        if not phone_is_valid(data["phone"]):
            raise serializers.ValidationError(
                {
                    "phone": "The number must be at least 11 digits long and must follow this template: '99 99999-9999'."
                }
            )
        return data


class CaseSerializer(serializers.ModelSerializer):
    responsible = serializers.ReadOnlyField(source="responsible.name")

    class Meta:
        model = Case
        fields = ["name", "responsible"]
