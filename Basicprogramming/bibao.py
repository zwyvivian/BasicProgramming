
def outer():
    name = 'vivian'
    def inner():
        print(name)

    return inner

func=outer()
func()