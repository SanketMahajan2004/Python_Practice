marks1 = int(input("Enter the Marks1 :"))
marks2 = int(input("Enter the Marks2 :"))
marks3 = int(input("Enter the Marks3 :"))

total_persentage =(100)*(marks1 + marks2 + marks3)/300
if (total_persentage>= 40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("Pass",total_persentage)
else:
    print("Fail",total_persentage)