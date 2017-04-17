#!/usr/bin/python3
# -*- coding: utf-8 -*-


class LeecoBase(object):

    """Docstring for LeecoBase. """

    def __init__(self):
        """TODO: to be defined1. """
        print("LeecoBase __init__")
        super().__init__()


class LeecoA(LeecoBase):

    """Docstring for LeecoA. """

    def __init__(self):
        """TODO: to be defined1. """
        super().__init__()
        print("LeecoA __init__") 


class LeecoB(LeecoBase):

    """Docstring for LeecoB. """

    def __init__(self):
        """TODO: to be defined1. """
        super().__init__()
        print("LeecoB __init__") 


class LeecoC(LeecoA, LeecoB):

    """Docstring for LeecoC. """

    def __init__(self):
        """TODO: to be defined1. """
        #  LeecoA.__init__(self)
        #  LeecoB.__init__(self)
        super().__init__()
        print("LeecoC __init__")

        

a = LeecoC()
