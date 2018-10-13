# WSDL
If you see xml in the requsts or responses, then it could be sending SOAP for communication and xml.
If the server has those, then it could have vulnerable wsdl endpint available.

You can find wsdl's from endpoits using *?wsdl* as the end of teh url:
```
http://webservice.example:1234/foo?WSDL
```
