from servode import Servo, ServoGroup, ServoProtocol
import log
import computervision as vision
import computerspeech as speech

# Create a logger object
logger = log.rLog(False)

def readThis(debug):
    # Take a picture
    vision.Vision.takeSinglePicture(debug)

    # Send to Reko image to text service
    result = vision.Vision.imageToText(debug)

    # Send image-to-text result to Polly
    speech.pollySays(result, debug)


def processCmd(command):
    try:
        if "read" in command:
            readThis(False)
    except KeyboardInterrupt as e:
        logger.LogThis("cortex: processCmd(): CTRL+C interrupt")
    except Exception as e:
        logger.LogError("cortex: processCmd(): {}".format(e))