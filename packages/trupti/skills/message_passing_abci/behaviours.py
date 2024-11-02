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

"""This package contains round behaviours of HelloWorldAbciApp."""

from abc import ABC
from typing import Generator, Set, Type, cast

from packages.trupti.skills.your_fsm_app_abci.payloads import ReceiveMessagePayload, SendMessagePayload
from packages.valory.skills.abstract_round_abci.base import AbstractRound
from packages.valory.skills.abstract_round_abci.behaviours import (
    AbstractRoundBehaviour,
    BaseBehaviour,
)

from packages.trupti.skills.your_fsm_app_abci.models import Params
from packages.trupti.skills.your_fsm_app_abci.rounds import (
    SynchronizedData,
    HelloWorldAbciApp,
    CollectRandomnessRound,
    PrintMessageRound,
    RegistrationRound,
    ResetAndPauseRound,
    SelectKeeperRound,
)
from packages.trupti.skills.your_fsm_app_abci.rounds import (
    PrintMessagePayload,
    RegistrationPayload,
    ResetAndPausePayload,
    SelectKeeperPayload,
)


class HelloWorldBaseBehaviour(BaseBehaviour, ABC):
    """Base behaviour for the your_fsm_app_abci skill."""

    @property
    def synchronized_data(self) -> SynchronizedData:
        """Return the synchronized data."""
        return cast(SynchronizedData, super().synchronized_data)

    @property
    def params(self) -> Params:
        """Return the params."""
        return cast(Params, super().params)


class ReceiveMessageBehaviour(HelloWorldBaseBehaviour):
    """ReceiveMessageBehaviour"""

    matching_round: Type[AbstractRound] = CollectRandomnessRound   #........................

    def async_act(self, message) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            instance = ReceiveMessagePayload(sender=sender, content=message)
            payload = instance.encode_payload_to_hex()

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class PrintMessageBehaviour(HelloWorldBaseBehaviour):
    """PrintMessageBehaviour"""

    matching_round: Type[AbstractRound] = PrintMessageRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self, payload) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            # sender = self.context.agent_address
            instance = PrintMessagePayload(content=payload)
            instance.decode_payload_from_hex()

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class RegistrationBehaviour(HelloWorldBaseBehaviour):
    """RegistrationBehaviour"""

    matching_round: Type[AbstractRound] = RegistrationRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = RegistrationPayload(sender=sender, content=...)

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()

class SendMessageBehaviour(HelloWorldBaseBehaviour):
    """SendMessageBehaviour"""

    # matching_round: Type[AbstractRound] = RegistrationRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self, message) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = SendMessagePayload(sender=sender, content=message)

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()

class ResetAndPauseBehaviour(HelloWorldBaseBehaviour):
    """ResetAndPauseBehaviour"""

    matching_round: Type[AbstractRound] = ResetAndPauseRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self, message) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = ResetAndPausePayload(sender=sender, content=message)

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class SelectKeeperBehaviour(HelloWorldBaseBehaviour):
    """SelectKeeperBehaviour"""

    matching_round: Type[AbstractRound] = SelectKeeperRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self, message) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = SelectKeeperPayload(sender=sender, content=message)

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class HelloWorldRoundBehaviour(AbstractRoundBehaviour):
    """HelloWorldRoundBehaviour"""

    initial_behaviour_cls = RegistrationBehaviour
    abci_app_cls = HelloWorldAbciApp  # type: ignore
    behaviours: Set[Type[BaseBehaviour]] = [
        ReceiveMessageBehaviour,
        PrintMessageBehaviour,
        RegistrationBehaviour,
        ResetAndPauseBehaviour,
        SelectKeeperBehaviour
    ]
