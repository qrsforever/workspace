### R code from vignette source 'cont-eff.rnw'

###################################################
### code chunk number 1: cont-eff.rnw:3-7
###################################################
options( width=90,
         prompt=" ", continue=" ",
         SweaveHooks=list( fig=function()
         par(mar=c(3,3,1,1),mgp=c(3,1,0)/1.6) ) )


###################################################
### code chunk number 2: cont-eff.rnw:41-46
###################################################
library( Epi )
sessionInfo()
data( testisDK )
str( testisDK )
head( testisDK )


###################################################
### code chunk number 3: cont-eff.rnw:51-63
###################################################
round( ftable( xtabs( cbind(D,PY=Y/1000) ~ I(floor(A/10)*10) +
                                           I(floor(P/10)*10),
                      data=testisDK ),
               row.vars=c(3,1) ), 1 )

stat.table( list(A=floor(A/10)*10,
                 P=floor(P/10)*10),
            list( D=sum(D),
                  Y=sum(Y/1000),
               rate=ratio(D,Y,10^5) ),
            margins=TRUE,
            data=testisDK )


###################################################
### code chunk number 4: cont-eff.rnw:78-80
###################################################
ml <- glm( D ~ A, offset=log(Y), family=poisson, data=testisDK )
ci.exp( ml )


###################################################
### code chunk number 5: cont-eff.rnw:91-92
###################################################
( cf <- coef( ml ) )


###################################################
### code chunk number 6: cont-eff.rnw:97-98
###################################################
round( cbind( 25:45, exp( cf[1] + cf[2]*(25:45) )*10^5 ), 3 )


###################################################
### code chunk number 7: cont-eff.rnw:108-110
###################################################
( CM <- cbind( 1, 25:45 ) )
round( ci.exp( ml, ctr.mat=CM )*10^5, 3 )


###################################################
### code chunk number 8: mort-lin
###################################################
CM <- cbind( 1, 15:65 )
matplot( 15:65, ci.exp( ml, ctr.mat=CM )*10^5,
         log="y", xlab="Age", ylab="Testis cancer incidence rate per 100,000 PY",
         type="l", lty=1, lwd=c(3,1,1), col="black" )


###################################################
### code chunk number 9: cont-eff.rnw:125-127
###################################################
mq <- glm( D ~ A + I(A^2), offset=log(Y), family=poisson, data=testisDK )
ci.exp( mq, Exp=F )


###################################################
### code chunk number 10: mort-qdr
###################################################
aa <- 15:65
CM <- cbind( 1, aa, aa^2 )
matplot( aa, ci.exp( mq, ctr.mat=CM )*10^5,
         log="y", xlab="Age", ylab="Testis cancer incidence rate per 100,000 PY",
         type="l", lty=1, lwd=c(3,1,1), col="black" )
matlines( aa, ci.exp( ml, ctr.mat=CM[,1:2] )*10^5,
          type="l", lty=1, lwd=c(3,1,1), col="blue" )


###################################################
### code chunk number 11: mort-qdr
###################################################
mc <- glm( D ~ A + I(A^2) + I(A^3), offset=log(Y), family=poisson, data=testisDK )
CM <- cbind( 1, aa, aa^2, aa^3 )
matplot( aa, ci.exp( mc, ctr.mat=CM )*10^5,
         log="y", xlab="Age", ylab="Testis cancer incidence rate per 100,000 PY",
         type="l", lty=1, lwd=c(3,1,1), col="black" )


###################################################
### code chunk number 12: mort-spl
###################################################
library( splines )
ms <- glm( D ~ Ns(A,knots=seq(15,65,10)), offset=log(Y), family=poisson, data=testisDK )
As <- Ns( aa, knots=seq(15,65,10) )
matplot( aa, ci.exp( ms, ctr.mat=cbind(1,As) )*10^5,
         log="y", xlab="Age", ylab="Testis cancer incidence rate per 100,000 PY",
         type="l", lty=1, lwd=c(3,1,1), col="black" )


###################################################
### code chunk number 13: mort-spl-P
###################################################
msp <- glm( D ~ Ns(A,knots=seq(15,65,10)) + P, offset=log(Y), family=poisson, data=testisDK )
CM <- cbind( 1, Ns( aa, knots=seq(15,65,10) ), 1980 )
matplot( aa, ci.exp( msp, ctr.mat=CM )*10^5,
         log="y", xlab="Age", ylab="Testis cancer incidence rate per 100,000 PY",
         type="l", lty=1, lwd=c(3,1,1), col="black" )


###################################################
### code chunk number 14: cont-eff.rnw:182-183
###################################################
ci.exp( msp, subset="P" )


###################################################
### code chunk number 15: cont-eff.rnw:189-195
###################################################
yy <- 1943:1996
Cp <- cbind( yy - 1980 )
matplot( yy, ci.exp( msp, ctr.mat=Cp, subset="P" ),
         log="y", xlab="Date", ylab="RR of Testis cancer",
         type="l", lty=1, lwd=c(3,1,1), col="black" )
