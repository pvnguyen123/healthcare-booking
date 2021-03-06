import click
from flask.cli import FlaskGroup

from healthcarebooking.app import create_app


def create_healthcarebooking(info):
    return create_app(cli=True, testing=True)


@click.group(cls=FlaskGroup, create_app=create_healthcarebooking)
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """Init application, create database tables
    and create a new user named admin with password admin
    """
    from healthcarebooking.extensions import db
    click.echo("create database")
    db.create_all()
    db.session.commit()
    click.echo("done")


    # from healthcarebooking.models import User
    # click.echo("create user")
    # user = User(
    #     username='admin',
    #     email='admin@mail.com',
    #     password='admin',
    #     active=True
    # )
    # db.session.add(user)

    # click.echo("created user admin")


if __name__ == "__main__":
    cli()
