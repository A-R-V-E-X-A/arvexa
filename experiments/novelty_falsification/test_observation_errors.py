import unittest

from observation_errors import (
    class_confusion,
    independent_missed_detections,
    persistent_missed_detections,
)


class ObservationErrorTests(unittest.TestCase):
    def setUp(self):
        # Repeated track IDs model candidate detections over consecutive frames.
        self.records = [
            {"vehicle_id": str(i % 20), "frame": i // 20,
             "vehicle_class": "car", "movement": "N"}
            for i in range(1000)
        ]

    def test_independent_is_seed_reproducible(self):
        a = independent_missed_detections(self.records, 0.25, 42)
        b = independent_missed_detections(self.records, 0.25, 42)
        self.assertEqual(a, b)
        self.assertLess(len(a), len(self.records))

    def test_zero_and_full_error_rates(self):
        self.assertEqual(independent_missed_detections(self.records, 0, 7), self.records)
        self.assertEqual(persistent_missed_detections(self.records, 0, 0.8, 7), self.records)
        self.assertEqual(persistent_missed_detections(self.records, 1, 0.8, 7), [])

    def test_confusion_preserves_object_count(self):
        matrix = {"car": {"car": 0.7, "bus": 0.3}}
        result = class_confusion(self.records, matrix, 11)
        self.assertEqual(len(result), len(self.records))
        self.assertTrue(any(r["vehicle_class"] == "bus" for r in result))

    def test_invalid_rates_rejected(self):
        with self.assertRaises(ValueError):
            independent_missed_detections(self.records, 1.1, 1)

    def test_invalid_persistent_configuration_rejected(self):
        with self.assertRaises(ValueError):
            persistent_missed_detections(self.records, 0.99, 0.0, 1)


if __name__ == "__main__":
    unittest.main()
