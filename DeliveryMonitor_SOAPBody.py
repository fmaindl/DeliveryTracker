import datetime



class SOAPBody():

    def getSOAPBody():
        current_date = datetime.date.today() - datetime.timedelta(days=2)
        body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:cis="http://www.i2.com/cis">
        <soapenv:Header/>
        <soapenv:Body>
            <cis:findEntities>
            <cis:EntityType>ShipmentType</cis:EntityType>
                     <Select>
				<Name>ReferenceNumber4</Name>
				<Name>ShipmentNumber</Name>
				<Name>ShipFromLocationCode</Name>
                <Name>SplitShipmentNumber</Name>
			   </Select>     
                <cis:Filter>
                          <cis:Name>ReferenceNumber4</cis:Name>
                          <cis:Op>NeOrNull</cis:Op>  
                          <cis:Value>000000000</cis:Value>                     
              </cis:Filter>
                <cis:Filter>
                          <cis:Name>CreatedDateTime</cis:Name>
                          <cis:Op>Ge</cis:Op>  
                          <cis:Value>{}</cis:Value>                     
              </cis:Filter>

              <Page>

			      <StartAtRow>0</StartAtRow>

				   <MaxRows>30000</MaxRows>

			    </Page>
               </cis:findEntities>
               </soapenv:Body>
               </soapenv:Envelope>""".format(current_date)
        return body
