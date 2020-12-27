from flask import *

app=Flask(__name__)

#------------------------Registration Response---------------
@app.route('/registration-status',methods=["POST","GET"])
def success_registration():
    if(request.method=="POST"):
        email = request.form["email"]
        password = request.form["pwd"]
        response = make_response(render_template("registration-response.html"))
        response.set_cookie('email',email)
        response.set_cookie('password',password)
    return response
#------------------------------------------------------------------

#-------------------Login Template Render----------------------
@app.route('/login')
def login_page_render():
    return make_response(render_template('login-template.html'))
#---------------------------------------------------------------

#-------------------------Login Response------------------------
@app.route('/login-status',methods=["POST"])
def login_response():
    user = request.form["email"]
    pwd = request.form["pwd"]

    if(user == request.cookies.get('email') and (pwd == request.cookies.get('password'))):
        response = make_response(render_template('login-response.html'))
    else:
        response = make_response(render_template('index.html'))
    return response
#---------------------------------------------------------------

#---------------Home page Render ----------------
@app.route('/home')
def home_render():
    return make_response(render_template('index.html'))
#------------------------------------------------


if __name__ == "__main__":
    app.run(debug=True)