from rest_framework import serializers

from .models import Document, Label, Project


class ProjectSerializer(serializers.ModelSerializer):
    """serializer for Project"""

    class Meta:
        model = Project
        fields = ("id", "name", "description")


class LabelSerializer(serializers.ModelSerializer):
    """serializer for Label"""

    class Meta:
        model = Label
        fields = (
            "id",
            "project_id",
            "name",
            "shortcut",
            "background_color",
            "text_color",
        )


class DocumentSerializer(serializers.ModelSerializer):
    """serializer for Document"""

    class Meta:
        model = Document
        fields = ("id", "text", "project_id", "annotations", "predications", "is_checked")
