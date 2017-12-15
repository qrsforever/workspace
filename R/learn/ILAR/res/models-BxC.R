### R code from vignette source 'models-BxC.rnw'
### Encoding: UTF-8

###################################################
### code chunk number 1: models-BxC.rnw:17-22
###################################################
#s <- bwrapPlot("fig/Regfig01",width=3,height=3)
x <- 1:5
set.seed(141164)
y <- round(2 + 1 * x + rnorm(length(x)),1)
X <- cbind (rep(1,5),x)


###################################################
### code chunk number 2: Regfig01
###################################################
plot(x,y,col="red",lwd=2)


###################################################
### code chunk number 3: models-BxC.rnw:27-28
###################################################
#ewrapPlot(s)


###################################################
### code chunk number 4: models-BxC.rnw:78-82
###################################################
y
X
beta.hat <- solve(t(X)%*% X)%*% t(X)%*%y
beta.hat


###################################################
### code chunk number 5: models-BxC.rnw:221-224
###################################################
library(Epi)
ci.mat()
ci.mat(alpha=0.1)


###################################################
### code chunk number 6: models-BxC.rnw:229-233
###################################################
beta <- c(1.83,2.38)
se <- c(0.32,1.57)
cbind(beta,se) %*% ci.mat()
cbind(beta,se) %*% ci.mat(0.1)


###################################################
### code chunk number 7: models-BxC.rnw:306-311
###################################################
data(births)
str(births)
ma <- lm( bweight ~ gestwks + I(gestwks^2), data=births )
( beta <- coef( ma ) )
( cova <- vcov( ma ) )


###################################################
### code chunk number 8: ci-demo1
###################################################
ga.pts <- 32:42
G <- cbind( 1, ga.pts, ga.pts^2 )
wt.eff <- G %*% beta
sd.eff <- sqrt( diag(G %*% cova %*% t(G)) )
wt.pred <- cbind( wt.eff, sd.eff ) %*% ci.mat()
matplot( ga.pts, wt.pred, type="l", lwd=c(3,1,1), col="black", lty=1 )


###################################################
### code chunk number 9: ci-demo2
###################################################
wt.ci <- ci.lin( ma, ctr.mat=G )[,c(1,5,6)]
matplot( ga.pts, wt.ci, type="l", lty=1, lwd=c(3,1,1), col="black" )


###################################################
### code chunk number 10: models-BxC.rnw:354-357
###################################################
ma2 <- lm( bweight ~ gestwks + I(gestwks^2) +
                     matage  + I(matage^2), data=births )
ci.lin( ma2 )


###################################################
### code chunk number 11: models-BxC.rnw:369-373
###################################################
ma.ref <- 35
ma.pts <- 20:45
M <- cbind(ma.pts,ma.pts^2)
M.ref <- cbind(ma.ref,ma.ref^2)


###################################################
### code chunk number 12: ci-gest
###################################################
bw.ga <- ci.lin( ma2, ctr.mat=cbind(G,M.ref[rep(1,nrow(G)),]) )[,c(1,5,6)]
matplot( ga.pts, bw.ga, type="l", lty=1, lwd=c(2,1,1), col="black" )


###################################################
### code chunk number 13: ci-mata
###################################################
bw.ma <- ci.lin( ma2, subset="matage", ctr.mat=M-M.ref[rep(1,nrow(M)),] )[,c(1,5,6)]
matplot( ma.pts, bw.ma, type="l", lty=1, lwd=c(2,1,1), col="black" )


###################################################
### code chunk number 14: models-BxC.rnw:457-462
###################################################
FF <- factor( rep(1:3,each=2) )
( X <- model.matrix(~FF  ) )
( A <- model.matrix(~FF-1) )
library(MASS)
ginv(A) %*% X


