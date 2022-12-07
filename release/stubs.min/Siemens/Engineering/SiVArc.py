# encoding: utf-8
# module Siemens.Engineering.SiVArc calls itself SiVArc
# from Siemens.Engineering,Version=15.1.0.0,Culture=neutral,PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AlarmRule(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents alarm rule object """
 def Delete(self):
  """
  Delete(self: AlarmRule)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: AlarmRule,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: AlarmRule,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: AlarmRule) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: AlarmRule,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: AlarmRule) -> str

  

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
 Comment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Alarm rule comment



Get: Comment(self: AlarmRule) -> str



"""

 Condition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Alarm rule condition



Get: Condition(self: AlarmRule) -> str



"""

 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Checks whether alarm rule is selected



Get: Enabled(self: AlarmRule) -> bool



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Alarm rule name



Get: Name(self: AlarmRule) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: AlarmRule) -> IEngineeringObject



"""



class AlarmRuleComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[AlarmRule],IEquatable[object]):
 """ Collection of immediate alarm rules """
 def Contains(self,item):
  """
  Contains(self: AlarmRuleComposition,item: AlarmRule) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def CreateFrom(self,ruleMasterCopy,createOption=None):
  """
  CreateFrom(self: AlarmRuleComposition,ruleMasterCopy: MasterCopy) -> AlarmRule

  

   Copy alarm rule from library to project with default replace option

  

   ruleMasterCopy: Alarm rule master copy

   Returns: Siemens.Engineering.SiVArc.AlarmRule

  CreateFrom(self: AlarmRuleComposition,ruleMasterCopy: MasterCopy,createOption: CreateOptions) -> AlarmRule

  

   Copy alarm rule from library to project with create options

  

   ruleMasterCopy: Alarm rule master copy

   createOption: Create option

   Returns: Siemens.Engineering.SiVArc.AlarmRule
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: AlarmRuleComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: AlarmRuleComposition,name: str) -> AlarmRule

  

   Finds alarm rule based on name

  

   name: Alarm rule name

   Returns: Siemens.Engineering.SiVArc.AlarmRule
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: AlarmRuleComposition) -> IEnumerator[AlarmRule]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: AlarmRuleComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: AlarmRuleComposition,item: AlarmRule) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: AlarmRuleComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[AlarmRule](enumerable: IEnumerable[AlarmRule],value: AlarmRule) -> bool """
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



Get: Count(self: AlarmRuleComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: AlarmRuleComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: AlarmRuleComposition) -> IEngineeringObject



"""



class AlarmRuleGroup(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents alarm rule group """
 def Delete(self):
  """
  Delete(self: AlarmRuleGroup)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: AlarmRuleGroup,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: AlarmRuleGroup,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: AlarmRuleGroup) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: AlarmRuleGroup,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: AlarmRuleGroup) -> str

  

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
 Comment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Alarm rule group comment



Get: Comment(self: AlarmRuleGroup) -> str



"""

 Condition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Alarm rule group condition



Get: Condition(self: AlarmRuleGroup) -> str



"""

 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Checks whether alarm rule group is selected



Get: Enabled(self: AlarmRuleGroup) -> bool



"""

 Groups=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Collection of immediate groups



Get: Groups(self: AlarmRuleGroup) -> AlarmRuleGroupComposition



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Alarm rule group name



Get: Name(self: AlarmRuleGroup) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: AlarmRuleGroup) -> IEngineeringObject



"""

 Rules=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Collection of immediate rules



Get: Rules(self: AlarmRuleGroup) -> AlarmRuleComposition



