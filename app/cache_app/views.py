import datetime
from django.core.cache import cache
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import TimeStampSerializer
import uuid

# Create your views here.
dx = []


class NaiveAPIView(GenericAPIView):
    serializer_class = TimeStampSerializer

    def get(self, request, *args, **kwargs):
        ts = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S.%f")
        _id = str(uuid.uuid4())
        dx.append((ts, _id))
        res = {}
        for k, v in sorted(dx, reverse=True):
            res[k] = v
        return Response(data=res, status=status.HTTP_200_OK)


class CachedAPIView(GenericAPIView):
    serializer_class = TimeStampSerializer

    def get(self, request, *args, **kwargs):
        ts = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S.%f")
        _id = str(uuid.uuid4())

        cache_key = "timestamps"

        ts_data = cache.get(cache_key)

        if not ts_data:
            # set the key
            cache.set(cache_key, {ts: _id})
            ts_data = {ts: _id}
            return Response(data=ts_data, status=status.HTTP_200_OK)
        else:
            # add new data
            ts_data[ts] = _id

            # invalidate old cache
            cache.delete(cache_key)

            # update cache
            cache.set(cache_key, ts_data)

            # sort and send response back to user
            res = {}
            for k, v in sorted(ts_data.items(), reverse=True):
                res[k] = v
            return Response(data=ts_data, status=status.HTTP_200_OK)