abline( h=1 )


###################################################
### code chunk number 16: mort-spl-P
###################################################
msp <- glm( D ~ Ns(A,knots=seq(15,65,10)) + P + I(P^2), offset=log(Y), family=poisson, data=testisDK )
Cq <- cbind( yy, yy^2 ) - cbind( rep(1980,length(yy)),
                                     1980^2 )
matplot( yy, ci.exp( msp, ctr.mat=Cq, subset="P" ),
         log="y", xlab="Age", ylab="Testis cancer incidence rate ratio",
         type="l", lty=1, lwd=c(3,1,1), col="black" )
abline( h=1, v=1980 )


###################################################
### code chunk number 17: cont-eff.rnw:213-216
###################################################
mssp <- glm( D ~ Ns(A,knots=seq(15,65,10)) +
                 Ns(P,knots=seq(1950,1990,10)),
                 offset=log(Y), family=poisson, data=testisDK )


###################################################
### code chunk number 18: mort-spl-splP
###################################################
Ps <- Ns(                 yy  , knots=seq(1950,1990,10) )
Pr <- Ns( rep(1970,length(yy)), knots=seq(1950,1990,10) )
matplot( yy, ci.exp( mssp, ctr.mat=Ps-Pr, subset="P" ),
         log="y", xlab="Age", ylab="Testis cancer incidence RR",
         type="l", lty=1, lwd=c(3,1,1), col="black" )


###################################################
### code chunk number 19: mort-spl-splP
###################################################
Ar <- Ns( rep(1970,length(aa)), knots=seq(1950,1990,10) )
matplot( aa, ci.exp( mssp, ctr.mat=cbind(1,As,Ar) )*10^5,
         log="y", xlab="Age", ylab="Testis cancer incidence RR",
         type="l", lty=1, lwd=c(3,1,1), col="black" )


###################################################
### code chunk number 20: cont-eff.rnw:248-271
###################################################
a.kn <- seq(15,65,20)
p.kn <- seq(1950,1990,10)
a.pt <- 10:65
p.pt <- 1945:1993
p.ref <- 1970
na <- length(a.pt)
np <- length(p.pt)
As <- Ns( a.pt, knots=a.kn )
Ps <- Ns( p.pt, knots=p.kn )
Pr <- Ns( rep(p.ref,np), knots=p.kn )
Ar <- Ns( rep(p.ref,na), knots=p.kn )
mAP <- glm( D ~ Ns(A,knots=a.kn) + Ns(P,knots=p.kn),
                offset=log(Y), family=poisson, data=testisDK )
par( mfrow=c(1,2) )
matplot( a.pt, ci.exp( mAP, ctr.mat=cbind(1,As,Ar) )*10^5,
         log="y", xlab="Age", ylab="Testis cancer incidence RR",
         type="l", lty=1, lwd=c(3,1,1), col="black",
         ylim=c(1,20) )
matplot( p.pt, ci.exp( mAP, ctr.mat=Ps-Pr, subset="P" ),
         log="y", xlab="Age", ylab="Testis cancer incidence RR",
         type="l", lty=1, lwd=c(3,1,1), col="black",
         ylim=c(1,20)/5 )
abline( h=1, v=p.ref )


###################################################
### code chunk number 21: cont-eff.rnw:277-303
###################################################
testisDK <- transform( testisDK, B = P-A )
with( testisDK, hist( rep(B,D), breaks=100, col="black" ) )
a.kn <- seq(15,65,5)
b.kn <- seq(1900,1970,5)
a.pt <- 10:65
b.pt <- 1890:1970
b.ref <- 1950
na <- length(a.pt)
nb <- length(b.pt)
As <- Ns( a.pt, knots=a.kn )
Bs <- Ns( b.pt, knots=b.kn )
Br <- Ns( rep(b.ref,nb), knots=b.kn )
Ar <- Ns( rep(b.ref,na), knots=b.kn )
mAB <- glm( D ~ Ns(A,knots=a.kn) + Ns(B,knots=b.kn),
                offset=log(Y), family=poisson, data=testisDK )
ci.exp( mAB, subset="B" )
par( mfrow=c(1,2) )
matplot( a.pt, ci.exp( mAB, ctr.mat=cbind(1,As,Ar) )*10^5,
         log="y", xlab="Age", ylab="Testis cancer incidence RR",
         type="l", lty=1, lwd=c(3,1,1), col="black",
         ylim=c(1,20) )
matplot( b.pt, ci.exp( mAB, ctr.mat=Bs-Br, subset="B" ),
         log="y", xlab="Age", ylab="Testis cancer incidence RR",
         type="l", lty=1, lwd=c(3,1,1), col="black",
         ylim=c(1,20)/4 )
abline( h=1, v=b.ref )


