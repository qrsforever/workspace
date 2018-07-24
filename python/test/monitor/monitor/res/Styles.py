#!/usr/bin/python3
# -*- coding: utf-8 -*-

from res import Colors

gColors = Colors.colors

styles = {
        'monitor': {
            '.': { # Root
                'configure': {
                    'background'        : gColors['MungBeanPaste'],
                    'foreground'        : gColors['Black'],
                    'relief'            : 'flat',
                    'highlightcolor'    : gColors['GreenYellow']
                    }
                },

            'TFrame': {
                'configure': {
                    'font'              : ('Calibri', 12)
                    }
                },

            'TLabel': {
                'configure': {
                    'borderwidth'       : 2,
                    'padding'           : 10,               # add spaces for four sides
                    'font'              : ('Calibri', 12)
                    }
                },

            'TNotebook': {
                'configure': {
                    'padding'           : 5
                    }
                },

            'TNotebook.Tab': {
                'configure': {
                    'padding'           : [25, 5], 
                    'foreground'        : gColors['Black']
                    },
                'map': {
                    'background'        : [('selected', gColors['DimGray'])],
                    'expand'            : [('selected', [1, 1, 1, 0])]
                    }
                },

            'TCombobox': {
                'configure': {
                    'selectbackground'  : gColors['DarkGray'],
                    'fieldbackground'   : gColors['White'],
                    'background'        : gColors['LightGray'],
                    'foreground'        : gColors['Black']
                    }
                },

            'TButton': {
                'configure': {
                    'font'              : ('Calibri', 12),
                    'background'        : gColors['LightSteelBlue'],
                    'foreground'        : gColors['Black'],
                    'relief'            : 'raised'
                    },
                'map': {
                    'foreground'        : [('pressed', 'red'), ('active', 'blue')],
                    'background'        : [('pressed', '!disabled', 'black'), ('active', 'white')]
                    }
                },

            'TEntry': {
                    'configure': {
                        'foreground'    : 'black'
                        }
                    },

            'Horizontal.TProgressbar': {
                    'configure': {
                        'background'    : gColors['DimGray']
                        }
                    }
            } # app
        }


'''
Button	        TButton
Checkbutton	TCheckbutton
Combobox	TCombobox
Entry	        TEntry
Frame	        TFrame
Label	        TLabel
LabelFrame	TLabelFrame
Menubutton	TMenubutton
Notebook	TNotebook
PanedWindow	TPanedwindow (not TPanedWindow!)
Progressbar	Horizontal.TProgressbar or Vertical.TProgressbar, depending on the orient option.
Radiobutton	TRadiobutton
Scale	        Horizontal.TScale or Vertical.TScale, depending on the orient option.
Scrollbar	Horizontal.TScrollbar or Vertical.TScrollbar, depending on the orient option.
Separator	TSeparator
Sizegrip	TSizegrip
Treeview	Treeview (not TTreview!)
'''
