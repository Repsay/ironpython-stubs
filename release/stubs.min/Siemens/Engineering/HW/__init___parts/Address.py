class Address(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ The object holding the address data """
 def AssignProcessImageToOrganizationBlock(self,organizationBlock):
  """
  AssignProcessImageToOrganizationBlock(self: Address,organizationBlock: OB)

   Assign the current process image to the OB.

  

   organizationBlock: The organizational block to assign.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: Address,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttribute(self,name):
  """
  GetAttribute(self: Address,name: str) -> object

  

   Gets an attribute with the given name.

  

   name: The name of the attribute to get.

   Returns: The attribute with the given name; otherwise,null.
  """
  pass
 def GetAttributeInfos(self):
  """
  GetAttributeInfos(self: Address) -> IList[EngineeringAttributeInfo]

  

   Returns a collection of EngineeringAttributeInfo objects describing the different attributes on this object.

   Returns: A collection of EngineeringAttributeInfo objects describing the different attributes on this object.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: Address,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Address) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttribute(self,name,value):
  """
  SetAttribute(self: Address,name: str,value: object)

   Sets value of the attribute.

  

   name: The name of the attribute to set.

   value: The value of the attribute to set.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: Address,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: Address) -> str

  

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
 AddressControllers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Address's associated AddressControllers



Get: AddressControllers(self: Address) -> AddressControllerAssociation



"""

 IoType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The IO type of the address



Get: IoType(self: Address) -> AddressIoType



"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Length of the address



Get: Length(self: Address) -> int



Set: Length(self: Address)=value

"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: Address) -> IEngineeringObject



"""

 StartAddress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The start address of this address



Get: StartAddress(self: Address) -> int



Set: StartAddress(self: Address)=value

"""