"""



class AlarmRuleGroupComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[AlarmRuleGroup],IEquatable[object]):
 """ Collection of immediate alarm rule groups """
 def Contains(self,item):
  """
  Contains(self: AlarmRuleGroupComposition,item: AlarmRuleGroup) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def CreateFrom(self,groupMasterCopy,createOption=None):
  """
  CreateFrom(self: AlarmRuleGroupComposition,groupMasterCopy: MasterCopy) -> AlarmRuleGroup

  

   Copy alarm rule group from library to project with default replace option

  

   groupMasterCopy: Alarm rule group master copy

   Returns: Siemens.Engineering.SiVArc.AlarmRuleGroup

  CreateFrom(self: AlarmRuleGroupComposition,groupMasterCopy: MasterCopy,createOption: CreateOptions) -> AlarmRuleGroup

  

   Copy alarm rule group from library to project with create options

  

   groupMasterCopy: Alarm rule group master copy

   createOption: Create option

   Returns: Siemens.Engineering.SiVArc.AlarmRuleGroup
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: AlarmRuleGroupComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: AlarmRuleGroupComposition,name: str) -> AlarmRuleGroup

  

   Finds alarm rule group based on name

  

   name: Alarm rule group name

   Returns: Siemens.Engineering.SiVArc.AlarmRuleGroup
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: AlarmRuleGroupComposition) -> IEnumerator[AlarmRuleGroup]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: AlarmRuleGroupComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: AlarmRuleGroupComposition,item: AlarmRuleGroup) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: AlarmRuleGroupComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[AlarmRuleGroup](enumerable: IEnumerable[AlarmRuleGroup],value: AlarmRuleGroup) -> bool """
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



Get: Count(self: AlarmRuleGroupComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: AlarmRuleGroupComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: AlarmRuleGroupComposition) -> IEngineeringObject



"""



class AlarmRules(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents alarm rules editor """
 def Equals(self,obj):
  """
  Equals(self: AlarmRules,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: AlarmRules,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: AlarmRules) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: AlarmRules,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: AlarmRules) -> str

  

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
 Groups=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Navigate to all immediate alarm rule groups



Get: Groups(self: AlarmRules) -> AlarmRuleGroupComposition



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: AlarmRules) -> IEngineeringObject



"""

 Rules=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Navigate to all immediate alarm rules



Get: Rules(self: AlarmRules) -> AlarmRuleComposition



"""



class CopyRule(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents copy rule object """
 def Delete(self):
  """
  Delete(self: CopyRule)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: CopyRule,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: CopyRule,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: CopyRule) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: CopyRule,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: CopyRule) -> str

  

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
 Comment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Copy rule comment



Get: Comment(self: CopyRule) -> str



"""

 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Checks whether copy rule is selected



Get: Enabled(self: CopyRule) -> bool



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Copy rule name



Get: Name(self: CopyRule) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: CopyRule) -> IEngineeringObject



"""



class CopyRuleComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[CopyRule],IEquatable[object]):
 """ Collection of immediate copy rules """
 def Contains(self,item):
  """
  Contains(self: CopyRuleComposition,item: CopyRule) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def CreateFrom(self,ruleMasterCopy,createOption=None):
  """
  CreateFrom(self: CopyRuleComposition,ruleMasterCopy: MasterCopy) -> CopyRule

  

   Copy the copy rule from library to project with default replace option

  

   ruleMasterCopy: Copy rule master copy

   Returns: Siemens.Engineering.SiVArc.CopyRule

  CreateFrom(self: CopyRuleComposition,ruleMasterCopy: MasterCopy,createOption: CreateOptions) -> CopyRule

  

   Copy the copy rule from library to project with create options

  

   ruleMasterCopy: Copy rule master copy

   createOption: Create option

   Returns: Siemens.Engineering.SiVArc.CopyRule
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: CopyRuleComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: CopyRuleComposition,name: str) -> CopyRule

  

   Finds copy rule based on name

  

   name: Copy rule name

   Returns: Siemens.Engineering.SiVArc.CopyRule
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: CopyRuleComposition) -> IEnumerator[CopyRule]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: CopyRuleComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: CopyRuleComposition,item: CopyRule) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: CopyRuleComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[CopyRule](enumerable: IEnumerable[CopyRule],value: CopyRule) -> bool """
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



Get: Count(self: CopyRuleComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: CopyRuleComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: CopyRuleComposition) -> IEngineeringObject



