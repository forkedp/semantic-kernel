# Copyright (c) Microsoft. All rights reserved.

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, AsyncGenerator, List, Optional, Union

if TYPE_CHECKING:
    from semantic_kernel.connectors.ai.chat_request_settings import ChatRequestSettings
    from semantic_kernel.models.chat.chat_message import ChatMessage


class ChatCompletionClientBase(ABC):
    @abstractmethod
    async def complete_chat_async(
        self,
        messages: List["ChatMessage"],
        settings: "ChatRequestSettings",
        logger: Optional[Any] = None,
    ) -> Union[str, List[str]]:
        """
        This is the method that is called from the kernel to get a response from a chat-optimized LLM.

        Arguments:
            messages {List[ChatMessage]} -- A list of chat messages, that can be rendered into a
                set of messages, from system, user, assistant and function.
            settings {ChatRequestSettings} -- Settings for the request.
            logger {Logger} -- A logger to use for logging. (Deprecated)

        Returns:
            Union[str, List[str]] -- A string or list of strings representing the response(s) from the LLM.
        """
        pass

    @abstractmethod
    async def complete_chat_stream_async(
        self,
        messages: List["ChatMessage"],
        settings: "ChatRequestSettings",
        logger: Optional[Any] = None,
    ) -> AsyncGenerator[Union[str, List[str]], None]:
        """
        This is the method that is called from the kernel to get a stream response from a chat-optimized LLM.

        Arguments:
            messages {List[ChatMessage]} -- A list of chat messages, that can be rendered into a
                set of messages, from system, user, assistant and function.
            settings {ChatRequestSettings} -- Settings for the request.
            logger {Logger} -- A logger to use for logging. (Deprecated)

        Yields:
            A stream representing the response(s) from the LLM.
        """
        pass
