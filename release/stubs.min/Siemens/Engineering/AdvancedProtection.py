# encoding: utf-8
# module Siemens.Engineering.AdvancedProtection calls itself AdvancedProtection
# from Siemens.Engineering,Version=15.1.0.0,Culture=neutral,PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ProtectionProviderBase(object,IEngineeringService,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Defines the contract of a Protection Provider,should be used as the base class for client-specific ProtectionProviders """
 def Equals(self,obj):
  """
  Equals(self: ProtectionProviderBase,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: ProtectionProviderBase) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def GetInvalidPasswordCharacters(self):
  """
  GetInvalidPasswordCharacters(self: ProtectionProviderBase) -> IEnumerable[Char]

  

   Gets the invalid characters from the user password input

   Returns: System.Collections.Generic.IEnumerable<System.Char>
  """
  pass
 def Protect(self,newPassword):
  """
  Protect(self: ProtectionProviderBase,newPassword: SecureString)

   Sets protection for the underlying object

  

   newPassword: the password to protect the object with
  """
  pass
 def ToString(self):
  """
  ToString(self: ProtectionProviderBase) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def Unprotect(self,currentPassword):
  """
  Unprotect(self: ProtectionProviderBase,currentPassword: SecureString)

   Removes protection from the underlying object

  

   currentPassword: the password the underlying object is currently protected with
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

