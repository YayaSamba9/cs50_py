# List of all months in order
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Infinite loop until the user enters a valid date
while True:
    date = input("Date: ")

    # --- First format: M/D/YYYY ---
    try:
        # Split the input by "/"
        m, d, y = date.split("/")
        # Convert each part into an integer
        m = int(m)
        d = int(d)
        y = int(y)

        # Check if the month and day are within valid ranges
        if 1 <= m <= 12 and 1 <= d <= 31:
            # Print in ISO format YYYY-MM-DD
            print(f"{y}-{m:02d}-{d:02d}")
            break  # Exit the loop after success
    except:
        # If any error occurs (wrong format, conversion error, etc.), skip this block
        pass

    # --- Second format: Month D, YYYY ---
    try:
        # Check if the date contains a comma (e.g., "September 8, 1636")
        if "," in date:
            # Remove the comma and split the parts
            date = date.replace(",", "")
            rt = date.split()

            # If there are exactly three parts, assign them
            if len(rt) == 3:
                month_rt, d, y = rt

            # Verify that the month name exists in the list of months
            # and that the day number is valid
            if month_rt in months and 1 <= int(d) <= 31:
                # Get the numerical value of the month (1–12)
                m = months.index(month_rt) + 1
                # Convert day and year to integers
                d, y = int(d), int(y)
                # Print in ISO format YYYY-MM-DD
                print(f"{y}-{m:02d}-{d:02d}")
                break  # Exit the loop after success
    except:
        # Skip errors (e.g., wrong input format)
        pass
