if __name__ == '__main__':
    import os, sys

    sys.path.append(os.path.dirname(os.path.dirname(__file__)))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    import django

    django.setup()
    # 导入model包需要在setup后面导入
    from django_orm.models import BlobQuestion

    print(BlobQuestion.objects.all())
