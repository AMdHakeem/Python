class Combined:
    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")
    def OddEven():
        num=int(input("Enter a number:"))
        if((num%2)==0):
            print(num, "is Even number")
        else:
            print(num, "is Odd number")
    def Elegible():
        gender="Male"
        age=20
        print("Your Gender:", gender)
        print("Your Age:", age)
        if (gender=="male" and age>=21):
            print("ELIGIBLE")
        elif (gender=="female" and age>=18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
    def percentage():
        s1=98
        s2=87
        s3=95
        s4=95
        s5=93
        print("Subject1=", s1)
        print("Subject2=", s2)
        print("Subject3=", s3)
        print("Subject4=", s4)
        print("Subject5=", s5)
        Total=s1+s2+s3+s4+s5
        print("Total :", Total)
        Percentage=Total/5 
        print("Percentage :", Percentage)
    def triangle():
        Height=32
        Breadth=34
        print("Height:", Height)
        print("Breadth:", Breadth)
        print("Area formula: (Height*Breadth)/2")
        area=(Height*Breadth)/2
        print("Area of Triangle: ", area)
        Height1=2
        Height2=4
        Breadth=4
        print("Height1:", Height1)
        print("Height2:", Height2)
        print("Breadth:", Breadth)
        print("Perimeter formula: Height1+Height2+Breadth")
        Perimeter=Height1+Height2+Breadth
        print("Perimeter of Triangle: ", Perimeter)