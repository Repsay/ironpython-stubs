# encoding: utf-8
# module Siemens.Engineering calls itself Engineering
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.Hmi, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AttachingEventArgs(EventArgs):
    """ Attaching event arguments """
    def GrantAccess(self):
        """
        GrantAccess(self: AttachingEventArgs)
            Grants permission to the attaching Openness application to attach.
        """
        pass

    AccessLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets access level argument of the attaching event.

Get: AccessLevel(self: AttachingEventArgs) -> TiaPortalAccessLevel

"""

    ProcessId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets attaching process identifier.

Get: ProcessId(self: AttachingEventArgs) -> int

"""

    ProcessPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets attaching event process path.

Get: ProcessPath(self: AttachingEventArgs) -> str

"""

    TrustAuthority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets TIA-Portal trust authority of the attaching event.

Get: TrustAuthority(self: AttachingEventArgs) -> TiaPortalTrustAuthority

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets version argument of the attaching event.

Get: Version(self: AttachingEventArgs) -> str

"""



class ConfirmationChoices(Enum, IComparable, IFormattable, IConvertible):
    """
    The list of possible confirmation choices
    
    enum (flags) ConfirmationChoices, values: Abort (8), Cancel (256), Ignore (32), No (64), None (0), NoToAll (128), Ok (1), Retry (16), Yes (2), YesToAll (4)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Abort = None
    Cancel = None
    Ignore = None
    No = None
    None = None
    NoToAll = None
    Ok = None
    Retry = None
    value__ = None
    Yes = None
    YesToAll = None


class ConfirmationEventArgs(EventArgs):
    """ Confirmation event arguments """
    Caption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the caption of the confirmation.

Get: Caption(self: ConfirmationEventArgs) -> str

"""

    Choices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the choices of the confirmation.

Get: Choices(self: ConfirmationEventArgs) -> ConfirmationChoices

"""

    DetailText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the detail text of the confirmation.

Get: DetailText(self: ConfirmationEventArgs) -> str

"""

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the icon.

Get: Icon(self: ConfirmationEventArgs) -> ConfirmationIcon

"""

    IsHandled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets if the confirmation is handled.

Get: IsHandled(self: ConfirmationEventArgs) -> bool

Set: IsHandled(self: ConfirmationEventArgs) = value
"""

    Result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the result of the confirmation.

Get: Result(self: ConfirmationEventArgs) -> ConfirmationResult

Set: Result(self: ConfirmationEventArgs) = value
"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the text of the confirmation.

Get: Text(self: ConfirmationEventArgs) -> str

"""



class ConfirmationIcon(Enum, IComparable, IFormattable, IConvertible):
    """
    The list of possible confirmation icons
    
    enum ConfirmationIcon, values: Critical (1), Error (2), General (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Critical = None
    Error = None
    General = None
    value__ = None


class ConfirmationResult(Enum, IComparable, IFormattable, IConvertible):
    """
    The list of possible confirmation results
    
    enum ConfirmationResult, values: Abort (3), Cancel (8), Ignore (5), No (6), NoToAll (7), Ok (0), Retry (4), Yes (1), YesToAll (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Abort = None
    Cancel = None
    Ignore = None
    No = None
    NoToAll = None
    Ok = None
    Retry = None
    value__ = None
    Yes = None
    YesToAll = None


class EngineeringAttributeAccessMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Flags enum that describes different access levels
    
    enum (flags) EngineeringAttributeAccessMode, values: None (0), Read (1), ReadWrite (3), Write (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    None = None
    Read = None
    ReadWrite = None
    value__ = None
    Write = None


class EngineeringAttributeInfo(object):
    """ Represents composition information. """
    def ToString(self):
        """
        ToString(self: EngineeringAttributeInfo) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    AccessMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the level of access supported by the attribute.

Get: AccessMode(self: EngineeringAttributeInfo) -> EngineeringAttributeAccessMode

"""

    CreateRelevance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CreateRelevance(self: EngineeringAttributeInfo) -> EngineeringCreateRelevance

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the attribute.

Get: Name(self: EngineeringAttributeInfo) -> str

"""



class EngineeringCompositionInfo(object):
    """ Represents composition information. """
    def ToString(self):
        """
        ToString(self: EngineeringCompositionInfo) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets composition name.

Get: Name(self: EngineeringCompositionInfo) -> str

"""



class EngineeringCreateRelevance(Enum, IComparable, IFormattable, IConvertible):
    """ enum EngineeringCreateRelevance, values: Mandatory (2), None (0), Relevant (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Mandatory = None
    None = None
    Relevant = None
    value__ = None


class EngineeringCreationInfo(object):
    """ Represents the necessary information required to create an object. """
    def ToString(self):
        """
        ToString(self: EngineeringCreationInfo) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    ParameterInfos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The parameters needed to create the object.

Get: ParameterInfos(self: EngineeringCreationInfo) -> IList[EngineeringCreationParameterInfo]

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of the objec that will be created.

Get: Type(self: EngineeringCreationInfo) -> Type

"""



class EngineeringCreationParameterInfo(object):
    """ The parameter info """
    def ToString(self):
        """
        ToString(self: EngineeringCreationParameterInfo) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    IsMandatory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets if the parameter is mandatory.

Get: IsMandatory(self: EngineeringCreationParameterInfo) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the parameter.

Get: Name(self: EngineeringCreationParameterInfo) -> str

"""



class EngineeringException(Exception, ISerializable, _Exception):
    """
    Engineering exception.
    
    EngineeringException()
    EngineeringException(text: str)
    EngineeringException(text: str, exception: Exception)
    EngineeringException(text: str, *detailTexts: Array[str])
    """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: EngineeringException, info: SerializationInfo, context: StreamingContext)
            When overridden in a derived class, sets the System.Runtime.Serialization.SerializationInfoB with information 
             about the exception.
        
        
            info: The System.Runtime.Serialization.SerializationInfo that holds the serialized object data about the exception 
             being thrown.
        
            context: The System.Runtime.Serialization.StreamingContext that contains contextual information about the source or 
             destination.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, text=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, text: str)
        __new__(cls: type, text: str, exception: Exception)
        __new__(cls: type, text: str, *detailTexts: Array[str])
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DetailMessageData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the detail message data that describes the current exception.

Get: DetailMessageData(self: EngineeringException) -> IList[ExceptionMessageData]

"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a message that describes the current exception.

Get: Message(self: EngineeringException) -> str

"""

    MessageData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the message data that describes the current exception.

Get: MessageData(self: EngineeringException) -> ExceptionMessageData

"""

    StackTrace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the stack trace of the current exception.

Get: StackTrace(self: EngineeringException) -> str

"""


    SerializeObjectState = None


class EngineeringTargetInvocationException(EngineeringException, ISerializable, _Exception):
    """
    Engineering Target Invocation Exception
    
    EngineeringTargetInvocationException()
    EngineeringTargetInvocationException(text: str)
    EngineeringTargetInvocationException(text: str, exception: Exception)
    EngineeringTargetInvocationException(text: str, *detailTexts: Array[str])
    """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: EngineeringTargetInvocationException, info: SerializationInfo, context: StreamingContext)
            When overridden in a derived class, sets the System.Runtime.Serialization.SerializationInfoB with information 
             about the exception.
        
        
            info: The System.Runtime.Serialization.SerializationInfo that holds the serialized object data about the exception 
             being thrown.
        
            context: The System.Runtime.Serialization.StreamingContext that contains contextual information about the source or 
             destination.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, text=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, text: str)
        __new__(cls: type, text: str, exception: Exception)
        __new__(cls: type, text: str, *detailTexts: Array[str])
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class EngineeringDelegateInvocationException(EngineeringTargetInvocationException, ISerializable, _Exception):
    """
    Engineering Delegate Invocation Exception
    
    EngineeringDelegateInvocationException()
    EngineeringDelegateInvocationException(text: str)
    EngineeringDelegateInvocationException(text: str, exception: Exception)
    EngineeringDelegateInvocationException(text: str, *detailTexts: Array[str])
    """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: EngineeringDelegateInvocationException, info: SerializationInfo, context: StreamingContext)
            When overridden in a derived class, sets the System.Runtime.Serialization.SerializationInfoB with information 
             about the exception.
        
        
            info: The System.Runtime.Serialization.SerializationInfo that holds the serialized object data about the exception 
             being thrown.
        
            context: The System.Runtime.Serialization.StreamingContext that contains contextual information about the source or 
             destination.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, text=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, text: str)
        __new__(cls: type, text: str, exception: Exception)
        __new__(cls: type, text: str, *detailTexts: Array[str])
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class EngineeringInvocationInfo(object):
    """ Represents an action info. """
    def ToString(self):
        """
        ToString(self: EngineeringInvocationInfo) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the action.

Get: Name(self: EngineeringInvocationInfo) -> str

"""

    ParameterInfos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parameter info list.

