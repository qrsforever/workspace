### R code from vignette source 'poppyr.Rnw'

###################################################
### code chunk number 1: poppyr.Rnw:4-6
###################################################
#Pause between graphs, so we can inspect them
sweave.oldpar <- par(ask=TRUE)


###################################################
### code chunk number 2: poppyr.Rnw:12-15
###################################################
library( Epi )
data( N.dk )
head( N.dk )


###################################################
### code chunk number 3: poppyr.Rnw:19-21
###################################################
pp <- xtabs( N ~ sex + A + P, data=N.dk )
str( pp )


###################################################
### code chunk number 4: poppyr.Rnw:24-26
###################################################
barplot( pp["1",,"1980"] )
barplot( pp["1",,"1980"], horiz=TRUE, col="blue", border="blue" )


###################################################
### code chunk number 5: poppyr.Rnw:30-32
###################################################
dim( pp[,,"1980"] )
barplot( pp[,,"1980"], horiz=TRUE, col=c("blue","red"), border="transparent" )


###################################################
### code chunk number 6: poppyr.Rnw:39-41
###################################################
barplot( rbind(-pp["1",,"1980"], pp[,,"1980"] ),
         horiz=TRUE, col=c("red","blue"), border="transparent", space=0 )


###################################################
### code chunk number 7: poppyr.Rnw:45-51
###################################################
barplot( rbind(-pp["1",,"1980"], pp[,,"1980"] )/1000,
         xlim=c(-1,1)*50, xlab="Persons (1000s)", yaxt="n",  xaxt="n",
         horiz=TRUE, col=c("red","blue"), border="transparent", space=0 )
axis( side=2, at=0:10*10, las=1 )
axis( side=1, at=c(-5:0,1:5)*10, labels=c(5:0,1:5)*10 )
text( -48, 100, "1980", font=2, adj=0 )


###################################################
### code chunk number 8: poppyr.Rnw:55-57
###################################################
dimnames(pp)[3]
dimnames(pp)[[3]]


###################################################
### code chunk number 9: poppyr.Rnw:62-73
###################################################
pdf( "./graph/DKpyr.pdf", height=8, width=8 )
for( yy in dimnames(pp)[[3]] )
   { 
barplot( rbind(-pp["1",,yy], pp[,,yy] )/1000,
         xlim=c(-1,1)*50, xlab="Persons (1000s)", yaxt="n",  xaxt="n",
         horiz=TRUE, col=c("red","blue"), border="transparent", space=0 )
axis( side=2, at=0:10*10, las=1 )
axis( side=1, at=c(-5:0,1:5)*10, labels=c(5:0,1:5)*10 )
text( -48, 100, yy, font=2, adj=0 )
   }
dev.off()


