#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""

from argo import argo

def validate_profile(p):
    pass

def test_extract_1_profile():
    p = argo.extract_profile('test_data/D20150316_prof.nc', 0)
    assert len(p) == 1
    validate_profile(p)

def test_extract_list_profiles():
    p = argo.extract_profile('test_data/D20150316_prof.nc', [0, 2, 5])
    assert len(p) == 3
    validate_profile(p)

def test_extract_all_profiles():
    p = argo.extract_profile('test_data/D20150316_prof.nc')
    assert len(p) > 1
    validate_profile(p)
