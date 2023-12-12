from fastapi import FastAPI, Request, File, UploadFile
import requests

app = FastAPI()

@app.post("/download")
async def download_file(url: str, file: UploadFile = None):
  """
  Download a file from a URL.

  Args:
      url: The URL of the file to download.
      file: (optional) An uploaded file containing the download URL.

  Returns:
      A JSON response with the downloaded file content and filename.
  """

  try:
    if file:
      # Get the URL from the uploaded file content
      url = await file.read()
    # Make a request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
      # Generate a filename based on the URL
      filename = url.split("/")[-1]

      # Return the downloaded file content and filename
      return {"filename": filename, "content": response.content}
    else:
      return {"error": "Error: Could not download file."}, 400
  except Exception as e:
    return {"error": "Error: {}".format(e)}, 500