Get: ParameterInfos(self: EngineeringInvocationInfo) -> IList[EngineeringInvocationParameterInfo]

"""



class EngineeringInvocationParameterInfo(object):
    """ The parameter info """
    def ToString(self):
        """
        ToString(self: EngineeringInvocationParameterInfo) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the parameter.

Get: Name(self: EngineeringInvocationParameterInfo) -> str

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of the parameter.

Get: Type(self: EngineeringInvocationParameterInfo) -> Type

"""



class EngineeringNotSupportedException(EngineeringException, ISerializable, _Exception):
    """
    Engineering Not Supported Exception
    
    EngineeringNotSupportedException()
    EngineeringNotSupportedException(text: str)
    EngineeringNotSupportedException(text: str, exception: Exception)
    EngineeringNotSupportedException(text: str, *detailTexts: Array[str])
    """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: EngineeringNotSupportedException, info: SerializationInfo, context: StreamingContext)
            When overridden in a derived class, sets the System.Runtime.Serialization.SerializationInfoB with information 
             about the exception.
        
        
            info: The System.Runtime.Serialization.SerializationInfo that holds the serialized object data about the exception 
             being thrown.
        
            context: The System.Runtime.Serialization.StreamingContext that contains contextual information about the source or 
             destination.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, text=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, text: str)
        __new__(cls: type, text: str, exception: Exception)
        __new__(cls: type, text: str, *detailTexts: Array[str])
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class EngineeringObjectDisposedException(EngineeringException, ISerializable, _Exception):
    """
    Engineering Object Disposed Exception
    
    EngineeringObjectDisposedException()
    EngineeringObjectDisposedException(text: str)
    EngineeringObjectDisposedException(text: str, exception: Exception)
    EngineeringObjectDisposedException(text: str, *detailTexts: Array[str])
    """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: EngineeringObjectDisposedException, info: SerializationInfo, context: StreamingContext)
            When overridden in a derived class, sets the System.Runtime.Serialization.SerializationInfoB with information 
             about the exception.
        
        
            info: The System.Runtime.Serialization.SerializationInfo that holds the serialized object data about the exception 
             being thrown.
        
            context: The System.Runtime.Serialization.StreamingContext that contains contextual information about the source or 
             destination.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, text=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, text: str)
        __new__(cls: type, text: str, exception: Exception)
        __new__(cls: type, text: str, *detailTexts: Array[str])
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class EngineeringOutOfMemoryException(EngineeringException, ISerializable, _Exception):
    """
    Engineering Out Of Memory Exception
    
    EngineeringOutOfMemoryException()
    EngineeringOutOfMemoryException(text: str)
    EngineeringOutOfMemoryException(text: str, exception: Exception)
    EngineeringOutOfMemoryException(text: str, *detailTexts: Array[str])
    """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: EngineeringOutOfMemoryException, info: SerializationInfo, context: StreamingContext)
            When overridden in a derived class, sets the System.Runtime.Serialization.SerializationInfoB with information 
             about the exception.
        
        
            info: The System.Runtime.Serialization.SerializationInfo that holds the serialized object data about the exception 
             being thrown.
        
            context: The System.Runtime.Serialization.StreamingContext that contains contextual information about the source or 
             destination.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, text=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, text: str)
        __new__(cls: type, text: str, exception: Exception)
        __new__(cls: type, text: str, *detailTexts: Array[str])
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class EngineeringRuntimeException(EngineeringException, ISerializable, _Exception):
    """
    Engineering Runtime Exception
    
    EngineeringRuntimeException()
    EngineeringRuntimeException(text: str)
    EngineeringRuntimeException(text: str, exception: Exception)
    EngineeringRuntimeException(text: str, *detailTexts: Array[str])
    """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: EngineeringRuntimeException, info: SerializationInfo, context: StreamingContext)
            When overridden in a derived class, sets the System.Runtime.Serialization.SerializationInfoB with information 
             about the exception.
        
        
            info: The System.Runtime.Serialization.SerializationInfo that holds the serialized object data about the exception 
             being thrown.
        
            context: The System.Runtime.Serialization.StreamingContext that contains contextual information about the source or 
             destination.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, text=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, text: str)
        __new__(cls: type, text: str, exception: Exception)
        __new__(cls: type, text: str, *detailTexts: Array[str])
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class EngineeringSecurityException(EngineeringException, ISerializable, _Exception):
    """
    Engineering Security Exception
    
    EngineeringSecurityException()
    EngineeringSecurityException(text: str)
    EngineeringSecurityException(text: str, exception: Exception)
    EngineeringSecurityException(text: str, *detailTexts: Array[str])
    """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: EngineeringSecurityException, info: SerializationInfo, context: StreamingContext)
            When overridden in a derived class, sets the System.Runtime.Serialization.SerializationInfoB with information 
             about the exception.
        
        
            info: The System.Runtime.Serialization.SerializationInfo that holds the serialized object data about the exception 
             being thrown.
        
            context: The System.Runtime.Serialization.StreamingContext that contains contextual information about the source or 
             destination.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, text=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, text: str)
        __new__(cls: type, text: str, exception: Exception)
        __new__(cls: type, text: str, *detailTexts: Array[str])
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class EngineeringServiceInfo(object):
    """ Represents an action info. """
    def ToString(self):
        """
        ToString(self: EngineeringServiceInfo) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the action.

