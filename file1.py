from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/requirements/')
def requirements():
    with open('requirements.txt') as f:
     file_data = f.read()
    return(file_data)
    f.close()

@app.route('/generate-users/')
def generate_users():
    from faker import Faker
    fake = Faker()
    usernames_and_emails = {}
    number = request.args.get('number', default = 1, type = int)
    number == int(number)
    if not number:
        number == 100
    for i in range(number):
        username = fake.name()
        email = fake.email()
        usernames_and_emails.update({username: email})
    return usernames_and_emails


@app.route('/mean/')
def mean():
    import re
    from statistics import mean
    with open('hw (2) (1).csv') as f1:
        file_data = re.sub("[A-Za-z,/()]", "", str(f1.read()))
    f1.close
    height_and_weight = [i for i in file_data.split()]
    del height_and_weight[0:3]
    height = height_and_weight[1::3]
    weight = height_and_weight[2::3]
    height_in_sm = [float(i) * 2.54 for i in height]
    weight_in_kg = [float(i) * 0.454 for i in weight]
    average_weight = str(mean(weight_in_kg))
    average_height = str(mean(height_in_sm))
    average_height_and_weight = {average_weight: average_height}
    return average_height_and_weight


@app.route('/space/')
def space():
    import requests
    data = requests.get("http://api.open-notify.org/astros.json").text
    number = data[len(data)-3]+data[len(data)-2]
    return number

if __name__ == "__main__":
    app.run()

