# sortBy(prop){
#     this.projects.sort((a,b) => a[prop] < b[prop] ? -1 : 1)
# }

# inputRules: [
#     v => v.length >=3 || 'Minimum is 3 char.'
# ]

# if (this.$refs.form.validate()){
#     submit form here
# }

#########
# Python's program to get first and last day of Current Quarter Year
 
# from datetime import datetime, timedelta
 
# current_date = datetime.now()
# current_quarter = round((current_date.month - 1) / 3 + 1)
# first_date = datetime(current_date.year, 3 * current_quarter - 2, 1)
# last_date = datetime(current_date.year, 3 * current_quarter + 1, 1)\
#     + timedelta(days=-1)
 
# print("First Day of Quarter:", first_date)
# print("Last Day of Quarter:", last_date)