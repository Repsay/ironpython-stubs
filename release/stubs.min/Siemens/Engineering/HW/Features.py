# encoding: utf-8
# module Siemens.Engineering.HW.Features calls itself Features
# from Siemens.Engineering,Version=15.1.0.0,Culture=neutral,PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class HardwareFeature(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Base class for all HW related services """
 def Equals(self,obj):
  """
  Equals(self: HardwareFeature,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttribute(self,name):
  """
  GetAttribute(self: HardwareFeature,name: str) -> object

  

   Gets an attribute with the given name.

  

   name: The name of the attribute to get.

   Returns: The attribute with the given name; otherwise,null.
  """
  pass
 def GetAttributeInfos(self):
  """
  GetAttributeInfos(self: HardwareFeature) -> IList[EngineeringAttributeInfo]

  

   Returns a collection of EngineeringAttributeInfo objects describing the different attributes on this object.

   Returns: A collection of EngineeringAttributeInfo objects describing the different attributes on this object.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: HardwareFeature,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: HardwareFeature) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttribute(self,name,value):
  """
  SetAttribute(self: HardwareFeature,name: str,value: object)

   Sets value of the attribute.

  

   name: The name of the attribute to set.

   value: The value of the attribute to set.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: HardwareFeature,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: HardwareFeature) -> str

  

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
 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: HardwareFeature) -> IEngineeringObject



"""



class DeviceItemFeature(HardwareFeature,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Base class for all DeviceItem related services """
 def Equals(self,obj):
  """
  Equals(self: DeviceItemFeature,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: DeviceItemFeature) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: DeviceItemFeature) -> str

  

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
 OwnedBy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """DeviceItem Object that owns this role



Get: OwnedBy(self: DeviceItemFeature) -> DeviceItem



"""



class AddressController(DeviceItemFeature,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object],IEngineeringService):
 """ Address controller device """
 def Equals(self,obj):
  """
  Equals(self: AddressController,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: AddressController) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: AddressController) -> str

  

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
 RegisteredAddresses=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Associated registered address



Get: RegisteredAddresses(self: AddressController) -> AddressAssociation



"""



class AddressControllerAssociation(object,IEngineeringAssociation,IEngineeringInstance,IEnumerable,IInternalAssociationAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[AddressController],IEquatable[object]):
 """ Associated address controllers """
 def Contains(self,item):
  """
  Contains(self: AddressControllerAssociation,item: AddressController) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: AddressControllerAssociation,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: AddressControllerAssociation) -> IEnumerator[AddressController]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: AddressControllerAssociation) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: AddressControllerAssociation,item: AddressController) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: AddressControllerAssociation) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[AddressController](enumerable: IEnumerable[AddressController],value: AddressController) -> bool """
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



Get: Count(self: AddressControllerAssociation) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: AddressControllerAssociation) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent..



Get: Parent(self: AddressControllerAssociation) -> IEngineeringObject



"""



class DeviceFeature(HardwareFeature,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Base class for all Device related services """
 def Equals(self,obj):
  """
  Equals(self: DeviceFeature,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: DeviceFeature) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: DeviceFeature) -> str

  

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
 OwnedBy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Device Object that owns this role



Get: OwnedBy(self: DeviceFeature) -> Device



"""



class FrontPanelDisplay(DeviceItemFeature,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object],IEngineeringService):
 """ Represents the Front Panel Display """
 def Equals(self,obj):
  """
  Equals(self: FrontPanelDisplay,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: FrontPanelDisplay) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetUserDefinedLogo(self,logoImagePath):
  """
  SetUserDefinedLogo(self: FrontPanelDisplay,logoImagePath: FileInfo)

   Sets the Logo on the Display

  

   logoImagePath: Specifies the file info of the logo
  """
  pass
 def ToString(self):
  """
  ToString(self: FrontPanelDisplay) -> str

  

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
 AdaptLogoActivated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Adapt the logo to the display



Get: AdaptLogoActivated(self: FrontPanelDisplay) -> bool



