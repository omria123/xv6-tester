from pytest import fixture

BRANCHES = ['util', 'pgtbl', 'traps', 'lazy', 'cow', 'thread', 'lock', 'fs', 'mmap', 'networking']

'''
This is meant to be use in order to micro testing BRANCHES specific exercises.
That way we can also make students do only specific exercise instead of the entire exercise.
Still in development.

EXERCISES_TO_TESTS = {
    'sleep': ('util', 'sleep'),
    'pingpong': 'util',
    'trace': '',
    'pte': 'pgtbl',
    'kvm': 'pgtbl',
    'backtrace': 'traps',
    'alarm': 'traps',
    'lazy': 'all',
    'cow': 'all',
    'thread': [],
    'lock': [],
    'fs': [],
    'mmap': [],
    'networking': []
}
EXERCISES_TO_BRANCHES = {
    'sleep': 'util',
    'pingpong': 'util',
    'trace': 'syscall',
    'pte': 'pgtbl',
    'kvm': 'pgtbl',
    'backtrace': 'traps',
    'alarm': 'traps',
    'lazy': 'lazy',
    'cow': 'cow',
    'uthread': 'thread',
    'barrier': ''
    'lock': [],
    'fs': [],
    'mmap': [],
    'networking': []
}
    
@fixture()
def exercise(request):
    ex = request.config.getoption('--exercise')
    assert ex is not None, 'Must provide exercise'
    assert ex in EXERCISES_TO_TESTS, 'Unknown exercise'
    return EXERCISES_TO_TESTS[ex]
'''


def pytest_addoption(parser):
    parser.addoption(
        "--repo-url",
        action="store"
    )
    parser.addoption(
        "--branch",
        action="store",

    )
    '''
    parser.addoption(
        "--exercise",
        action="store",

    )
    '''


@fixture()
def repo_url(request):
    url = request.config.getoption("--repo-url")
    assert url is not None, 'Must provide repo-url'
    return url


@fixture()
def branch(request):
    br = request.config.getoption("--branch")
    assert br in BRANCHES, 'Must provide a valid branch'
    return br
