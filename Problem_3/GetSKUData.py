import csv

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/getSKU/<metadata_input>')
def getSKU(metadata_input):
    filename = "SKUData"
    # initializing the titles and rows list
    fields = []
    rows = []
    metadata_input = metadata_input.split(",")

    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)
        answerRows = ""
        # extracting each data row one by one
        for row in csvreader:
            #   rows.append(row)
            if all(item in row for item in metadata_input):
                answerRows = answerRows + "\n" + str(row)
    return render_template('getSKU.html', answerRows=answerRows)


if __name__ == '__main__':
    app.run(debug=True)
