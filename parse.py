import numpy as np

# Convenience functions for reading bytes
from scipy.io.idl import _read_uint32


def read_string(f):
    length = _read_uint32(f)
    if length > 64:
        raise ValueError("length out of range")
    string = f.read(length)
    print length, string
    return string


def read_iposition(f):
    assert read_string(f) == "IPosition"
    unkn = _read_uint32(f)
    print unkn
    unkn = _read_uint32(f)
    print unkn
    unkn = _read_uint32(f)
    print unkn
    unkn = _read_uint32(f)
    print unkn
    unkn = _read_uint32(f)
    print unkn
    unkn = _read_uint32(f)
    print unkn


def read_record_desc(f):
    assert read_string(f) == "RecordDesc"
    unkn = _read_uint32(f)
    print unkn
    unkn = _read_uint32(f)
    print unkn
    unkn = _read_uint32(f)
    print unkn
    unkn = _read_uint32(f)
    print unkn
    f.read(1)


def read_record(f):
    assert read_string(f) == "Record"
    unkn = _read_uint32(f)
    print unkn


def read_map(f):
    assert read_string(f) == "map"
    unkn = _read_uint32(f)
    print unkn
    unkn = _read_uint32(f)
    print unkn
    unkn = _read_uint32(f)
    print unkn
    unkn = _read_uint32(f)
    print unkn
    unkn = _read_uint32(f)
    print unkn
    unkn = _read_uint32(f)
    print unkn
    f.read(1)
    unkn = _read_uint32(f)
    print unkn
    unkn = _read_uint32(f)
    print unkn


def read_tiledstman(f):
    assert read_string(f) == "TiledStMan"
    f.read(1)
    # print repr(f.read(30))
    unkn = _read_uint32(f)
    print unkn
    unkn = _read_uint32(f)
    print unkn
    unkn = _read_uint32(f)
    print unkn
    unkn = _read_uint32(f)
    print unkn


def read_table(f):
    assert read_string(f) == "Table"
    unkn = _read_uint32(f)
    print unkn
    unkn = _read_uint32(f)
    print unkn


def read_tiledcellstman(f):
    assert read_string(f) == "TiledCellStMan"
    unkn = _read_uint32(f)
    print unkn


def read_plain_table(f):
    assert read_string(f) == "PlainTable"

def read_table_desc(f):
    assert read_string(f) == "TableDesc"
    unkn = _read_uint32(f)
    print unkn
    unkn = _read_uint32(f)
    print unkn
    unkn = _read_uint32(f)
    print unkn
    unkn = _read_uint32(f)


def read_table_record(f):
    assert read_string(f) == "TableRecord"
    unkn = _read_uint32(f)
    print unkn

def read_record_desc(f):
    # Needs to be more flexible - length is content-dependent
    assert read_string(f) == "RecordDesc"
    first = _read_uint32(f)
    print first
    unkn = _read_uint32(f)
    print unkn
    if unkn == 0:
        unkn = _read_uint32(f)
        print unkn
    string = read_string(f)
    print string
    unkn = _read_uint32(f)
    print unkn

    if unkn == 12:

        unkn = _read_uint32(f)
        print unkn
        unkn = _read_uint32(f)
        print unkn
        string = read_string(f)
        print string
        unkn = _read_uint32(f)
        print unkn

    if unkn == 11:

        unkn = _read_uint32(f)
        print unkn
        unkn = _read_uint32(f)
        print unkn
        string = read_string(f)
        print string

def read_block(f):
    record_type = _read_uint32(f)
    if record_type == 41:
        return read_iposition(f)
    elif record_type == 26:
        return read_record_desc(f)
    elif record_type == 48:
        return read_record(f)
    elif record_type == 7:
        return read_map(f)
    elif record_type == 222:
        return read_tiledstman(f)
    elif record_type == 289:
        return read_tiledcellstman(f)
    elif record_type == 7717:
        return read_table(f)
    elif record_type == 1:
        return read_plain_table(f)
    elif record_type == 7616:
        return read_table_desc(f)
    elif record_type == 6965 or record_type == 6079:
        return read_table_record(f)
    elif record_type == 158 or record_type == 983:
        return read_record_desc(f)
    else:
        raise ValueError("Unknown record type: {0}".format(record_type))


def read_table_header(filename):

    f = open(filename)
    f.read(4)
    for block in range(20):
        print "-" * 72
        read_block(f)


if __name__ == "__main__":
    # read_table_header('BR1202.line.selfcal.clean.image/table.f0')
    read_table_header('BR1202.line.selfcal.clean.image/table.dat')

    f = open('BR1202.line.selfcal.clean.image/table.dat')
    content = f.read()
    for i in range(1000):
        if content[i:i+10] == "RecordDesc":
            print repr(content[i:i+128])
