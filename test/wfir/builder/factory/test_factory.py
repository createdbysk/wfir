import wfir.builder.factory


def test_create_task(mocker):
    # GIVEN
    kwargs = dict(
        type="task_type",
        property1="property1"
    )

    mock_task = mocker.patch("wfir.builder.factory.task.Task", auto_spec=True)

    expected_result = mock_task.return_value

    # WHEN
    actual_result = wfir.builder.factory.create_task(**kwargs)

    # THEN
    mock_task.assert_called_with(**kwargs)
    assert expected_result == actual_result
