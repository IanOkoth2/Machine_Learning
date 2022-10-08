import pandas as pd

# LOADING DATA IN PANDAS

# df = pd.read_excel('pokemon_data.xlsx')
df = pd.read_csv('pokemon_data.csv')
# df = pd.read_csv('pokemon_data.txt', delimiter='\t')

# Prints the first three rows
# print(df.head(3))

# Prints the last three rows
# print(df.tail(3))



# READING DATA IN PANDAS

# Reading Headers
# print(df.columns)

# Reading each column
# print(df['Name'][0:5])
# print(df.Name)

# Getting multiple columns
# print(df[['Name', 'Type 1', 'Type 2']])

# Reading each row
# print(df.head(4))
# print(df.iloc[1])
# print(df.iloc[0:4])

# Iterating through rows
# for index, row in df.iterrows():
# 	# print(index, row)
# 	print(index, row['Name'])

# Read a specific location (R, C)
# print(df.iloc[2, 1])

# Specific textual information
# info = df.loc[df['Type 1'] == "Fire"]
# print(info)



# SORTING/DESCRIBING DATA
# print(df.describe())

# Sorts according to alphabet
# print(df.sort_values('Name')) 
# print(df.sort_values('Name', ascending=False))
# print(df.sort_values(['Type 1', 'HP'], ascending=[1, 0]))



# MAKING CHANGES TO DATA
# print(df.head(6))
# df['total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
# df['total'] = df.iloc[:, 4:10].sum(axis=1)
# print(df.head(5))

# Dropping a column
# df = df.drop(columns = ['total'])
# print(df.head(5))

# Reordering the totals column
# cols = list(df.columns.values)
# print(cols)
# df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
# print(df.head(5))


# SAVING OUR CSV
# df.to_csv('modified.csv', index=False)

# df.to_excel('modified.xlsx', index=False)

# df.to_csv('modified.txt', index=False, sep='\t')



# FILTERING DATA
# print(df.head())
# Grass = df.loc[df['Type 1'] == 'Grass']
# print(Grass)

# Two different aspects
# new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Generation'] == 1) & (df['Speed'] > 70)]
# new_df = new_df.reset_index()
# new_df.to_excel('Filtered.xlsx')

# Removing names that contain 'Mega'
# print(df.loc[df['Name'].str.contains('Mega')])
# The "not" function
# print(!df.loc[df['Name'].str.contains('Mega')])


# CONDITIONAL CHANGES
# Changes all the characters whose Type 1 value is Fire i.e Legendary values become True
# df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True



# AGGREGATE STATISTICS(GROUPBY)
# aggr = df.groupby(['Type 1']).mean().sort_values('Speed', ascending=False)
# print(aggr)
# df['count'] = 1
# x = df.groupby(['Type 1']).count()['count']
# y = df.groupby(['Type 1', 'Type 2']).count()['count']
# print(y)



# WORKING WiTH VERY LARGE DATASETS
new_df = pd.DataFrame(columns=df.columns)
for df in pd.read_csv('modified.csv', chunksize=5):
	results = df.groupby(['Type 1']).count()
    
new_df = pd.concat([new_df, results])

print(new_df)