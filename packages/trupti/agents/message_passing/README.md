The agent should support these
operations and characteristics:
● Continuously consume messages (of different types) from an InBox.
● Emit messages to an OutBox.
● Allow for registration of message handlers to process different message types.
This implements the reactive part of the agent (if a message of type X is received
on the InBox, then action Y is executed by the corresponding handler).
● Allow for registration of behaviors. This implements the proactive part of the
agent (if the internal state or local time satisfies some condition, then a certain
message is created in the OutBox).