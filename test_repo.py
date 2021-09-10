import os
import subprocess as sp

import git
import pytest


@pytest.fixture()
def repo(repo_url, tmp_path):
    git.Repo.clone_from(repo_url, tmp_path / 'clone')
    repo = git.Repo(tmp_path / 'clone')
    if repo.bare:
        raise ValueError(f'Couldn\'t load repo at {tmp_path / "clone"}')
    return repo


@pytest.fixture()
def br_repo(repo, branch):
    repo.git.checkout(branch)
    return repo


def test_br_repo(br_repo, exercise):
    os.chdir(br_repo.working_tree_dir)
    result = sp.run(['make', f'GRADEFLAGS={exercise}', 'grade'])
    assert result.returncode == 0
