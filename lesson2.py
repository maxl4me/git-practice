skills = ["Git", "Python", "Postman"]

for skill in skills:
	print("I am learning",skill)

count = 0
while count  < 3:
	print("Count is:", count)
	count += 1


status_code = 200

if status_code == 200:
	print("PASS: API is OK")
elif status_code == 404:
	print("FAIL: Not Found")
else:
	print("FAIL: Unknow Error") 
