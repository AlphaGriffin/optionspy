# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

"""Alpha Griffin Python Options

Options for Python.

.. module:: ag.options
   :platform: Unix
   :synopsis: Options for Python
.. moduleauthor:: Eric Petersen <ruckusist@alphagriffin.com>
"""
import os, subprocess, shlex, platform, datetime

from .__version__ import __version__
# print ("Alpha Griffin Python Options version %s" % (__version__))

#import ag.logging as log
#log.set(log.INFO)

import os
import yaml

class Options(object):
    """First Release of basic options 10/2017.

    Features: Print all options at commandline.
    """

    def __init__(self, data_path=None):
        """Setup datapath for file reading.

        If not path is provided Options looks for a
        config in the local directory.
        """
        if data_path is None:
            data_path = os.path.join(
                os.getcwd(),
                "config.yaml"
                )
        self.config = self.load_options(data_path)
        for i in self.config:
            setattr(
                self,
                '{}'.format(i),
                # '{}'.format(self.config[i])
                self.config[i]
            )

    def __call__(self):
        """Sanity check."""
        if self.config:
            return True
        return False

    def __str__(self):
        """Print all options."""
        options = ""
        for i in self.__dict__:
            if 'config' not in i:
                options += "{}: {}\n".format(i, self.__dict__[i])
        return str(options)

    @staticmethod
    def load_options(data_path):
        """Open and read yaml file just like any other."""
        with open(data_path, 'r') as config:
            new_config = yaml.load(config)
        return new_config
