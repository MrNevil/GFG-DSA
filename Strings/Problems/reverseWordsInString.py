def reverseWords(s):
    tokens = s.split('.')
    rtokens = tokens[::-1]
    return '.'.join(rtokens)
    
if __name__ == '__main__':
    t = int(input())
    for tcase in range(t):
        s = input()
        print (reverseWords(s))