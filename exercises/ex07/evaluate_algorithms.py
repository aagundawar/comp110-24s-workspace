__author__ = "730663390"

import matplotlib.pyplot as plt

START_SIZE: int = 0
END_SIZE: int = 1000

from exercises.ex07.runtime_analysis_functions import evaluate_runtime
 
times = evaluate_runtime("insertion_sort", START_SIZE, END_SIZE)
plt.plot(times)
plt.title("Runtime Analysis of Insertion Sort - ayushg")
plt.show()