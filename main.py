from torchvision import datasets, transforms
from torch.utils.data import DataLoader

import torch
import torch.nn as nn
import torch.optim as optim

import snntorch as snn
import snntorch.spikegen as spikegen
from snntorch import spikeplot as splt

import matplotlib.pyplot as plt


# ==========================================
# 1. LOAD MNIST
# ==========================================

transform = transforms.ToTensor()

mnist_train = datasets.MNIST(
    root="./data",
    train=True,
    download=True,
    transform=transform
)

mnist_test = datasets.MNIST(
    root="./data",
    train=False,
    download=True,
    transform=transform
)

print("Train Images:", len(mnist_train))
print("Test Images:", len(mnist_test))


# ==========================================
# 2. DATALOADERS
# ==========================================

train_loader = DataLoader(
    mnist_train,
    batch_size=128,
    shuffle=True
)

test_loader = DataLoader(
    mnist_test,
    batch_size=128,
    shuffle=False
)


# ==========================================
# 3. DEVICE
# ==========================================

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

print("Using Device:", device)


# ==========================================
# 4. SNN MODEL
# ==========================================

class Net(nn.Module):

    def __init__(self):

        super().__init__()

        beta = 0.95

        self.fc1 = nn.Linear(784, 128)
        self.lif1 = snn.Leaky(beta=beta)

        self.fc2 = nn.Linear(128, 10)
        self.lif2 = snn.Leaky(beta=beta)

    def forward(self, x):

        mem1 = self.lif1.init_leaky()
        mem2 = self.lif2.init_leaky()

        spk2_rec = []

        for step in range(x.size(0)):

            batch_size = x.shape[1]

            current1 = self.fc1(
                x[step].view(batch_size, -1)
            )

            spk1, mem1 = self.lif1(
                current1,
                mem1
            )

            current2 = self.fc2(spk1)

            spk2, mem2 = self.lif2(
                current2,
                mem2
            )

            spk2_rec.append(spk2)

        return torch.stack(spk2_rec)


# ==========================================
# 5. CREATE MODEL
# ==========================================

net = Net().to(device)

loss_fn = nn.CrossEntropyLoss()

optimizer = optim.Adam(
    net.parameters(),
    lr=0.001
)


# ==========================================
# 6. TRAIN
# ==========================================

epochs = 1
num_steps = 25

print("\nTraining Started...\n")

for epoch in range(epochs):

    net.train()

    for batch_idx, (images, labels) in enumerate(train_loader):

        images = images.to(device)
        labels = labels.to(device)

        spike_data = spikegen.rate(
            images,
            num_steps=num_steps
        )

        output = net(spike_data)

        scores = output.sum(dim=0)

        loss = loss_fn(scores, labels)

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

        if batch_idx % 100 == 0:

            print(
                f"Batch {batch_idx} | Loss: {loss.item():.4f}"
            )

print("\nTraining Complete!\n")


# ==========================================
# 7. TEST ACCURACY
# ==========================================

net.eval()

correct = 0
total = 0

with torch.no_grad():

    for images, labels in test_loader:

        images = images.to(device)
        labels = labels.to(device)

        spike_data = spikegen.rate(
            images,
            num_steps=num_steps
        )

        output = net(spike_data)

        scores = output.sum(dim=0)

        predicted = scores.argmax(dim=1)

        total += labels.size(0)

        correct += (
            predicted == labels
        ).sum().item()

accuracy = 100 * correct / total

print(f"\nAccuracy: {accuracy:.2f}%\n")


# ==========================================
# 8. SHOW PREDICTION
# ==========================================

image, label = mnist_test[0]

spike_data = spikegen.rate(
    image,
    num_steps=num_steps
)

spike_data = spike_data.to(device)

with torch.no_grad():

    output = net(spike_data)

prediction = output.sum(dim=0).argmax()

plt.figure(figsize=(5,5))

plt.imshow(
    image.squeeze(),
    cmap="gray"
)

plt.title(
    f"Actual: {label} | Predicted: {prediction.item()}"
)

plt.show()


# ==========================================
# 9. RASTER PLOT
# ==========================================

spike_data = spikegen.rate(
    image,
    num_steps=num_steps
)

spikes = spike_data.reshape(
    num_steps,
    -1
)

fig, ax = plt.subplots(
    figsize=(10,5)
)

splt.raster(
    spikes,
    ax
)

plt.title(
    f"Raster Plot For Digit {label}"
)

plt.show()


# ==========================================
# 10. TIMESTEP GRAPH
# ==========================================

timesteps = [10, 25, 50]

# Replace with your real results
accuracies = [
    92,
    95.24,
    96
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

plt.show()

