festival_name_query = "SELECT name, province FROM festivaldb.festival;"

festivals_by_province_query = "SELECT name, province FROM festivaldb.festival WHERE province = %s;"

festivals_by_name_and_month_query = "SELECT name, location, startDate, endDate, province FROM festivaldb.festival WHERE name LIKE %s AND (date_format(startDate, '%m') = %s OR date_format(endDate, '%m') = %s);"
