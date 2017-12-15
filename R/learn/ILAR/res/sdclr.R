sdclr <- c( rgb(  0, 25,101,max=255),
            rgb(  0,159,218,max=255),
            rgb(200, 31, 73,max=255),
            rgb(  0,175, 65,max=255),
            rgb(245,130, 32,max=255),
            rgb(130,120,111,max=255),
            rgb(174,167,159,max=255),
            rgb(199,194,186,max=255),
            rgb(224,222,216,max=255))
names( sdclr ) <- c("darkblue",
                    "lightblue",
                    "rubinered",
                    "green",
                    "clearorange",
                    "granitegrey",
                    "concretegrey",
                    "marblegrey",
                    "pearlgrey")
cbind( sdclr )
#if(FALSE)
{
par( mar=c(0,0,0,0) )
plot( 0:10, 0:10, type="n", xaxt="n", yaxt="n", xlab="", ylab="", bty="n")
text( 5, seq(9,1,,9), names(sdclr), col=sdclr, font=2, cex=3.5 )
}

# Semitransparent colors
sdclrt <- c( rgb(  0, 25,101,alpha=128,max=255),
             rgb(  0,159,218,alpha=128,max=255) )
names( sdclrt ) <- c("darkblue-tr",
                     "lightblue-tr")
cbind( sdclrt )

# Illustrate - you migt want to adjust the cex= to get overlapping blobs
par( mar=c(0,0,0,0) )
( cl <- c(sdclrt,sdclr[1:2]) )
wh <- c(4,4,3,4,1,2,2,3)
plot( rep(4.5+0:1,each=4), rep(yy<-1:4*2,2),
      col=cl[wh],
      pch=16, cex=15,
      bty="n",
      xaxt="n", xlab="", xlim=c(0,10),
      yaxt="n", ylab="", ylim=c(0,10) )
text( 3, yy, names(cl)[wh[1:4  ]], col=cl[wh[1:4  ]], adj=1, font=2 )
text( 7, yy, names(cl)[wh[1:4+4]], col=cl[wh[1:4+4]], adj=0, font=2 )
