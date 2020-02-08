from mockito import mock, verify
import unittest

from models.provider import Provider

pr = Provider(1111,"TechTrends","Barranquilla",True,False)

#Confirm expected data
pr.Change_Name("ComputersCo")
assert pr.Provider_Name == "ComputersCo"

assert pr.Show_data() == "Provider_ID 1111\nProvider_Name ComputersCo\nProvider_Address Barranquilla\nLocal_Company True\nQuality_Cert False"


#from contracts import contracts

#class ContractsTest(unittest.TestCase):
    #def test_should_issue_(self):
        #out = mock()

        #contracts(out)

        #verify(out).write("Hello world of Python\n")
