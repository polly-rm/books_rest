from rest_framework import serializers

from django_rest.books_api.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def validate(self, data):
        if data.get('title'):
            if not data.get('title')[0].isupper():
                raise serializers.ValidationError('Title must start with a capital letter')
        return data
