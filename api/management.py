import click
import uvicorn

@click.group()
def cli():
    pass

@cli.command()
def start():
    "Start the FastAPI server"
    uvicorn.run("src.core.main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    cli()