Get: Type(self: EngineeringServiceInfo) -> Type

"""



class EngineeringUserAbortException(EngineeringTargetInvocationException, ISerializable, _Exception):
    """
    Engineering User Abort Exception
    
    EngineeringUserAbortException()
    EngineeringUserAbortException(text: str)
    EngineeringUserAbortException(text: str, exception: Exception)
    EngineeringUserAbortException(text: str, *detailTexts: Array[str])
    """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: EngineeringUserAbortException, info: SerializationInfo, context: StreamingContext)
            When overridden in a derived class, sets the System.Runtime.Serialization.SerializationInfoB with information 
             about the exception.
        
        
            info: The System.Runtime.Serialization.SerializationInfo that holds the serialized object data about the exception 
             being thrown.
        
            context: The System.Runtime.Serialization.StreamingContext that contains contextual information about the source or 
             destination.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, text=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, text: str)
        __new__(cls: type, text: str, exception: Exception)
        __new__(cls: type, text: str, *detailTexts: Array[str])
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class ExceptionMessageData(object):
    """ Exception Message Data structure. """
    def ToString(self):
        """
        ToString(self: ExceptionMessageData) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    DetailText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the detail text.

Get: DetailText(self: ExceptionMessageData) -> str

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the text.

Get: Text(self: ExceptionMessageData) -> str

"""



class IEngineeringInstance:
    """ IEngineeringInstance """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent of the instance.

Get: Parent(self: IEngineeringInstance) -> IEngineeringObject

"""



class IEngineeringCompositionOrObject(IEngineeringInstance):
    """ IEngineeringCompositionOrObject """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IEngineeringObject(IEngineeringCompositionOrObject, IEngineeringInstance):
    """ IEngineeringObject """
    def Create(self, compositionName, type, parameters):
        """ Create(self: IEngineeringObject, compositionName: str, type: Type, parameters: IEnumerable[KeyValuePair[str, object]]) -> IEngineeringObject """
        pass

    def GetAttribute(self, name):
        """
        GetAttribute(self: IEngineeringObject, name: str) -> object
        
            Gets an attribute with the given name.
        
            name: The name of the attribute to get.
            Returns: The attribute with the given name or a null if not found.
        """
        pass

    def GetAttributeInfos(self):
        """
        GetAttributeInfos(self: IEngineeringObject) -> IList[EngineeringAttributeInfo]
        
            Returns a collection of EngineeringAttributeInfo objects describing the different attributes on this object.
            Returns: A collection of EngineeringAttributeInfo objects describing the different attributes on this object.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: IEngineeringObject, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetComposition(self, name):
        """
        GetComposition(self: IEngineeringObject, name: str) -> IEngineeringCompositionOrObject
        
            Gets an IEngineeringCompositionOrObject with the given name.
        
            name: The name of the IEngineeringCompositionOrObject to get.
            Returns: The IEngineeringCompositionOrObject with the given name; otherwise a null.
        """
        pass

    def GetCompositionInfos(self):
        """
        GetCompositionInfos(self: IEngineeringObject) -> IList[EngineeringCompositionInfo]
        
            Gets the list of composition infos available for the object.
            Returns: The list of composition infos available for the object.
        """
        pass

    def GetCreationInfos(self, compositionName):
        """ GetCreationInfos(self: IEngineeringObject, compositionName: str) -> IList[EngineeringCreationInfo] """
        pass

    def GetInvocationInfos(self):
        """
        GetInvocationInfos(self: IEngineeringObject) -> IList[EngineeringInvocationInfo]
        
            Returns a collection of EngineeringInvocationInfo objects describing the different actions on this object.
            Returns: A collection of EngineeringInvocationInfo objects describing the different actions on this object.
        """
        pass

    def Invoke(self, name, parameters):
        """ Invoke(self: IEngineeringObject, name: str, parameters: IEnumerable[KeyValuePair[Type, object]]) -> object """
        pass

    def SetAttribute(self, name, value):
        """
        SetAttribute(self: IEngineeringObject, name: str, value: object)
            Sets an attribute with the given name to the given value value.
        
            name: The name of the attribute to set with the given value.
            value: The value to set for the attribute with the given name.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: IEngineeringObject, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ExclusiveAccess(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IDisposable, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ The class representing an exclusive access session to the TIA Portal """
    def Dispose(self):
        """
        Dispose(self: ExclusiveAccess)
            Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: ExclusiveAccess, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: ExclusiveAccess, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ExclusiveAccess) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: ExclusiveAccess, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: ExclusiveAccess) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def Transaction(self, peristence, undoDescription):
        """
        Transaction(self: ExclusiveAccess, peristence: ITransactionSupport, undoDescription: str) -> Transaction
        
            Acquires a transaction instance from the active exclusive access session
        
            peristence: The persistence where the transaction is to be created
            undoDescription: The description of the undo unit that is created for the open transaction
            Returns: Siemens.Engineering.Transaction
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsCancellationRequested = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indication if the user has requested a cancellation of the exclusive access session

Get: IsCancellationRequested(self: ExclusiveAccess) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: ExclusiveAccess) -> IEngineeringObject

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The information to display while an exclusive access session is active

Get: Text(self: ExclusiveAccess) -> str

Set: Text(self: ExclusiveAccess) = value
"""



class ExportOptions(Enum, IComparable, IFormattable, IConvertible):
    """
    The list of possible scenarios supported by export action parameterization
    
    enum (flags) ExportOptions, values: None (0), WithDefaults (1), WithReadOnly (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    None = None
    value__ = None
    WithDefaults = None
    WithReadOnly = None


class HistoryEntry(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents a TIAP project history event """
    def Equals(self, obj):
        """
        Equals(self: HistoryEntry, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: HistoryEntry, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: HistoryEntry) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: HistoryEntry, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: HistoryEntry) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The time when the event occurred

Get: DateTime(self: HistoryEntry) -> DateTime

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: HistoryEntry) -> IEngineeringObject

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The event description

Get: Text(self: HistoryEntry) -> str

"""



