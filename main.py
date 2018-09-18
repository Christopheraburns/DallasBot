import log
import sys
import cortex

# Create a logger object
logger = log.rLog(True)

def listen():
    command = input("Enter a command").lower()
    print("You'd like the DallasBot to: {}".format(command))
    listen()

def main():
    try:
        if len(sys.argv) == 1: # no sys args given
            listen()
        elif len (sys.argv) == 2: # Command supplied at launch
            cortex.processCmd(sys.argv[1])
            listen()
    except KeyboardInterrupt as intr:
        logger.LogThis("__main__.py: main(): Ctrl-C interrupt")
        sys.exit()


if __name__== "__main__":
    main()