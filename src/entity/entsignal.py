############
# SIGNALS  #
#############

class SIG:
    #unfortinately this is the best way for realsies
    #because relative import forces the architecture
    # from .a import b
    # and using wildcard means importing all local vars without the signal.a
    # so i'm finna do it this way and regret it
    #
    noOperation = ""

    killme = "killme"
    finishedCourse = "fincur"
    NEWREDFOX = "newredfox"