Set: AdaptLogoActivated(self: FrontPanelDisplay)=value

"""

 UserDefinedLogoActivated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Activate or deactivate the User Defined Logo



Get: UserDefinedLogoActivated(self: FrontPanelDisplay) -> bool



Set: UserDefinedLogoActivated(self: FrontPanelDisplay)=value

"""



class IGsdObject:
 """ Properties of a Gsd hardware object """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 GsdId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Gsd ID of the Gsd object



Get: GsdId(self: IGsdObject) -> str



"""

 GsdName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Gsd Name of the Gsd object



Get: GsdName(self: IGsdObject) -> str



"""

 GsdType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Gsd Type of the Gsd object



Get: GsdType(self: IGsdObject) -> str



"""

 IsProfibus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if this Gsd device item supports Profibus



Get: IsProfibus(self: IGsdObject) -> bool



"""

 IsProfinet=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if this Gsd object supports Profinet



Get: IsProfinet(self: IGsdObject) -> bool



"""



class GsdDevice(DeviceFeature,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object],IGsdObject,IEngineeringService):
 """ Represents a Gsd device """
 def Equals(self,obj):
  """
  Equals(self: GsdDevice,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: GsdDevice) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: GsdDevice) -> str

  

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
 GsdId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Gsd ID of the Gsd object



Get: GsdId(self: GsdDevice) -> str



"""

 GsdName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Gsd Name of the Gsd object



Get: GsdName(self: GsdDevice) -> str



"""

 GsdType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Gsd Type of the Gsd object



Get: GsdType(self: GsdDevice) -> str



"""

 IsProfibus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if this Gsd device item supports Profibus



Get: IsProfibus(self: GsdDevice) -> bool



"""

 IsProfinet=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if this Gsd object supports Profinet



Get: IsProfinet(self: GsdDevice) -> bool



"""



class GsdDeviceItem(DeviceItemFeature,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object],IGsdObject,IEngineeringService):
 """ Represents a Gsd device item """
 def Equals(self,obj):
  """
  Equals(self: GsdDeviceItem,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: GsdDeviceItem) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def GetPrmData(self,dsNumber,byteOffset,length):
  """
  GetPrmData(self: GsdDeviceItem,dsNumber: int,byteOffset: int,length: int) -> Array[Byte]

  

   Returns the Prm Data for this Gsd device item

  

   dsNumber: Specifies which dsNumber to set the Prm Data to this Gsd device item

   byteOffset: The byte offset

   length: Specifies which length to get the Prm Data from this Gsd device item

   Returns: System.Byte[]
  """
  pass
 def SetPrmData(self,dsNumber,byteOffset,prmData):
  """ SetPrmData(self: GsdDeviceItem,dsNumber: int,byteOffset: int,prmData: IEnumerable[Byte]) """
  pass
 def ToString(self):
  """
  ToString(self: GsdDeviceItem) -> str

  

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
 GsdId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Gsd ID of the Gsd object



Get: GsdId(self: GsdDeviceItem) -> str



"""

 GsdName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Gsd Name of the Gsd object



Get: GsdName(self: GsdDeviceItem) -> str



"""

 GsdType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Gsd Type of the Gsd object



Get: GsdType(self: GsdDeviceItem) -> str



"""

 IsProfibus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if this Gsd device item supports Profibus



Get: IsProfibus(self: GsdDeviceItem) -> bool



"""

 IsProfinet=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if this Gsd object supports Profinet



Get: IsProfinet(self: GsdDeviceItem) -> bool



"""



class HwIdentifierController(DeviceItemFeature,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object],IEngineeringService):
 """ Represents a HW identifier controller """
 def Equals(self,obj):
  """
  Equals(self: HwIdentifierController,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: HwIdentifierController) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: HwIdentifierController) -> str

  

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
 RegisteredHwIdentifiers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Associated registered HW identifiers



Get: RegisteredHwIdentifiers(self: HwIdentifierController) -> HwIdentifierAssociation



"""



