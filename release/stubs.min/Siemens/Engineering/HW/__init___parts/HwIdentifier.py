class HwIdentifier(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents a HW identifier """
 def Equals(self,obj):
  """
  Equals(self: HwIdentifier,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttribute(self,name):
  """
  GetAttribute(self: HwIdentifier,name: str) -> object

  

   Gets an attribute with the given name.

  

   name: The name of the attribute to get.

   Returns: The attribute with the given name; otherwise,null.
  """
  pass
 def GetAttributeInfos(self):
  """
  GetAttributeInfos(self: HwIdentifier) -> IList[EngineeringAttributeInfo]

  

   Returns a collection of EngineeringAttributeInfo objects describing the different attributes on this object.

   Returns: A collection of EngineeringAttributeInfo objects describing the different attributes on this object.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: HwIdentifier,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: HwIdentifier) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttribute(self,name,value):
  """
  SetAttribute(self: HwIdentifier,name: str,value: object)

   Sets value of the attribute.

  

   name: The name of the attribute to set.

   value: The value of the attribute to set.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: HwIdentifier,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: HwIdentifier) -> str

  

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
 HwIdentifierControllers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Associated Hw identifier controllers



Get: HwIdentifierControllers(self: HwIdentifier) -> HwIdentifierControllerAssociation



"""

 Identifier=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifier for this HW identifier



Get: Identifier(self: HwIdentifier) -> Int64



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: HwIdentifier) -> IEngineeringObject



"""


