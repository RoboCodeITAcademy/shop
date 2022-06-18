from .models import Category


def get_all(request):
    context = {
        "categories": Category.objects.all()
    }
    return context