"""



class CopyRuleGroup(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents copy rule group """
 def Delete(self):
  """
  Delete(self: CopyRuleGroup)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: CopyRuleGroup,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: CopyRuleGroup,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: CopyRuleGroup) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: CopyRuleGroup,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: CopyRuleGroup) -> str

  

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
 Comment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Copy rule group comment



Get: Comment(self: CopyRuleGroup) -> str



"""

 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Checks whether copy rule group is selected



Get: Enabled(self: CopyRuleGroup) -> bool



"""

 Groups=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Collection of immediate groups



Get: Groups(self: CopyRuleGroup) -> CopyRuleGroupComposition



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Copy rule group name



Get: Name(self: CopyRuleGroup) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: CopyRuleGroup) -> IEngineeringObject



"""

 Rules=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Collection of immediate rules



Get: Rules(self: CopyRuleGroup) -> CopyRuleComposition



"""



class CopyRuleGroupComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[CopyRuleGroup],IEquatable[object]):
 """ Collection of immediate copy rule groups """
 def Contains(self,item):
  """
  Contains(self: CopyRuleGroupComposition,item: CopyRuleGroup) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def CreateFrom(self,groupMasterCopy,createOption=None):
  """
  CreateFrom(self: CopyRuleGroupComposition,groupMasterCopy: MasterCopy) -> CopyRuleGroup

  

   Copy the copy rule group from library to project with default replace option

  

   groupMasterCopy: Copy rule group master copy

   Returns: Siemens.Engineering.SiVArc.CopyRuleGroup

  CreateFrom(self: CopyRuleGroupComposition,groupMasterCopy: MasterCopy,createOption: CreateOptions) -> CopyRuleGroup

  

   Copy the copy rule group from library to project with create options

  

   groupMasterCopy: Copy rule group master copy

   createOption: Create option

   Returns: Siemens.Engineering.SiVArc.CopyRuleGroup
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: CopyRuleGroupComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: CopyRuleGroupComposition,name: str) -> CopyRuleGroup

  

   Finds copy rule group based on name

  

   name: Copy rule group name

   Returns: Siemens.Engineering.SiVArc.CopyRuleGroup
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: CopyRuleGroupComposition) -> IEnumerator[CopyRuleGroup]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: CopyRuleGroupComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: CopyRuleGroupComposition,item: CopyRuleGroup) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: CopyRuleGroupComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[CopyRuleGroup](enumerable: IEnumerable[CopyRuleGroup],value: CopyRuleGroup) -> bool """
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



Get: Count(self: CopyRuleGroupComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: CopyRuleGroupComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: CopyRuleGroupComposition) -> IEngineeringObject



"""



class CopyRules(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents copy rules editor """
 def Equals(self,obj):
  """
  Equals(self: CopyRules,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: CopyRules,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: CopyRules) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: CopyRules,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: CopyRules) -> str

  

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
 Groups=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Navigate to all immediate copy rule groups



Get: Groups(self: CopyRules) -> CopyRuleGroupComposition



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: CopyRules) -> IEngineeringObject



"""

 Rules=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Navigate to all immediate copy rules



Get: Rules(self: CopyRules) -> CopyRuleComposition



"""



class CreateOptions(Enum,IComparable,IFormattable,IConvertible):
 """
 Indicates the kind of create options

 

 enum CreateOptions,values: Rename (1),Replace (0)
 """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Rename=None
 Replace=None
 value__=None


class GenerationOptions(Enum,IComparable,IFormattable,IConvertible):
 """
 Indicates the kind of generation options

 

 enum (flags) GenerationOptions,values: AllTags (1),FullGeneration (4),None (0),UsedHmiTags (2)
 """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 AllTags=None
 FullGeneration=None
 None=None
 UsedHmiTags=None
 value__=None


class MessageType(Enum,IComparable,IFormattable,IConvertible):
 """
 Message type

 

 enum MessageType,values: Error (0),Information (2),Warning (1)
 """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Error=None
 Information=None
 value__=None
 Warning=None


class ScreenRule(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents screen rule object """
 def Delete(self):
  """
  Delete(self: ScreenRule)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: ScreenRule,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: ScreenRule,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: ScreenRule) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: ScreenRule,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: ScreenRule) -> str

  

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
 Comment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Screen rule comment



Get: Comment(self: ScreenRule) -> str



"""

 Condition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Screen rule condition



