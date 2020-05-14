from django.db import models


class Project(models.Model):
    """项目表"""

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "label_project"


class Label(models.Model):
    """项目Label"""

    project_id = models.ForeignKey(
        Project,
        db_column="project_id",
        related_name="project_label",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=128)
    shortcut = models.CharField(max_length=8)
    background_color = models.CharField(max_length=8)
    text_color = models.CharField(max_length=8)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "label_label"


class Document(models.Model):
    """标注文本表"""

    text = models.TextField()
    project_id = models.IntegerField()
    annotations = models.CharField(max_length=2048, default="[[]]")
    predications = models.TextField(default="[[]]")
    is_checked = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "label_document"
