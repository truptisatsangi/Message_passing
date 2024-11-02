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

"""This module contains the transaction payloads of the HelloWorldAbciApp."""

from dataclasses import dataclass

from packages.valory.skills.abstract_round_abci.base import BaseTxPayload

@dataclass(frozen=True)
class PrintMessagePayload(BaseTxPayload):
    """Represent a transaction payload for the PrintMessageRound."""
    encoded_payload: str
    @staticmethod
    def decode_payload_from_hex(self) -> tuple:
        """Decode a hex-encoded payload back to sender and content strings."""
        decoded = bytes.fromhex(self.encoded_payload).decode("utf-8")
        sender, content = decoded.split(":", 1)  # Split only on the first colon
        print("sender: ", sender, " message: ", content)
        return sender, content


@dataclass(frozen=True)
class RegistrationPayload(BaseTxPayload):
    """Represent a transaction payload for the RegistrationRound."""

    # TODO: define your attributes


@dataclass(frozen=True)
class ResetAndPausePayload(BaseTxPayload):
    """Represent a transaction payload for the ResetAndPauseRound."""

    # TODO: define your attributes


@dataclass(frozen=True)
class SelectKeeperPayload(BaseTxPayload):
    """Represent a transaction payload for the SelectKeeperRound."""

    # TODO: define your attributes

@dataclass(frozen=True)
class ReceiveMessagePayload(BaseTxPayload):
    """Represents a transaction payload for the ReceiveMessage."""
    sender: str
    content: str
    def encode_payload_to_hex(self) -> str:
        """Encode both sender and content to UTF-8 and convert to hex format."""
        message = f"{self.sender}:{self.content}"
        return message.encode("utf-8").hex()
    
@dataclass(frozen=True)
class SendMessagePayload(BaseTxPayload):
    """Represents a transaction payload for the ReceiveMessage."""
    sender: str
    content: str
    def encode_payload_to_hex(self) -> str:
        """Encode both sender and content to UTF-8 and convert to hex format."""
        message = f"{self.sender}:{self.content}"
        return message.encode("utf-8").hex()