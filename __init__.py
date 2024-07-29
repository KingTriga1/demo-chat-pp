import click, os
from flask import Flask, request, render_template, url_for


app = Flask(__name__)

app.config.from_mapping(SECRET_KEY='dev',
                        DATABASE=os.path.join(os.getcwd(), 'appMain/appMain.sqlite')
                        )





@click.command('init-db')
def init_db_command():
    from db.db import DatabaseObject
    db = DatabaseObject()
    db.init_db()
    click.echo("Initialized the database")


def init_app(mainapp):
    from db.db import DatabaseObject
    db = DatabaseObject()
    mainapp.teardown_appcontext(db.close_db)
    mainapp.cli.add_command(init_db_command)


init_app(app)





@app.route('/')
def hello():


    return render_template("Login form.html")

@app.route('/catalog')
def getCatalog():
    return render_template('catalogpage.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5032)



