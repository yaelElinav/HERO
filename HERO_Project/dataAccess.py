class dataAccess:
    source = "file"
    path = " "

    def __init__(src, pth):
        if src == "file":
            path = pth
        # load the data sets from configuration file

    def loader(self, name, state):
        # the vm stats divided to the different categories
        stats = {'vm_name': name, 'state': state}

        if state == 'on':
            self.loadOn(stats)
        if state == 'off':
            # read the virsh commands from the kvm itself
            pass

    def loadOn(self, stats):
        cpu = []
        nic = []
        ram = []
        mismatch = []

        if self.source == "file":
            # if files become too big, can be changed to .readline() with a while and another .readline at the end
            file = open(self.path, 'r')
            lines = file.readlines()
            file.close()

            for line in lines:
                if line.startswith("Date: "):
                    # add to all the strings that care for date
                    cpu.append(line)
                    nic.append(line)
                    ram.append(line)

                if line.startswith("CPU Average:"):
                    # add to cpu
                    cpu.append(line)
                elif line.startswith("Network "):
                    nic.append(line)
                elif line.startswith("Used RAM:"):
                    ram.append(line)
                else:
                    mismatch.append(line)

            # TODO: do we want a list or string
            stats['cpu'] = '\n'.join(cpu)
            stats['nic'] = '\n'.join(nic)
            stats['ram'] = '\n'.join(ram)
            stats['mismatch'] = '\n'.join(mismatch)

    @classmethod
    def getOnVMs(cls):
        # TODO: Figure out how to run virsh commands

        # returns an array/list of the VM names
        pass

    @classmethod
    def getOffVMs(cls):
        # returns an array/list of the VM names
        pass

    @classmethod
    def geAllVMs(cls):
        # returns an array/list of the VM names
        pass
