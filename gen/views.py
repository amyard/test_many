from django.shortcuts import render

from .models import Article, Publication
import pandas as pd



def get_value_from_list(value, iter=0, sort_direct=True):
    try:
        value = value[iter]
    except IndexError:
        # value =  999999 if sort_direct == True else 0
        value = 0 
    return value


def get_unique_val(qs, sort_direct):
    df = pd.DataFrame(columns = ['id', 'headline', 'name', 'count'])

    for numb, item in enumerate(qs):
        df.loc[numb, 'id'] = item.id
        df.loc[numb, 'headline'] = item
        df.loc[numb, 'name'] = item.publications.values_list('title', flat=True)
        df.loc[numb, 'count'] = item.publications.count()

    max_val = df['count'].values.max()
    df = df.drop_duplicates(subset='id', keep="last")
    for i in range(0, max_val):
        df[f'col_{i}'] = df['name'].apply(lambda x: get_value_from_list(x, i, sort_direct))

    sort_by_col = [ f'col_{i}' for i in range(max_val) ]
    df2 = df.sort_values(sort_by_col, ascending=sort_direct)
    ids = df2['headline'].tolist()
    return ids




def index(request):

    df = Article.objects.all()
    ids_asc = get_unique_val(df, True)
    ids_desc = get_unique_val(df, False)

    context = { 
        'asc': Article.objects.order_by('publications__title'),
        'desc': ids_asc
    }
    return render(request, 'base.html', context = context)