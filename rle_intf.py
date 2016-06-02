
"""The interface(s) to the run-length-encoder (RLE).
The goal is to capture the interfaces between subblocks and build 
an interface and transactors to the subblocks then these interfaces 
will be used to test and verify the models and implementations.

The run-length-encoder encodes 64 inputs samples into a variable 
number of output symbols.  The RLE, base on reference 1, has and 
interface that streams the data in and streams symbols out.
"""

from myhdl import Signal, intbv


class DataStream(object):
    def __init__(self, width=8):
        """Streaming data interface to each subblock
        """
        # each block has a global system clock and reset as 
        # separate ports.  It has been suggested that a basic 
        # ready valid 
        self.ready = Signal(bool(0))
        self.valid_in = Signal(bool(0))
        self.data = Signal(intbv(0)[width:0])


class RunLengthSymbols(object):
    def __init__(self):
        self.runlength = Signal(intbv(0)[4:0])
        self.size = Signal(intbv(0)[4:0])
        self.valid = Signal(bool(0))
        # need to determine if the "addr" should be in the 
        # producer or consumer ...


class RunLengthEncoderConfig(object):
    def __init__(self):
        """The configuration (settings) for the subblock
        pass
        
        