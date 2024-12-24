import pytest


def greet(greet):
  return f'{greet} Rahul'


class Test_class0:
  def test_case0(self):
    assert greet('Hi') == 'Hi Rahul'

  def test_case1(self):
    assert greet('Namaste') == 'Namaste Rahul'

  def test_case2(self):
    assert greet('Hi') == 'Hi Rahul'


class Test_class1:
  def test_case1(self):
    assert greet('Hello') == 'Hello Rahul'

  def test_case2(self):
    assert greet('Hey') == 'Hey Rahul'
