from address_split import address_split

# import data for testing
with open('input.txt') as test_data_file:
    for line in test_data_file:
        (street, house) = address_split(line)
        print "Address: {} \tStr: {} \tHouse: {}\n".format(line, street, house)
