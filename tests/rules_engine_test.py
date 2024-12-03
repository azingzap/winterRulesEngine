import pytest
'''
This file includes all the unit tests that get run against the rules engine function
'''
from RulesEngine.rules_engine import rulesEngine

def test_rulesEngine_single_no_children():
    """Test rulesEngine for correct supplement amounts in the case of a single person with no children."""
    familyComposition = "single"
    numberOfChildren = 0

    expectedBaseAmountValue = 60
    expectedChildrenAmountValue = 0
    expectedSupplementAmountValue = 60

    baseAmountValue, childrenAmountValue, supplementAmountValue = rulesEngine(familyComposition, numberOfChildren)

    assert baseAmountValue == expectedBaseAmountValue
    assert childrenAmountValue == expectedChildrenAmountValue
    assert supplementAmountValue == expectedSupplementAmountValue

def test_rulesEngine_couple_no_children():
    """Test rulesEngine for correct supplement amounts in the case of a couple with no children."""
    familyComposition = "couple"
    numberOfChildren = 0

    expectedBaseAmountValue = 120
    expectedChildrenAmountValue = 0
    expectedSupplementAmountValue = 120

    baseAmountValue, childrenAmountValue, supplementAmountValue = rulesEngine(familyComposition, numberOfChildren)

    assert baseAmountValue == expectedBaseAmountValue
    assert childrenAmountValue == expectedChildrenAmountValue
    assert supplementAmountValue == expectedSupplementAmountValue

def test_rulesEngine_couple_three_children():
    """Test rulesEngine for correct supplement amounts in the case of a couple with three children."""
    familyComposition = "couple"
    numberOfChildren = 3

    expectedBaseAmountValue = 120
    expectedChildrenAmountValue = 60
    expectedSupplementAmountValue = 180

    baseAmountValue, childrenAmountValue, supplementAmountValue = rulesEngine(familyComposition, numberOfChildren)

    assert baseAmountValue == expectedBaseAmountValue
    assert childrenAmountValue == expectedChildrenAmountValue
    assert supplementAmountValue == expectedSupplementAmountValue

def test_rulesEngine_single_3_children():
    """Test rulesEngine for correct supplement amounts in the case of a single person with three children."""
    familyComposition = "single"
    numberOfChildren = 3

    expectedBaseAmountValue = 120
    expectedChildrenAmountValue = 60
    expectedSupplementAmountValue = 180

    baseAmountValue, childrenAmountValue, supplementAmountValue = rulesEngine(familyComposition, numberOfChildren)

    assert baseAmountValue == expectedBaseAmountValue
    assert childrenAmountValue == expectedChildrenAmountValue
    assert supplementAmountValue == expectedSupplementAmountValue

def test_rulesEngine_negative_numberOfChildren():
    """Test rulesEngine for correct exception message in the case that a negative numberOfChildren is given ."""
    familyComposition = "single"
    numberOfChildren = -5
    with pytest.raises(Exception) as e:
        rulesEngine(familyComposition, numberOfChildren)

    assert str(e.value) == "You can't have a negative amount of kids"

def test_rulesEngine_inacurate_familyComposition():
    """Test rulesEngine for correct exception message in the case that inaccurate familyComposition is given ."""
    familyComposition = "singlelady"
    numberOfChildren = 5
    with pytest.raises(Exception) as e:
        rulesEngine(familyComposition, numberOfChildren)
    assert str(e.value) == "Your family composition must be 'single' or 'couple'"

def test_rulesEngine_char_numberOfChildren():
    """Test rulesEngine for correct exception if a char value is entered"""
    familyComposition = "single"
    numberOfChildren = "a"
    with pytest.raises(Exception) as e:
        rulesEngine(familyComposition, numberOfChildren)
    assert str(e.value)