## sum_columns_of_list.py

Write a script that takes each column of an array/list/tuple and adds it to the corresponding column of another array/list/tuple and returns the result as an array/list/tuple. Consider these asserts for perhaps a better explanation of the goal:

```python3
assert [6, 5, 2] == sum_columnns([2, 5, 7], [3, 9, 5])
assert [1, 9, 9, 8] == sum_columns([9, 9, 9], [9, 9, 9])
```

## Running Tests

```bash
(py3) rriehle@ontario:~/src/coding-challenge (master)$ pytest -vv *.py
============================= test session starts ==============================
platform darwin -- Python 3.7.3, pytest-4.4.1, py-1.8.0, pluggy-0.9.0 -- 
/Users/brew/.virtualenvs/py3/bin/python3.7
cachedir: .pytest_cache
rootdir: /Users/rriehle/src/coding-challenge
collected 2 items

sum_columns_of_list.py::test_sum_as_tuple PASSED                         [ 50%]
sum_columns_of_list.py::test_solutions PASSED                            [100%]

=========================== 2 passed in 0.01 seconds ===========================
```

