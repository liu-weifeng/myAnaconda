import string
from flags import flags

def getDiskPart(dev, storage):
    device = storage.devicetree.getDeviceByName(dev)
    if device is None:
        return (dev, None)
    path = device.path[5:]
    cut = len(dev)
    if dev[-1] in string.digits:
        if (path.startswith('rd/') or path.startswith('ida/') or
                path.startswith('cciss/') or path.startswith('sx8/') or
                path.startswith('mapper/') or path.startswith('mmcblk') or
                path.startswith('md') or path.startswith('nvme')):
            if dev[-2] == 'p':
                cut = -2
            elif dev[-3] == 'p' and dev[-2] in string.digits:
                cut = -3
        else:
            if dev[-2] in string.digits:
                cut = -2
            else:
                cut = -1

    name = dev[:cut]

    if cut < 0:
        part = dev[cut:]
        if part[0] == 'p':
            part = part[1:]
        partNum = int(part) - 1
    else:
        partNum = None

    return (name, partNum)