Get: Condition(self: ScreenRule) -> str



"""

 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Checks whether screen rule is selected



Get: Enabled(self: ScreenRule) -> bool



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Screen rule name



Get: Name(self: ScreenRule) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: ScreenRule) -> IEngineeringObject



"""



class ScreenRuleComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[ScreenRule],IEquatable[object]):
 """ Collection of immediate screen rules """
 def Contains(self,item):
  """
  Contains(self: ScreenRuleComposition,item: ScreenRule) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def CreateFrom(self,ruleMasterCopy,createOption=None):
  """
  CreateFrom(self: ScreenRuleComposition,ruleMasterCopy: MasterCopy) -> ScreenRule

  

   Copy screen rule from library to project with default replace option

  

   ruleMasterCopy: Screen rule master copy

   Returns: Siemens.Engineering.SiVArc.ScreenRule

  CreateFrom(self: ScreenRuleComposition,ruleMasterCopy: MasterCopy,createOption: CreateOptions) -> ScreenRule

  

   Copy screen rule from library to project with create options

  

   ruleMasterCopy: Screen rule master copy

   createOption: Create option

   Returns: Siemens.Engineering.SiVArc.ScreenRule
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: ScreenRuleComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: ScreenRuleComposition,name: str) -> ScreenRule

  

   Finds screen rule based on name

  

   name: Screen rule name

   Returns: Siemens.Engineering.SiVArc.ScreenRule
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: ScreenRuleComposition) -> IEnumerator[ScreenRule]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: ScreenRuleComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: ScreenRuleComposition,item: ScreenRule) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: ScreenRuleComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[ScreenRule](enumerable: IEnumerable[ScreenRule],value: ScreenRule) -> bool """
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



Get: Count(self: ScreenRuleComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: ScreenRuleComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: ScreenRuleComposition) -> IEngineeringObject



"""



class ScreenRuleGroup(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents screen rule group """
 def Delete(self):
  """
  Delete(self: ScreenRuleGroup)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: ScreenRuleGroup,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: ScreenRuleGroup,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: ScreenRuleGroup) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: ScreenRuleGroup,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: ScreenRuleGroup) -> str

  

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
 Comment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Screen rule group comment



Get: Comment(self: ScreenRuleGroup) -> str



"""

 Condition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Screen rule group condition



Get: Condition(self: ScreenRuleGroup) -> str



"""

 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Checks whether screen rule group is selected



Get: Enabled(self: ScreenRuleGroup) -> bool



"""

 Groups=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Collection of immediate groups



Get: Groups(self: ScreenRuleGroup) -> ScreenRuleGroupComposition



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Screen rule group name



Get: Name(self: ScreenRuleGroup) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: ScreenRuleGroup) -> IEngineeringObject



"""

 Rules=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Collection of immediate rules



Get: Rules(self: ScreenRuleGroup) -> ScreenRuleComposition



"""



class ScreenRuleGroupComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[ScreenRuleGroup],IEquatable[object]):
 """ Collection of immediate screen rule groups """
 def Contains(self,item):
  """
  Contains(self: ScreenRuleGroupComposition,item: ScreenRuleGroup) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def CreateFrom(self,groupMasterCopy,createOption=None):
  """
  CreateFrom(self: ScreenRuleGroupComposition,groupMasterCopy: MasterCopy) -> ScreenRuleGroup

  

   Copy screen rule group from library to project with default replace option

  

   groupMasterCopy: Screen rule group master copy

   Returns: Siemens.Engineering.SiVArc.ScreenRuleGroup

  CreateFrom(self: ScreenRuleGroupComposition,groupMasterCopy: MasterCopy,createOption: CreateOptions) -> ScreenRuleGroup

  

   Copy screen rule group from library to project with create options

  

   groupMasterCopy: Screen rule group master copy

   createOption: Create option

   Returns: Siemens.Engineering.SiVArc.ScreenRuleGroup
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: ScreenRuleGroupComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: ScreenRuleGroupComposition,name: str) -> ScreenRuleGroup

  

   Finds screen rule group based on name

  

   name: Screen rule group name

   Returns: Siemens.Engineering.SiVArc.ScreenRuleGroup
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: ScreenRuleGroupComposition) -> IEnumerator[ScreenRuleGroup]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: ScreenRuleGroupComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: ScreenRuleGroupComposition,item: ScreenRuleGroup) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: ScreenRuleGroupComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[ScreenRuleGroup](enumerable: IEnumerable[ScreenRuleGroup],value: ScreenRuleGroup) -> bool """
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



