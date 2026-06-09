import matplotlib.pyplot as plt

timesteps = [10, 25, 50]

accuracies = [
    95.91,
    96.23,
    95.44
]

plt.figure(figsize=(6,4))

plt.plot(
    timesteps,
    accuracies,
    marker="o"
)

plt.xlabel("Timesteps")
plt.ylabel("Accuracy (%)")
plt.title("Accuracy vs Timesteps")

plt.grid(True)

for x, y in zip(timesteps, accuracies):
    plt.text(x, y, f"{y:.2f}%")

plt.savefig("accuracy_vs_timesteps.png")

plt.show()