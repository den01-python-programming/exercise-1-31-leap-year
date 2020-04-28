import pytest
import src.exercise

def test_exercise():
    input_values = ["2016","2010","1200"]
    input_values_stored = ["2016","2010","1200"]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert [output[0],output[1]] == ["Give a year:","The year is a leap year."]
    assert [output[2],output[3]] == ["Give a year:","The year is not a leap year."]
    assert [output[4],output[5]] == ["Give a year:","The year is not a leap year."]
