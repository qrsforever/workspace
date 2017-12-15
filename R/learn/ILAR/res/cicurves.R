# Predicted VAT given W/H-ratio from PrFR
pp <- seq(0.38,0.8,0.01)
load( "../data/p0African.rda")
pp <- cbind( pp, p0 )
load( "../data/p0Inuit.rda")
pp <- cbind( pp, p0 )
load( "../data/p0European.rda")
pp <- cbind( pp, p0 )
head( pp )
save( pp, file="../data/vat.whr.Rda" )
load(     file="../data/vat.whr.Rda" )

# colors for the curves:
clr <- c("limegreen","blue","red")
col2rgb( clr )
# and transparent versions
( clt <- rgb( t(col2rgb(clr)), alpha=70, max=255 ) )

# The curves
par( mar=c(3,3,1,1), mgp=c(3,1,0)/1.6, bty="n", las=1 )
matplot( pp[,1], pp[,c(2,5,8)],
         type="l", col=clr, lwd=4, lty=1,
         xlab="W/H ratio",
         ylab="VAT (cm)", ylim=c(1.4,2.8) )
# The the semi-transparent confidence intervals
polygon( c(pp[,1],rev(pp[,1])),
         c(pp[,3],rev(pp[,4])),
         col=clt[1], border="transparent" )
polygon( c(pp[,1],rev(pp[,1])),
         c(pp[,6],rev(pp[,7])),
         col=clt[2], border="transparent" )
polygon( c(pp[,1],rev(pp[,1])),
         c(pp[,9],rev(pp[,10])),
         col=clt[3], border="transparent" )
abline( h=14:28/10, v=40:80/100, col="white" )
text( rep(0.8,3), 1.7-0.05*2:0,
      c("African","Inuit","European"),
      col=clr, adj=1, font=2, cex=2 )
