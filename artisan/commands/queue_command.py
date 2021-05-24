import click
from artisan.contexts.queue_context import QueueContext

HELP_TEXT = """
    Create a new queue resource, with default context.
"""


@click.command(
    help=HELP_TEXT
)
@click.option(
    "--name",
    "-n",
    "resource_name",
    required=True,
    prompt="Step 2. Queue name"
)
@click.pass_context
def cli(
    ctx,
    resource_name,
):
    do_cli(
        resource_name,
        ctx.obj['relative_path']
    )


def do_cli(
    resource_name,
    relative_path
):
    with QueueContext(
        resource_name,
        relative_path=relative_path
    ) as context:
        try:
            context.execute()
        except Exception as e:
            raise e
        else:
            print(f"Success! {context.TYPE.capitalize()} created!")
