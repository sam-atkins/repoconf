import click


@click.command()
@click.option("-n", "--name")
def main(name):
    print(f"Hello {name}")
