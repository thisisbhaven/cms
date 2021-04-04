from django.urls import path

from articles.views import ArticleList, ArticleCreate, ArticleDetail, ArticleUpdateDelete

app_name = 'article'

urlpatterns = [
    path('', ArticleList.as_view()),
    path('create/', ArticleCreate.as_view()),
    path('<slug>/', ArticleDetail.as_view()),
    path('update/<slug>/', ArticleUpdateDelete.as_view()),
]
