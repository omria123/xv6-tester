from pytest import fixture

AVAILABLE_BRANCHES = [
    'cow',
    'fs',
    'lazy',
    'lock',
    'mmap',
    'net',
    'pgtbl',
    'riscv',
    'syscall',
    'thread',
    'traps',
    'util',
]


def pytest_addoption(parser):
    parser.addoption(
        "--repo-url",
        action="store"
    )
    parser.addoption(
        "--branch",
        action="store"
    )

    parser.addoption(
        "--exercise",
        action="store"
    )


@fixture()
def repo_url(request):
    url = request.config.getoption("--repo-url")
    assert url is not None, 'Must provide repo-url'
    return url


@fixture()
def branch(request):
    br = request.config.getoption('--branch')
    assert br is not None, 'Must provide branch'
    assert br in AVAILABLE_BRANCHES, f'{br} is not an available branch'
    return br


@fixture()
def exercise(request):
    ex = request.config.getoption('--exercise')
    assert ex is not None, 'Must provide exercise'
    return ex
