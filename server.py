from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "blahhhhhhhh"

@app.route('/')
def show_homepage():

    # print(session['name'])
    return render_template('homepage.html')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################


@app.route('/form')
def show_form():
    """Render to forms page."""

    return render_template('form.html')

@app.route('/results')
def show_results():
    """Render to results page."""

    return render_template('results.html')

@app.route('/save-name')
def save_name():
    """Save user's name into session."""

    name = request.args.get('name')
    # print(name)
    session['name'] = name
    # print(session['name'])

    return redirect('/')



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
