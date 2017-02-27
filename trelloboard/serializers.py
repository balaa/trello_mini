from rest_framework import serializers
from trelloboard.models import Board, Card, List


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('id', 'name')


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ('id', 'name')


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'name', 'description', 'due_date', 'label')
