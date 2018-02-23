#!/usr/bin/env Rscript

state = c("tas", "qld", "sa", "sa",  "sa",  "vic", 
        "nt", "act", "qld", "nsw", "wa", "nt", "wa", 
        "nsw", "nsw", "vic", "vic", "vic", "nsw", "qld", "qld", "vic", 
        "wa", "qld", "sa", "tas", "nsw", "nsw", "wa","act")

## 将向量分组(多个水平)
statef = factor(state)
statef
## 组(水平)
levels(statef)
