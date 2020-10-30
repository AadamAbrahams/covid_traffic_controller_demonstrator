"""Console script for covid_traffic_controller_demonstrator."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for covid_traffic_controller_demonstrator."""
    click.echo("Replace this message by putting your code into "
               "covid_traffic_controller_demonstrator.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
