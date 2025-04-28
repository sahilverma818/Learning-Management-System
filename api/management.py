import click
import uvicorn
import subprocess
import sys

@click.group()
def cli():
    pass

@cli.command()
def start():
    """ Start the FastAPI server """
    uvicorn.run(
        "src.core.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )

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
