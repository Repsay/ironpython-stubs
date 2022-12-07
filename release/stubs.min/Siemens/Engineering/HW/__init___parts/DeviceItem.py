class DeviceItem(HardwareObject,IHardwareCompareTarget,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object],IMasterCopySource,IEngineeringServiceProvider,IServiceProvider):
 """ DeviceItem object as representation of a hardware module """
 def Delete(self):
  """
  Delete(self: DeviceItem)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: DeviceItem,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: DeviceItem) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def GetService(self):
# Error generating skeleton for function GetService: Method must be called on a Type for which Type.IsGenericParameter is false.

 def ToString(self):
  """
  ToString(self: DeviceItem) -> str

  

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
 def __str__(self,*args):
  pass
 Addresses=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of addresses



Get: Addresses(self: DeviceItem) -> AddressComposition



"""

 Channels=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of channels



Get: Channels(self: DeviceItem) -> ChannelComposition



"""

 Classification=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The classifications a device item can belong to; Flags-enum



Get: Classification(self: DeviceItem) -> DeviceItemClassifications



"""

 Container=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This is the object where other DeviceItems are placed



Get: Container(self: DeviceItem) -> HardwareObject



"""

 IsBuiltIn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the device item is built into the device



Get: IsBuiltIn(self: DeviceItem) -> bool



"""

 IsPlugged=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if this device item is plugged into a device



Get: IsPlugged(self: DeviceItem) -> bool



"""

 PositionNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Position number of this device item



Get: PositionNumber(self: DeviceItem) -> int



"""


