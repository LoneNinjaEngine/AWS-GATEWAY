# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest

from keyspace import KeyspaceWrapper
from scenario_get_started_keyspaces import KeyspaceScenario


@pytest.fixture
def mock_wait(monkeypatch):
    return


@pytest.mark.integ
def test_run_keyspace_scenario_integ(input_mocker, capsys):
    scenario = KeyspaceScenario(KeyspaceWrapper.from_client())

    input_mocker.mock_answers([
        'doc_example_test_keyspace',    # Create keyspace.
        'movietabletest',               # Create table.
        'y',                            # Ensure TLS cert.
        1,                              # Query table.
        '', 'y',                        # Update and restore table.
        'y',                            # Cleanup.
    ])

    scenario.run_scenario()

    capt = capsys.readouterr()
    assert "Thanks for watching!" in capt.out
