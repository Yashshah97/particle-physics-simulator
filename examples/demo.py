"""Demo for Particle Physics Simulation Engine."""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import particle_physics_simulator

print("Particle Physics Simulation Engine", "v" + particle_physics_simulator.__version__)
print("modules:", [m for m in dir(particle_physics_simulator) if not m.startswith('_')])
