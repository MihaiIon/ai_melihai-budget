import click
from flask_migrate import Migrate
from api import create_app
from api.models import db

# Create an app instance
app = create_app()

# Initialize the database
migrate = Migrate(app, db)

###
# Custom CLI commands to recreate the database
###
@app.cli.command("recreate_db")
def recreate_db():
    """Recreates a database."""
    db.drop_all()
    db.create_all()
    click.echo("Database recreated successfully.")

###
# Custom CLI commands to run the development server
###
@app.cli.command("runserver")
@click.option("--host", default="127.0.0.1", help="Host IP address")
@click.option("--port", default=5000, help="Port number")
@click.option("--debug", is_flag=True, help="Enable debug mode")
def runserver(host, port, debug):
    """Runs the development server."""
    app.run(host=host, port=port, debug=debug)

if __name__ == "__main__":
    app.run()
