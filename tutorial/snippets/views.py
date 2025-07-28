from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins,  generics

# Create your views here.
class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
    List all code snippets, or create a new snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SnippetDetail(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    """
    Retrieve, update or delete a code snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
# This code defines views for listing, creating, retrieving, updating, and deleting code snippets using Django REST Framework.
# The `SnippetList` view handles listing all snippets and creating a new snippet,
# while the `SnippetDetail` view handles retrieving, updating, and deleting a specific snippet by its primary key.
# Both views use mixins to provide the necessary functionality and inherit from `GenericAPIView` for common behaviors.
# The `queryset` attribute specifies the set of snippets to operate on, and the `serializer_class` defines how to serialize and deserialize the snippet data.
# The `get`, `post`, `put`, and `delete` methods are overridden to handle the respective HTTP methods for the views.
# This structure allows for a clean and reusable implementation of RESTful API endpoints for managing code snippets.
# The `SnippetList` view supports listing all snippets and creating new ones,