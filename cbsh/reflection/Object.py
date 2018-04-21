# automatically generated by the FlatBuffers compiler, do not modify

# namespace: reflection

import flatbuffers

class Object(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsObject(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Object()
        x.Init(buf, n + offset)
        return x

    # Object
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Object
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

    # Object
    def Fields(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Field import Field
            obj = Field()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Object
    def FieldsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Object
    def IsStruct(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

    # Object
    def Minalign(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Object
    def Bytesize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Object
    def Attributes(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .KeyValue import KeyValue
            obj = KeyValue()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Object
    def AttributesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Object
    def Documentation(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # Object
    def DocumentationLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def ObjectStart(builder): builder.StartObject(7)
def ObjectAddName(builder, name): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def ObjectAddFields(builder, fields): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(fields), 0)
def ObjectStartFieldsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ObjectAddIsStruct(builder, isStruct): builder.PrependBoolSlot(2, isStruct, 0)
def ObjectAddMinalign(builder, minalign): builder.PrependInt32Slot(3, minalign, 0)
def ObjectAddBytesize(builder, bytesize): builder.PrependInt32Slot(4, bytesize, 0)
def ObjectAddAttributes(builder, attributes): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(attributes), 0)
def ObjectStartAttributesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ObjectAddDocumentation(builder, documentation): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(documentation), 0)
def ObjectStartDocumentationVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ObjectEnd(builder): return builder.EndObject()
