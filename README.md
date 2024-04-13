# Leetcode

A repository for my bumbling attempts at Leetcode problems in Python.

Setup on a mac:

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

To run tests with pytest, run

```
pytest
```

in the root directory. Or use e.g.

```
pytest tests/test_dynamic_programming.py -k 'test_climb_stairs'
```

to test a specific problem.