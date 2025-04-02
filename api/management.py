import click
import uvicorn
import subprocess

@click.group()
def cli():
    pass

@cli.command()
def start():
    """ Start the FastAPI server """
    uvicorn.run("src.core.main:app", host="0.0.0.0", port=8000, reload=True)

@cli.command()
@click.argument("message", required=True)
def makemigration(message):
    """ create a new alembic migration """
    subprocess.run(["alembic", "revision", "--autogenerate", "-m", message], check=True)

@cli.command()
def migrate():
    """ Applying migration"""
    subprocess.run(["alembic", "upgrade", "head"], check=True)

if __name__ == "__main__":
    cli()
