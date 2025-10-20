from flask import Flask, render_template_string, url_for
import secrets
import string

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Password Generator</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
      body{font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;display:flex;min-height:100vh;align-items:center;justify-content:center;background:#f5f7fb}
      .card{background:#fff;padding:2rem;border-radius:16px;box-shadow:0 10px 30px rgba(0,0,0,.08);text-align:center;width:min(620px,92vw)}
      h1{font-size:1.25rem;margin:0 0 1rem}
      .pwd{font-family:ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;background:#0f172a;color:#e2e8f0;padding:.75rem 1rem;border-radius:10px;margin:.75rem 0;word-break:break-all}
      button{padding:.75rem 1.25rem;border:none;border-radius:999px;cursor:pointer;font-weight:600}
      .primary{background:#2563eb;color:white}
    </style>
  </head>
  <body>
    <div class="card">
      <h1>OneClick PassworD GENERATOR</h1>
      {% if password %}
        <div class="pwd" id="pwd">{{ password }}</div>
        <button onclick="copy()">Copy</button>
      {% endif %}
      <form method="post" action="{{ url_for('generate') }}">
        <button class="primary" type="submit">Generate password</button>
      </form>
      <p style="opacity:.7;margin-top:.75rem">Length: 16, includes A–Z, a–z, 0–9, symbols</p>
    </div>
    <script>
      function copy(){
        const el = document.getElementById('pwd');
        navigator.clipboard.writeText(el.textContent);
        alert('Copied!');
      }
    </script>
  </body>
</html>
"""

SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?/"


def make_password(length=16):
    alphabet = string.ascii_letters + string.digits + SYMBOLS
    while True:
        pwd = "".join(secrets.choice(alphabet) for _ in range(length))
        if (
            any(c.islower() for c in pwd)
            and any(c.isupper() for c in pwd)
            and any(c.isdigit() for c in pwd)
            and any(c in SYMBOLS for c in pwd)
        ):
            return pwd


@app.get("/")
def home():
    return render_template_string(TEMPLATE, password=None)


@app.post("/generate")
def generate():
    pwd = make_password()
    return render_template_string(TEMPLATE, password=pwd)


if __name__ == "__main__":
    app.run(debug=True)  # visit http://127.0.0.1:5000
