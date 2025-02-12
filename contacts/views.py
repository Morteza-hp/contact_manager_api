from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Contact
from .serializers import ContactSerializer

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS', 'POST')

class IsAuthenticatedOrReadAndPostOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )

class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filterset_fields = ['first_name','last_name','phone_number']
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['first_name','last_name','phone_number']
    ordering_fields = ['first_name', 'last_name']
    ordering = ['-id']
    permission_classes = [IsAuthenticatedOrReadAndPostOnly]
    # authentication_classes = [TokenAuthentication]


# class ContactListView(viewsets.generics.ListAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['first_name','last_name','phone_number']

# class ContactViewSet(ViewSet):
#   def list(self, request):
#     queryset = Contact.objects.all()
#     serializer = ContactSerializer(queryset, many=True)
#     return Response(serializer.data)
#   def retrieve(self, request,pk):
#     queryset = Contact.objects.get(pk=pk)
#     serializer = ContactSerializer(queryset)
#     return Response(serializer.data)
#   def create(self, request):
#     pass
#   def update(self, request):
#     pass
#   def destroy(self, request):
#     pass

# class ContactApiView(APIView):
#     def get(self, request):
#         pass
#     def post(self, request):
#         pass
#     def put(self, request):
#         pass
#     def delete(self, request):
#         pass

# class ContactApiView(ListCreateAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#
# class ContactItemView(RetrieveUpdateDestroyAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer