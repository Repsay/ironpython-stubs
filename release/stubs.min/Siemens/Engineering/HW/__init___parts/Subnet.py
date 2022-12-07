class Subnet(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IMasterCopySource,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEngineeringServiceProvider,IServiceProvider,IEquatable[object]):
 """ Represents a Subnet,one of the following (SubnetMpi or SubnetIE) represents the net object """
 def Delete(self):
  """
  Delete(self: Subnet)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: Subnet,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttribute(self,name):
  """
  GetAttribute(self: Subnet,name: str) -> object

  

   Gets an attribute with the given name.

  

   name: The name of the attribute to get.

   Returns: The attribute with the given name; otherwise,null.
  """
  pass
 def GetAttributeInfos(self):
  """
  GetAttributeInfos(self: Subnet) -> IList[EngineeringAttributeInfo]

  

   Returns a collection of EngineeringAttributeInfo objects describing the different attributes on this object.

   Returns: A collection of EngineeringAttributeInfo objects describing the different attributes on this object.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: Subnet,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Subnet) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def GetService(self):
# Error generating skeleton for function GetService: Method must be called on a Type for which Type.IsGenericParameter is false.

 def SetAttribute(self,name,value):
  """
  SetAttribute(self: Subnet,name: str,value: object)

   Sets value of the attribute.

  

   name: The name of the attribute to set.

   value: The value of the attribute to set.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: Subnet,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: Subnet) -> str

  

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
 IoSystems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Associated IO systems



Get: IoSystems(self: Subnet) -> IoSystemAssociation



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the Subnet



Get: Name(self: Subnet) -> str



Set: Name(self: Subnet)=value

"""

 NetType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Particular subnet net type



Get: NetType(self: Subnet) -> NetType



"""

 Nodes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Associated nodes



Get: Nodes(self: Subnet) -> NodeAssociation



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: Subnet) -> IEngineeringObject



"""

 TypeIdentifier=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The type identifier of this Subnet



Get: TypeIdentifier(self: Subnet) -> str



"""


