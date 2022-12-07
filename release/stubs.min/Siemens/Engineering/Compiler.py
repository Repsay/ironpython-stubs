# encoding: utf-8
# module Siemens.Engineering.Compiler calls itself Compiler
# from Siemens.Engineering,Version=15.1.0.0,Culture=neutral,PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CompilerResult(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ The results of a compilation """
 def Equals(self,obj):
  """
  Equals(self: CompilerResult,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: CompilerResult,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: CompilerResult) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: CompilerResult,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: CompilerResult) -> str

  

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
 """Number of errors in a given compile scenario



Get: ErrorCount(self: CompilerResult) -> int



"""

 Messages=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Collection of output messages for the result of a given compile scenario



Get: Messages(self: CompilerResult) -> CompilerResultMessageComposition



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: CompilerResult) -> IEngineeringObject



"""

 State=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Final state of a given compile scenario



Get: State(self: CompilerResult) -> CompilerResultState



"""

 WarningCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Number of warnings in a given compile scenario



Get: WarningCount(self: CompilerResult) -> int



"""



class CompilerResultMessage(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Compilation results message """
 def Equals(self,obj):
  """
  Equals(self: CompilerResultMessage,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: CompilerResultMessage,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: CompilerResultMessage) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: CompilerResultMessage,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: CompilerResultMessage) -> str

  

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
 """Date and time in a compiler message



Get: DateTime(self: CompilerResultMessage) -> DateTime



"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Description or content of a compiler message



Get: Description(self: CompilerResultMessage) -> str



"""

 ErrorCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Number of errors in a compiler message



Get: ErrorCount(self: CompilerResultMessage) -> int



"""

 Messages=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Access to the compiler messages for a given compile scenario



Get: Messages(self: CompilerResultMessage) -> CompilerResultMessageComposition



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: CompilerResultMessage) -> IEngineeringObject



"""

 Path=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Path to a compiler message



Get: Path(self: CompilerResultMessage) -> str



"""

 State=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Final state in a compiler message



Get: State(self: CompilerResultMessage) -> CompilerResultState



"""

 WarningCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Number of warnings in a compiler message



Get: WarningCount(self: CompilerResultMessage) -> int



"""



class CompilerResultMessageComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[CompilerResultMessage],IEquatable[object]):
 """ Composition of CompareResultMessages """
 def Contains(self,item):
  """
  Contains(self: CompilerResultMessageComposition,item: CompilerResultMessage) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: CompilerResultMessageComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: CompilerResultMessageComposition) -> IEnumerator[CompilerResultMessage]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: CompilerResultMessageComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: CompilerResultMessageComposition,item: CompilerResultMessage) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: CompilerResultMessageComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[CompilerResultMessage](enumerable: IEnumerable[CompilerResultMessage],value: CompilerResultMessage) -> bool """
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



Get: Count(self: CompilerResultMessageComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: CompilerResultMessageComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: CompilerResultMessageComposition) -> IEngineeringObject



"""



class CompilerResultState(Enum,IComparable,IFormattable,IConvertible):
 """
 The list of possible compiler result options

 

 enum CompilerResultState,values: Error (3),Information (1),Success (0),Warning (2)
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
 Success=None
 value__=None
 Warning=None


class ICompilable(IEngineeringService):
 """ An interface indication that the item supports compilation """
 def Compile(self):
  """
  Compile(self: ICompilable) -> CompilerResult

  

   Compiles the item

   Returns: Siemens.Engineering.Compiler.CompilerResult
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

