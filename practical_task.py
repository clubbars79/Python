import pandas as pd
import numpy as np
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.get_dummies(lst)
data.head()