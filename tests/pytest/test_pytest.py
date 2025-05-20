def test_first_try():
    print("Hello, world!")

def test_assert_positive_case():
    assert 1 == 1

def test_assert_negative_case():
    assert 1 == 2

def test_test(function_file):
    print(function_file.response)

def test_test_2(function_exercise):
    print(function_exercise.response.model_dump_json())
