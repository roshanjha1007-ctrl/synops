from torchvision import datasets, transforms
from snntorch import spikegen
from snntorch import spikeplot as splt

import matplotlib.pyplot as plt

transform = transforms.ToTensor()

mnist_test = datasets.MNIST(
    root="./data",
    train=False,
    download=True,
    transform=transform
)

target_digits = [0, 1, 2, 7, 9]

T = 25

for target_digit in target_digits:

    image = None

    for img, lbl in mnist_test:
        if lbl == target_digit:
            image = img
            break

    if image is None:
        print(f"Digit {target_digit} not found!")
        continue

    spikes = spikegen.rate(
        image,
        num_steps=T
    )

    spikes_flat = spikes.reshape(T, -1)

    fig, ax = plt.subplots(figsize=(10, 5))

    splt.raster(spikes_flat, ax)

    plt.title(f"Raster Plot - Digit {target_digit}")

    filename = f"digit_{target_digit}_raster.png"

    plt.savefig(filename)

    print(f"Saved {filename}")

    plt.close(fig)

print("Done!")