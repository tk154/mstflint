# Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. ALL RIGHTS RESERVED.
#
# This software is available to you under a choice of one of two
# licenses.  You may choose to be licensed under the terms of the GNU
# General Public License (GPL) Version 2, available from the file
# COPYING in the main directory of this source tree, or the
# OpenIB.org BSD license below:
#
#     Redistribution and use in source and binary forms, with or
#     without modification, are permitted provided that the following
#     conditions are met:
#
#      - Redistributions of source code must retain the above
#        copyright notice, this list of conditions and the following
#        disclaimer.
#
#      - Redistributions in binary form must reproduce the above
#        copyright notice, this list of conditions and the following
#        disclaimer in the documentation and/or other materials
#        provided with the distribution.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#######################################################
#
# QueryCommand.py
# Python implementation of the Class QueryCommand
# Generated by Enterprise Architect
# Created on:      14-Aug-2019 10:12:00 AM
# Original author: talve
#
#######################################################
from resourcedump_lib.commands.ResDumpCommand import ResDumpCommand
from resourcedump_lib.commands.CommandFactory import CommandFactory
from resourcedump_lib.utils import constants as cs
from resourcedump_lib.validation.CapabilityValidator import CapabilityValidator
from resourcedump_lib.filters.SegmentsFilter import SegmentsFilter


class QueryCommand(ResDumpCommand):
    """This class is responsible for performing the query command flow by validate,
    getting the data and print it.
    """

    def __init__(self, **kwargs):
        """QueryCommand initialization.
        """
        super().__init__()

        self.device_name = kwargs['device']
        self.segment = cs.RESOURCE_DUMP_SEGMENT_TYPE_MENU
        self.vHCAid = kwargs.get('vHCAid', cs.DEFAULT_VHCA)
        self.index1 = 0
        self.index2 = 0
        self.numOfObj1 = 0
        self.numOfObj2 = 0
        self.depth = 0
        self.mem = kwargs.get('mem', "")

    def retrieve_data(self):
        """call the QueryData for getting the menu data.
        """
        self.retrieve_data_from_sdk()

    def get_segments(self, aggregate=False):
        if not self.segments:
            super().get_segments(aggregate)
            self.segments = SegmentsFilter.get_segments(self.segments, cs.RESOURCE_DUMP_SEGMENT_TYPE_MENU)
            if len(self.segments) == 0:
                raise Exception("Menu segment wasn't found after filtering by menu type")
        return self.segments

    def validate(self):
        """call the capability validator and check if the core dump supported by the FW.
        """

        if CapabilityValidator.validate():
            return True
        else:
            raise Exception("Resource Dump register is not supported by the FW")


CommandFactory.register(cs.RESOURCE_DUMP_COMMAND_TYPE_QUERY, QueryCommand)