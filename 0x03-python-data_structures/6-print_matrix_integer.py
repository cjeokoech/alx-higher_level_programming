#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
     if not matrix:
        print()
    else:
        # Loop through the rows
        for row in matrix:
            # Loop through the items in row
            for item in row:
                # Add space between items if not last item in row
                if row.index(item) != len(row) - 1:
                    endspace = " "
                else:
                    endspace = ""
                    print("{:d}".format(item), end=endspace)
            print()
