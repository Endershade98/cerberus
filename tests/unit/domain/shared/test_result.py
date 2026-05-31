# tests/unit/domain/shared/test_result.py

from domain.shared.result import Result


def test_ok():
    r = Result.ok(10)
    assert r.is_ok()
    assert r.value == 10


def test_fail():
    r = Result.fail("error")
    assert r.is_fail()
    assert r.error == "error"