class IEngineeringComposition(IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable):
    """ IEngineeringComposition """
    def Contains(self, item):
        """
        Contains(self: IEngineeringComposition, item: IEngineeringObject) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Create(self, type, parameters):
        """ Create(self: IEngineeringComposition, type: Type, parameters: IEnumerable[KeyValuePair[str, object]]) -> IEngineeringObject """
        pass

    def GetCreationInfos(self):
        """
        GetCreationInfos(self: IEngineeringComposition) -> IList[EngineeringCreationInfo]
        
            Gets the collection of EngineeringCreateInfo objects describing the different CreateInfos on this object.
            Returns: The collection of EngineeringCreationInfo objects
        """
        pass

    def GetInvocationInfos(self):
        """
        GetInvocationInfos(self: IEngineeringComposition) -> IList[EngineeringInvocationInfo]
        
            Returns a collection of EngineeringInvocationInfo objects describing the different actions on this object.
            Returns: A collection of EngineeringInvocationInfo objects describing the different actions on this object.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: IEngineeringComposition, item: IEngineeringObject) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The element at the specified item.
        """
        pass

    def Invoke(self, name, parameters):
        """ Invoke(self: IEngineeringComposition, name: str, parameters: IEnumerable[KeyValuePair[Type, object]]) -> object """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements contained within this Composition.

Get: Count(self: IEngineeringComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this Composition was instantiated as ReadOnly.

Get: IsReadOnly(self: IEngineeringComposition) -> bool

"""



class HistoryEntryComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[HistoryEntry], IEquatable[object]):
    """ Composition of HistoryEntries """
    def Contains(self, item):
        """
        Contains(self: HistoryEntryComposition, item: HistoryEntry) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: HistoryEntryComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: HistoryEntryComposition) -> IEnumerator[HistoryEntry]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: HistoryEntryComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: HistoryEntryComposition, item: HistoryEntry) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: HistoryEntryComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[HistoryEntry](enumerable: IEnumerable[HistoryEntry], value: HistoryEntry) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the count.

Get: Count(self: HistoryEntryComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: HistoryEntryComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: HistoryEntryComposition) -> IEngineeringObject

"""



class IEngineeringAssociation(IEngineeringInstance, IEnumerable):
    """ IEngineeringAssociation """
    def Contains(self, item):
        """
        Contains(self: IEngineeringAssociation, item: IEngineeringObject) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def GetInvocationInfos(self):
        """
        GetInvocationInfos(self: IEngineeringAssociation) -> IList[EngineeringInvocationInfo]
        
            Returns a collection of EngineeringInvocationInfo objects describing the different actions on this object.
            Returns: A collection of EngineeringInvocationInfo objects describing the different actions on this object.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: IEngineeringAssociation, item: IEngineeringObject) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The element at the specified item.
        """
        pass

    def Invoke(self, name, parameters):
        """ Invoke(self: IEngineeringAssociation, name: str, parameters: IEnumerable[KeyValuePair[Type, object]]) -> object """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements contained within this association.

Get: Count(self: IEngineeringAssociation) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this association was instantiated as ReadOnly.

Get: IsReadOnly(self: IEngineeringAssociation) -> bool

"""



class IEngineeringObjectAssociation(object, IEngineeringAssociation, IEngineeringInstance, IEnumerable, IInternalAssociationAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[IEngineeringObject], IEquatable[object]):
    """ Associated engineering objects """
    def Contains(self, item):
        """
        Contains(self: IEngineeringObjectAssociation, item: IEngineeringObject) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: IEngineeringObjectAssociation, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: IEngineeringObjectAssociation) -> IEnumerator[IEngineeringObject]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: IEngineeringObjectAssociation) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: IEngineeringObjectAssociation, item: IEngineeringObject) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: IEngineeringObjectAssociation) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[IEngineeringObject](enumerable: IEnumerable[IEngineeringObject], value: IEngineeringObject) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the count.

Get: Count(self: IEngineeringObjectAssociation) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: IEngineeringObjectAssociation) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent..

Get: Parent(self: IEngineeringObjectAssociation) -> IEngineeringObject

"""



class IEngineeringRoot(IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance):
    """ IEngineeringRoot """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IEngineeringService:
    """ The interface representing an engineering service """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IEngineeringServiceProvider(IServiceProvider):
    """ IEngineeringServiceProvider """
    def GetService(self):
# Error generating skeleton for function GetService: Method must be called on a Type for which Type.IsGenericParameter is false.

    def GetServiceInfos(self):
        """
        GetServiceInfos(self: IEngineeringServiceProvider) -> IList[EngineeringServiceInfo]
        
            Returns a collection of EngineeringServiceInfo objects describing the different services on this object.
            Returns: A collection of EngineeringServiceInfo objects describing the different services on this object.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ImportOptions(Enum, IComparable, IFormattable, IConvertible):
    """
    The list of possible options for Import
    
    enum (flags) ImportOptions, values: None (0), Override (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    None = None
    Override = None
    value__ = None


class IShowable:
    """ Access to Showable attributes """
    def ShowInEditor(self):
        """
        ShowInEditor(self: IShowable)
            Flag to indicate to show in the editor
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ISystemObject:
    """ Access to SystemObject attributes """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsSystemObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if this instance is a system object

Get: IsSystemObject(self: ISystemObject) -> bool

"""



class ITransactionSupport:
    """ An interface indication that the item supports transactions """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class Language(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents a language that can be enabled in this Project """
    def Equals(self, obj):
        """
        Equals(self: Language, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: Language, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Language) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: Language, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: Language) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Culture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The culture info object

Get: Culture(self: Language) -> CultureInfo

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: Language) -> IEngineeringObject

"""



class LanguageAssociation(object, IEngineeringAssociation, IEngineeringInstance, IEnumerable, IInternalAssociationAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[Language], IEquatable[object]):
    """ Collection of Languages. """
    def Add(self, item):
        """
        Add(self: LanguageAssociation, item: Language)
            Adds an item.
        
            item: The item to be added.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: LanguageAssociation, item: Language) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: LanguageAssociation, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, culture):
        """
        Find(self: LanguageAssociation, culture: CultureInfo) -> Language
        
            Searches for a language by a given culture.
        
            culture: Language culture
            Returns: Siemens.Engineering.Language
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: LanguageAssociation) -> IEnumerator[Language]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: LanguageAssociation) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: LanguageAssociation, item: Language) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def Remove(self, item):
        """
        Remove(self: LanguageAssociation, item: Language) -> bool
        
            Removes an item.
        
            item: The item to be removed.
            Returns: true if the item was removed; otherwise false.
        """
        pass

    def ToString(self):
        """
        ToString(self: LanguageAssociation) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Language](enumerable: IEnumerable[Language], value: Language) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the count.

Get: Count(self: LanguageAssociation) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: LanguageAssociation) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent..

Get: Parent(self: LanguageAssociation) -> IEngineeringObject

