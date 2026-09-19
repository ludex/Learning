import os

import connexion
from flask import render_template

# Create the application instance
# app = Flask(__name__, template_folder="templates")
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

@app.route('/')
def home():
    '''
    This function just responds to the browser URL localhost:5000/
    
    '''
    return render_template("home.html")


# Run the application if we're running in stand-alone mode
if __name__ == '__main__':
    # Debug mode and non-loopback binding require explicit local opt-in.
    app.run(
        host=os.getenv("FLASK_HOST", "127.0.0.1"),
        port=int(os.getenv("FLASK_PORT", "5000")),
        debug=os.getenv("FLASK_DEBUG") == "1",
    )
