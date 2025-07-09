

import sys 


for i in sys.stdin:
    A, B = map(int, i.split())
    print(A+B)

# sys.stdout.write('\n'.join(outputs) + '\n')