class HwIdentifierControllerAssociation(object,IEngineeringAssociation,IEngineeringInstance,IEnumerable,IInternalAssociationAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[HwIdentifierController],IEquatable[object]):
 """ Associated Hw identifier controllers """
 def Contains(self,item):
  """
  Contains(self: HwIdentifierControllerAssociation,item: HwIdentifierController) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: HwIdentifierControllerAssociation,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: HwIdentifierControllerAssociation) -> IEnumerator[HwIdentifierController]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: HwIdentifierControllerAssociation) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: HwIdentifierControllerAssociation,item: HwIdentifierController) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: HwIdentifierControllerAssociation) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[HwIdentifierController](enumerable: IEnumerable[HwIdentifierController],value: HwIdentifierController) -> bool """
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



Get: Count(self: HwIdentifierControllerAssociation) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: HwIdentifierControllerAssociation) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent..



Get: Parent(self: HwIdentifierControllerAssociation) -> IEngineeringObject



"""



class NetworkInterface(DeviceItemFeature,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object],IEngineeringService):
 """ Represents a HW interface """
 def Equals(self,obj):
  """
  Equals(self: NetworkInterface,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: NetworkInterface) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: NetworkInterface) -> str

  

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
 InterfaceOperatingMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The operating mode of this interface



Get: InterfaceOperatingMode(self: NetworkInterface) -> InterfaceOperatingModes



Set: InterfaceOperatingMode(self: NetworkInterface)=value

"""

 InterfaceType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The type of this interface



Get: InterfaceType(self: NetworkInterface) -> NetType



Set: InterfaceType(self: NetworkInterface)=value

"""

 IoConnectors=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of IO connectors



Get: IoConnectors(self: NetworkInterface) -> IoConnectorComposition



"""

 IoControllers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of IO controllers



Get: IoControllers(self: NetworkInterface) -> IoControllerComposition



"""

 Nodes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of nodes



Get: Nodes(self: NetworkInterface) -> NodeComposition



"""

 Ports=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Associated ports



Get: Ports(self: NetworkInterface) -> NetworkPortAssociation



"""

 TransferAreas=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of transfer areas



Get: TransferAreas(self: NetworkInterface) -> TransferAreaComposition



"""



class NetworkPort(DeviceItemFeature,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object],IEngineeringService):
 """ Represents a port on a device item """
 def ConnectToPort(self,partnerPort):
  """
  ConnectToPort(self: NetworkPort,partnerPort: NetworkPort)

   Connects to the Port

  

   partnerPort: The partner port to be disconnected
  """
  pass
 def DisconnectFromPort(self,partnerPort):
  """
  DisconnectFromPort(self: NetworkPort,partnerPort: NetworkPort)

   Disconnects a device from the given port

  

   partnerPort: The partner port to be disconnected
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: NetworkPort,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: NetworkPort) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: NetworkPort) -> str

  

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
 ConnectedPorts=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Internal use only



Get: ConnectedPorts(self: NetworkPort) -> NetworkPortAssociation



"""

 Interface=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The interface supported by this port



Get: Interface(self: NetworkPort) -> NetworkInterface



"""



class NetworkPortAssociation(object,IEngineeringAssociation,IEngineeringInstance,IEnumerable,IInternalAssociationAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[NetworkPort],IEquatable[object]):
 """ Associated ports """
 def Contains(self,item):
  """
  Contains(self: NetworkPortAssociation,item: NetworkPort) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: NetworkPortAssociation,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: NetworkPortAssociation) -> IEnumerator[NetworkPort]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: NetworkPortAssociation) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: NetworkPortAssociation,item: NetworkPort) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: NetworkPortAssociation) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[NetworkPort](enumerable: IEnumerable[NetworkPort],value: NetworkPort) -> bool """
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



Get: Count(self: NetworkPortAssociation) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: NetworkPortAssociation) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent..



Get: Parent(self: NetworkPortAssociation) -> IEngineeringObject



