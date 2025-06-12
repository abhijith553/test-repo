from dash import Dash, html
import os

app = Dash(__name__)
app.layout = html.H1("Hello from Dash on Render!")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    print("Starting on port", port)
    app.run(debug=False, host="0.0.0.0", port=port)
