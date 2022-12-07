# encoding: utf-8
# module Siemens.Engineering.SW.TechnologicalObjects.Motion calls itself Motion
# from Siemens.Engineering,Version=15.1.0.0,Culture=neutral,PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AxisEncoderHardwareConnectionInterface(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Handles connections to hardware objects for axis and encoder TechnologicalInstanceDBs """
 def Connect(self,*__args):
  """
  Connect(self: AxisEncoderHardwareConnectionInterface,channel: Channel)

   Connect with a Channel (e.g. of a TechnologyModule)

  

   channel: Channel to connect

  Connect(self: AxisEncoderHardwareConnectionInterface,moduleInOut: DeviceItem)

   Connect with a mixed (sub) module that contains input and output addresses

  

   moduleInOut: Module or submodule that contains input and output addresses

  Connect(self: AxisEncoderHardwareConnectionInterface,outputTag: PlcTag)

   Connect to an output PlcTag in order to establish an analog connection

  

   outputTag: Output PlcTag to connect

  Connect(self: AxisEncoderHardwareConnectionInterface,pathToDBMember: str)

   Connect to DB member

  

   pathToDBMember: Path to the DB member

  Connect(self: AxisEncoderHardwareConnectionInterface,moduleIn: DeviceItem,moduleOut: DeviceItem)

   Connect with separate (sub) modules for inputs and outputs,specifying an additional ConnectOption

  

   moduleIn: Module or submodule that contains the input address

   moduleOut: Module or submodule that contains the output address

  Connect(self: AxisEncoderHardwareConnectionInterface,moduleIn: DeviceItem,moduleOut: DeviceItem,connectOption: ConnectOption)

   Connect with separate (sub) modules for inputs and outputs,specifying an additional ConnectOption

  

   moduleIn: Module or submodule that contains the input address

   moduleOut: Module or submodule that contains the output address

   connectOption: Additional option for making the connection

  Connect(self: AxisEncoderHardwareConnectionInterface,addressIn: int,addressOut: int,connectOption: ConnectOption)

   Connect specifying input and output bit addresses directly

  

   addressIn: Input bit address to connect

   addressOut: Output bit address to connect

   connectOption: Additional option for making the connection
  """
  pass
 def Disconnect(self):
  """
  Disconnect(self: AxisEncoderHardwareConnectionInterface)

   Remove an existing connection
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: AxisEncoderHardwareConnectionInterface,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: AxisEncoderHardwareConnectionInterface,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: AxisEncoderHardwareConnectionInterface) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: AxisEncoderHardwareConnectionInterface,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: AxisEncoderHardwareConnectionInterface) -> str

  

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
 Channel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Connected Channel



Get: Channel(self: AxisEncoderHardwareConnectionInterface) -> Channel



"""

 ConnectOption=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """ConnectOption that has been set when the connection was made



Get: ConnectOption(self: AxisEncoderHardwareConnectionInterface) -> ConnectOption



"""

 InputAddress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Raw input bit address



Get: InputAddress(self: AxisEncoderHardwareConnectionInterface) -> int



"""

 InputModule=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Connected input (sub) module



Get: InputModule(self: AxisEncoderHardwareConnectionInterface) -> DeviceItem



"""

 InputOutputModule=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Connected mixed (sub) module that contains input and output addresses



Get: InputOutputModule(self: AxisEncoderHardwareConnectionInterface) -> DeviceItem



"""

 IsConnected=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether the interface is connected



Get: IsConnected(self: AxisEncoderHardwareConnectionInterface) -> bool



"""

 OutputAddress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Raw output bit address



Get: OutputAddress(self: AxisEncoderHardwareConnectionInterface) -> int



"""

 OutputModule=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Connected output (sub) module



Get: OutputModule(self: AxisEncoderHardwareConnectionInterface) -> DeviceItem



"""

 OutputTag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Connected tag (analog connection)



Get: OutputTag(self: AxisEncoderHardwareConnectionInterface) -> PlcTag



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: AxisEncoderHardwareConnectionInterface) -> IEngineeringObject



"""

 PathToDBMember=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Path to connected DB member



Get: PathToDBMember(self: AxisEncoderHardwareConnectionInterface) -> str



"""

 SensorIndexInActorTelegram=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Connection to sensor part in actor telegram.



Get: SensorIndexInActorTelegram(self: AxisEncoderHardwareConnectionInterface) -> int



