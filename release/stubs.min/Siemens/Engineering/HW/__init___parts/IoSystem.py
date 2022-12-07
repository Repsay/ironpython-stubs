class IoSystem(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents an IO system """
 def Delete(self):
  """
  Delete(self: IoSystem)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: IoSystem,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttribute(self,name):
  """
  GetAttribute(self: IoSystem,name: str) -> object

  

   Gets an attribute with the given name.

  

   name: The name of the attribute to get.

   Returns: The attribute with the given name; otherwise,null.
  """
  pass
 def GetAttributeInfos(self):
  """
  GetAttributeInfos(self: IoSystem) -> IList[EngineeringAttributeInfo]

  

   Returns a collection of EngineeringAttributeInfo objects describing the different attributes on this object.

   Returns: A collection of EngineeringAttributeInfo objects describing the different attributes on this object.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: IoSystem,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: IoSystem) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttribute(self,name,value):
  """
  SetAttribute(self: IoSystem,name: str,value: object)

   Sets value of the attribute.

  

   name: The name of the attribute to set.

   value: The value of the attribute to set.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: IoSystem,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: IoSystem) -> str

  

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
 ConnectedIoDevices=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The connected IO devices



Get: ConnectedIoDevices(self: IoSystem) -> IoConnectorAssociation



"""

 HwIdentifiers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of HW identifiers



Get: HwIdentifiers(self: IoSystem) -> HwIdentifierComposition



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the IO system



Get: Name(self: IoSystem) -> str



Set: Name(self: IoSystem)=value

"""

 Number=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number of this IO system



Get: Number(self: IoSystem) -> int



Set: Number(self: IoSystem)=value

"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: IoSystem) -> IEngineeringObject



"""

 Subnet=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Associated Subnet



Get: Subnet(self: IoSystem) -> Subnet



"""