Get: Count(self: ScreenRuleGroupComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: ScreenRuleGroupComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: ScreenRuleGroupComposition) -> IEngineeringObject



"""



class ScreenRules(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents screen rules editor """
 def Equals(self,obj):
  """
  Equals(self: ScreenRules,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: ScreenRules,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: ScreenRules) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: ScreenRules,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: ScreenRules) -> str

  

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
 Groups=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Navigate to all immediate screen rule groups



Get: Groups(self: ScreenRules) -> ScreenRuleGroupComposition



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: ScreenRules) -> IEngineeringObject



"""

 Rules=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Navigate to all immediate screen rules



Get: Rules(self: ScreenRules) -> ScreenRuleComposition



"""



class Sivarc(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IEngineeringService,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents SiVArc folder """
 def Equals(self,obj):
  """
  Equals(self: Sivarc,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Generate(self,deviceName,plcs,genrationOptions):
  """ Generate(self: Sivarc,deviceName: str,plcs: IEnumerable[str],genrationOptions: GenerationOptions) -> SivarcGenerationResult """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: Sivarc,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Sivarc) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: Sivarc,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: Sivarc) -> str

  

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
 AlarmRules=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Alarm rules editor



Get: AlarmRules(self: Sivarc) -> AlarmRules



"""

 CopyRules=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Copy rules editor



Get: CopyRules(self: Sivarc) -> CopyRules



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: Sivarc) -> IEngineeringObject



"""

 ScreenRules=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Screen rules editor



Get: ScreenRules(self: Sivarc) -> ScreenRules



"""

 TagRules=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Tag rules editor



Get: TagRules(self: Sivarc) -> TagRules



"""

 TextlistRules=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Textlist rules editor



Get: TextlistRules(self: Sivarc) -> TextlistRules



"""



class SivarcFeedbackMessage(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Generation result message """
 def Equals(self,obj):
  """
  Equals(self: SivarcFeedbackMessage,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: SivarcFeedbackMessage,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: SivarcFeedbackMessage) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: SivarcFeedbackMessage,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: SivarcFeedbackMessage) -> str

  

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
 DateTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Date and time for generation message



Get: DateTime(self: SivarcFeedbackMessage) -> DateTime



"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Description of a generation message



Get: Description(self: SivarcFeedbackMessage) -> str



"""

 ErrorCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Number of errors of generation message



Get: ErrorCount(self: SivarcFeedbackMessage) -> int



"""

 Messages=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Access to the child messages for a given scenario



Get: Messages(self: SivarcFeedbackMessage) -> SivarcFeedbackMessageComposition



"""

 MessageType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Message type of a generation message



Get: MessageType(self: SivarcFeedbackMessage) -> MessageType



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: SivarcFeedbackMessage) -> IEngineeringObject



"""

 Path=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Path to a generation message



Get: Path(self: SivarcFeedbackMessage) -> str



"""

 WarningCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Number of warnings of generation message



Get: WarningCount(self: SivarcFeedbackMessage) -> int



"""



class SivarcFeedbackMessageComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[SivarcFeedbackMessage],IEquatable[object]):
 """ Composition of GeneratedResultMessages """
 def Contains(self,item):
  """
  Contains(self: SivarcFeedbackMessageComposition,item: SivarcFeedbackMessage) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: SivarcFeedbackMessageComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: SivarcFeedbackMessageComposition) -> IEnumerator[SivarcFeedbackMessage]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: SivarcFeedbackMessageComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: SivarcFeedbackMessageComposition,item: SivarcFeedbackMessage) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: SivarcFeedbackMessageComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[SivarcFeedbackMessage](enumerable: IEnumerable[SivarcFeedbackMessage],value: SivarcFeedbackMessage) -> bool """
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



Get: Count(self: SivarcFeedbackMessageComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: SivarcFeedbackMessageComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: SivarcFeedbackMessageComposition) -> IEngineeringObject



"""



class SivarcGenerationResult(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Sivarc generation result """
 def Equals(self,obj):
  """
  Equals(self: SivarcGenerationResult,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: SivarcGenerationResult,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: SivarcGenerationResult) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: SivarcGenerationResult,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: SivarcGenerationResult) -> str

  

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
 ErrorCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Error count



Get: ErrorCount(self: SivarcGenerationResult) -> int



"""

 IsGenerationSuccessful=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Checks whether generation is successful or not



Get: IsGenerationSuccessful(self: SivarcGenerationResult) -> bool



"""

 Messages=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Collection of messages



Get: Messages(self: SivarcGenerationResult) -> SivarcFeedbackMessageComposition



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: SivarcGenerationResult) -> IEngineeringObject



"""

 WarningCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Warning Count



Get: WarningCount(self: SivarcGenerationResult) -> int



"""



class TagRule(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents tag rule object """
 def Delete(self):
  """
  Delete(self: TagRule)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: TagRule,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: TagRule,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TagRule) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: TagRule,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: TagRule) -> str

  

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
 Comment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Tag rule comment



Get: Comment(self: TagRule) -> str



"""

 Condition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Tag rule condition



Get: Condition(self: TagRule) -> str



"""

 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Checks whether tag rule is selected



Get: Enabled(self: TagRule) -> bool



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Tag rule name



Get: Name(self: TagRule) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: TagRule) -> IEngineeringObject



"""



class TagRuleComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[TagRule],IEquatable[object]):
 """ Collection of immediate tag rules """
 def Contains(self,item):
  """
  Contains(self: TagRuleComposition,item: TagRule) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def CreateFrom(self,ruleMasterCopy,createOption=None):
  """
  CreateFrom(self: TagRuleComposition,ruleMasterCopy: MasterCopy) -> TagRule

  

   Copy tag rule from library to project with default replace option

  

   ruleMasterCopy: Tag rule master copy

   Returns: Siemens.Engineering.SiVArc.TagRule

  CreateFrom(self: TagRuleComposition,ruleMasterCopy: MasterCopy,createOption: CreateOptions) -> TagRule

  

   Copy tag rule from library to project with create options

  

   ruleMasterCopy: Tag rule master copy

   createOption: Create option

   Returns: Siemens.Engineering.SiVArc.TagRule
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: TagRuleComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: TagRuleComposition,name: str) -> TagRule

  

   Finds tag rule based on name

  

   name: Tag rule name

   Returns: Siemens.Engineering.SiVArc.TagRule
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: TagRuleComposition) -> IEnumerator[TagRule]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TagRuleComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: TagRuleComposition,item: TagRule) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: TagRuleComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[TagRule](enumerable: IEnumerable[TagRule],value: TagRule) -> bool """
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



Get: Count(self: TagRuleComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: TagRuleComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: TagRuleComposition) -> IEngineeringObject



"""



class TagRuleGroup(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents tag rule group """
 def Delete(self):
  """
  Delete(self: TagRuleGroup)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: TagRuleGroup,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: TagRuleGroup,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TagRuleGroup) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: TagRuleGroup,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: TagRuleGroup) -> str

  

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
 Comment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Tag rule group comment



Get: Comment(self: TagRuleGroup) -> str



"""

 Condition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Tag rule group condition



Get: Condition(self: TagRuleGroup) -> str



"""

 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Checks whether tag rule group is selected



Get: Enabled(self: TagRuleGroup) -> bool



