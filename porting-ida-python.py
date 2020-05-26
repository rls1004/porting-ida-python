import sys

ida6 = []
ida7 = []

def init():
  global ida6, ida7
  ida6 = open('ida6_types.txt').read().split('\n')[:-1]+open('ida6_idc.txt').read().split('\n')[:-1]
  ida7 = open('ida7_types.txt').read().split('\n')[:-1]+open('ida7_idc.txt').read().split('\n')[:-1]

def main():
  if len(sys.argv) < 2:
    print('Usage: porting.py [file]')
    return

  fname = sys.argv[1]
  data = open(fname).read()
  
  for i in range(len(ida6)):
    target = '.'+ida6[i].split('.')[-1]
    cnt = data.count(target.split('(')[0])
    if cnt > 0:
      if '(' in target:
        replace_data = ida7[i]
        before_argv = target.split('(')[1].split(')')[0].split(',')
        before_argc = len(before_argv)
        after_argv = replace_data.split('(')[1].split(')')[0].split(',')
        after_argc = len(after_argv)
        argvTo = [-1 for _ in range(after_argc)]
        for i in range(before_argc):
          try:
            argvTo[after_argv.index(before_argv[i])] = i
          except:
            continue
        replace_data = '.'+replace_data.split('.')[1].split('(')[0]+'('

        real_code = data[data.index(target.split('(')[0]):]
        real_code = real_code.split(')')[0]+')'
        real_argv = real_code.split('(')[1].split(')')[0].split(',')
        
        for i in range(after_argc):
          if i > 0: replace_data += ', '
          if argvTo[i] != -1:
            replace_data += real_argv[argvTo[i]]
          else:
            replace_data += after_argv[i]

        replace_data += ')'
        print(real_code+' -> '+replace_data)
        data = data.replace(real_code, replace_data, cnt)
      else:
        print(target+' -> '+'.'+ida7[i].split('.')[-1])
        data = data.replace(target, '.'+ida7[i].split('.')[-1], cnt)

  open('ida7_'+fname, 'w').write(data)
  print('create: ida7_'+fname)
      

if __name__ == '__main__':
  init()
  main()