"""



class PcInterfaceAssignment(DeviceItemFeature,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object],IEngineeringService):
 """ Interface Assignment Provider """
 def AssignInterface(self,interfaceAssignmentFor,softwareTarget=None):
  """
  AssignInterface(self: PcInterfaceAssignment,interfaceAssignmentFor: PcInterfaceAssignmentMode)

   Assign interface to one of the following( None,PC Station)

  

   interfaceAssignmentFor: assignment type for interface

  AssignInterface(self: PcInterfaceAssignment,interfaceAssignmentFor: PcInterfaceAssignmentMode,softwareTarget: DeviceItem)

   Assign interface to Software PLC

  

   interfaceAssignmentFor: assignment type for interface

   softwareTarget: if interface assignment will be to CPU,provide cpu device item
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: PcInterfaceAssignment,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAvailableIPCExpansions(self):
  """
  GetAvailableIPCExpansions(self: PcInterfaceAssignment) -> IEnumerable[str]

  

   Get available IPC expansion list that can be selected

   Returns: System.Collections.Generic.IEnumerable<System.String>
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PcInterfaceAssignment) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: PcInterfaceAssignment) -> str

  

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
 HardwareResource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get or set hardware resource of interface



Get: HardwareResource(self: PcInterfaceAssignment) -> HardwareResource



Set: HardwareResource(self: PcInterfaceAssignment)=value

"""

 IpcExpansion=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get or set hardware IPC Expansion of interface



Get: IpcExpansion(self: PcInterfaceAssignment) -> str



Set: IpcExpansion(self: PcInterfaceAssignment)=value

"""

 PcInterfaceAssignmentMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns type of interface assignment



Get: PcInterfaceAssignmentMode(self: PcInterfaceAssignment) -> PcInterfaceAssignmentMode



"""

 SoftwarePlc=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns cpu DeviceItem



Get: SoftwarePlc(self: PcInterfaceAssignment) -> DeviceItem



"""



class PlcAccessLevelProvider(DeviceItemFeature,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object],IEngineeringService):
 """ Represents the Access level of the PLC Plus """
 def Equals(self,obj):
  """
  Equals(self: PlcAccessLevelProvider,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcAccessLevelProvider) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ResetPassword(self,accessLevelType):
  """
  ResetPassword(self: PlcAccessLevelProvider,accessLevelType: PlcProtectionAccessLevel)

   Reset the password for the specific Access Level Type

  

   accessLevelType: Specifies the Access level type
  """
  pass
 def SetPassword(self,accessLevelType,password):
  """
  SetPassword(self: PlcAccessLevelProvider,accessLevelType: PlcProtectionAccessLevel,password: SecureString)

   set the password for the specific Access Level Type

  

   accessLevelType: Specifies the protection Access level type

   password: Specifies the password for the access level type
  """
  pass
 def ToString(self):
  """
  ToString(self: PlcAccessLevelProvider) -> str

  

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
 PlcProtectionAccessLevel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """To set the protection access level type



Get: PlcProtectionAccessLevel(self: PlcAccessLevelProvider) -> PlcProtectionAccessLevel



Set: PlcProtectionAccessLevel(self: PlcAccessLevelProvider)=value

"""



class SoftwareContainer(DeviceItemFeature,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object],IEngineeringService):
 """ Represents a class containing software components """
 def Equals(self,obj):
  """
  Equals(self: SoftwareContainer,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: SoftwareContainer) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: SoftwareContainer) -> str

  

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
 Software=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the software target containing the software elements of the device



Get: Software(self: SoftwareContainer) -> Software



"""



class SubnetOwner(DeviceItemFeature,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object],IEngineeringService):
 """ Represents a Subnet owner """
 def Equals(self,obj):
  """
  Equals(self: SubnetOwner,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: SubnetOwner) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: SubnetOwner) -> str

  

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
 Subnets=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of Subnets



Get: Subnets(self: SubnetOwner) -> SubnetComposition



"""



