import click
import uvicorn
import subprocess
import sys

@click.group()
def cli():
    pass

@cli.command()
@click.option(
    "--env",
    default = 'local',
    show_default = True,
    help='Select the server environment (local/production)'
)
@click.option(
    "--host",
    default = "0.0.0.0",
    show_default=True,
    help = "Host to run the fastapi server"
)
@click.option(
    "--port",
    default = 8000,
    show_default = True,
    help = 'Port to run the server'
)
@click.option(
    "--workers",
    default = 4,
    show_default = True,
    help = "Number of gunicorn workers"
)
def start(env, host, port, workers):
    """ Start the FastAPI server """
    if env == 'local':
        uvicorn.run(
            "src.core.main:app",
            host=f"{host}",
            port=f"{port}",
            reload=True
        )
    else:
        command = [
            "gunicorn",
            "-w", f"{workers}",
            "-k", "uvicorn.workers.UvicornWorker",
            "-b", f"{host}:{port}",
            "src.core.main:app"
        ]
        subprocess.run(command)
    
    click.echo(click.style(f"====================================", fg="green"))
    click.echo(click.style(f"connected to {env} environment", fg="green"))
    click.echo(click.style(f"====================================", fg="green"))


@cli.command()
@click.option("-m", "--message", required=True, help="Migration message")
def makemigration(message):
    """Create a new Alembic migration."""
    try:
        subprocess.run(
            [
                "alembic",
                "revision",
                "--autogenerate",
                "-m",
                message
            ],
            check=True
        )
        click.echo(click.style("Migration created successfully!", fg="green"))
    except subprocess.CalledProcessError as e:
        click.echo(click.style(f"Error: Failed to create migration.\n{e}", fg="red"), err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(click.style(f"Unexpected error: {e}", fg="red"), err=True)
        sys.exit(1)


@cli.command()
def migrate():
    """ Applying migration"""
    subprocess.run(
        [
            "alembic",
            "upgrade",
            "head"
        ],
        check=True
    )

if __name__ == "__main__":
    cli()
