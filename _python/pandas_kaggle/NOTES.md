



# :memo: Summary 

- data_frame
- df['col1',] 
- df.from_csv(, index_col)
- .loc(indexes, columns) : here indexes can be name of rows or the integgers if the rows have no columns
    - the slicing [begin:end] takes the end in consideration 
- .iloc(indexes, columns_as_indexes): this one takes only integers as indexes
    - the slicing [begin:end] it takes until end-1 

df.at[index, 'column']


- masking
- ~masking the negation of masking 
- in pandas we use the & and not the and (like in python )
- | is for or

- .str (to retrun the string ) 
- Att.isnull() and att.isnotnull()
- ...att.isin([elements...])
- .indexbackwards : to reverse the df order of rows 


- renaming reviews.rename(columns={'points':'score'})
- pd.concat([df1, df2]) 
left_df.join(right_df, lsuffix='_CAN', rsuffix='_UK')
-merge() 


.unique()
.value_count()


for index, row in df.iterrows():
    # dosomethign


.sort_values()

df.describe()
series.describe()

--- 

```py
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
```

```py
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
```

```py
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
```

```py
pd.Series([1, 2, 3, 4, 5])
```

```py
pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
```

```py
wine_reviews = pd.read_csv("datasets/winemag-data-130k-v2.csv")
wine_reviews.head()
```

```py
wine_reviews.shape
```

```py
reviews = pd.read_csv("datasets/winemag-data-130k-v2.csv", index_col=0)
```

```py
reviews['country'][0]
```

```py
reviews['country'][0:5]
```

```py
reviews.iloc[0]
```

```py
reviews.iloc[[1,2,0], 0]
```

```py
import numpy as np 
# Boolean indexing must have same length of the dataframe
bool_array = np.random.choice([True, False], len(reviews))
reviews.iloc[bool_array, 0]
```

```py
reviews.loc[:, 'country']
```

```py
reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]
```

```py
reviews.set_index('title')
```

```py
df = reviews.loc[[0,1,10,100], ['country', 'province', 'region_1', 'region_2']]
```

```py
reviews.country =='Italy'
```

```py
reviews.loc[reviews.country=='Italy']
```

```py
reviews.loc[reviews.country.isin(['Italy', 'France'])]
```

```py
reviews.loc[reviews.price.notnull()]
# reviews.loc[reviews.price.isnull()]
```

```py
reviews['critic'] = 'everyone'
reviews.head()
```

```py
# with iterable of values 
reviews['index_backwards'] = range(len(reviews), 0, -1)
```

```py
reviews.rename(columns={'points':'score'})
```

```py
# rename indexes 
reviews.rename(
    index= {
        0:'fistEntry',
        1:'SecondEntry' 
    }
)
```

```py
reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')
```

```py
pd.concat([british_youtube, canadian_youtube])
```

```py
left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])


left.join(right, lsuffix='_CAN', rsuffix='_UK')
```

```py
reviews.points.describe()
```

```py
reviews.points.mean()
```

```py
reviews.taster_name.unique()
```

```py
reviews.taster_name.value_counts()
```

```py
review_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - review_points_mean)
```


```py
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

# axis = 'columns' to transform each row
reviews.apply(remean_points, axis='columns') # wow it takes some times tbh
```

```py
review_points_mean = reviews.points.mean()
reviews.points - review_points_mean
```

```py
reviews.country + " - " + reviews.region_1
```

```py
bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']
```

```py
reviews.groupby('points').designation.count()
```

```py
x = reviews.groupby('winery').apply(lambda df: df.title.iloc[0])
```

```py
x = reviews.groupby('winery').apply(lambda df: df.iloc[0:2])
```

```py
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
```


```py
reviews.groupby(['country']).price.agg([len, min, max])
```

```py
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
```

```py
countries_reviewed.reset_index()
```

```py
countries_reviewed.sort_values(by='len')
```

```py
countries_reviewed.sort_values(by='len', ascending=False)
```

```py
countries_reviewed.sort_values(by=['country', 'len'], ascending=True).country
```

```py
country_variety_counts = reviews.groupby(['country', 'variety']).description.count().sort_values(ascending=False)

```

```py
reviews.price.dtype
```


```py
reviews.dtypes
```

```py
reviews.points.astype('float64')
# reviews.points.astype('str')
```

```py
reviews.index.dtype
```

```py
reviews[pd.isnull(reviews.country)]
```

```py
reviews[pd.isnotnull(reviews.country)]
```

```py
reviews[pd.isnull(reviews.price)].price
```

```py

```

```py

```


```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```


```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```


```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```


```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```


```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```


```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```


```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```