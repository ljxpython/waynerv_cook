"""Console script for waynerv_cook."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("waynerv_cook")
    click.echo("=" * len("waynerv_cook"))
    click.echo("学习waynerv的cook")


if __name__ == "__main__":
    main()  # pragma: no cover
