import json

from django.http import JsonResponse
from django.views.generic import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .models import Document, Label, Project
from .serializers import DocumentSerializer, LabelSerializer, ProjectSerializer


class ProjectStatus(View):
    def get(self, request):
        project_id = request.GET["project_id"]
        total_count = Document.objects.filter(project_id=project_id).count()
        is_checked_count = Document.objects.filter(
            project_id=project_id, is_checked=1
        ).count()
        return JsonResponse(
            {
                "total_count": total_count,
                "is_checked_count": is_checked_count,
                "precent": is_checked_count / total_count if total_count > 0 else 0,
            }
        )


class ProjectImport(View):
    def post(self, request):
        try:
            import_list = json.load(request.FILES.get("file").file)
            project_id = request.POST["project_id"]
            for item in import_list:
                Document.objects.create(project_id=project_id, text=item["text"])
            return JsonResponse({"total_count": len(import_list)})
        except Exception as e:
            return JsonResponse({"err": "json格式有问题"}, status=400)


class ProjectExport(View):
    def get(self, request):
        project_id = request.GET["project_id"]
        documents_by_project_id = Document.objects.filter(project_id=project_id)
        serializer = DocumentSerializer(documents_by_project_id, many=True)
        return JsonResponse(serializer.data, safe=False)


class DocumentList(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["project_id"]


class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class LabelList(generics.ListCreateAPIView):

    queryset = Label.objects.all()
    serializer_class = LabelSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["project_id"]


class LabelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
