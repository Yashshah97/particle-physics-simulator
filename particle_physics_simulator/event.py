"""
Collision Event Data Structure and Manipulation.

This module provides a simple data structure to represent collision events,
along with methods for manipulating these events.
"""

class CollisionEvent:
    """Represents a single collision event."""

    def __init__(self, id: int, particles: list[tuple[int, float, float]], energy: float):
        """
        Initializes a new CollisionEvent.

        Args:
            id (int): Unique identifier for the event.
            particles (list[tuple[int, float, float]]): List of particle properties
                (mass, charge, momentum).
            energy (float): Total energy released in the collision.
        """
        self.id = id
        self.particles = particles
        self.energy = energy

    def __repr__(self):
        return f"CollisionEvent(id={self.id}, particles={self.particles}, energy={self.energy})"

def create_collision_event(id: int, particles: list[tuple[int, float, float]], energy: float) -> CollisionEvent:
    """
    Creates a new CollisionEvent instance.

    Args:
        id (int): Unique identifier for the event.
        particles (list[tuple[int, float, float]]): List of particle properties
            (mass, charge, momentum).
        energy (float): Total energy released in the collision.

    Returns:
        CollisionEvent: The newly created CollisionEvent instance.
    """
    return CollisionEvent(id, particles, energy)

def merge_collision_events(event1: CollisionEvent, event2: CollisionEvent) -> CollisionEvent:
    """
    Merges two CollisionEvent instances into a new one.

    Args:
        event1 (CollisionEvent): First collision event to merge.
        event2 (CollisionEvent): Second collision event to merge.

    Returns:
        CollisionEvent: The merged CollisionEvent instance.
    """
    merged_particles = event1.particles + event2.particles
    return create_collision_event(event1.id, merged_particles, event1.energy + event2.energy)
