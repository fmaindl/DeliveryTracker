from DeliveryMonitor_config import URL_WEB_SERVICES,ENCODED_BASIC_AUTH,XML_WRAPPER
from DeliveryMonitor_SOAPBody import SOAPBody
import requests
import xml.etree.ElementTree




class SOAPRequest():

    def CreateSOAPRequest():
        

        request = SOAPBody.getSOAPBody()
        
        return request

    def SendSOAPRequest(request):
        
        url = URL_WEB_SERVICES
        
        response = requests.post(url,data = request, headers={"Content-Type": "text/xml;charset=UTF-8","SOAPAction": "findEntities","Authorization": "{}".format(ENCODED_BASIC_AUTH)})
        status = response.status_code
        return response.content, status

    def ParseSOAPResponse(response):

        shipment_list=[]

        root = xml.etree.ElementTree.fromstring(response)

        for i in root.iter('{}Shipment'.format(XML_WRAPPER)):
            temp_list=[]
            for j in i: 
                if j.tag == '{}ReferenceNumber4'.format(XML_WRAPPER) and len(temp_list) == 2:
                    temp_list.append('')
                    temp_list.append(j.text)
                else:
                    temp_list.append(j.text)
            shipment_list.append(temp_list)
        temp_list.clear

        return shipment_list
            
    def ProcessSOAPResponse(shipment_list):

        doublons = []

        for i in shipment_list:
            position = shipment_list.index(i)+1
            for j in range(position, len(shipment_list)):
                shipment_list[j]
                if i[3] == shipment_list[j][3] and (i[2] != shipment_list[j][2] or (i[2] == '' and shipment_list[j][2] == '')):
                    doublons.append([i[0], i[1], i[3]])
                    doublons.append([shipment_list[j][0],shipment_list[j][1],shipment_list[j][3]])
        return doublons
            












