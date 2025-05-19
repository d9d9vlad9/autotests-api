import random
import pytest


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_reruns():
    """
    Test that fails randomly to demonstrate reruns.
    """
    assert random.choice([True, False])


@pytest.mark.flaky(reruns=3, reruns_delay=2)
class TestReruns:
    def test_rerun_class(self):
        """
        Test that fails randomly to demonstrate reruns in a class.
        """
        assert random.choice([True, False])

    def test_rerun_class_2(self):
        assert random.choice([True, False])

@pytest.mark.flaky(reruns=3, reruns_delay=2, condition=lambda: random.choice([True, False]))
def test_rerun_with_condition():
    assert random.choice([True, False])