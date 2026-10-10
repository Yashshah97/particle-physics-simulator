import unittest
from particle_physics_simulator import event

class TestEvent(unittest.TestCase):

    def test_collision_event_init(self):
        event1 = event.CollisionEvent(1, [(1, 2.0, 3.0)], 4.0)
        self.assertEqual(event1.id, 1)
        self.assertEqual(event1.particles, [(1, 2.0, 3.0)])
        self.assertEqual(event1.energy, 4.0)

    def test_create_collision_event(self):
        event1 = event.create_collision_event(1, [(1, 2.0, 3.0)], 4.0)
        self.assertIsInstance(event1, event.CollisionEvent)
        self.assertEqual(event1.id, 1)
        self.assertEqual(event1.particles, [(1, 2.0, 3.0)])
        self.assertEqual(event1.energy, 4.0)

    def test_merge_collision_events(self):
        event1 = event.create_collision_event(1, [(1, 2.0, 3.0)], 4.0)
        event2 = event.create_collision_event(2, [(5, 6.0, 7.0)], 8.0)
        merged_event = event.merge_collision_events(event1, event2)
        self.assertIsInstance(merged_event, event.CollisionEvent)
        self.assertEqual(merged_event.id, 1)
        self.assertEqual(len(merged_event.particles), 2)
        self.assertEqual(merged_event.energy, 12.0)

if __name__ == '__main__':
    unittest.main()
