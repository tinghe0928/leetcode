import pytest
import pdb
@pytest.fixture(scope='module')
def print_line():
    print("this is fixture start !")
    yield
    print("this is fixture end !")



def test_2(print_line):
    print("----------------2")
    pass


@pytest.mark.testdemo
def test_demo01():
    print("函数级别的test_demo01")


@pytest.mark.smoke
def test_demo02():
    print("函数级别的test_demo02")


@pytest.mark.hello
class TestDemo:
    def test_demo01(self):
        # pdb.set_trace()
        print("test_demo01")

@pytest.mark.hello
def test_1(print_line):
    print("----------------1")
    pass