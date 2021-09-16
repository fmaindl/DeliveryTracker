from email.message import Message
from DeliveryMonitor_SOAP_Message import SOAPRequest
from datetime import datetime
import logging
from DeliveryMonitor_config import LOG_PATH,MESSAGE
from DeliveryMonitor_Email import EmailHandler





if __name__ == "__main__":

    logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',filename=LOG_PATH, level=logging.DEBUG,datefmt='%Y-%m-%d %H:%M:%S', force=True)
    logging.info("Program Started")

    try:
        request=SOAPRequest.CreateSOAPRequest()
        logging.info("Creating SOAP Request")
    except:
        logging.error("Couldn't create the SOAP Request")

    try:
        response = SOAPRequest.SendSOAPRequest(request)
        soap_message = response[0]
        status = response[1]
        logging.info("SOAP Response:{}".format(status))
  
    except:

        logging.error("SOAP Response:{}".format(status))
    
    try:
        list = SOAPRequest.ParseSOAPResponse(soap_message)
        logging.info("Parsed SOAP Response from TMS. Found {} entries".format(len(list)))

    except:
        logging.error("Couldn't Parse Reponse from TMS")
        
    try:
        duplicate_entries = SOAPRequest.ProcessSOAPResponse(list)
        logging.info("Parsed SOAP Response from TMS. Found {} entries".format(len(duplicate_entries)))
        logging.info("Duplicate entries are: {}".format(duplicate_entries))
    except:
        logging.error("Couldn't Process the XML document")

    if len(duplicate_entries) > 0:
        try: 
            CurrentTime = datetime.now()
            email = EmailHandler.CreateEmail(MESSAGE.format(duplicate_entries),CurrentTime)
        except:
            logging.error("Couldn't create e-mail")
        
        try:
            EmailHandler.SendEmail(email)
        except:
            logging.error("Couldn't send e-mail")


    
