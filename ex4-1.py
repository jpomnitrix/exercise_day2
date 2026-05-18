number = 7
if number % 2:
    print("奇数")
else:
    print("偶数")

score = 85
if score >= 90:
    print("S")
elif 80 <= score < 90:
    print("A")
elif 70 <= score < 80:
    print("B")
else:
    print("C")

height = 130
age = 9
if height >= 120 and age >= 10:
    print("乗車可能")
else:
    print("乗車不可")

x = 50
if 0 < x < 100:
    print("範囲内です")

is_member = True
purchase_amount = 5000
if is_member and purchase_amount >= 3000:
    print("送料無料")
elif is_member and purchase_amount <= 3000:
    print("送料500円")
else:
    print("非会員は送料1000円")







