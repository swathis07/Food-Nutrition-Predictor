"""Evaluating model"""

import graphlab as gl
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

test_data = gl.SFrame.read_csv('test_data.csv')
model = gl.load_model('74per_model')
with open('class_map.pickle', 'rb') as fhand:
    class_map = pickle.load(fhand)

inv_map = {v: k for k, v in class_map.items()}

pred = model.predict_topk(validation_data, k=1)

table = gl.SFrame({'true': test_data['category'], 'predicted': pred['class']})
table = table.to_dataframe()

table['target_label'] = table['target'].apply(lambda x: inv_map[x])
table['predicted_label'] = table['predicted'].apply(lambda x: inv_map[x])
labels = sorted(class_map.keys())

cm = confusion_matrix(table['target_label'], table['predicted_label'], labels)
cm_normalized = np.round(cm.astype('float') / cm.sum(axis=1)[:, np.newaxis], 2)

fig = plt.figure()
f, ax = plt.subplots(1, 1, figsize=(8, 8))
cax = ax.matshow(cm_normalized)

plt.title('Confusion matrix of the classifier')
f.colorbar(cax)
ax.set_xticklabels([''] + labels)
ax.set_yticklabels([''] + labels)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.save('confusion_matrix.png')
