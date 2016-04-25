"""Evaluate top 3 accuracy"""

import graphlab as gl
import numpy as np
import pandas as pd


model = gl.load_model('model_cnn')
test_data = gl.SFrame.read_csv('test_data.csv')

predictions = model.predict_topk(test_data, k=3)
predictions.remove_column('probability')

unstacked = predictions.unstack('class', new_column_name='classes')

true = gl.SFrame(test_data['category', 'path'])
n = len(true['category'])
true['row_id'] = np.arange(0, n)

multiclass = true.join(unstacked, on='row_id')
multiclass.rename({'category': 'true', 'classes': 'predicted'})

true_pos = sum(multiclass.apply(lambda x: 1 if x['true'] in x['predicted'] else 0))
accuracy = true_pos/n

print "Top 3 accuracy: {}".format(accuracy)
