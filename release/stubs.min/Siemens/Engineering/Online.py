# encoding: utf-8
# module Siemens.Engineering.Online calls itself Online
# from Siemens.Engineering,Version=15.1.0.0,Culture=neutral,PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class OnlineProvider(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IEngineeringService,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Service provider for online behaviors """
 def Equals(self,obj):
  """
  Equals(self: OnlineProvider,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: OnlineProvider,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: OnlineProvider) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def GoOffline(self):
  """
  GoOffline(self: OnlineProvider)

   Command to go offline
  """
  pass
 def GoOnline(self):
  """
  GoOnline(self: OnlineProvider) -> OnlineState

  

   Command to go online

   Returns: Siemens.Engineering.Online.OnlineState
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: OnlineProvider,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: OnlineProvider) -> str

  

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
 Configuration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the connection configuration



Get: Configuration(self: OnlineProvider) -> ConnectionConfiguration



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: OnlineProvider) -> IEngineeringObject



"""

 State=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Check the Online state.



Get: State(self: OnlineProvider) -> OnlineState



"""



class OnlineState(Enum,IComparable,IFormattable,IConvertible):
 """
 The list of possible online states

 

 enum OnlineState,values: Connecting (1),Disconnecting (6),Incompatible (3),NotReachable (4),Offline (0),Online (2),Protected (5)
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
 Connecting=None
 Disconnecting=None
 Incompatible=None
 NotReachable=None
 Offline=None
 Online=None
 Protected=None
 value__=None


class RHOnlineProvider(object,IEngineeringService,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Service provides online functionality for R/H systems """
 def Equals(self,obj):
  """
  Equals(self: RHOnlineProvider,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: RHOnlineProvider) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def GoOffline(self):
  """
  GoOffline(self: RHOnlineProvider)

   Command to go offline
  """
  pass
 def GoOnlineToBackup(self):
  """
  GoOnlineToBackup(self: RHOnlineProvider) -> OnlineState

  

   Command to go online to the backup PLC

   Returns: Siemens.Engineering.Online.OnlineState
  """
  pass
 def GoOnlineToPrimary(self):
  """
  GoOnlineToPrimary(self: RHOnlineProvider) -> OnlineState

  

   Command to go online to the primary Primary

   Returns: Siemens.Engineering.Online.OnlineState
  """
  pass
 def ToString(self):
  """
  ToString(self: RHOnlineProvider) -> str

  

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
 BackupState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Check the Online state of the Backup PLC.



Get: BackupState(self: RHOnlineProvider) -> OnlineState



"""

 Configuration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the connection configuration



Get: Configuration(self: RHOnlineProvider) -> ConnectionConfiguration



"""

 PrimaryState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Check the Online state of the Primary PLC.



Get: PrimaryState(self: RHOnlineProvider) -> OnlineState



"""



