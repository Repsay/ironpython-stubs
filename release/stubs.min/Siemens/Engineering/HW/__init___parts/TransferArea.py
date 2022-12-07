class TransferArea(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Addressmapping between local I-Slave / I-device and remote partner """
 def Delete(self):
  """
  Delete(self: TransferArea)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: TransferArea,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttribute(self,name):
  """
  GetAttribute(self: TransferArea,name: str) -> object

  

   Gets an attribute with the given name.

  

   name: The name of the attribute to get.

   Returns: The attribute with the given name; otherwise,null.
  """
  pass
 def GetAttributeInfos(self):
  """
  GetAttributeInfos(self: TransferArea) -> IList[EngineeringAttributeInfo]

  

   Returns a collection of EngineeringAttributeInfo objects describing the different attributes on this object.

   Returns: A collection of EngineeringAttributeInfo objects describing the different attributes on this object.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: TransferArea,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TransferArea) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttribute(self,name,value):
  """
  SetAttribute(self: TransferArea,name: str,value: object)

   Sets value of the attribute.

  

   name: The name of the attribute to set.

   value: The value of the attribute to set.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: TransferArea,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: TransferArea) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __ne__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 Direction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Direction of data communication between local and partner device



Get: Direction(self: TransferArea) -> TransferAreaDirection



Set: Direction(self: TransferArea)=value

"""

 LocalAddresses=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Local addresses of a transfer area



Get: LocalAddresses(self: TransferArea) -> AddressComposition



"""

 LocalToPartnerLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Length of transferred data from local to partner device



Get: LocalToPartnerLength(self: TransferArea) -> int



Set: LocalToPartnerLength(self: TransferArea)=value

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Name of the transfer area



Get: Name(self: TransferArea) -> str



Set: Name(self: TransferArea)=value

"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: TransferArea) -> IEngineeringObject



"""

 PartnerAddresses=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Partner addresses of a transfer area



Get: PartnerAddresses(self: TransferArea) -> AddressComposition



"""

 PartnerToLocalLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Length of transferred data from partner to local device



Get: PartnerToLocalLength(self: TransferArea) -> int



Set: PartnerToLocalLength(self: TransferArea)=value

"""

 PositionNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Subslotnumber / Slotnumber of transfer area



Get: PositionNumber(self: TransferArea) -> int



"""

 TransferAreaMappingRules=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Mapping rules for transfer areas



Get: TransferAreaMappingRules(self: TransferArea) -> TransferAreaMappingRuleComposition



"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Transfer area type



Get: Type(self: TransferArea) -> TransferAreaType



Set: Type(self: TransferArea)=value

"""


