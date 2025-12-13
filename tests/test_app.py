import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add
from app import subtraction
from app import multiplication
from app import division
from app import square
from app import log
from app import sine
from app import cosine
from app import square_root
from app import percentage

def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10

def test_add3():
    assert add(5, 10) == 15

def test_subtract():
    assert subtraction(6, 5) == 1

def test_subtract2():
    assert subtraction(10, 4) != 5

def test_subtract3():
    assert subtraction(10, 4) == 6

def test_multiply():
    assert multiplication(5, 6) == 30

def test_multiply2():
    assert multiplication(5, 6) != 25

def test_divide():
    assert division(6, 3) == 2

def test_divide2():
    assert division(4, 2) != 7

def test_square():
    assert square(2) == 4

def test_square2():
    assert square(3) != 8

def test_log():
    assert log(1) == 0

def test_log2():
    assert log(1) != 1

def test_sin():
    assert sine(90) == 1

def test_sin2():
    assert sine(90) != 2

def test_cos():
    assert abs(cosine(90)) < 1e-9

def test_cos2():
    assert cosine(90) != 1

def test_square_root():
    assert square_root(4) == 2

def test_square_root2():
    assert square_root(4) != 3

def test_percentage():
    assert percentage(5, 10) == 50

def test_percentage2():
    assert percentage(6, 10) != 50
