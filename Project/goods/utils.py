from django.db.models import Q
from django.contrib.postgres.search import SearchVector
from goods.models import Products

# 検索クエリに基づいて商品を検索する関数
def q_search(query):
    
    # クエリが数字であり、かつ長さが5文字以内の場合、商品IDで検索
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    # PostgreSQLのSearchVectorを使用した全文検索
    # ただし、日本語には対応していないため、Elasticsearchなどの他の検索エンジンを使用する必要があります
    #return Products.objects.annotate(search=SearchVector('name', 'description', )).filter(search=query)
    
    # クエリを単語に分割
    keywords = [word for word in query.split()]

    # Qオブジェクトを作成し、条件を追加
    q_objects = Q()

    for token in keywords:
        q_objects |= Q(description__icontains=token)  # 説明にトークンが含まれるかどうかを確認
        q_objects |= Q(name__icontains=token)  # 名前にトークンが含まれるかどうかを確認

    # 条件に一致する商品を返す
    return Products.objects.filter(q_objects)