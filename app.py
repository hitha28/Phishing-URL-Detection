import flask
import pickle
import pandas as pd
from feature_extractor import extract_features_from_url

app = flask.Flask(__name__)

with open('model.pkl','rb') as f:
    model = pickle.load(f)

with open('feature_columns.pkl','rb') as f:
    feature_columns = pickle.load(f)

HTML = """
<!DOCTYPE html>
<html>
<head>

<title>Phishing URL Detection System</title>

<style>

body{
    font-family: Arial, sans-serif;
    background: linear-gradient(120deg,#4facfe,#00f2fe);
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
}

.container{
    background:white;
    width:420px;
    padding:40px;
    border-radius:12px;
    box-shadow:0px 8px 25px rgba(0,0,0,0.2);
    text-align:center;
}

h2{
    margin-bottom:20px;
}

input{
    width:90%;
    padding:12px;
    margin-top:10px;
    border-radius:6px;
    border:1px solid #ccc;
}

button{
    margin-top:20px;
    padding:12px 25px;
    border:none;
    background:#007BFF;
    color:white;
    border-radius:6px;
    font-size:16px;
    cursor:pointer;
}

button:hover{
    background:#0056b3;
}

.result{
    margin-top:25px;
    font-size:20px;
    font-weight:bold;
}

.safe{
    color:green;
}

.phishing{
    color:red;
}

</style>

</head>

<body>

<div class="container">

<h2>Phishing URL Detection</h2>

<form method="POST">

<input type="text" name="url" placeholder="Enter Website URL (Example: https://google.com)" required>

<br>

<button type="submit">Check URL</button>

</form>

{% if result %}

<div class="result">

{% if result == "Legitimate" %}
<span class="safe">Safe Website!</span>
{% else %}
<span class="phishing">Phishing Website</span>
{% endif %}

</div>

{% endif %}

</div>

</body>
</html>
"""

@app.route("/",methods=['GET','POST'])

def home():

    result=None

    if flask.request.method=='POST':

        url=flask.request.form['url']

        features=pd.DataFrame([extract_features_from_url(url)])

        features=features.reindex(columns=feature_columns,fill_value=0)

        prediction=model.predict(features)[0]

        result="Phishing" if prediction==1 else "Legitimate"

    return flask.render_template_string(HTML,result=result)

if __name__=="__main__":
    app.run(debug=True)