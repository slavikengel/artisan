import click
from artisan.contexts.job_context import JobContext


HELP_TEXT = """
    Create a new job resource, with default context.
"""


@click.command(
    help=HELP_TEXT,
)
@click.option(
    "--name",
    "-n",
    "resource_name",
    required=True,
    prompt="Step 2. Job name"
)
@click.option(
    "--period",
    "-p",
    "period",
    help='Sets the interval for running job',
    default='10',
    show_default=True,
    prompt="Step 3. Job schedule"
)
@click.pass_context
def cli(
    ctx,
    resource_name,
    period,
):
    do_cli(
        resource_name,
        ctx.obj['relative_path'],
        period,
    )


def do_cli(
    resource_name,
    relative_path,
    period
):
    with JobContext(
        resource_name,
        relative_path=relative_path,
        period=period
    ) as context:
        try:
            context.execute()
        except Exception as e:
            raise e
        else:
            print(f"Success! {context.TYPE.capitalize()} created!")