"""

 Groups=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Collection of immediate groups



Get: Groups(self: TagRuleGroup) -> TagRuleGroupComposition



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Tag rule group name



Get: Name(self: TagRuleGroup) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: TagRuleGroup) -> IEngineeringObject



"""

 Rules=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Collection of immediate rules



Get: Rules(self: TagRuleGroup) -> TagRuleComposition



"""



class TagRuleGroupComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[TagRuleGroup],IEquatable[object]):
 """ Collection of immediate tag rule groups """
 def Contains(self,item):
  """
  Contains(self: TagRuleGroupComposition,item: TagRuleGroup) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def CreateFrom(self,groupMasterCopy,createOption=None):
  """
  CreateFrom(self: TagRuleGroupComposition,groupMasterCopy: MasterCopy) -> TagRuleGroup

  

   Copy tag rule group from library to project with default replace option

  

   groupMasterCopy: Tag rule group master copy

   Returns: Siemens.Engineering.SiVArc.TagRuleGroup

  CreateFrom(self: TagRuleGroupComposition,groupMasterCopy: MasterCopy,createOption: CreateOptions) -> TagRuleGroup

  

   Copy tag rule group from library to project with create options

  

   groupMasterCopy: Tag rule group master copy

   createOption: Create option

   Returns: Siemens.Engineering.SiVArc.TagRuleGroup
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: TagRuleGroupComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: TagRuleGroupComposition,name: str) -> TagRuleGroup

  

   Finds tag rule group based on name

  

   name: Tag rule group name

   Returns: Siemens.Engineering.SiVArc.TagRuleGroup
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: TagRuleGroupComposition) -> IEnumerator[TagRuleGroup]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TagRuleGroupComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: TagRuleGroupComposition,item: TagRuleGroup) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: TagRuleGroupComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[TagRuleGroup](enumerable: IEnumerable[TagRuleGroup],value: TagRuleGroup) -> bool """
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



Get: Count(self: TagRuleGroupComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: TagRuleGroupComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: TagRuleGroupComposition) -> IEngineeringObject



"""



class TagRules(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents tag rules editor """
 def Equals(self,obj):
  """
  Equals(self: TagRules,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: TagRules,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TagRules) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: TagRules,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: TagRules) -> str

  

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
 Groups=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Navigate to all immediate tag rule groups



Get: Groups(self: TagRules) -> TagRuleGroupComposition



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: TagRules) -> IEngineeringObject



"""

 Rules=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Navigate to all immediate tag rules



Get: Rules(self: TagRules) -> TagRuleComposition



"""



class TextlistRule(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents textlist rule object """
 def Delete(self):
  """
  Delete(self: TextlistRule)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: TextlistRule,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: TextlistRule,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TextlistRule) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: TextlistRule,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: TextlistRule) -> str

  

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
 Comment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Textlist rule comment



Get: Comment(self: TextlistRule) -> str



"""

 Condition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Textlist rule condition



Get: Condition(self: TextlistRule) -> str



"""

 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Checks whether textlist rule is selected



Get: Enabled(self: TextlistRule) -> bool



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Textlist rule name



Get: Name(self: TextlistRule) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: TextlistRule) -> IEngineeringObject



"""



class TextlistRuleComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[TextlistRule],IEquatable[object]):
 """ Collection of immediate textlist rules """
 def Contains(self,item):
  """
  Contains(self: TextlistRuleComposition,item: TextlistRule) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def CreateFrom(self,ruleMasterCopy,createOption=None):
  """
  CreateFrom(self: TextlistRuleComposition,ruleMasterCopy: MasterCopy) -> TextlistRule

  

   Copy textlist rule from library to project with default replace option

  

   ruleMasterCopy: Textlist rule master copy

   Returns: Siemens.Engineering.SiVArc.TextlistRule

  CreateFrom(self: TextlistRuleComposition,ruleMasterCopy: MasterCopy,createOption: CreateOptions) -> TextlistRule

  

   Copy textlist rule from library to project with create options

  

   ruleMasterCopy: Textlist rule master copy

   createOption: Create option

   Returns: Siemens.Engineering.SiVArc.TextlistRule
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: TextlistRuleComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: TextlistRuleComposition,name: str) -> TextlistRule

  

   Finds textlist rule based on name

  

   name: Textlist rule name

   Returns: Siemens.Engineering.SiVArc.TextlistRule
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: TextlistRuleComposition) -> IEnumerator[TextlistRule]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TextlistRuleComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: TextlistRuleComposition,item: TextlistRule) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: TextlistRuleComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[TextlistRule](enumerable: IEnumerable[TextlistRule],value: TextlistRule) -> bool """
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



Get: Count(self: TextlistRuleComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: TextlistRuleComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: TextlistRuleComposition) -> IEngineeringObject



"""



