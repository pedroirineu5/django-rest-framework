from rest_framework import generics

from reviews.models import Review


class ReviewCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    # TODO colocar o serializer class
    serializer_class = ...


class ReviewRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    # TODO colocar o serializer class
    serializer_class = ...