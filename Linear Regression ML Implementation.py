import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.datasets import load_boston
from sklearn.preprocessing import minmax_scale
data=load_boston()
df = pd.DataFrame(data=data.data, columns=data.feature_names)
df.head()
print("sai")
