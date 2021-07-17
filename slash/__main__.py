import sys
def main():
    args = sys.argv[1:]
    for arg in args:
        str = arg
        print(str)
        st=''
        arr = str.split("\\")
        for i in arr:
            if(st==''):
                st= i + "/"
            else: 
                st= st + i + "/"
        print(st)
if __name__ == '__main__':
    main()