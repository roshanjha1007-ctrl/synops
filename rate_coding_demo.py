import torch
from snntorch import spikegen

T = 50

bright_pixel = torch.tensor([0.9])
dark_pixel = torch.tensor([0.1])

bright_spikes = spikegen.rate(
    bright_pixel,
    num_steps=T
)

dark_spikes = spikegen.rate(
    dark_pixel,
    num_steps=T
)

print("Bright pixel spikes:")
print(bright_spikes.squeeze())

print("\nDark pixel spikes:")
print(dark_spikes.squeeze())

print(
    f"Bright spike count: {bright_spikes.sum().item()}"
)

print(
    f"Dark spike count: {dark_spikes.sum().item()}"
)