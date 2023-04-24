def set_alarm(employed, vacation):
    if employed and vacation:
        print("False")
        # return False
    elif employed == False and vacation == True:
        print("False")
        # return False
    elif employed == False and vacation == False:
        print("False")
        # return False
    elif employed and vacation == False:
        print("True")
        # return True


set_alarm(True, True)
