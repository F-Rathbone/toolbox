# -*- coding: UTF-8 -*-

# Import from standard library
import os
import toolbox
import pandas as pd
# Import from our lib
from toolbox.lib import clean_data
import pytest


def test_clean_data():
    datapath = os.path.dirname(os.path.abspath(toolbox.__file__)) + '/data'
    df = pd.read_csv('{}/data.csv.gz'.format(datapath))
    first_cols = ['id', 'civility', 'birthdate', 'city', 'postal_code', 'vote_1']
    assert list(df.columns)[:6] == first_cols
    assert df.shape == (999, 142)
    out = clean_data(df)
    assert out.shape == (985, 119)

def test_fizzbuzz():
    assert fizzbuzz(51) == fizz buzz
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizz buzz
16
17
fizz
19
buzz
fizz
22
23
fizz
buzz
26
fizz
28
29
fizz buzz
31
32
fizz
34
buzz
fizz
37
38
fizz
buzz
41
fizz
43
44
fizz buzz
46
47
fizz
49
buzz


