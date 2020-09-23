#!/usr/bin/python
"""Simple Hyperion client request demonstration."""

import asyncio
from hyperion import client

HOST = "hyperion"


async def print_if_auth_required():
    """Print whether auth is required."""

    hc = client.HyperionClient(HOST)
    await hc.async_client_connect()

    result = await hc.async_is_auth_required()
    print("Result: %s" % result)


asyncio.get_event_loop().run_until_complete(print_if_auth_required())
