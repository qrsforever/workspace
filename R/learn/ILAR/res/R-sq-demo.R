sessionInfo()


# Utility functions to select indices of the middle or outer parts of a distribution
middle <- function (w, rm = 1/3)
{ qnt <- quantile(w, probs = 0:1 + c(1, -1) * rm/2)
  w > qnt[1] & w < qnt[2] }
ends <- function (w, rm = 1/3) !middle(w, 1 - rm)

# Here is the data generation
x <- rnorm(200)
y <- 0.7 + 0.3*x + rnorm(200)/5

# Select midle and ends of data
wm <- middle(x+y/2,1/3)
wo <-   ends(x+y/2,1/3)

# Same regression on different subsets
all    <- lm(y~x)
middle <- lm(y[wm]~x[wm])
ends   <- lm(y[wo]~x[wo])
first  <- lm(y[1:100]~x[1:100])
last   <- lm(y[101:200]~x[101:200])

summary(all)
summary(middle)
summary(ends)
summary(first)
summary(last)

plres <- function(obj,x,y,txt=deparse(substitute(obj)),col="black")
{
 res <- c( summary(obj)$coef[1,1:2], # intercept + se
           summary(obj)$coef[2,1:2], # slope + se
           summary(obj)$sigma,       # residual sd
           summary(obj)$r.squared,   # R-sq
           summary(obj)$df[2] )      # residual df
 text(x,y-1/7,expression(paste(alpha,": ")), adj=1,font=2)
 text(x+0.1,y-1/7,
      paste(formatC(res[1],format="f",digits=3,width=5), " (",
            formatC(res[2],format="f",digits=3,width=5), ")",sep=""),
      adj=0,font=2)
 text(x    ,y-2/7,expression(paste(beta,"; ")), adj=1,font=2)
 text(x+0.1,y-2/7,
      paste(formatC(res[3],format="f",digits=3,width=5), " (",
            formatC(res[4],format="f",digits=3,width=5), ")",sep=""),
      adj=0,font=2)
 text(x    ,y-3/7,expression(paste(sigma,": ")), adj=1,font=2)
 text(x+0.1,y-3/7,
      formatC(res[5],format="f",digits=3,width=5),
      adj=0,font=2)
 text(x    ,y-4/7,expression(paste(r^2,": ")), adj=1,font=2)
 text(x+0.1,y-4/7,
      paste(formatC(res[6],format="f",digits=3,width=5),
            "    d.f:",
            formatC(res[7],format="f",digits=0,width=4) ),
      adj=0,font=2)
}

par(mar=c(3,3,1,1),mgp=c(3,1,0)/1.6,bty="n")

plot(x,y,pch=16,xlim=c(-3,3),ylim=c(-1,2))
points(x,y,cex=1.1,pch=16)

plot(x,y,pch=16,xlim=c(-3,3),ylim=c(-1,2),type="n")
points(x,y,cex=1.1,pch=16)
abline ( all )
plres(all,1,-0.25,col="black")

plot(x[1:100],y[1:100],type="n",xlim=c(-3,3),ylim=c(-1,2))
points(x[1:100],y[1:100],col=gray(0.4),pch=16,cex=1.1)
abline(first,col=gray(0.4),lwd=2)
plres(first,1,-0.25,col=gray(0.4))

plot(x[101:200],y[101:200],type="n",xlim=c(-3,3),ylim=c(-1,2))
points(x[101:200],y[101:200],col=gray(0.6),pch=16,cex=1.1)
abline(last,col=gray(0.6),lwd=2)
plres(last,1,-0.25,col=gray(0.6))

plot(x[wm],y[wm],type="n",xlim=c(-3,3),ylim=c(-1,2))
points(x[wm],y[wm],pch=3,lwd=2,col="black",cex=1.1)
abline(middle,col="black",lwd=1)
plres(middle,1,-0.25,col="black")

plot(x[wo],y[wo],type="n",xlim=c(-3,3),ylim=c(-1,2))
points(x[wo],y[wo],pch=3,lwd=2,col="black",cex=1.1)
abline(ends,col="black",lwd=1)
plres(ends,1,-0.25,col="black")
