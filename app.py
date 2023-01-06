from flask import Flask, render_template, redirect, request
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField

from calorie import Calorie
from temperature import Temperature

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class CaloriesFormPage(MethodView):

    def get(self):
        calories_form = CaloriesForm()
        location = Temperature(country=calories_form.country.data,
                               city=calories_form.city.data)

        return render_template('calories_form_page.html',
                               calorie=calories_form,
                               location=location)

    def post(self):
        calories_form = CaloriesForm(request.form)

        location = Temperature(country=calories_form.country.data,
                               city=calories_form.city.data)

        temperature = Temperature(country=calories_form.country.data,
                                  city=calories_form.city.data).get()

        calorie = Calorie(weight=float(calories_form.weight.data),
                          height=float(calories_form.height.data),
                          age=float(calories_form.age.data),
                          temperature=temperature)

        calories = calorie.calculate()

        return render_template('calories_form_page.html',
                               submit=True,
                               location=location,
                               temperature=temperature,
                               calorie=calorie,
                               calories=calories)


class CaloriesForm(Form):
    weight = StringField("Weight: ", default=100)
    height = StringField("Height: ", default=192)
    age = StringField("Age: ", default=41)
    country = StringField("Country: ", default="croatia")
    city = StringField("City: ", default="zagreb")
    button = SubmitField("Calculate")


app.add_url_rule("/", view_func=HomePage.as_view('home_page'))
app.add_url_rule("/calories_form", view_func=CaloriesFormPage.as_view('calories_form_page'))

if __name__ == '__main__':
    app.run(debug=True)
