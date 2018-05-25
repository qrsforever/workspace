;=======================================
; date: 2018-05-24 13:29:13
; title: defmodule
;=======================================

(clear)
(defmodule A)
(defglobal A ?*x* = 1)
(ppdefglobal x)

(defmodule B)
(defglobal B ?*x* = 0)
(ppdefglobal x)

(ppdefglobal A::x)

(set-current-module A)
(ppdefglobal x)
(ppdefglobal B::x)

(exit)
