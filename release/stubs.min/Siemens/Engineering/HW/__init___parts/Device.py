class Device(HardwareObject,IHardwareCompareTarget,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object],IMasterCopySource,IMasterCopyTarget,IEngineeringServiceProvider,IServiceProvider):
 """ Device as an container for DeviceItems """
 def Delete(self):
  """
  Delete(self: Device)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: Device,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Device) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def GetService(self):
# Error generating skeleton for function GetService: Method must be called on a Type for which Type.IsGenericParameter is false.

 def ShowInEditor(self,view):
  """
  ShowInEditor(self: Device,view: View)

   Show the indicated item in the HW editor

  

   view: Which view of the HW editor to show
  """
  pass
 def ToString(self):
  """
  ToString(self: Device) -> str

  

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
 IsGsd=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if this device is a Gsd device



Get: IsGsd(self: Device) -> bool



"""

 UnpluggedItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Associate unplugged items



Get: UnpluggedItems(self: Device) -> DeviceItemAssociation



"""


