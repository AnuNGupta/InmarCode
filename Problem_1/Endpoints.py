from flask import Flask, json, render_template, request
import os

# create instance of Flask app
app = Flask(__name__)


# decorator
def hello():
    # it is a good idea to include information on how to use your API on the home route
    # this is just another way to do that
    text = f"go to /locations to see all events <br> \
              and /location/<location_name> to see all data of a location <br> \
              and /location/<locationDetailsInForm> to add additional locations"
    return text


@app.route("/locations")
def all():
    json_url = "metadata.json"
    data_json = json.load(open(json_url))
    # render_template is always looking in templates folder
    return render_template('index.html', html_page_text=data_json)


@app.route("/location/<location_name>", methods=['GET', 'POST'])
def add_location(location_name):
    json_url = "metadata.json"
    if request.method == 'GET':
        data_json = json.load(open(json_url))
        data = data_json['locations']
        location = request.view_args['location_name']
        output_data = [x for x in data if x['Location'] == location_name]

        # render template is always looking in tempate folder
        return render_template('location_display.html', html_page_text=output_data)
    elif request.method == 'POST':
        location = request.form['location_name']

        # case sensitive, so be careful!
        department = request.form['department']
        category = request.form['category']
        subcategory = request.form['subcategory']
        new_location = {"Location": location,
                        "Department": department,
                        "Category": category,
                        "SubCategory": subcategory
                        }

        with open(json_url, "r+") as file:
            data_json = json.load(file)
            data_json["locations"].append(new_location)
            file.seek(0)
            json.dump(data_json, file, indent=4)

        # Adding text
        text_success = "Data successfully added: " + str(new_location)
        return render_template('index.html', html_page_text=text_success)


@app.route("/deleteLocation/<location_name>", methods=['DELETE'])
def del_location(location_name):
    json_url = "metadata.json"
    location = request.form['location_name']

    # case sensitive, so be careful!
    department = request.form['department']
    category = request.form['category']
    subcategory = request.form['subcategory']
    new_location = {"Location": location,
                    "Department": department,
                    "Category": category,
                    "SubCategory": subcategory
                    }

    with open(json_url, "r+") as file:
        data_json = json.load(file)
        for i in range(len(data_json["locations"])):
            if data_json["locations"][i]["Location"] == location_name and \
                    data_json["locations"][i]["SubCategory"] == subcategory:
                del data_json["locations"][i]
                break
        file.seek(0)
        with open(json_url, "w") as writefile:
            json.dump(data_json, writefile, indent=4)

    # Adding text
    text_success = "Data successfully removed: " + str(new_location)
    return render_template('index.html', html_page_text=text_success)


@app.route("/updateLocation/<location_name>", methods=['PATCH'])
def update_location(location_name):
    json_url = "metadata.json"
    location = request.form['location_name']

    # case sensitive, so be careful!
    department = request.form['department']
    category = request.form['category']
    subcategory = request.form['subcategory']

    new_location = request.form['new_location_name']
    new_department = request.form['new_department']
    new_category = request.form['new_category']
    new_subcategory = request.form['new_subcategory']

    existing_entry = {"Location": location,
                      "Department": department,
                      "Category": category,
                      "SubCategory": subcategory
                      }
    new_entry = {"Location": new_location,
                 "Department": new_department,
                 "Category": new_category,
                 "SubCategory": new_subcategory
                 }
    with open(json_url, "r+") as file:
        data_json = json.load(file)
        # get_data = data_json["locations"][1]["SubCategory"]
        for i in range(len(data_json["locations"])):
            if data_json["locations"][i]["Location"] == location_name and \
                    data_json["locations"][i]["Department"] == department and \
                    data_json["locations"][i]["Category"] == category and \
                    data_json["locations"][i]["SubCategory"] == subcategory:
                check_in = data_json["locations"][i]
                data_json["locations"][i] = new_entry
                break
        file.seek(0)
        check_in = data_json
        with open(json_url, "w") as writefile:
            json.dump(data_json, writefile, indent=4)

    # Adding text
    text_success = "Data successfully updated: " + str(check_in)
    return render_template('index.html', html_page_text=text_success)


if __name__ == "__main__":
    app.run(debug=True)
