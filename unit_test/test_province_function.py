from province_functions import get_formatted_province
import unittest

# print("Enter 'q' at any time to quit\n")
# end_loop : bool = False
# while end_loop == False:
#   province_name : str = input("Enter province name: ")
#   if province_name == 'q': break
#   country_name : str = input("Enter country name: ")
#   if country_name == 'q': break
#   population_val : str = input("Enter population value: ")
#   if population_val == 'q': break
#   end_loop = True

# print(f"\n{get_formatted_province(province_name, country_name, population_val)}")

class TestProvinceModule(unittest.TestCase):
    """ Tests for 'province_functions.py' """

    def test_province_country(self):
        """ Do only province and country work?"""
        formatted_province = get_formatted_province("Laguna", "Philippines")
        self.assertEqual(formatted_province, "Laguna, Philippines")

    def test_prov_country_population(self):
        """ what if the information is complete? """
        x = get_formatted_province("Manila", "Philippines", "3 million")
        self.assertEqual(x, "Manila, Philippines - 3 Million")

    def test_no_info(self):
        """ what if there's no info? """
        x = get_formatted_province()
        self.assertEqual(x,'no inputs given')

if __name__ == '__main__':
    unittest.main()