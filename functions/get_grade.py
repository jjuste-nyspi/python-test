def get_grade(s1, s2, s3):
    average = (s1 + s2 + s3)/3
    if 90 <= average <= 100:
        print('A')
        # return 'A'
    elif 80 <= average <= 89:
        print('B')
        # return 'B'
    elif 70 <= average <= 79:
        print('C')
        # return 'C'
    elif 60 <= average <= 69:
        print('D')
        # return 'D'
    elif 0 <= average <= 59:
        print('F')
        # return 'F'


get_grade(97, 47, 95)
