import unittest
from admin import Admin
from connection import Connection


class AdminTests(unittest.TestCase):

    person_1_valid_data = [
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
    person_1_edit_valid_data = {
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

    visit_valid_data = {
        "person_id": "4",
        "doctor": "4",
        "time_of_reception": "2",
        "treatment_cost": "10000",
    }

    add_visit_valid_data = [{
        "person_id": "4",
        "visit_date": "21.11.2021",
        "doctor": "3",
        "time_of_reception": "13:00",
        "duration_of_reception": "2",
        "description": "",
        "treatment_cost": "1000",
        "img": "",
    }]

    person_1_invalid_data = [
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
    person_1_edit_invalid_data = {
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

    visit_invalid_data = {
        "person_id": "4",
        "doctor": "4",
        "time_of_reception": "2",
        "treatment_cost": "10000",
    }

    add_visit_invalid_data = [{
        "person_id": "4",
        "visit_date": "21.11.2021",
        "doctor": "3",
        "time_of_reception": "13:00",
        "duration_of_reception": "2",
        "description": "",
        "treatment_cost": "1000",
        "img": "",
    }]

    def setUp(self):
        self.admin = Admin()
        pass

    def test_add_person(self,):
        person = Admin()
        self.assertIsInstance(person, Admin)
        print('Test 1.1: pass.')
        pass
    def test_edit_person(self,):
        pass
    def test_get_person_data(self,):
        pass
    def test_get_visit_info(self,):
        pass
    def test_edit_visit(self,):
        pass
    def test_add_visit(self,):
        pass