from news1.models import category

def category_list(request):
    category_list = category.objects.all()
    return {'cat': category_list}