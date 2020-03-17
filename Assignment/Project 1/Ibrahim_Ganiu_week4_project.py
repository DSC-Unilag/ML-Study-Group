import pandas as pd
import numpy as np
import datetime

def extractAgeFromDOB(date):
	""" Computes the age using full date passed [date] """
	return int(datetime.datetime.now().year-date)

training_ds = pd.read_csv('Training set values.csv')
test_ds = pd.read_csv('Test Set values.csv')

# Replacing construction_year that is empty with 0 for futur flexible adjustment
training_ds = training_ds.replace({'construction_year':np.NaN}, 0)

training_ds = training_ds.dropna()
test_ds = test_ds.dropna()

replacements_for_training_ds={
	'construction_year':training_ds.construction_year.median(),
	'water_quality':training_ds.water_quality.mode(),
	'quality_group':training_ds.quality_group.mode(),
	'quantity':training_ds.quantity.mode(),
	'quantity_group':training_ds.quantity_group.mode(),
	'source_class':training_ds.source_class.mode()
	}


training_ds = training_ds.replace({
	'construction_year': 0,
	'water_quality': 'unknown',
	'quality_group': 'unknown',
	'quantity': 'unknown',
	'quantity_group': 'unknown',
	'source_class': 'unknown'
	}, replacements_for_training_ds)


replacements_for_test_ds={
	'construction_year':int(test_ds.construction_year.median()),
	'water_quality':test_ds.water_quality.mode(),
	'quality_group':test_ds.quality_group.mode(),
	'quantity':test_ds.quantity.mode(),
	'quantity_group':test_ds.quantity_group.mode(),
	'source_class':test_ds.source_class.mode()
	}
test_ds = test_ds.replace({
	'construction_year': 0,
	'water_quality': 'unknown',
	'quality_group': 'unknown',
	'quantity': 'unknown',
	'quantity_group': 'unknown',
	'source_class': 'unknown'
	}, replacements_for_test_ds)



################ QUALITY OF WATER ####################


# Features from training dataset for the quality of water
x_train = training_ds[['payment_type','water_quality','source_type','source_class','waterpoint_type']]
y_train = training_ds['quality_group']

# Features from test dataset for the quality of water
x_train = test_ds[['payment_type','water_quality','source_type','source_class','waterpoint_type']]
y_train = test_ds['quality_group']



############# FAULT OF THE PUMP ##############


training_ds['Age'] = training_ds['construction_year'].apply(extractAgeFromDOB)
test_ds['Age'] = test_ds['construction_year'].apply(extractAgeFromDOB)
training_ds.drop(columns=['construction_year'])
test_ds.drop(columns=['construction_year'])


# Features from train dateset for the quantity of the water
x_train2 = training_ds[['population','Age','payment_type','management','source_class']]
y_train2 = training_ds['quantity_group']

# print(x_train2.head(3))
# print('###########################')
# print(training_ds.head(3))
