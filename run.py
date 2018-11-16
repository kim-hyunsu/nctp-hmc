import sys

if __name__=="__main__":
  if len(sys.argv) != 2:
    print("python test.py [experiment_name]")
  else:
    test = __import__('experiments.' + sys.argv[1], globals(), locals(), ['main'], 0)
    test.main()