from addsplit import address_split
# coding=utf-8
import unittest

# import data (optional)
# with open('input.txt') as test_data_file:
#     for line in test_data_file:
#         (street, house) = address_split(line)
#         print "Address: {} \tStr: {} \tHouse: {}\n".format(line, street, house)

class TestAddressSplit(unittest.TestCase):

    # check if gives an error when too short input
    def test_badinput(self):
        with self.assertRaises(ValueError) as context:
            address_split("")
        self.assertTrue('Empty line or just one argument!' in context.exception)
        with self.assertRaises(ValueError) as context:
            address_split("Stiftstrasse")
        self.assertTrue('Empty line or just one argument!' in context.exception)
        
    # normal case
    def test_normalcase(self):
        self.assertEqual(address_split("Winterallee 3"), ("Winterallee", "3"))
        self.assertEqual(address_split("Musterstrasse 45"), ("Musterstrasse", "45"))
        self.assertEqual(address_split("Blaufeldweg 123/B"), ("Blaufeldweg", "123/B"))

    # long names
    def test_case2(self):
        self.assertEqual(address_split("Am Bächle 23"), ("Am Bächle", "23"))
        self.assertEqual(address_split("Am Bächle 23-25"), ("Am Bächle", "23-25"))
        self.assertEqual(address_split("Auf der Vogelwiese 23 b"), ("Auf der Vogelwiese", "23 b"))
        self.assertEqual(address_split("Auf der Vogelwiese 23-b"), ("Auf der Vogelwiese", "23-b"))

    # comma separated
    def test_case3(self):
        self.assertEqual(address_split("4, rue de la revolution"), ("rue de la revolution", "4"))
        self.assertEqual(address_split("Calle Aduana, 29"), ("Calle Aduana", "29"))
        self.assertEqual(address_split("Calle 39, 156"), ("Calle 39", "156"))
        self.assertEqual(address_split("3-koningenstraat, 21 13b"), ("3-koningenstraat", "21 13b"))
        self.assertEqual(address_split("Heuvel, 2a"), ("Heuvel", "2a"))
        self.assertEqual(address_split("Russkaya, 25, 127"), ("Russkaya", "25, 127"))

    # other complex cases
    def test_case4(self):
        self.assertEqual(address_split("200 Broadway Av"), ("Broadway Av", "200"))
        self.assertEqual(address_split("kerkstraat 42-f3"), ("kerkstraat", "42-f3"))
        self.assertEqual(address_split("Calle 39 No 156"), ("Calle 39", "No 156"))

if __name__ == '__main__':
    unittest.main()
