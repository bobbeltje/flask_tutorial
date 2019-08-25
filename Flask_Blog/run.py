
# the app variable needs to exist in __init__
from flaskblog import app

# to run the app without setting environmental variables
if __name__ == '__main__':
    app.run(debug=True)
