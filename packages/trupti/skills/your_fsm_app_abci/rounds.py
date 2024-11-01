# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2024 Valory AG
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""This package contains the rounds of HelloWorldAbciApp."""

from enum import Enum
from typing import Dict, FrozenSet, List, Optional, Set, Tuple

from packages.valory.skills.abstract_round_abci.base import (
    AbciApp,
    AbciAppTransitionFunction,
    AbstractRound,
    AppState,
    BaseSynchronizedData,
    DegenerateRound,
    EventToTimeout,
)

from packages.trupti.skills.your_fsm_app_abci.payloads import (
    CollectRandomnessPayload,
    PrintMessagePayload,
    RegistrationPayload,
    ResetAndPausePayload,
    SelectKeeperPayload,
)


class Event(Enum):
    """HelloWorldAbciApp Events"""

    RESET_TIMEOUT = "reset_timeout"
    NO_MAJORITY = "no_majority"
    NONE = "none"
    DONE = "done"
    ROUND_TIMEOUT = "round_timeout"


class SynchronizedData(BaseSynchronizedData):
    """
    Class to represent the synchronized data.

    This data is replicated by the tendermint application.
    """


class CollectRandomnessRound(AbstractRound):
    """CollectRandomnessRound"""

    payload_class = CollectRandomnessPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        raise NotImplementedError

    def check_payload(self, payload: CollectRandomnessPayload) -> None:
        """Check payload."""
        raise NotImplementedError

    def process_payload(self, payload: CollectRandomnessPayload) -> None:
        """Process payload."""
        raise NotImplementedError


class PrintMessageRound(AbstractRound):
    """PrintMessageRound"""

    payload_class = PrintMessagePayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        raise NotImplementedError

    def check_payload(self, payload: PrintMessagePayload) -> None:
        """Check payload."""
        raise NotImplementedError

    def process_payload(self, payload: PrintMessagePayload) -> None:
        """Process payload."""
        raise NotImplementedError


class RegistrationRound(AbstractRound):
    """RegistrationRound"""

    payload_class = RegistrationPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        raise NotImplementedError

    def check_payload(self, payload: RegistrationPayload) -> None:
        """Check payload."""
        raise NotImplementedError

    def process_payload(self, payload: RegistrationPayload) -> None:
        """Process payload."""
        raise NotImplementedError


class ResetAndPauseRound(AbstractRound):
    """ResetAndPauseRound"""

    payload_class = ResetAndPausePayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        raise NotImplementedError

    def check_payload(self, payload: ResetAndPausePayload) -> None:
        """Check payload."""
        raise NotImplementedError

    def process_payload(self, payload: ResetAndPausePayload) -> None:
        """Process payload."""
        raise NotImplementedError


class SelectKeeperRound(AbstractRound):
    """SelectKeeperRound"""

    payload_class = SelectKeeperPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        raise NotImplementedError

    def check_payload(self, payload: SelectKeeperPayload) -> None:
        """Check payload."""
        raise NotImplementedError

    def process_payload(self, payload: SelectKeeperPayload) -> None:
        """Process payload."""
        raise NotImplementedError


class HelloWorldAbciApp(AbciApp[Event]):
    """HelloWorldAbciApp"""

    initial_round_cls: AppState = RegistrationRound
    initial_states: Set[AppState] = {RegistrationRound}
    transition_function: AbciAppTransitionFunction = {
        CollectRandomnessRound: {
            Event.DONE: SelectKeeperRound,
            Event.NONE: CollectRandomnessRound,
            Event.NO_MAJORITY: CollectRandomnessRound,
            Event.ROUND_TIMEOUT: CollectRandomnessRound
        },
        PrintMessageRound: {
            Event.DONE: ResetAndPauseRound,
            Event.ROUND_TIMEOUT: RegistrationRound
        },
        RegistrationRound: {
            Event.DONE: CollectRandomnessRound
        },
        ResetAndPauseRound: {
            Event.DONE: CollectRandomnessRound,
            Event.NO_MAJORITY: RegistrationRound,
            Event.RESET_TIMEOUT: RegistrationRound
        },
        SelectKeeperRound: {
            Event.DONE: PrintMessageRound,
            Event.NONE: RegistrationRound,
            Event.NO_MAJORITY: RegistrationRound,
            Event.ROUND_TIMEOUT: RegistrationRound
        }
    }
    final_states: Set[AppState] = set()
    event_to_timeout: EventToTimeout = {}
    cross_period_persisted_keys: FrozenSet[str] = frozenset()
    db_pre_conditions: Dict[AppState, Set[str]] = {
        RegistrationRound: [],
    }
    db_post_conditions: Dict[AppState, Set[str]] = {

    }
