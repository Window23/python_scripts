""" (Intro to Data Science: Visualizing Survey Response Statistics)
    Using the list in Exercise 5.28 and the techniques you learned in Section 5.17.2,
    display a bar chart showing the response frequencies and their percentages of the total responses. """

import matplotlib.pyplot as plt
import numpy as np
import random as rd
import seaborn as sns


lst = [rd.randint(1, 5) for i in range(20000)]

val, freq = np.unique(lst, return_counts=True)

title = f'Rolling a two-side die {len(lst):,} Times'
sns.set_style('whitegrid')

axes = sns.barplot(x=val, y=freq, hue=val, palette="bright", legend=False, )   #pentru a seta graficul cu valorile obtinute
axes.set_title(title)   #pentru a seta titlul
axes.set(xlabel="die value", ylabel="frequency")  #pentru a seta descrierile pe fiecare axa.. X si Y
axes.set_ylim(top=max(freq) * 1.10)     #pentru a seta inaltimea dorita pentru axa Y
 #pentru a call-ui matplotlib si a face display-ul graficului

for bar, frequency in zip(axes.patches, freq):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / len(lst):.2%}'
    axes.text(text_x, text_y, text,
    fontsize=11, ha='center', va='bottom')

plt.show()