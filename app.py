
from urllib import request
from flask import (Flask, render_template, session, redirect, url_for)
from flask_wtf import FlaskForm
from wtforms import (SubmitField, SelectField, FileField, EmailField)
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'


class InfoForm(FlaskForm):
    tablesListFile = FileField("Upload Tables")
    columnsListFile = FileField("Columns List")
    userEmail = EmailField("Email")
    cirrusServer = SelectField("Cirrus Server", choices=[
                               "Cirrus Memgroups", "Cirrus Alpha", "Cirrus benefits", "Cirrus Provider"])
    UDWserver = SelectField("UDW server", choices=[
                            "udwDEV", "udwSIT", "udwUAT", "udwPROD"])
    submit = SubmitField("Submit")


@app.route('/', methods=['GET', 'POST'])
def ddlCheck():
    form = InfoForm()
    if form.validate_on_submit():
        uploadedFilesDirectory =os.path.join(
        os.path.dirname(app.instance_path), 'uploads'
    )
        tablesFile = form.tablesListFile.data
        if tablesFile:
            tablesFileName = secure_filename(tablesFile.filename)
            tablesFile.save(os.path.join(uploadedFilesDirectory,tablesFileName))
        columnsFile = form.columnsListFile.data
        if columnsFile:
            columnsFileName = secure_filename(columnsFile.filename)
            columnsFile.save(os.path.join(uploadedFilesDirectory,columnsFileName))
        userEmail = form.userEmail.data
        cirrusServer = form.cirrusServer.data
        udwServer = form.UDWserver.data
        return render_template("home.html", form=form)
    else:
        print("You did not supply the details properly!!")

    return render_template("home.html", form=form)


if __name__ == '__main__':
    app.run(debug=True,port=5001)
