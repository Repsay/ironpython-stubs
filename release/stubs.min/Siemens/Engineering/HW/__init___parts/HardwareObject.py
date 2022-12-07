class HardwareObject(object,IHardwareCompareTarget,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ The base for hardware modules like devices or device items """
 def CanPlugCopy(self,deviceItem,positionNumber):
  """
  CanPlugCopy(self: HardwareObject,deviceItem: DeviceItem,positionNumber: int) -> bool

  

   Determines if plug can be copied

  

   deviceItem: Device for which the Plug will be moved

   positionNumber: The position number where to create the plug

   Returns: System.Boolean
  """
  pass
 def CanPlugMove(self,deviceItem,positionNumber):
  """
  CanPlugMove(self: HardwareObject,deviceItem: DeviceItem,positionNumber: int) -> bool

  

   Determines if plug can be moved

  

   deviceItem: Device for which the Plug will be moved

   positionNumber: The position number where to create the plug

   Returns: System.Boolean
  """
  pass
 def CanPlugNew(self,typeIdentifier,name,positionNumber):
  """
  CanPlugNew(self: HardwareObject,typeIdentifier: str,name: str,positionNumber: int) -> bool

  

   Determines if plug can be created

  

   typeIdentifier: The type identifier to use to create the plug

   name: The name of the plug to create

   positionNumber: The position number where to create the plug

   Returns: System.Boolean
  """
  pass
 def CompareTo(self,compareTarget):
  """
  CompareTo(self: HardwareObject,compareTarget: IHardwareCompareTarget) -> CompareResult

  

   Compare the hardware object vs the given target

  

   compareTarget: The target to compare to the hardware object

   Returns: Siemens.Engineering.Compare.CompareResult
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: HardwareObject,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttribute(self,name):
  """
  GetAttribute(self: HardwareObject,name: str) -> object

  

   Gets an attribute with the given name.

  

   name: The name of the attribute to get.

   Returns: The attribute with the given name; otherwise,null.
  """
  pass
 def GetAttributeInfos(self):
  """
  GetAttributeInfos(self: HardwareObject) -> IList[EngineeringAttributeInfo]

  

   Returns a collection of EngineeringAttributeInfo objects describing the different attributes on this object.

   Returns: A collection of EngineeringAttributeInfo objects describing the different attributes on this object.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: HardwareObject,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: HardwareObject) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def GetPlugLocations(self):
  """
  GetPlugLocations(self: HardwareObject) -> IList[PlugLocation]

  

   Determine some information about free slots.

   Returns: System.Collections.Generic.IList<Siemens.Engineering.HW.Extensions.PlugLocation>
  """
  pass
 def PlugCopy(self,deviceItem,positionNumber):
  """
  PlugCopy(self: HardwareObject,deviceItem: DeviceItem,positionNumber: int) -> DeviceItem

  

   Copies a plug to a given device

  

   deviceItem: Device for which the Plug will be moved

   positionNumber: The position number where to create the plug

   Returns: Siemens.Engineering.HW.DeviceItem
  """
  pass
 def PlugMove(self,deviceItem,positionNumber):
  """
  PlugMove(self: HardwareObject,deviceItem: DeviceItem,positionNumber: int) -> DeviceItem

  

   Moves a plug to a given device

  

   deviceItem: Device for which the Plug will be moved

   positionNumber: The position number where to create the plug

   Returns: Siemens.Engineering.HW.DeviceItem
  """
  pass
 def PlugNew(self,typeIdentifier,name,positionNumber):
  """
  PlugNew(self: HardwareObject,typeIdentifier: str,name: str,positionNumber: int) -> DeviceItem

  

   Creates and plugs a device item in a given hardware object.

  

   typeIdentifier: The type identifier of the device item to create.

   name: The name of the device item to create.

   positionNumber: The position number where to plug the created device item

   Returns: Siemens.Engineering.HW.DeviceItem
  """
  pass
 def SetAttribute(self,name,value):
  """
  SetAttribute(self: HardwareObject,name: str,value: object)

   Sets value of the attribute.

  

   name: The name of the attribute to set.

   value: The value of the attribute to set.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: HardwareObject,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: HardwareObject) -> str

  

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
 DeviceItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of device items



Get: DeviceItems(self: HardwareObject) -> DeviceItemComposition



"""

 HwIdentifiers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of HW identifiers



Get: HwIdentifiers(self: HardwareObject) -> HwIdentifierComposition



"""

 Items=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Associated device items for this device



Get: Items(self: HardwareObject) -> DeviceItemAssociation



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the device



Get: Name(self: HardwareObject) -> str



Set: Name(self: HardwareObject)=value

"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: HardwareObject) -> IEngineeringObject



"""

 TypeIdentifier=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The type identifier of this device



Get: TypeIdentifier(self: HardwareObject) -> str



"""