"""



class AxisEncoderHardwareConnectionInterfaceComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[AxisEncoderHardwareConnectionInterface],IEquatable[object]):
 """ AxisEncoderHardwareConnectionInterface Composition """
 def Contains(self,item):
  """
  Contains(self: AxisEncoderHardwareConnectionInterfaceComposition,item: AxisEncoderHardwareConnectionInterface) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: AxisEncoderHardwareConnectionInterfaceComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: AxisEncoderHardwareConnectionInterfaceComposition) -> IEnumerator[AxisEncoderHardwareConnectionInterface]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: AxisEncoderHardwareConnectionInterfaceComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: AxisEncoderHardwareConnectionInterfaceComposition,item: AxisEncoderHardwareConnectionInterface) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: AxisEncoderHardwareConnectionInterfaceComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[AxisEncoderHardwareConnectionInterface](enumerable: IEnumerable[AxisEncoderHardwareConnectionInterface],value: AxisEncoderHardwareConnectionInterface) -> bool """
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



Get: Count(self: AxisEncoderHardwareConnectionInterfaceComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: AxisEncoderHardwareConnectionInterfaceComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: AxisEncoderHardwareConnectionInterfaceComposition) -> IEngineeringObject



"""



class AxisHardwareConnectionProvider(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IEngineeringService,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Handles connections to hardware objects for axis TechnologicalInstanceDBs """
 def Equals(self,obj):
  """
  Equals(self: AxisHardwareConnectionProvider,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: AxisHardwareConnectionProvider,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: AxisHardwareConnectionProvider) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: AxisHardwareConnectionProvider,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: AxisHardwareConnectionProvider) -> str

  

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
 ActorInterface=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides access to the connections for the actor interface of the axis



Get: ActorInterface(self: AxisHardwareConnectionProvider) -> AxisEncoderHardwareConnectionInterface



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: AxisHardwareConnectionProvider) -> IEngineeringObject



"""

 SensorInterface=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides access to the connections for the sensor interfaces of the axis



Get: SensorInterface(self: AxisHardwareConnectionProvider) -> AxisEncoderHardwareConnectionInterfaceComposition



"""

 TorqueInterface=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides access to the torque connection interface of the axis



Get: TorqueInterface(self: AxisHardwareConnectionProvider) -> TorqueHardwareConnectionInterface



"""



class CamDataFormat(Enum,IComparable,IFormattable,IConvertible):
 """
 Describes the format in which a cam object should be Exportet/Imported

 

 enum CamDataFormat,values: MCD (0),PointList (2),Scout (1)
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
 MCD=None
 PointList=None
 Scout=None
 value__=None


class CamDataFormatSeparator(Enum,IComparable,IFormattable,IConvertible):
 """
 Describes a Seperator with which the data should be seperated on Import/Export

 

 enum CamDataFormatSeparator,values: Comma (0),Tab (1)
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
 Comma=None
 Tab=None
 value__=None


class CamDataSupport(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IEngineeringService,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Handles import export commands for Cam """
 def Equals(self,obj):
  """
  Equals(self: CamDataSupport,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: CamDataSupport,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: CamDataSupport) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def LoadCamData(self,sourceFile,separator):
  """
  LoadCamData(self: CamDataSupport,sourceFile: FileInfo,separator: CamDataFormatSeparator)

   Loads the cam data from the specified file

  

   sourceFile: Path to the file that will be loaded

   separator: Separator to use
  """
  pass
 def LoadCamDataBinary(self,sourceFile):
  """
  LoadCamDataBinary(self: CamDataSupport,sourceFile: FileInfo)

   Loads the cam data from the specified binary file

  

   sourceFile: Path to the file that will be loaded
  """
  pass
 def SaveCamData(self,destinationFile,format,separator):
  """
  SaveCamData(self: CamDataSupport,destinationFile: FileInfo,format: CamDataFormat,separator: CamDataFormatSeparator)

   Saves the cam data to the specified file in the given format

  

   destinationFile: Path to the destination file

   format: format in which the data should be stored

   separator: Separator to use
  """
  pass
 def SaveCamDataBinary(self,destinationFile):
  """
  SaveCamDataBinary(self: CamDataSupport,destinationFile: FileInfo)

   Saves the cam data to the specified file in binary format

  

   destinationFile: Path to the destination file
  """
  pass
 def SaveCamDataPointList(self,destinationFile,separator,samplePoints):
  """
  SaveCamDataPointList(self: CamDataSupport,destinationFile: FileInfo,separator: CamDataFormatSeparator,samplePoints: int)

   Saves the cam data to the specified file as a point list

  

   destinationFile: Path to the destination file

   separator: Separator to use

   samplePoints: Number of sample points
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: CamDataSupport,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: CamDataSupport) -> str

  

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



Get: Parent(self: CamDataSupport) -> IEngineeringObject



"""



class ConnectOption(Enum,IComparable,IFormattable,IConvertible):
 """
 Describes additional options for making a connection

 

 enum ConnectOption,values: AllowAllModules (1),Default (0)
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
 AllowAllModules=None
 Default=None
 value__=None


