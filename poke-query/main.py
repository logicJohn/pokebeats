# Flask Setup
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from flask import Flask, jsonify, request, abort
from flask import render_template
app = Flask(__name__)

# Google Sheets API Setup
credential = ServiceAccountCredentials.from_json_keyfile_name("credentials.json",
                                                              ["https://spreadsheets.google.com/feeds",
                                                               "https://www.googleapis.com/auth/spreadsheets",
                                                               "https://www.googleapis.com/auth/drive.file",
                                                               "https://www.googleapis.com/auth/drive"])

client = gspread.authorize(credential)
gsheet = client.open("Hungry in Chapel Hill").sheet1
# An example GET Route to get all reviews


@app.route('/test')
def all_reviews():
    print(gsheet.get_all_records())
    return jsonify(gsheet.get_all_records())
@app.route("/")
def hello_world():
    print(gsheet.get_all_records())
    #print(gsheet.get_all_records()[0]['Timestamp'])
    timestamps = []
    for x in gsheet.get_all_records():
        timestamps.append(x['Timestamp'])
    return render_template('index.html', test=timestamps)

@app.route('/temp')
def temp():
    print("temp")
    return "This is working \n"
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

