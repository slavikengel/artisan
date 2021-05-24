import click
from artisan.commands.lamda_command import cli as lambda_function
from artisan.commands.job_command import cli as job
from artisan.commands.model_command import cli as model
from artisan.commands.queue_command import cli as queue

HELP_TEXT = """
    Artisan is the command line interface.
    Artisan exists at the root of your application as the artisan script and provides a number of helpful
     commands that can assist you while you build your application. 
"""


@click.group(help=HELP_TEXT)
@click.pass_context
def cli(ctx):
    """
    Entry point for command-line app
    """

    ctx.ensure_object(dict)
    ctx.obj['relative_path'] = click.prompt('Step 1. Set relative file path', default='/')


cli.add_command(lambda_function, 'lambda')
cli.add_command(job, 'job')
cli.add_command(model, 'model')
cli.add_command(queue, 'queue')


# TODO DONE:
# TODO MAIN - add imports common, app, Request for handlers - DONE, set default template for handlers.


# TODO MAIN - remove spec symbols from name
# TODO MAIN - add name attribute as required
# TODO MAIN - add normalize file name, only underscore name, except "Model" command type
# TODO - add template files where will be describe text's for feature template.yaml
# TODO - add param for all commands --path for change template store path
# TODO MAYBE - add --name param for group and pass context for all command
