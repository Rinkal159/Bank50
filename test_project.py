from CS50P.CS50P_Problems.Week_9_Final_Project.project import hash_PIN, withdraw, deposit

def test_hash_PIN():
    assert hash_PIN(1234) == hash_PIN(1234)
    assert hash_PIN(0000) == hash_PIN(0000)
    assert hash_PIN(9999) == hash_PIN(9999)
    
def test_withdraw():
    assert withdraw("1000", 500) == 500
    assert withdraw("1000", 1000) == 0
    
def test_deposit():
    assert deposit("1000", 500) == 1500
    assert deposit("1000", 1000) == 2000