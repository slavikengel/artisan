import click
from artisan.contexts.model_context import ModelContext

HELP_TEXT = """
    Create a new model resource, with default context.
"""


@click.command(
    help=HELP_TEXT
)
@click.option(
    "--name",
    "-n",
    "resource_name",
    required=True,
    prompt="Step 2. Model name"
)
@click.pass_context
def cli(
    ctx,
    resource_name
):
    do_cli(
        resource_name,
        ctx.obj['relative_path'],
    )


def do_cli(
    resource_name,
    relative_path,
):
    with ModelContext(
        resource_name,
        relative_path=relative_path
    ) as context:
        try:
            context.execute()
        except Exception as e:
            raise e
        else:
            print(f"Success! {context.TYPE.capitalize()} created!")
