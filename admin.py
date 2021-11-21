import psycopg2
from settings import *
from connection import Connection


class Admin(Connection):
    def add_person(self, data):
        table = "persons"
        result = self._postData(table, data)
        return result

    def edit_person(self, data, selector):
        table = "persons"
        result = self.updateData(table, data, selector)
        return result

    def get_person_data(self, selector):
        table = ("persons",)
        fields = ("*",)
        data = self.getData(table, fields, selector)
        print(data)
        return data

    def get_visit_info(self, selector):
        table = ("visits",)
        fields = ("*",)
        data = self.getData(table, fields, selector)
        print(data)
        return data

    def add_visit(self, data):
        table = "visits"
        result = self._postData(table, data)
        return result

    def edit_visit(self, data, selector):
        table = "visits"
        result = self.updateData(table, data, selector)
        print("Updated successfully")
        return result


if __name__ == "__main__":

    person_1_data = [
        {
            "first_name": "new",
            "last_name": "user",
            "phone_number": "+380677681243",
            "role": "4",
            "gender": "female",
            "birth_date": "26.04.1963",
            "registration_date": "20.09.2021",
            "discount": "0",
            "city": "Rivne",
            "allergy": "",
            "disease": "",
        }
    ]
    person_1_edit_data = {
        "first_name": "new",
        "last_name": "user",
        "phone_number": "+380677681243",
        "role": "4",
        "gender": "female",
        "birth_date": "26.04.1963",
        "registration_date": "20.09.2021",
        "discount": "0",
        "city": "Rivne",
        "allergy": "",
        "disease": "",
    }

    visit_data = {
        "person_id": "4",
        "doctor": "4",
        "time_of_reception": "2",
        "treatment_cost": "10000",
    }

    add_visit_data = [{
        "person_id": "4",
        "visit_date": "21.11.2021",
        "doctor": "3",
        "time_of_reception": "13:00",
        "duration_of_reception": "2",
        "description": "",
        "treatment_cost": "1000",
        "img": "",
    }]

    person_1 = Admin()
    # person_1.add_person(person_1_data)
    # person_1.edit_person(person_1_edit_data, "id = '4'")
    # person_1.get_person_data("where id = '4'")
    # person_1.get_visit_info("where person_id = '4'")
    # person_1.edit_visit(visit_data, "id = '1'")
    person_1.add_visit(add_visit_data)
