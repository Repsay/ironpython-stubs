class Node(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEngineeringServiceProvider,IServiceProvider,IEquatable[object]):
 """ Node is an object which is used as an interface from DeviceItem to Subnet """
 def ConnectToSubnet(self,subnet):
  """
  ConnectToSubnet(self: Node,subnet: Subnet)

   Connects to the Subnet

  

   subnet: The subnet to be connected
  """
  pass
 def CreateAndConnectToSubnet(self,name):
  """
  CreateAndConnectToSubnet(self: Node,name: str) -> Subnet

  

   Create and connect to a subnet

  

   name: The name of the Subnet to create and connect

   Returns: Siemens.Engineering.HW.Subnet
  """
  pass
 def DisconnectFromSubnet(self):
  """
  DisconnectFromSubnet(self: Node)

   Disconnects a device from the given Subnet
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: Node,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttribute(self,name):
  """
  GetAttribute(self: Node,name: str) -> object

  

   Gets an attribute with the given name.

  

   name: The name of the attribute to get.

   Returns: The attribute with the given name; otherwise,null.
  """
  pass
 def GetAttributeInfos(self):
  """
  GetAttributeInfos(self: Node) -> IList[EngineeringAttributeInfo]

  

   Returns a collection of EngineeringAttributeInfo objects describing the different attributes on this object.

   Returns: A collection of EngineeringAttributeInfo objects describing the different attributes on this object.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: Node,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Node) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def GetService(self):
# Error generating skeleton for function GetService: Method must be called on a Type for which Type.IsGenericParameter is false.

 def SetAttribute(self,name,value):
  """
  SetAttribute(self: Node,name: str,value: object)

   Sets value of the attribute.

  

   name: The name of the attribute to set.

   value: The value of the attribute to set.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: Node,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: Node) -> str

  

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
 ConnectedSubnet=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The connected subnet



Get: ConnectedSubnet(self: Node) -> Subnet



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the node



Get: Name(self: Node) -> str



"""

 NodeId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of this node



Get: NodeId(self: Node) -> str



"""

 NodeType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Particular type e.g. Industrial Ethernet or Wireless LAN



Get: NodeType(self: Node) -> NetType



Set: NodeType(self: Node)=value

"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: Node) -> IEngineeringObject



"""


