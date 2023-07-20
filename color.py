def color(n):
    return n.replace("1", colors.RED + "1" + colors.END)

def decolor(n):
    return n.replace(colors.RED + "1" + colors.END, "1")

def bincolor(n, extra=False):
    if extra:
        return color(bin(n))
    return color(format(n, 'b'))

class colors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def fprint(strings, end="\n"):
    vals = {
        "e" : colors.END,
        "u" : colors.UNDERLINE,
        "b" : colors.BOLD,
        "r" : colors.RED
    }
    outstr = ''.join([vals[str(x)] if x in vals else str(x) for x in strings])
    print(outstr, end=end)

if __name__ == '__main__':
    print("Running Color File")