class EncoderHardwareConnectionProvider(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IEngineeringService,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Handles connections to hardware objects for encoder TechnologicalInstanceDBs """
 def Equals(self,obj):
  """
  Equals(self: EncoderHardwareConnectionProvider,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: EncoderHardwareConnectionProvider,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: EncoderHardwareConnectionProvider) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: EncoderHardwareConnectionProvider,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: EncoderHardwareConnectionProvider) -> str

  

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



Get: Parent(self: EncoderHardwareConnectionProvider) -> IEngineeringObject



"""

 SensorInterface=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides access to the connections for the sensor interface of the encoder



Get: SensorInterface(self: EncoderHardwareConnectionProvider) -> AxisEncoderHardwareConnectionInterface



"""



class MeasuringInputHardwareConnectionProvider(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IEngineeringService,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Handles connections to hardware objects for measuring input TechnologicalInstanceDBs """
 def Connect(self,*__args):
  """
  Connect(self: MeasuringInputHardwareConnectionProvider,channel: Channel)

   Connect with a Channel (e.g. of a TechnologyModule)

  

   channel: Channel to connect

  Connect(self: MeasuringInputHardwareConnectionProvider,addressIn: int)

   Connect specifying the input bit address directly

  

   addressIn: Input bit address to connect

  Connect(self: MeasuringInputHardwareConnectionProvider,moduleIn: DeviceItem,channelIndex: int)

   Connect with a (sub) module,specifying an additional channel index

  

   moduleIn: Module or submodule to connect

   channelIndex: Index of connected channel with respect to moduleIn
  """
  pass
 def Disconnect(self):
  """
  Disconnect(self: MeasuringInputHardwareConnectionProvider)

   Remove an existing connection
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: MeasuringInputHardwareConnectionProvider,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: MeasuringInputHardwareConnectionProvider,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: MeasuringInputHardwareConnectionProvider) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: MeasuringInputHardwareConnectionProvider,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: MeasuringInputHardwareConnectionProvider) -> str

  

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
 Channel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Connected Channel



Get: Channel(self: MeasuringInputHardwareConnectionProvider) -> Channel



"""

 ChannelIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Index of connected channel with respect to InputModule



Get: ChannelIndex(self: MeasuringInputHardwareConnectionProvider) -> int



"""

 InputAddress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Raw input bit address



Get: InputAddress(self: MeasuringInputHardwareConnectionProvider) -> int



"""

 InputModule=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Connected input (sub) module



Get: InputModule(self: MeasuringInputHardwareConnectionProvider) -> DeviceItem



"""

 IsConnected=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether the interface is connected



Get: IsConnected(self: MeasuringInputHardwareConnectionProvider) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: MeasuringInputHardwareConnectionProvider) -> IEngineeringObject



"""



class OutputCamHardwareConnectionProvider(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IEngineeringService,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Handles connections to hardware objects for output cam and cam track TechnologicalInstanceDBs """
 def Connect(self,*__args):
  """
  Connect(self: OutputCamHardwareConnectionProvider,channel: Channel)

   Connect with a Channel (e.g. of a TechnologyModule)

  

   channel: Channel to connect

  Connect(self: OutputCamHardwareConnectionProvider,outputTag: PlcTag)

   Connect to an output PlcTag

  

   outputTag: Output PlcTag to connect

  Connect(self: OutputCamHardwareConnectionProvider,addressOut: int)

   Connect specifying the output bit address directly

  

   addressOut: Output bit address to connect
  """
  pass
 def Disconnect(self):
  """
  Disconnect(self: OutputCamHardwareConnectionProvider)

   Remove an existing connection
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: OutputCamHardwareConnectionProvider,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: OutputCamHardwareConnectionProvider,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: OutputCamHardwareConnectionProvider) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: OutputCamHardwareConnectionProvider,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: OutputCamHardwareConnectionProvider) -> str

  

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
 Channel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Connected Channel



Get: Channel(self: OutputCamHardwareConnectionProvider) -> Channel



"""

 IsConnected=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether the interface is connected



Get: IsConnected(self: OutputCamHardwareConnectionProvider) -> bool



"""

 OutputAddress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Raw output bit address



Get: OutputAddress(self: OutputCamHardwareConnectionProvider) -> int



"""

 OutputTag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Connected tag



Get: OutputTag(self: OutputCamHardwareConnectionProvider) -> PlcTag



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: OutputCamHardwareConnectionProvider) -> IEngineeringObject



