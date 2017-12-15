### R code from vignette source 'R-intro-SDC.rnw'

###################################################
### code chunk number 1: sim-sample.rnw:3-7
###################################################
options(width=95)
library(Epi)
library(gRbase)
print(sessionInfo(),l=F)


###################################################
### code chunk number 2: sim-sample.rnw:83-84
###################################################
c(20,30) * 7.94


###################################################
### code chunk number 3: sim-sample.rnw:93-94
###################################################
exp( 1.96/sqrt(c(159,238)) )


###################################################
### code chunk number 4: sim-sample.rnw:134-138
###################################################
inc <- 20      # Incidence per 1000 PY
RR  <- 1.5     # RR associated with carrier status
pr  <- 10      # Prevalence (%) of carrier status
py  <- 8       # Person-years in 1000s


###################################################
### code chunk number 5: sim-sample.rnw:143-144
###################################################
( PY <- py*1000 * c( pr/100, 1-pr/100 ) )


###################################################
### code chunk number 6: sim-sample.rnw:147-148
###################################################
( IR <- c(RR,1) * inc/1000 )


###################################################
### code chunk number 7: sim-sample.rnw:151-152
###################################################
PY*IR


###################################################
### code chunk number 8: sim-sample.rnw:158-159
###################################################
( D <- rpois( 2, lambda=PY*IR ) )


###################################################
### code chunk number 9: sim-sample.rnw:162-163
###################################################
( rt <- D / PY )


###################################################
### code chunk number 10: sim-sample.rnw:166-167
###################################################
( RR <- rt[1]/rt[2] )


###################################################
### code chunk number 11: sim-sample.rnw:170-171
###################################################
exp( 1.96 * sqrt( sum(1/D) ) )


###################################################
### code chunk number 12: sim-sample.rnw:175-177
###################################################
( chtst <- log(rt[2]/rt[1])^2 / ( 1/D[1] + 1/D[2] ) )
( pval <- 1 - pchisq( chtst, 1 ) )


###################################################
### code chunk number 13: sim-sample.rnw:186-187
###################################################
nsim <- 5


###################################################
### code chunk number 14: sim-sample.rnw:190-191
###################################################
( PY <- py*1000 * c( 1-pr/100, pr/100 ) )


###################################################
### code chunk number 15: sim-sample.rnw:194-195
###################################################
( IR <- c(RR,1) * inc/1000 )


###################################################
### code chunk number 16: sim-sample.rnw:198-199
###################################################
( cuminc <- PY*IR )


###################################################
### code chunk number 17: sim-sample.rnw:202-206
###################################################
# Events in exposed:
( nx <- rpois( nsim, cuminc[1] ) )
# Events in unexposed:
( nr <- rpois( nsim, cuminc[2] ) )


###################################################
### code chunk number 18: sim-sample.rnw:209-210
###################################################
( rr <-  (nx/PY[1]) / (nr/PY[2]) )


###################################################
### code chunk number 19: sim-sample.rnw:212-213
###################################################
( erf <- exp( 1.96*sqrt(1/nx+1/nr) ) )


###################################################
### code chunk number 20: sim-sample.rnw:217-218
###################################################
( sgn <- abs(log(rr)) > log(erf) )


###################################################
### code chunk number 21: sim-sample.rnw:234-244
###################################################
library( Epi )
prpw <- NArray( list( RR = seq(1.05,1.5,0.05),
                      pr = seq(5,50,5),
                      PY = 8:13,
                     inc = c(20,30),
                    what = c("RR","Erf","Pwr") ) )
str( prpw )
dim( prpw )
prod( dim( prpw ) )
dimnames( prpw )


###################################################
### code chunk number 22: sim-sample.rnw:256-284
###################################################
nsim <- 10000
system.time(
for( ir in dimnames(prpw)[["RR"]] )
for( ip in dimnames(prpw)[["pr"]] )
for( iy in dimnames(prpw)[["PY"]] )
for( ii in dimnames(prpw)[["inc"]] )
{
nr <- as.numeric(ir)
np <- as.numeric(ip)/100
ny <- as.numeric(iy)
ni <- as.numeric(ii)
# Cumulative incidence in exposed and non-exposed:
cuminc <- ny * c(np,1-np) * ni * c(nr,1)
# Events in exposed:
nx <- rpois( nsim, cuminc[1] )
# Events in unexposed:
nr <- rpois( nsim, cuminc[2] )
# Rate Ratio
rr <-  (nx/np) / (nr/(1-np))
# Error factor
erf <- exp( 1.96*sqrt(1/nx+1/nr) )
# Significance
sgn <- abs(log(rr)) > log(erf)
# Store results - not we use the *character* variables for indexing:
prpw[ir,ip,iy,ii,"RR" ] <- median( rr )
prpw[ir,ip,iy,ii,"Erf"] <- median( erf )
prpw[ir,ip,iy,ii,"Pwr"] <- mean( sgn )
} )


###################################################
### code chunk number 23: sim-sample.rnw:288-289
###################################################
prpw[,,"12",,"RR" ]


###################################################
### code chunk number 24: sim-sample.rnw:293-294
###################################################
round( ftable( prpw[,,"12",,"RR" ], col.vars=1, row.vars=c(3,2) ), 2 )


###################################################
### code chunk number 25: sim-sample.rnw:299-301
###################################################
round( ftable( prpw[,,c("8","12"),,"Erf"],
               col.vars=1, row.vars=c(3,4,2) ), 2 )


###################################################
### code chunk number 26: sim-sample.rnw:305-307
###################################################
round( ftable( prpw[,,c("8","12"),,"Pwr"]*100,
               col.vars=1, row.vars=c(3,4,2) ), 1 )


###################################################
### code chunk number 27: sim-sample.rnw:311-314
###################################################
print( ftable( (prpw[,,c("8","12"),,"Pwr"]>0.7)*1,
               col.vars=1, row.vars=c(3,4,2) ),
       zero.print="." )


