### R code from vignette source 'NDR-crit.rnw'

###################################################
### code chunk number 1: NDR-crit.rnw:3-7
###################################################
options(width=95)
library(Epi)
library(gRbase)
print(sessionInfo(),l=F)


###################################################
### code chunk number 2: NDR-crit.rnw:19-44 (eval = FALSE)
###################################################
## load("/bendix/Steno/DM-register/NDR/2012/data/NDR2011.Rda")
## str( dr )
## ndr <- subset( dr, runif(nrow(dr))<0.1 )
## names( ndr )[whd <- grep("D_",names(ndr))]
## ( nr <- nrow( ndr ) )
## rownames( ndr ) <- 1:nr
## for( i in whd ) ndr[,i] <- as.Date(as.character(ndr[,i])) + sample(-7:7,nr,r=T)
## ndr <- transform( ndr, D_INKLDTO = pmin( D_LPR,D_FODT,D_BLOD2I5,D_BLOD5I1,D_INS,D_OAD,
##                                          na.rm=TRUE ) )
## 
## # redeem the inclusion criterion met
## lvl <- levels( ndr$C_INKLAARSAG )
## dfd <- ndr[,paste("D_",toupper(lvl),sep="")] - ndr[,rep("D_INKLDTO",6)]
## ndr$C_INKLAARSAG <- factor(lvl[apply( pmax(dfd==0,0,na.rm=TRUE) %*% diag(1:6), 1, max )])
## 
## # move date of birth and detah away from inclusioin date
## ndr <- transform( ndr, D_FODDTO  = pmin( D_INKLDTO-7, D_FODDTO , na.rm=TRUE ),
##                        D_DODSDTO = pmax( D_INKLDTO+7, D_DODSDTO, na.rm=TRUE ) )
## 
## # back to factor as in the original version
## for( i in whd ) ndr[,i] <- factor( ndr[,i] )
## str( ndr )
## summary( ndr )
## head( ndr )
## save( ndr, file="/bendix/Steno/DM-register/NDR/2012/data/NDR2011-bogus.Rda" )


###################################################
### code chunk number 3: NDR-crit.rnw:53-57
###################################################
library( Epi )
clear()
load( file=url("http://BendixCarstensen.com/DMreg/data/NDR2011-bogus.Rda") )
lls()


###################################################
### code chunk number 4: NDR-crit.rnw:61-63
###################################################
str( ndr )
summary( ndr )


###################################################
### code chunk number 5: NDR-crit.rnw:73-75
###################################################
names( ndr )
grep( "D_", names(ndr) )


###################################################
### code chunk number 6: NDR-crit.rnw:79-82
###################################################
wh <- grep( "D_", names(ndr) )
for( i in wh ) ndr[,i] <- cal.yr( ndr[,i] )
head( ndr )


###################################################
### code chunk number 7: NDR-crit.rnw:92-95
###################################################
names( ndr ) <- tolower( substr(names(ndr),3,10) )
names( ndr )
save( ndr, file="ndr.Rda" )


###################################################
### code chunk number 8: NDR-crit.rnw:109-118
###################################################
load( file="ndr.Rda" )
ndr$new.dto <- with( ndr, pmin( fodt, lpr, oad, ins, na.rm=TRUE ) )
# Assigning levels is a bit more tricky
ndr$new.aars                       <- NA
ndr$new.aars[ndr$new.dto==ndr$fodt]<- "fodt"
ndr$new.aars[ndr$new.dto==ndr$oad] <- "oad"
ndr$new.aars[ndr$new.dto==ndr$ins] <- "ins"
ndr$new.aars[ndr$new.dto==ndr$lpr] <- "lpr"
summary( ndr )


###################################################
### code chunk number 9: NDR-crit.rnw:122-123
###################################################
addmargins( with( ndr, table( inklaars, new.aars, useNA="ifany" ) ) )


###################################################
### code chunk number 10: NDR-crit.rnw:129-134
###################################################
ndr <- transform( ndr, A = inkldto-foddto )
mF <- glm( is.na(new.aars) ~ A + I(A^2) + I(A^3),
           family = binomial,
           data = subset( ndr, sex=="K" ) )
summary( mF )


###################################################
### code chunk number 11: NDR-crit.rnw:142-145
###################################################
nd <- data.frame( A=5:90 )
pr.F <- predict( mF, newdata=nd, type="response" )
plot( nd$A, pr.F, type="l" )


###################################################
### code chunk number 12: NDR-crit.rnw:150-158
###################################################
library( splines )
a.kn <- c(10,20,25,30,35,4:9*10)
mF <- glm( is.na(new.aars) ~ Ns( A, knots=a.kn ),
           family = binomial,
           data = subset( ndr, sex=="K" ) )
summary( mF )
pr.F <- predict( mF, newdata=nd, type="response" )
plot( nd$A, pr.F, type="l" )


###################################################
### code chunk number 13: NDR-crit.rnw:163-172
###################################################
p.kn <- seq(1996,2010,,4)
mF <- glm( is.na(new.aars) ~ Ns( A, knots=a.kn ) +
                             Ns( inkldto, knots=p.kn ),
           family = binomial,
           data = subset( ndr, sex=="K" ) )
summary( mF )
nd <- data.frame( A=5:90, inkldto=2000 )
pr.F <- predict( mF, newdata=nd, type="response" )
plot( nd$A, pr.F, type="l" )


###################################################
### code chunk number 14: NDR-crit.rnw:179-189
###################################################
pr.F <- NULL
for( p in 1996:2011 )
   {
   nd <- data.frame( A=5:90, inkldto=p )
   pr.F <- cbind( pr.F, predict( mF, newdata=nd, type="response" ) )
   }
matplot( nd$A, pr.F,
         type="l", lty=1, lwd=1:2, col=heat.colors(25)[1:16] )
text( c(80,80), c(55,60)/100, c(1996,2011),
      col=heat.colors(25)[c(1,16)], font=2 )


###################################################
### code chunk number 15: NDR-crit.rnw:194-199
###################################################
iF <- glm( is.na(new.aars) ~ Ns( A, knots=a.kn )*Ns( inkldto, knots=p.kn ),
           family = binomial,
           data = subset( ndr, sex=="K" ) )
summary( iF )
anova( mF, iF, test="Chisq" )


###################################################
### code chunk number 16: NDR-crit.rnw:202-212
###################################################
pr.F <- NULL
for( p in 1996:2011 )
   {
   nd <- data.frame( A=5:90, inkldto=p )
   pr.F <- cbind( pr.F, predict( iF, newdata=nd, type="response" ) )
   }
matplot( nd$A, pr.F,
         type="l", lty=1, lwd=1:2, col=heat.colors(25)[1:16] )
text( c(80,80), c(55,60)/100, c(1996,2011),
      col=heat.colors(25)[c(1,16)], font=2 )


