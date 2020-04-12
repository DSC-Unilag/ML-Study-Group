import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder


training_ds = pd.read_csv('Training set values.csv')
test_ds = pd.read_csv('Test Set values.csv')


replacements_for_training_ds={
	'source_type':training_ds.source_type.mode(),
	'payment_type':training_ds.payment_type.mode()
	}

training_ds = training_ds.replace({
	'source_type': 'unknown',
	'payment_type': 'unknown'
	}, replacements_for_training_ds)


replacements_for_test_ds={
	'source_type':test_ds.source_type.mode(),
	'payment_type':test_ds.payment_type.mode()
	}
test_ds = test_ds.replace({
	'source_type': 'unknown',
	'payment_type': 'unknown'
	}, replacements_for_test_ds)


training_ds = training_ds.dropna()

x = training_ds[['source_type', 'payment_type']]
y = training_ds['quantity_group']

x1_id = test_ds['id']
x1 = test_ds[['source_type', 'payment_type']]
y1 = test_ds['quantity_group']

le = LabelEncoder()

x['source_type_n'] = le.fit_transform(x['source_type'])
x['payment_type_n'] = le.fit_transform(x['payment_type'])
x = x.drop(columns=['source_type', 'payment_type'])

y = le.fit_transform(y)

x1['source_type_n'] = le.fit_transform(x1['source_type'])
x1['payment_type_n'] = le.fit_transform(x1['payment_type'])
x1 = x1.drop(columns=['source_type', 'payment_type'])

y1 = le.fit_transform(y1)

model = DecisionTreeClassifier()
model.fit(x,y)
print('Length of test ds', len(x1))
print(model.score(x1, y1))

inv_transform = le.inverse_transform(model.predict(x1))
result = pd.DataFrame(inv_transform, index=x1_id, columns=['status_group'])
result = result.replace({
	'enough': 'functional',
	'dry': 'non functional',
	'seasonal': 'functional needs repair',
	'insufficient': 'functional needs repair'
	})
result.reset_index(inplace=True)
result.to_csv('Ibrahim_ganiu.csv', index=False)