"""



class LanguageComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[Language], IEquatable[object]):
    """ Composition of Languages """
    def Contains(self, item):
        """
        Contains(self: LanguageComposition, item: Language) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: LanguageComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, culture):
        """
        Find(self: LanguageComposition, culture: CultureInfo) -> Language
        
            Searches for a language by a given culture.
        
            culture: Language culture.
            Returns: Siemens.Engineering.Language
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: LanguageComposition) -> IEnumerator[Language]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: LanguageComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: LanguageComposition, item: Language) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: LanguageComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Language](enumerable: IEnumerable[Language], value: Language) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the count.

Get: Count(self: LanguageComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: LanguageComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: LanguageComposition) -> IEngineeringObject

"""



class LanguageSettings(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents a language settings object. """
    def Equals(self, obj):
        """
        Equals(self: LanguageSettings, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: LanguageSettings, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: LanguageSettings) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: LanguageSettings, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: LanguageSettings) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ActiveLanguages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The collection of active languages.

Get: ActiveLanguages(self: LanguageSettings) -> LanguageAssociation

"""

    EditingLanguage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents an editing language.

Get: EditingLanguage(self: LanguageSettings) -> Language

Set: EditingLanguage(self: LanguageSettings) = value
"""

    Languages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The collection of all supported languages.

Get: Languages(self: LanguageSettings) -> LanguageComposition

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: LanguageSettings) -> IEngineeringObject

"""

    ReferenceLanguage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents a reference language.

Get: ReferenceLanguage(self: LanguageSettings) -> Language

Set: ReferenceLanguage(self: LanguageSettings) = value
"""



class MultilingualText(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents a String in multiple language translations """
    def Equals(self, obj):
        """
        Equals(self: MultilingualText, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: MultilingualText, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: MultilingualText) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: MultilingualText, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: MultilingualText) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Contains a collection of multilingual text items.

Get: Items(self: MultilingualText) -> MultilingualTextItemComposition

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: MultilingualText) -> IEngineeringObject

"""



class MultilingualTextItem(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Multilingual text item. """
    def Equals(self, obj):
        """
        Equals(self: MultilingualTextItem, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: MultilingualTextItem, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: MultilingualTextItem) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: MultilingualTextItem, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: MultilingualTextItem) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Language = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents language of this item.

Get: Language(self: MultilingualTextItem) -> Language

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: MultilingualTextItem) -> IEngineeringObject

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents text content.

Get: Text(self: MultilingualTextItem) -> str

Set: Text(self: MultilingualTextItem) = value
"""



class MultilingualTextItemComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[MultilingualTextItem], IEquatable[object]):
    """ Collection of multilingual text items. """
    def Contains(self, item):
        """
        Contains(self: MultilingualTextItemComposition, item: MultilingualTextItem) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: MultilingualTextItemComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, language):
        """
        Find(self: MultilingualTextItemComposition, language: Language) -> MultilingualTextItem
        
            Searches multilingual text item by language.
        
            language: Language to find.
            Returns: Siemens.Engineering.MultilingualTextItem
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: MultilingualTextItemComposition) -> IEnumerator[MultilingualTextItem]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: MultilingualTextItemComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: MultilingualTextItemComposition, item: MultilingualTextItem) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: MultilingualTextItemComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[MultilingualTextItem](enumerable: IEnumerable[MultilingualTextItem], value: MultilingualTextItem) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the count.

Get: Count(self: MultilingualTextItemComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: MultilingualTextItemComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: MultilingualTextItemComposition) -> IEngineeringObject

"""



class NonRecoverableException(Exception, ISerializable, _Exception):
    """
    Non Recoverable Exception.
    
    NonRecoverableException()
    NonRecoverableException(text: str)
    NonRecoverableException(text: str, exception: Exception)
    NonRecoverableException(text: str, *detailTexts: Array[str])
    """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: NonRecoverableException, info: SerializationInfo, context: StreamingContext)
            When overridden in a derived class, sets the System.Runtime.Serialization.SerializationInfoB with information 
             about the exception.
        
        
            info: The System.Runtime.Serialization.SerializationInfo that holds the serialized object data about the exception 
             being thrown.
        
            context: The System.Runtime.Serialization.StreamingContext that contains contextual information about the source or 
             destination.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, text=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, text: str)
        __new__(cls: type, text: str, exception: Exception)
        __new__(cls: type, text: str, *detailTexts: Array[str])
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DetailMessageData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the detail message data that describes the current exception.

Get: DetailMessageData(self: NonRecoverableException) -> IList[ExceptionMessageData]

"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a message that describes the current exception.

Get: Message(self: NonRecoverableException) -> str

"""

    MessageData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the message data that describes the current exception.

Get: MessageData(self: NonRecoverableException) -> ExceptionMessageData

"""

    StackTrace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the stack trace of the current exception.

Get: StackTrace(self: NonRecoverableException) -> str

"""


    SerializeObjectState = None


class NotificationEventArgs(EventArgs):
    """ Notification event arguments """
    Caption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Notification event arguments

Get: Caption(self: NotificationEventArgs) -> str

"""

    DetailText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Notification event arguments

Get: DetailText(self: NotificationEventArgs) -> str

"""

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Notification event arguments

Get: Icon(self: NotificationEventArgs) -> NotificationIcon

"""

    IsHandled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Notification event arguments

Get: IsHandled(self: NotificationEventArgs) -> bool

Set: IsHandled(self: NotificationEventArgs) = value
"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Notification event arguments

Get: Text(self: NotificationEventArgs) -> str

"""



class NotificationIcon(Enum, IComparable, IFormattable, IConvertible):
    """
    The list of possible notification icons
    
    enum NotificationIcon, values: Error (3), Information (1), Success (0), Warning (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Error = None
    Information = None
    Success = None
    value__ = None
    Warning = None


class OpenMode(Enum, IComparable, IFormattable, IConvertible):
    """
    The modification state of an item being opened.
    
    enum OpenMode, values: ReadOnly (0), ReadWrite (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ReadOnly = None
    ReadWrite = None
    value__ = None


class Project(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, ITransactionSupport, IMasterCopyTarget, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEngineeringServiceProvider, IServiceProvider, IEquatable[object]):
    """ Represents a project """
    def Archive(self, targetDirectory, targetName, archivationMode):
        """
        Archive(self: Project, targetDirectory: DirectoryInfo, targetName: str, archivationMode: ProjectArchivationMode)
            Archives the current project
        
            targetDirectory: Directory where the project to be archived
            targetName: File name for the archived file
            archivationMode: Archivation mode
        """
        pass

    def Close(self):
        """
        Close(self: Project)
            Closes the project
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: Project, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def ExportProjectTexts(self, path, sourceLanguage, targetLanguage):
        """
        ExportProjectTexts(self: Project, path: FileInfo, sourceLanguage: CultureInfo, targetLanguage: CultureInfo)
            Export project text to an xlsx file
        
            path: Path to the xlsx file
            sourceLanguage: The source language to use for the export of project texts
            targetLanguage: The target language to use for the export of project texts
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: Project, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Project) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def GetService(self):
# Error generating skeleton for function GetService: Method must be called on a Type for which Type.IsGenericParameter is false.

    def ImportProjectTexts(self, path, updateSourceLanguage):
        """
        ImportProjectTexts(self: Project, path: FileInfo, updateSourceLanguage: bool) -> ProjectTextResult
        
            Import project text from an import file
        
            path: Path to the xlsx file
            updateSourceLanguage: True if the source language is to be updated
            Returns: Siemens.Engineering.ProjectTextResult
        """
        pass

    def Save(self):
        """
        Save(self: Project)
            Saves all changes of the project
        """
        pass

    def SaveAs(self, targetFolderPath):
        """
        SaveAs(self: Project, targetFolderPath: DirectoryInfo)
            Saves all changes of the project to a new location.
        
            targetFolderPath: Target location for newly SavedAs project
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: Project, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ShowHwEditor(self, view):
        """
        ShowHwEditor(self: Project, view: View)
            Show the indicated item in the HW editor of the attached TIA Portal
        
            view: Which view of the HW editor to show
        """
        pass

    def ToString(self):
        """
        ToString(self: Project) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Author = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Author of the project

