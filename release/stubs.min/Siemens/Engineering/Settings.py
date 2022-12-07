# encoding: utf-8
# module Siemens.Engineering.Settings calls itself Settings
# from Siemens.Engineering,Version=15.1.0.0,Culture=neutral,PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class TiaPortalSetting(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents a TiaPortal setting. """
 def Equals(self,obj):
  """
  Equals(self: TiaPortalSetting,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: TiaPortalSetting,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TiaPortalSetting) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: TiaPortalSetting,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: TiaPortalSetting) -> str

  

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
 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Represents the name of a TiaPortalSetting.



Get: Name(self: TiaPortalSetting) -> str



Set: Name(self: TiaPortalSetting)=value

"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: TiaPortalSetting) -> IEngineeringObject



"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Represents the value of a TiaPortalSetting.



Get: Value(self: TiaPortalSetting) -> object



Set: Value(self: TiaPortalSetting)=value

"""



class TiaPortalSettingComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[TiaPortalSetting],IEquatable[object]):
 """ Represents a composition of TiaPortalSettings. """
 def Contains(self,item):
  """
  Contains(self: TiaPortalSettingComposition,item: TiaPortalSetting) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: TiaPortalSettingComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: TiaPortalSettingComposition,name: str) -> TiaPortalSetting

  

   Returns the TiaPortalSetting with the matching name.

  

   name: The name of the TiaPortalSetting to find.

   Returns: Siemens.Engineering.Settings.TiaPortalSetting
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: TiaPortalSettingComposition) -> IEnumerator[TiaPortalSetting]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TiaPortalSettingComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: TiaPortalSettingComposition,item: TiaPortalSetting) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: TiaPortalSettingComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[TiaPortalSetting](enumerable: IEnumerable[TiaPortalSetting],value: TiaPortalSetting) -> bool """
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



Get: Count(self: TiaPortalSettingComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: TiaPortalSettingComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: TiaPortalSettingComposition) -> IEngineeringObject



"""



class TiaPortalSettingsFolder(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents a TiaPortal settings folder """
 def Equals(self,obj):
  """
  Equals(self: TiaPortalSettingsFolder,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: TiaPortalSettingsFolder,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TiaPortalSettingsFolder) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: TiaPortalSettingsFolder,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: TiaPortalSettingsFolder) -> str

  

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
 Folders=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of TiaPortalSettingsFolders



Get: Folders(self: TiaPortalSettingsFolder) -> TiaPortalSettingsFolderComposition



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Represents the name of a TiaPortalSettingsFolder.



Get: Name(self: TiaPortalSettingsFolder) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: TiaPortalSettingsFolder) -> IEngineeringObject



"""

 Settings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of TiaPortalSettings



Get: Settings(self: TiaPortalSettingsFolder) -> TiaPortalSettingComposition



"""



class TiaPortalSettingsFolderComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[TiaPortalSettingsFolder],IEquatable[object]):
 """ Composition of TiaPortalSettingsFolders """
 def Contains(self,item):
  """
  Contains(self: TiaPortalSettingsFolderComposition,item: TiaPortalSettingsFolder) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: TiaPortalSettingsFolderComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: TiaPortalSettingsFolderComposition,name: str) -> TiaPortalSettingsFolder

  

   Returns the TiaPortalSettingsFolder with the matching name.

  

   name: The name of the TiaPortalSettingsFolder to find.

   Returns: Siemens.Engineering.Settings.TiaPortalSettingsFolder
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: TiaPortalSettingsFolderComposition) -> IEnumerator[TiaPortalSettingsFolder]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TiaPortalSettingsFolderComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: TiaPortalSettingsFolderComposition,item: TiaPortalSettingsFolder) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: TiaPortalSettingsFolderComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[TiaPortalSettingsFolder](enumerable: IEnumerable[TiaPortalSettingsFolder],value: TiaPortalSettingsFolder) -> bool """
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



Get: Count(self: TiaPortalSettingsFolderComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: TiaPortalSettingsFolderComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: TiaPortalSettingsFolderComposition) -> IEngineeringObject



"""



