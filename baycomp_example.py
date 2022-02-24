import pandas as pd
import numpy as np
import baycomp
import matplotlib.pyplot as plt

n_cv = 10
n_runs = 10

shift = 0.05

data = {
    "alg0": {
        "task0": np.random.normal(loc=0.1, scale=0.4, size=n_cv * n_runs),
        "task1": np.random.normal(loc=0.2, scale=0.2, size=n_cv * n_runs),
        "task2": np.random.normal(loc=0.8, scale=0.4, size=n_cv * n_runs),
        "task3": np.random.normal(loc=0.24, scale=0.2, size=n_cv * n_runs),
        "task4": np.random.normal(loc=0.6, scale=0.3, size=n_cv * n_runs),
        "task5": np.random.normal(loc=0.2, scale=0.4, size=n_cv * n_runs),
        "task6": np.random.normal(loc=0.3, scale=0.1, size=n_cv * n_runs),
        "task7": np.random.normal(loc=0.4, scale=0.2, size=n_cv * n_runs),
        "task8": np.random.normal(loc=0.14, scale=0.2, size=n_cv * n_runs),
        "task9": np.random.normal(loc=0.19, scale=0.3, size=n_cv * n_runs),
    },
    "alg1": {
        "task0":
        np.random.normal(loc=shift + 0.15, scale=0.3, size=n_cv * n_runs),
        "task1":
        np.random.normal(loc=shift + 0.18, scale=0.22, size=n_cv * n_runs),
        "task2":
        np.random.normal(loc=shift + 0.7, scale=0.1, size=n_cv * n_runs),
        "task3":
        np.random.normal(loc=shift + 0.16, scale=0.11, size=n_cv * n_runs),
        "task4":
        np.random.normal(loc=shift + 0.6, scale=0.13, size=n_cv * n_runs),
        "task5":
        np.random.normal(loc=shift + 0.17, scale=0.3, size=n_cv * n_runs),
        "task6":
        np.random.normal(loc=shift + 0.28, scale=0.22, size=n_cv * n_runs),
        "task7":
        np.random.normal(loc=shift + 0.55, scale=0.3, size=n_cv * n_runs),
        "task8":
        np.random.normal(loc=shift + 0.12, scale=0.21, size=n_cv * n_runs),
        "task9":
        np.random.normal(loc=shift + 0.18, scale=0.73, size=n_cv * n_runs),
    }
}
data = pd.DataFrame.from_dict(data).unstack().apply(pd.Series)

print()
print("# only on task 0")
print()

data1 = data.loc[("alg0", "task0")]
data2 = data.loc[("alg1", "task0")]

names = data1.name[0], data2.name[0]

figs = []

probs, fig = baycomp.two_on_single(data1,
                                   data2,
                                   runs=n_runs,
                                   names=names,
                                   plot=True)
print("Without rope:", probs)
figs.append(fig)
plt.show()

print()
input("Next up: With rope …")
print()

probs, fig = baycomp.two_on_single(data1,
                                   data2,
                                   runs=n_runs,
                                   names=names,
                                   plot=True,
                                   rope=0.01)
print("With rope:", probs)
figs.append(fig)
plt.show()

print()
input("Next up: On all tasks …")
print()

print()
print("# On all tasks")
print()

data_ = data.apply(np.mean, axis=1)

probs, fig = baycomp.two_on_multiple(data_["alg0"],
                                     data_["alg1"],
                                     runs=n_runs,
                                     names=names,
                                     plot=True,
                                     rope=0.01)
print("With non-hierarchical test:", probs)
figs.append(fig)
plt.show()

print()
input("Next up: On all tasks, hierarchical test …")
print()

probs, fig = baycomp.two_on_multiple(data.loc["alg0"].to_numpy(),
                                     data.loc["alg1"].to_numpy(),
                                     runs=n_runs,
                                     names=names,
                                     plot=True,
                                     rope=0.01)
print("With hierarchical test:", probs)
figs.append(fig)
plt.show()
