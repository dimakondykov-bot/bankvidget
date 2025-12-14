from src.log import log


def test_log_success(capsys):
    @log()
    def add(a, b):
        return a + b

    result = add(2, 3)
    assert result == 5
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()
    assert len(lines) == 2
    assert "вызвана" in lines[0]
    assert "завершилась 5" in lines[1]


def test_log_exception_simple(capsys):
    @log()
    def call_error():
        raise ValueError("ошибка!")

    try:
        call_error()
    except ValueError as e:
        assert str(e) == "ошибка!"

    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()
    assert len(lines) == 2
    assert "вызвана" in lines[0]
    assert "ошибка" in lines[1]
    assert "ValueError" in lines[1]
