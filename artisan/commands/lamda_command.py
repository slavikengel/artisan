import click
from artisan.contexts.lambda_context import LambdaContext

HELP_TEXT = """
    Create a new lambda resource, with default context.
"""


@click.command(
    help=HELP_TEXT
)
@click.option(
    "--name",
    "-n",
    "resource_name",
    required=True,
    prompt="Step 2. Lambda name"
)
@click.option(
    "--url",
    "-u",
    "url",
    help="Sets the endpoint path",
    default="/",
    show_default=True,
    prompt='Step 3. Lambda url path'
)
@click.option(
    "--http_method",
    "-hm",
    "http_method",
    help="Sets the http method of request",
    default="GET",
    show_default=True,
    prompt='Step 4. Http request method'
)
@click.pass_context
def cli(
    ctx,
    resource_name,
    url,
    http_method,
):
    do_cli(
        resource_name,
        ctx.obj['relative_path'],
        url,
        http_method,
    )


def do_cli(
    resource_name,
    relative_path,
    url,
    http_method,
):
    with LambdaContext(
        resource_name,
        relative_path=relative_path,
        url=url,
        http_method=http_method,
    ) as context:
        try:
            context.execute()
        except Exception as e:
            raise e
        else:
            print(f"Success! {context.TYPE.capitalize()} created!")
