import numpy as np
import pytest

from playground.validation.zip_zarr_validator.src.ZipZarrValidator import ZipZarrValidator


test_ids = [
    'created',
    '6001240'
]
test_params = [
    {'uri': 'test.ozx', 'data': np.random.rand(100, 100), 'dim_order': 'yx', 'pixel_size': {'x': 1, 'y': 1}},
    {'uri': 'C:/Project/slides/ozx/6001240.ozx'}
]

@pytest.fixture()
def uri(request):
    return request.config.getoption('--uri')


class TestZipZarr:
    # no __init__ for pytest!

    @pytest.fixture(autouse=True, scope="class", ids=test_ids, params=test_params)
    @classmethod
    def setup_and_teardown(self, request) -> None:
        self.validator = ZipZarrValidator(**request.param)
        yield
        #self.validator.cleanup()

    def test_requirement12(self):
        self.validator.test_requirement12()

    def test_requirement3(self):
        self.validator.test_requirement3()

    def test_requirement4(self):
        self.validator.test_requirement4()

    def test_recommendation1(self):
        self.validator.test_recommendation1()

    def test_recommendation2(self):
        self.validator.test_recommendation2()

    def test_recommendation3(self):
        self.validator.test_recommendation3()

    def test_recommendation4(self):
        self.validator.test_recommendation4()

    def test_recommendation5(self):
        self.validator.test_recommendation5()

    def test_recommendation6(self):
        self.validator.test_recommendation6()


if __name__ == "__main__":
    uri = 'C:/Project/slides/ozx/6001240.ozx'
    validator = ZipZarrValidator(uri)

    validator.test_requirement12()
    validator.test_requirement3()
    validator.test_requirement4()

    validator.test_recommendation1()
    validator.test_recommendation2()
    validator.test_recommendation3()
    validator.test_recommendation4()
    validator.test_recommendation5()
    validator.test_recommendation6()
