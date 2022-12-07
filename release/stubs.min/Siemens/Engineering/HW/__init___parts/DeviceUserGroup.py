class DeviceUserGroup(DeviceGroup,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEngineeringServiceProvider,IServiceProvider,IEquatable[object],IMasterCopySource,IMasterCopyTarget):
 """ Group containing the devices """
 def Delete(self):
  """
  Delete(self: DeviceUserGroup)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: DeviceUserGroup,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: DeviceUserGroup) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: DeviceUserGroup) -> str

  

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
 Groups=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of device user groups



Get: Groups(self: DeviceUserGroup) -> DeviceUserGroupComposition



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the device user group



Get: Name(self: DeviceUserGroup) -> str



Set: Name(self: DeviceUserGroup)=value

"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: DeviceUserGroup) -> IEngineeringObject



"""


