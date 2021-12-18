from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,DestroyAPIView
from .serializers import DonorSerializer,DelDonorSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Donor

class CreateDonorAPIView(CreateAPIView):
    serializer_class=DonorSerializer
    def post(self, request):
        serializer=self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_200_OK)
        else:
            content={'ERROR':'VALIDATION'}
            return Response(content,status.HTTP_406_NOT_ACCEPTABLE)

class ReadDonorAPIView(ListAPIView):
    serializer_class=DonorSerializer
    queryset=Donor.objects.all()

    def get(self, request, *args, **kwargs):
        serializer=super().list(request,*args,**kwargs)

        return Response(serializer.data,status.HTTP_200_OK)


class UpdateDonorAPIView(UpdateAPIView):
    serializer_class=DonorSerializer
    def get_queryset(self):
        return Donor.objects.filter(donor_id=self.kwargs["pk"])

    def patch(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        instance=self.get_object()
        
        instance.donor_name=request.data["donor_name"]
        instance.blood_group=request.data["blood_group"]
        instance.contact_no=request.data["contact_no"]
        instance.last_donation=request.data["last_donation"]
        instance.location_donation=request.data["location_donation"]
        
        if serializer.is_valid(raise_exception=True):

            self.partial_update(serializer)
            return Response(serializer.data,status.HTTP_200_OK)
        else:
            content={'ERROR':'YOU ENTERED SOMETHING BUGGY'}
            return Response(content,status.HTTP_406_NOT_ACCEPTABLE)


class DeleteDonorAPIView(DestroyAPIView):
    serializer_class=DelDonorSerializer
    def get_queryset(self):
        return Donor.objects.filter(donor_id=self.kwargs["pk"])

    def delete(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.destroy(serializer)
            return Response("DELETE SUCCESS",status.HTTP_200_OK)
        else:
            content={'ERROR':'Primary key Mismatch'}
            return Response(content,status.HTTP_406_NOT_ACCEPTABLE)