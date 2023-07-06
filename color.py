def color(n):
    return n.replace("1", "\033[91m1\033[00m")

def decolor(n):
    return n.replace("\033[91m1\033[00m", "1")

if __name__ == '__main__':
    print("Running Color File")
