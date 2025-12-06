import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

from probeinterface import Probe, ProbeGroup
from probeinterface import generate_linear_probe, generate_multi_shank
from probeinterface import combine_probes
from probeinterface.plotting import plot_probe


multi_shank = generate_multi_shank(num_shank=2, num_columns=2, num_contact_per_column=12)
fig, ax = plt.subplots(figsize=(8, 10))
plot_probe(multi_shank, ax=ax)

# Create figures directory if it doesn't exist
output_path = Path('figures/probe_schematic.svg')
output_path.parent.mkdir(parents=True, exist_ok=True)

plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()


