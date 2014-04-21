# Convenience functions for reading bytes
from scipy.io.idl import _read_uint32


def read_string(f):
    length = _read_uint32(f)
    string = f.read(length)
    print string
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


def read_tiledcellstman(f):
    assert read_string(f) == "TiledCellStMan"
    unkn = _read_uint32(f)
    print unkn


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
    else:
        raise ValueError("Unknown record type: {0}".format(record_type))


def read_table_header(filename):

    f = open(filename)
    f.read(4)
    for block in range(8):
        print "-" * 72
        read_block(f)


if __name__ == "__main__":
    read_table_header('BR1202.line.selfcal.clean.image/table.f0')