"""



class OutputCamMeasuringInputContainer(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IEngineeringService,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Container for output cam,cam track and measuring input TOs """
 def Equals(self,obj):
  """
  Equals(self: OutputCamMeasuringInputContainer,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: OutputCamMeasuringInputContainer,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: OutputCamMeasuringInputContainer) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: OutputCamMeasuringInputContainer,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: OutputCamMeasuringInputContainer) -> str

  

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
 MeasuringInputs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Contains measuring input TOs



Get: MeasuringInputs(self: OutputCamMeasuringInputContainer) -> TechnologicalInstanceDBComposition



"""

 OutputCams=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Contains output cam and cam track TOs



Get: OutputCams(self: OutputCamMeasuringInputContainer) -> TechnologicalInstanceDBComposition



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: OutputCamMeasuringInputContainer) -> IEngineeringObject



"""



class SynchronousAxisMasterValues(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IEngineeringService,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Handles connections between SynchronousAxis Technological Objects and their master values """
 def Equals(self,obj):
  """
  Equals(self: SynchronousAxisMasterValues,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: SynchronousAxisMasterValues,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: SynchronousAxisMasterValues) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: SynchronousAxisMasterValues,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: SynchronousAxisMasterValues) -> str

  

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
 ActualValueCoupling=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Master values that are coupled via actual values



Get: ActualValueCoupling(self: SynchronousAxisMasterValues) -> TechnologicalInstanceDBAssociation



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: SynchronousAxisMasterValues) -> IEngineeringObject



"""

 SetPointCoupling=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Master values that are coupled via set points



Get: SetPointCoupling(self: SynchronousAxisMasterValues) -> TechnologicalInstanceDBAssociation



"""



class TorqueHardwareConnectionInterface(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Handles connections to Torque possible hardware objects for axis and encoder TechnologicalInstanceDBs """
 def Connect(self,*__args):
  """
  Connect(self: TorqueHardwareConnectionInterface,moduleInOut: DeviceItem)

   Connect with a mixed (sub) module that contains input and output addresses

  

   moduleInOut: Module or submodule that contains input and output addresses

  Connect(self: TorqueHardwareConnectionInterface,pathToDBMember: str)

   Connect to DB member

  

   pathToDBMember: Path to the DB member

  Connect(self: TorqueHardwareConnectionInterface,moduleIn: DeviceItem,moduleOut: DeviceItem)

   Connect with separate (sub) modules for inputs and outputs,specifying an additional ConnectOption

  

   moduleIn: Module or submodule that contains the input address

   moduleOut: Module or submodule that contains the output address

  Connect(self: TorqueHardwareConnectionInterface,moduleIn: DeviceItem,moduleOut: DeviceItem,connectOption: ConnectOption)

   Connect with separate (sub) modules for inputs and outputs,specifying an additional ConnectOption

  

   moduleIn: Module or submodule that contains the input address

   moduleOut: Module or submodule that contains the output address

   connectOption: Additional option for making the connection

  Connect(self: TorqueHardwareConnectionInterface,addressIn: int,addressOut: int,connectOption: ConnectOption)

   Connect specifying input and output bit addresses directly

  

   addressIn: Input bit address to connect

   addressOut: Output bit address to connect

   connectOption: Additional option for making the connection
  """
  pass
 def Disconnect(self):
  """
  Disconnect(self: TorqueHardwareConnectionInterface)

   Remove an existing connection
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: TorqueHardwareConnectionInterface,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: TorqueHardwareConnectionInterface,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TorqueHardwareConnectionInterface) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: TorqueHardwareConnectionInterface,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: TorqueHardwareConnectionInterface) -> str

  

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
 ConnectOption=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """ConnectOption that has been set when the connection was made



Get: ConnectOption(self: TorqueHardwareConnectionInterface) -> ConnectOption



"""

 InputAddress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Raw input bit address



Get: InputAddress(self: TorqueHardwareConnectionInterface) -> int



"""

 InputModule=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Connected input (sub) module



Get: InputModule(self: TorqueHardwareConnectionInterface) -> DeviceItem



"""

 InputOutputModule=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Connected mixed (sub) module that contains input and output addresses



Get: InputOutputModule(self: TorqueHardwareConnectionInterface) -> DeviceItem



"""

 IsConnected=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether the interface is connected



Get: IsConnected(self: TorqueHardwareConnectionInterface) -> bool



"""

 OutputAddress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Raw output bit address



Get: OutputAddress(self: TorqueHardwareConnectionInterface) -> int



"""

 OutputModule=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Connected output (sub) module



Get: OutputModule(self: TorqueHardwareConnectionInterface) -> DeviceItem



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: TorqueHardwareConnectionInterface) -> IEngineeringObject



"""

 PathToDBMember=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Path to connected DB member



Get: PathToDBMember(self: TorqueHardwareConnectionInterface) -> str



"""



