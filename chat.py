# -*- coding: utf-8 -*-
#
# MLHub toolkit for Ollama - Chat
#
# Time-stamp: <Thursday 2024-12-19 09:10:10 +1100 Graham Williams>
#
# Author: Graham.Williams@togaware.com
# Licensed under GPLv3.
# Copyright (c) Togaware Pty Ltd. All rights reserved.
#
# ml chat ollama <prompt>

# ----------------------------------------------------------------------
# Setup.
# ----------------------------------------------------------------------

import click
from ollama import chat
from ollama import ChatResponse

# -----------------------------------------------------------------------
# Command line argument and options.
# -----------------------------------------------------------------------

@click.command()
@click.argument("prompt",
                default="Why is the ocean blue?",
                required=False,
                type=str)

# -----------------------------------------------------------------------
# Perform the request.
# -----------------------------------------------------------------------

def cli(prompt):
    """Process the prompt."""

    print(prompt)
    response: ChatResponse = chat(model='llama3.2', messages=[
      {
        'role': 'user',
        'content': prompt,
      },
    ])

    print(response.message.content)

    print("")

if __name__ == '__main__':
    cli()
