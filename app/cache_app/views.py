import datetime
from django.core.cache import cache
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import TimeStampSerializer
import uuid

# Create your views here.
list_cache = []


class NaiveAPIView(GenericAPIView):
    serializer_class = TimeStampSerializer

    def get(self, request, *args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S.%f")
        _id = str(uuid.uuid4())
        list_cache.append((timestamp, _id))

        result = {k: v for k, v in sorted(list_cache, reverse=True)}
        return Response(data=result, status=status.HTTP_200_OK)


class CachedAPIView(GenericAPIView):
    serializer_class = TimeStampSerializer

    def get(self, request, *args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S.%f")
        _id = str(uuid.uuid4())

        cache_key = "timestamps"

        timestamp_data = cache.get(cache_key)

        if not timestamp_data:
            # set the key
            cache.set(cache_key, {timestamp: _id})
            timestamp_data = {timestamp: _id}
            return Response(data=timestamp_data, status=status.HTTP_200_OK)
        else:
            # add new data
            timestamp_data[timestamp] = _id

            # invalidate old cache
            cache.delete(cache_key)

            # update cache
            cache.set(cache_key, timestamp_data)

            # sort and send response back to user
            result = {k: v for k, v in sorted(
                timestamp_data.items(), reverse=True)}
            return Response(data=result, status=status.HTTP_200_OK)
