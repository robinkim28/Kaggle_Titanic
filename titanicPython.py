from IPython.core.display import HTML
HTML("""
<style>
.output_png {
    display: table-cell;
    text-align: center;
    vertical-align: middle;
}
</style>
""")

import warnings
warnings.filterwarnings('ignore')


print("hello World")

import pandas as pd

pd.options.display.max_columns = 100
from matplotlib import pyplot as plt
import matplotlib

matplotlib.style.use('ggplot')
import numpy as np

pd.options.display.max_rows = 100

def process_cabin():

    global combined

    #replacing missing cabins with U (U for unknown)
    combined.Cabin.fillna('U',inplace = True)

    #mapping each cabin value with the cabin letter
    combined.['Cabin'] = combined['Cabin']def process_cabin():

        global combined

        #replacing missing cabins with U (U for unknown)
        combined.Cabin.fillna('U',inplace = True)

        #mapping each cabin value with the cabin letter
        combined.['Cabin'] = combined['Cabin'].map(lambda c : c[0])

        #dummy encoding...
        cabin_dummies = pd.get_dummies(combined['Cabin'], prefix = 'Cabin')

        combined = pd.concat([combined, cabin_dummies], axis = 1)

        #combined.drop('Cabin',axis = 1, inplace=True)

        status('cabin')

process_cabin()


combined['Cabin'] = combined['Cabin'].map(lambda c: c[0])
grouped = combined.groupby(['Cabin','Pclass','Title'])
grouped.mean()
