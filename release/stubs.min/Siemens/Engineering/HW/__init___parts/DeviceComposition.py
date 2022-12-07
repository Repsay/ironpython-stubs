class DeviceComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[Device],IEquatable[object]):
 """ Composition of Devices """
 def Contains(self,item):
  """
  Contains(self: DeviceComposition,item: Device) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Create(self,typeIdentifier,name):
  """
  Create(self: DeviceComposition,typeIdentifier: str,name: str) -> Device

  

   Creates a Device

  

   typeIdentifier: Type identifier of the device to be created

   name: Name of device to be created

   Returns: Siemens.Engineering.HW.Device
  """
  pass
 def CreateFrom(self,masterCopy):
  """
  CreateFrom(self: DeviceComposition,masterCopy: MasterCopy) -> Device

  

   Create device from MasterCopy

  

   masterCopy: The source master copy

   Returns: Siemens.Engineering.HW.Device
  """
  pass
 def CreateWithItem(self,typeIdentifier,name,deviceName):
  """
  CreateWithItem(self: DeviceComposition,typeIdentifier: str,name: str,deviceName: str) -> Device

  

   Create a device with subcomponents

  

   typeIdentifier: Type identifier of the device to be created with sub items

   name: Name of the device to be created with sub items

   deviceName: The name of the device to create with subcomponents

   Returns: Siemens.Engineering.HW.Device
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: DeviceComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: DeviceComposition,name: str) -> Device

  

   Finds a given device

  

   name: Name to find

   Returns: Siemens.Engineering.HW.Device
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: DeviceComposition) -> IEnumerator[Device]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: DeviceComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: DeviceComposition,item: Device) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: DeviceComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[Device](enumerable: IEnumerable[Device],value: Device) -> bool """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __ne__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the count.



Get: Count(self: DeviceComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: DeviceComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: DeviceComposition) -> IEngineeringObject



"""