Get: Author(self: Project) -> str

"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The project's comment

Get: Comment(self: Project) -> MultilingualText

"""

    Copyright = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Project copyright information

Get: Copyright(self: Project) -> str

"""

    CreationTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The creation time of the project

Get: CreationTime(self: Project) -> DateTime

"""

    DeviceGroups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of device user groups

Get: DeviceGroups(self: Project) -> DeviceUserGroupComposition

"""

    Devices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of devices

Get: Devices(self: Project) -> DeviceComposition

"""

    Family = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The project family

Get: Family(self: Project) -> str

"""

    Graphics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of graphics

Get: Graphics(self: Project) -> MultiLingualGraphicComposition

"""

    HistoryEntries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Contains log of project history events

Get: HistoryEntries(self: Project) -> HistoryEntryComposition

"""

    HwUtilities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of HW extensions

Get: HwUtilities(self: Project) -> HardwareUtilityComposition

"""

    IsModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if there are unsaved changes to the project

Get: IsModified(self: Project) -> bool

"""

    IsPrimary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether the project is the primary project

Get: IsPrimary(self: Project) -> bool

"""

    LanguageSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Project's language settings.

Get: LanguageSettings(self: Project) -> LanguageSettings

"""

    LastModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The time of the last modification of the project

Get: LastModified(self: Project) -> DateTime

"""

    LastModifiedBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The project was last modified by this user.

Get: LastModifiedBy(self: Project) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the project

Get: Name(self: Project) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: Project) -> IEngineeringObject

"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The path to this project

Get: Path(self: Project) -> FileInfo

"""

    ProjectLibrary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the project library

Get: ProjectLibrary(self: Project) -> ProjectLibrary

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size of the project in KB

Get: Size(self: Project) -> Int64

"""

    Subnets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of Subnets

Get: Subnets(self: Project) -> SubnetComposition

"""

    UngroupedDevicesGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the devices system group

Get: UngroupedDevicesGroup(self: Project) -> DeviceSystemGroup

"""

    UsedProducts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of used products in the project

Get: UsedProducts(self: Project) -> UsedProductComposition

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The version of this project

Get: Version(self: Project) -> str

"""



class ProjectArchivationMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Archivation mode
    
    enum ProjectArchivationMode, values: Compressed (1), DiscardRestorableData (2), DiscardRestorableDataAndCompressed (3), None (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Compressed = None
    DiscardRestorableData = None
    DiscardRestorableDataAndCompressed = None
    None = None
    value__ = None


class ProjectComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[Project], IEquatable[object]):
    """ Composition of Projects """
    def Contains(self, item):
        """
        Contains(self: ProjectComposition, item: Project) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Create(self, targetDirectory, name):
        """
        Create(self: ProjectComposition, targetDirectory: DirectoryInfo, name: str) -> Project
        
            Create Action
        
            targetDirectory: Directory that will contain project's folder.
            name: The name of a project to be created.
            Returns: Siemens.Engineering.Project
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: ProjectComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ProjectComposition) -> IEnumerator[Project]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ProjectComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: ProjectComposition, item: Project) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def Open(self, path, umacDelegate=None, projectOpenMode=None):
        """
        Open(self: ProjectComposition, path: FileInfo) -> Project
        
            Open Action
        
            path: Path to the Tia Portal project file
            Returns: Siemens.Engineering.Project
        Open(self: ProjectComposition, path: FileInfo, umacDelegate: UmacDelegate) -> Project
        
            Open project and authenticate with UMAC if necessary.
        
            path: Path to the Tia Portal project file.
            umacDelegate: Delegate that will be called if user authentication with UMAC is required.
            Returns: Siemens.Engineering.Project
        Open(self: ProjectComposition, path: FileInfo, umacDelegate: UmacDelegate, projectOpenMode: ProjectOpenMode) -> Project
        
            Open project and authenticate with UMAC if necessary.
        
            path: Path to the Tia Portal project file.
            umacDelegate: Delegate that will be called if user authentication with UMAC is required.
            projectOpenMode: Open mode.
            Returns: Siemens.Engineering.Project
        """
        pass

    def OpenWithUpgrade(self, path, umacDelegate=None, projectOpenMode=None):
        """
        OpenWithUpgrade(self: ProjectComposition, path: FileInfo) -> Project
        
            Open Action with project update is necessary
        
            path: Path to the Tia Portal project file
            Returns: Siemens.Engineering.Project
        OpenWithUpgrade(self: ProjectComposition, path: FileInfo, umacDelegate: UmacDelegate) -> Project
        
            Open Action with project update and authenticate with UMAC if necessary.
        
            path: Path to the Tia Portal project file.
            umacDelegate: Delegate that will be called if user authentication with UMAC is required.
            Returns: Siemens.Engineering.Project
        OpenWithUpgrade(self: ProjectComposition, path: FileInfo, umacDelegate: UmacDelegate, projectOpenMode: ProjectOpenMode) -> Project
        
            Open Action with project update and authenticate with UMAC if necessary.
        
            path: Path to the Tia Portal project file.
            umacDelegate: Delegate that will be called if user authentication with UMAC is required.
            projectOpenMode: Open mode.
            Returns: Siemens.Engineering.Project
        """
        pass

    def Retrieve(self, sourcePath, targetDirectory, umacDelegate=None, projectOpenMode=None):
        """
        Retrieve(self: ProjectComposition, sourcePath: FileInfo, targetDirectory: DirectoryInfo) -> Project
        
            Retrieves an archived project
        
            sourcePath: The path of the archived project file
            targetDirectory: The path to the folder where project would be retrieved.
            Returns: Siemens.Engineering.Project
        Retrieve(self: ProjectComposition, sourcePath: FileInfo, targetDirectory: DirectoryInfo, umacDelegate: UmacDelegate) -> Project
        
            Retrieves an archived project with UMAC
        
            sourcePath: The path of the archived project file
            targetDirectory: The path to the folder where project would be retrieved.
            umacDelegate: Delegate will be called if the project is protected and user authentication is required. If the project is not 
             protected, then null can be passed as parameter
        
            Returns: Siemens.Engineering.Project
        Retrieve(self: ProjectComposition, sourcePath: FileInfo, targetDirectory: DirectoryInfo, umacDelegate: UmacDelegate, projectOpenMode: ProjectOpenMode) -> Project
        
            Retrieves an archived project with UMAC and opens the project as Primary or Secorndary
        
            sourcePath: The path of the archived project file
            targetDirectory: The path to the folder where project would be retrieved.
            umacDelegate: Delegate will be called if the project is protected and user authentication is required.If the project is not 
             protected, then null can be passed as parameter
        
            projectOpenMode: Project Open Mode
            Returns: Siemens.Engineering.Project
        """
        pass

    def RetrieveWithUpgrade(self, sourcePath, targetDirectory, umacDelegate=None, projectOpenMode=None):
        """
        RetrieveWithUpgrade(self: ProjectComposition, sourcePath: FileInfo, targetDirectory: DirectoryInfo) -> Project
        
            Retrieves a project from an archive and upgrades it to the current version
        
            sourcePath: The path of the archived project file
            targetDirectory: The path to the folder where project would be retrieved.
            Returns: Siemens.Engineering.Project
        RetrieveWithUpgrade(self: ProjectComposition, sourcePath: FileInfo, targetDirectory: DirectoryInfo, umacDelegate: UmacDelegate) -> Project
        
            Retrieves a project from an archive and upgrades it to the current version with umac
        
            sourcePath: The path of the archived project file
            targetDirectory: The path to the folder where project would be retrieved.
            umacDelegate: Delegate will be called if the project is protected and user authentication is required.If the project is not 
             protected, then null can be passed as parameter
        
            Returns: Siemens.Engineering.Project
        RetrieveWithUpgrade(self: ProjectComposition, sourcePath: FileInfo, targetDirectory: DirectoryInfo, umacDelegate: UmacDelegate, projectOpenMode: ProjectOpenMode) -> Project
        
            Retrieves a project from an archive and upgrades it to the current version
        
            sourcePath: The path of the archived project file
            targetDirectory: The path to the folder where project would be retrieved.
            umacDelegate: Delegate will be called if the project is protected and user authentication is required.If the project is not 
             protected, then null can be passed as parameter
        
            projectOpenMode: Project Open Mode
            Returns: Siemens.Engineering.Project
        """
        pass

    def ToString(self):
        """
        ToString(self: ProjectComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Project](enumerable: IEnumerable[Project], value: Project) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the count.

Get: Count(self: ProjectComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: ProjectComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: ProjectComposition) -> IEngineeringObject

"""



class ProjectOpenMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Project open mode
    
    enum ProjectOpenMode, values: Primary (0), Secondary (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Primary = None
    Secondary = None
    value__ = None


class ProjectTextResult(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents a project text result """
    def Equals(self, obj):
        """
        Equals(self: ProjectTextResult, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: ProjectTextResult, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ProjectTextResult) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: ProjectTextResult, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: ProjectTextResult) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: ProjectTextResult) -> IEngineeringObject

"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Path to a text result

Get: Path(self: ProjectTextResult) -> FileInfo

"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Final state of the project text result

Get: State(self: ProjectTextResult) -> ProjectTextResultState

"""



class ProjectTextResultState(Enum, IComparable, IFormattable, IConvertible):
    """
    The state of project text result
    
    enum ProjectTextResultState, values: Error (2), Info (0), Warning (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Error = None
    Info = None
    value__ = None
    Warning = None


class TiaPortal(object, IApplicationEntryPoint, IInternalApplicationAccess, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEngineeringRoot, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IEquatable[object], IDisposable):
    """
    TIAPortal.
    
    TiaPortal(tiaPortalMode: TiaPortalMode)
    """
    def Dispose(self):
        """
        Dispose(self: TiaPortal)
            Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.
        """
        pass

    def ExclusiveAccess(self, text=None):
        """
        ExclusiveAccess(self: TiaPortal) -> ExclusiveAccess
        
            Acquire an exclusive access session to the TIA Portal
            Returns: Siemens.Engineering.ExclusiveAccess
        ExclusiveAccess(self: TiaPortal, text: str) -> ExclusiveAccess
        
            Acquire an exclusive access session to the TIA Portal
        
            text: The text to present to the interactive user while an exclusive access session is active
            Returns: Siemens.Engineering.ExclusiveAccess
        """
        pass

    def GetCurrentProcess(self):
        """
        GetCurrentProcess(self: TiaPortal) -> TiaPortalProcess
        
            Gets the information of connected TIA-Portal.
            Returns: The connected TIA-Portal.
        """
        pass

    @staticmethod
    def GetProcess(processId, *__args):
        """
        GetProcess(processId: int, millisecondsTimeout: int) -> TiaPortalProcess
        
            Gets the information of the running TIA-Portal.
        
            processId: TIA-Portal's process id.
            millisecondsTimeout: An optional parameter that provides the ability to set a timeout.
            Returns: The running TIA-Portal.
        GetProcess(processId: int, timeout: TimeSpan) -> TiaPortalProcess
        
            Gets the information of the running TIA-Portal.
        
            processId: TIA-Portal's process id.
            timeout: An optional parameter that provides the ability to set a timeout.
            Returns: The running TIA-Portal.
        """
        pass

    @staticmethod
    def GetProcesses():
        """
        GetProcesses() -> IList[TiaPortalProcess]
        
            Gets the information of all running TIA-Portals.
            Returns: The running TIA-Portals.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, tiaPortalMode):
        """ __new__(cls: type, tiaPortalMode: TiaPortalMode) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    GlobalLibraries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of global libraries

Get: GlobalLibraries(self: TiaPortal) -> GlobalLibraryComposition

"""

    Projects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of open projects

Get: Projects(self: TiaPortal) -> ProjectComposition

"""

    SettingsFolders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The settings of the TIA portal

Get: SettingsFolders(self: TiaPortal) -> TiaPortalSettingsFolderComposition

"""


    Confirmation = None
    Disposed = None
    Notification = None


class TiaPortalAccessLevel(Enum, IComparable, IFormattable, IConvertible):
    """
    The access level of the associated TIA Portal
    
    enum (flags) TiaPortalAccessLevel, values: Elevated (256), Modify (4), NoLicense (1), None (0), Pilot (32), Published (8), Trusted (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Elevated = None
    Modify = None
    NoLicense = None
    None = None
    Pilot = None
    Published = None
    Trusted = None
    value__ = None


class TiaPortalMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Mode how to start the TIA-Portal.
    
    enum TiaPortalMode, values: WithoutUserInterface (0), WithUserInterface (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    value__ = None
    WithoutUserInterface = None
    WithUserInterface = None


class TiaPortalProcess(object, IDisposable):
    """ TiaPortalProcess """
    def Attach(self):
        """
        Attach(self: TiaPortalProcess) -> TiaPortal
        
            Gets an additional instance of a TIA-Portal that is attached to the TIA-Portal process.
            Returns: A TIA-Portal instance that is attached to the TIA-Portal process.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: TiaPortalProcess)
            Performs a close of the process.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AcquisitionTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time when the TiaPortalProcess object was acquired.

Get: AcquisitionTime(self: TiaPortalProcess) -> DateTime

"""

    AttachedSessions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a list of other process attached to this same TIA-Portal process.

Get: AttachedSessions(self: TiaPortalProcess) -> IList[TiaPortalSession]

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Process ID of the TIA Portal.

Get: Id(self: TiaPortalProcess) -> int

"""

    InstalledSoftware = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a list of installed software of the TIA-Portal process.

Get: InstalledSoftware(self: TiaPortalProcess) -> IList[TiaPortalProduct]

"""

    Mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the mode of the attached TIA-Portal.

Get: Mode(self: TiaPortalProcess) -> TiaPortalMode

"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The path to the executable of the TIA Portal.

Get: Path(self: TiaPortalProcess) -> FileInfo

"""

    ProjectPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the path of any project currently open in the attached TIA_Portal.

Get: ProjectPath(self: TiaPortalProcess) -> FileInfo

"""


    Attaching = None


class TiaPortalProduct(object):
    """ TiaPortalProduct """
    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the product name.

Get: Name(self: TiaPortalProduct) -> str

"""

    Options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a list of installed options of the TIA-Portal process.

Get: Options(self: TiaPortalProduct) -> IList[TiaPortalProduct]

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the product version.

Get: Version(self: TiaPortalProduct) -> str

"""



class TiaPortalSession(object, IDisposable):
    """ TiaPortalSession """
    def Dispose(self):
        """
        Dispose(self: TiaPortalSession)
            Performs a diconnect of the session.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AccessLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the access level of the process.

Get: AccessLevel(self: TiaPortalSession) -> TiaPortalAccessLevel

"""

    AttachTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the attached session date and time.

Get: AttachTime(self: TiaPortalSession) -> DateTime

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the attached session identifier.

Get: Id(self: TiaPortalSession) -> int

"""

    IsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a boolean value describing whether the TIA Portal is in  the middle of processing a call from this session.

Get: IsActive(self: TiaPortalSession) -> bool

"""

    ProcessId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the attached session process identifier.

Get: ProcessId(self: TiaPortalSession) -> int

"""

    ProcessPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the path to where the executable of the attached process lives.

Get: ProcessPath(self: TiaPortalSession) -> FileInfo

"""

    TrustAuthority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the current session was started by a process that was signed, and if so, if it is an Openness certificate or not.

Get: TrustAuthority(self: TiaPortalSession) -> TiaPortalTrustAuthority

"""

    UtilizationTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets time the process has spent actively using the TIA Portal.

Get: UtilizationTime(self: TiaPortalSession) -> TimeSpan

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the attached session version.

Get: Version(self: TiaPortalSession) -> str

"""



class TiaPortalTrustAuthority(Enum, IComparable, IFormattable, IConvertible):
    """
    The trust authority of the associated TIA Portal
    
    enum (flags) TiaPortalTrustAuthority, values: Certified (2), CertifiedWithExpiration (256), FeatureTokens (512), None (0), Signed (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Certified = None
    CertifiedWithExpiration = None
    FeatureTokens = None
    None = None
    Signed = None
    value__ = None


class Transaction(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IDisposable, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents an open transaction in a persistence (i.e. single unit of work) """
    def CommitOnDispose(self):
        """
        CommitOnDispose(self: Transaction)
            Commit transaction when disposed
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Transaction)
            Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: Transaction, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: Transaction, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Transaction) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: Transaction, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: Transaction) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CanCommit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the transaction can be committed.

Get: CanCommit(self: Transaction) -> bool

"""

    CommitRequested = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if a commit has been requested.

Get: CommitRequested(self: Transaction) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: Transaction) -> IEngineeringObject

"""



class UmacCredentials(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Object that is used to authenticate user. """
    def Equals(self, obj):
        """
        Equals(self: UmacCredentials, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: UmacCredentials, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: UmacCredentials) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: UmacCredentials, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def SetPassword(self, password):
        """
        SetPassword(self: UmacCredentials, password: SecureString)
            Set password.
        
            password: Password
        """
        pass

    def ToString(self):
        """
        ToString(self: UmacCredentials) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """User name.

Get: Name(self: UmacCredentials) -> str

Set: Name(self: UmacCredentials) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: UmacCredentials) -> IEngineeringObject

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """User Type

Get: Type(self: UmacCredentials) -> UmacUserType

Set: Type(self: UmacCredentials) = value
"""



class UmacDelegate(MulticastDelegate, ICloneable, ISerializable):
    """
    The delegate that will called back for user credetials if project is protected.
    
    UmacDelegate(object: object, method: IntPtr)
    """
    def BeginInvoke(self, umacCredentials, callback, object):
        """ BeginInvoke(self: UmacDelegate, umacCredentials: UmacCredentials, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- 
             
                    ll, if the method represented by the current delegate does not require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: UmacDelegate, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, umacCredentials):
        """ Invoke(self: UmacDelegate, umacCredentials: UmacCredentials) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified 
             delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its 
             invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class UmacUserType(Enum, IComparable, IFormattable, IConvertible):
    """
    User type.
    
    enum UmacUserType, values: Global (1), Project (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Global = None
    Project = None
    value__ = None


class UsedProduct(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents a product used by a project """
    def Equals(self, obj):
        """
        Equals(self: UsedProduct, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: UsedProduct, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: UsedProduct) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: UsedProduct, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: UsedProduct) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the used product

Get: Name(self: UsedProduct) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: UsedProduct) -> IEngineeringObject

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The product version

Get: Version(self: UsedProduct) -> str

"""



class UsedProductComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[UsedProduct], IEquatable[object]):
    """ Composition of UsedProducts """
    def Contains(self, item):
        """
        Contains(self: UsedProductComposition, item: UsedProduct) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: UsedProductComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: UsedProductComposition) -> IEnumerator[UsedProduct]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: UsedProductComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: UsedProductComposition, item: UsedProduct) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: UsedProductComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[UsedProduct](enumerable: IEnumerable[UsedProduct], value: UsedProduct) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the count.

Get: Count(self: UsedProductComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: UsedProductComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: UsedProductComposition) -> IEngineeringObject

"""



# variables with complex values

