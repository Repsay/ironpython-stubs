class SubnetComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[Subnet],IEquatable[object]):
 """ Composition of Subnets """
 def Contains(self,item):
  """
  Contains(self: SubnetComposition,item: Subnet) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Create(self,typeIdentifier,name):
  """
  Create(self: SubnetComposition,typeIdentifier: str,name: str) -> Subnet

  

   Creates a Subnet

  

   typeIdentifier: Type identifier of the Subnet to be created

   name: Name of Subnet to be created

   Returns: Siemens.Engineering.HW.Subnet
  """
  pass
 def CreateFrom(self,masterCopy):
  """
  CreateFrom(self: SubnetComposition,masterCopy: MasterCopy) -> Subnet

  

   Create subnet from MasterCopy

  

   masterCopy: The source MasterCopy

   Returns: Siemens.Engineering.HW.Subnet
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: SubnetComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: SubnetComposition,name: str) -> Subnet

  

   Finds a given Subnet

  

   name: Name to find

   Returns: Siemens.Engineering.HW.Subnet
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: SubnetComposition) -> IEnumerator[Subnet]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: SubnetComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: SubnetComposition,item: Subnet) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: SubnetComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[Subnet](enumerable: IEnumerable[Subnet],value: Subnet) -> bool """
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



Get: Count(self: SubnetComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: SubnetComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: SubnetComposition) -> IEngineeringObject



"""


