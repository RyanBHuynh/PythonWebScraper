import csv

# This file stores all of the functions to be used in main.py

# Purpose: convert all data to a string and remove any unnecessary data and characters
# Parameters: a list of data from the table
# Return values: None
def reformat_list(a_list):
    # I use a while loop instead of a for loop because data is being removed from the list
    i = 0
    while i < len(a_list):
        # Convert each entry to a string
        a_list[i] = str(a_list[i])

        # Remove certain leading and trailing characters
        a_list[i] = a_list[i].lstrip("'b")
        a_list[i] = a_list[i].lstrip("b")
        a_list[i] = a_list[i].rstrip("'")
        a_list[i] = a_list[i].lstrip(r"\\n")
        a_list[i] = a_list[i].rstrip(r"\\n")

        # Remove unnecessary strings
        if r'xc2\xa0' in a_list[i] or a_list[i] == '' or 'False' in a_list[i] or 'True' in a_list[i]:
            a_list.pop(i)  # Don't increment i if we pop it
        else:
            i += 1

# Purpose: Return a list where each row has the information for an individual business
# Parameters: a bs4 element that represents the body of the table
# Return value: a parsed list of all the business data
def parse_body(body):
    body_as_list = [tr.text.encode("utf-8") for tr in body.select("tr td")]
    reformat_list(body_as_list)

    # Parse the information in the body
    parsed_table = []
    cur = []  # Store each line in cur

    # Loop through body_as_list and store each row in parsed_table
    for i in range(len(body_as_list)):
        cur_string = body_as_list[i]

        # Add cur to parsed_table if curString is an ID number
        # The ID number kind of acts like a delimiter between rows in the table
        if type(cur_string) == str and len(cur_string) != 8 and cur_string.isnumeric() == True:
            if cur != []:
                parsed_table.append(cur)
                cur = []
        else:
            cur.append(body_as_list[i])

    # Finish refining the table
    for entry in parsed_table:
        reformat_list(entry)
        entry.pop(0)  # Remove duplicate title in each row

    return parsed_table


# Purpose: Takes headers and business_table and writes it to a CSV file
# Parameters: a list and a string that has the file name
# Return values: None
def write_table_to_csv(header_list, business_table, filename):
    with open(filename,"w") as f:
      write = csv.writer(f)
      write.writerow(header_list)
      write.writerows(business_table)
