from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '''<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title>Serverless Devs - Powered By Serverless Devs</title>
    <link href="https://example-static.oss-cn-beijing.aliyuncs.com/web-framework/style.css" rel="stylesheet" type="text/css"/>
</head>
<body>
<div class="website">
    <div class="ri-t">
        <h1>Devsapp</h1>
        <h2>This is a Flask project</h2>
        <span>Proudly deployed via Serverless Devs</span>
        <br/>
        <p>You can also quickly experience: <br/>
            • npm install @serverless-devs/s<br/>
            • s init start-flask <br/>
            • s deploy -y --use-local <br/>
            <br/>
            Powered by Serverless Devs!
        </p>
    </div>
</div>
</body>
</html>
'''


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
