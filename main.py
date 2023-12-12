from flask import Flask, request, send_file
import requests

app = Flask(__name__)

@app.route("/download", methods=["POST"])
def download_file():
  url = request.form["url"]

  try:
    # Make a request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
      # Get the filename from the response headers
      filename = response.headers.get("Content-Disposition").split("filename=")[1]

      # Write the content to a file
      with open(filename, "wb") as f:
        f.write(response.content)

      # Send the file to the user
      return send_file(filename, as_attachment=True)
    else:
      return "Error: Could not download file.", 400
  except Exception as e:
    return "Error: {}".format(e), 500

if __name__ == "__main__":
  app.run(debug=True)
