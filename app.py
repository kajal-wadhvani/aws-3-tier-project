
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>AWS 3-Tier Infrastructure Project</h1>
    <p>My Flask application is running successfully!</p>
    <p>Next: AWS VPC, EC2, ALB and RDS.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
