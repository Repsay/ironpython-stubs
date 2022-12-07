class TransferAreaMappingRule(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Mapping rule for transfer area """
 def Delete(self):
  """
  Delete(self: TransferAreaMappingRule)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: TransferAreaMappingRule,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttribute(self,name):
  """
  GetAttribute(self: TransferAreaMappingRule,name: str) -> object

  

   Gets an attribute with the given name.

  

   name: The name of the attribute to get.

   Returns: The attribute with the given name; otherwise,null.
  """
  pass
 def GetAttributeInfos(self):
  """
  GetAttributeInfos(self: TransferAreaMappingRule) -> IList[EngineeringAttributeInfo]

  

   Returns a collection of EngineeringAttributeInfo objects describing the different attributes on this object.

   Returns: A collection of EngineeringAttributeInfo objects describing the different attributes on this object.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: TransferAreaMappingRule,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TransferAreaMappingRule) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttribute(self,name,value):
  """
  SetAttribute(self: TransferAreaMappingRule,name: str,value: object)

   Sets value of the attribute.

  

   name: The name of the attribute to set.

   value: The value of the attribute to set.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: TransferAreaMappingRule,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: TransferAreaMappingRule) -> str

  

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
 Begin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Bit address of the begin of the mapped data



Get: Begin(self: TransferAreaMappingRule) -> int



Set: Begin(self: TransferAreaMappingRule)=value

"""

 End=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Bit address of the end of the mapped data



Get: End(self: TransferAreaMappingRule) -> int



Set: End(self: TransferAreaMappingRule)=value

"""

 IoType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Type of data to be mapped (Input or Output)



Get: IoType(self: TransferAreaMappingRule) -> AddressIoType



Set: IoType(self: TransferAreaMappingRule)=value

"""

 Offset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Offset of the transfered data



Get: Offset(self: TransferAreaMappingRule) -> int



Set: Offset(self: TransferAreaMappingRule)=value

"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: TransferAreaMappingRule) -> IEngineeringObject



"""

 PositionNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Transfer area mapping rule number



Get: PositionNumber(self: TransferAreaMappingRule) -> int



"""

 Target=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """I/O module or sub-module to be mapped



Get: Target(self: TransferAreaMappingRule) -> DeviceItem



Set: Target(self: TransferAreaMappingRule)=value

"""


