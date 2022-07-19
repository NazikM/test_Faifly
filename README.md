# test_Faifly

Urls:
 - workerlist/ - full list of workers
   - workerlist/?speciality=Dentist - list of workers filtered by speciality
   - workerlist/?full_name=Olya%20Pushko&day=1 - Datail about worker (can be added day option also 1-7 (Mon-Sun))
 - book/ - Book the procedure with POST method
   - You will get error info if data thrown data was incorrect, as specialist can't work in this day or time.
 - appointments/ - List of appointments
   - appointments/?day=1 - List of appointments for exact day 1-7 (Mon-Sun)