class TextlistRuleGroup(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents textlist rule group """
 def Delete(self):
  """
  Delete(self: TextlistRuleGroup)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: TextlistRuleGroup,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: TextlistRuleGroup,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TextlistRuleGroup) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: TextlistRuleGroup,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: TextlistRuleGroup) -> str

  

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
 Comment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Textlist rule group comment



Get: Comment(self: TextlistRuleGroup) -> str



"""

 Condition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Textlist rule group condition



Get: Condition(self: TextlistRuleGroup) -> str



"""

 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Checks whether textlist rule group is selected



Get: Enabled(self: TextlistRuleGroup) -> bool



"""

 Groups=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Collection of immediate groups



Get: Groups(self: TextlistRuleGroup) -> TextlistRuleGroupComposition



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Textlist rule group name



Get: Name(self: TextlistRuleGroup) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: TextlistRuleGroup) -> IEngineeringObject



"""

 Rules=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Collection of immediate rules



Get: Rules(self: TextlistRuleGroup) -> TextlistRuleComposition



"""



class TextlistRuleGroupComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[TextlistRuleGroup],IEquatable[object]):
 """ Collection of immediate textlist rule groups """
 def Contains(self,item):
  """
  Contains(self: TextlistRuleGroupComposition,item: TextlistRuleGroup) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def CreateFrom(self,groupMasterCopy,createOption=None):
  """
  CreateFrom(self: TextlistRuleGroupComposition,groupMasterCopy: MasterCopy) -> TextlistRuleGroup

  

   Copy textlist rule group from library to project with default replace option

  

   groupMasterCopy: Textlist rule group master copy

   Returns: Siemens.Engineering.SiVArc.TextlistRuleGroup

  CreateFrom(self: TextlistRuleGroupComposition,groupMasterCopy: MasterCopy,createOption: CreateOptions) -> TextlistRuleGroup

  

   Copy textlist rule group from library to project with create options

  

   groupMasterCopy: Textlist rule group master copy

   createOption: Create option

   Returns: Siemens.Engineering.SiVArc.TextlistRuleGroup
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: TextlistRuleGroupComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: TextlistRuleGroupComposition,name: str) -> TextlistRuleGroup

  

   Finds textlist rule group based on name

  

   name: Textlist rule group name

   Returns: Siemens.Engineering.SiVArc.TextlistRuleGroup
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: TextlistRuleGroupComposition) -> IEnumerator[TextlistRuleGroup]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TextlistRuleGroupComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: TextlistRuleGroupComposition,item: TextlistRuleGroup) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: TextlistRuleGroupComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[TextlistRuleGroup](enumerable: IEnumerable[TextlistRuleGroup],value: TextlistRuleGroup) -> bool """
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



Get: Count(self: TextlistRuleGroupComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: TextlistRuleGroupComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: TextlistRuleGroupComposition) -> IEngineeringObject



"""



class TextlistRules(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents textlist rules editor """
 def Equals(self,obj):
  """
  Equals(self: TextlistRules,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: TextlistRules,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TextlistRules) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: TextlistRules,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: TextlistRules) -> str

  

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
 Groups=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Navigate to all immediate textlist rule groups



Get: Groups(self: TextlistRules) -> TextlistRuleGroupComposition



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: TextlistRules) -> IEngineeringObject



"""

 Rules=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Navigate to all immediate textlist rules



Get: Rules(self: TextlistRules) -> TextlistRuleComposition



"""



