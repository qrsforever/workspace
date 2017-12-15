### R code from vignette source 'reshape.rnw'

###################################################
### code chunk number 1: reshape.rnw:2-3
###################################################
library(Epi)


###################################################
### code chunk number 2: reshape.rnw:12-16
###################################################
system.time(
# ret <- read.csv( "P:/JKOY/retinopathy/data/retinopathy.csv", header=T ) )
  ret <- read.csv(                          "retinopathy.csv", header=T ) )
dim( ret )


###################################################
### code chunk number 3: reshape.rnw:20-36
###################################################
names( ret ) <- tolower( names(ret) )
newnames <- c("doBth","doDth","doDM","DMtyp","height",
              "origin",
              "country",
              "category",
              "doRet",
              "doSev",
              "antihyp",
              "liplow")
cbind( names(ret)[c(3:7,178:184)],   newnames )
       names(ret)[c(3:7,178:184)] <- newnames
dim( ret )
retin <- ret[1:10000,c(1:6, 34:42, 35:121, 178:184 )]
dim( retin )
write.csv ( retin, file="retin1.csv" )
write.csv2( retin, file="retin2.csv" )


###################################################
### code chunk number 4: reshape.rnw:48-51
###################################################
rt <- read.csv( "retin1.csv" )
str( rt )
dim( rt )


###################################################
### code chunk number 5: reshape.rnw:54-55 (eval = FALSE)
###################################################
## rt <- read.csv( "retin2.csv" )


###################################################
### code chunk number 6: reshape.rnw:60-62
###################################################
rt <- read.csv2( "retin2.csv" )
str( rt )


###################################################
### code chunk number 7: reshape.rnw:73-74
###################################################
names( rt )


###################################################
### code chunk number 8: reshape.rnw:78-79
###################################################
grep( ".d_", names(rt) )


###################################################
### code chunk number 9: reshape.rnw:83-84
###################################################
names(rt)[whd<-grep( ".d_", names(rt) )]


###################################################
### code chunk number 10: reshape.rnw:88-90
###################################################
head( rt[,whd] )
for(i in whd) rt[,i] <- as.Date(rt[,i], format="%m/%d/%Y" )


###################################################
### code chunk number 11: reshape.rnw:124-127
###################################################
names(rt)[wdb<-grep("d.oth",names(rt))]
names(rt)[wdp<-grep("diabp",names(rt))]
names(rt)[wsp<-grep("sysbp",names(rt))]


###################################################
### code chunk number 12: reshape.rnw:132-138
###################################################
names(rt)[wdb<-grep("d.oth",names(rt))[-c(3,4)]]
names(rt)[wdp<-grep("diabp",names(rt))[-c(3,4)]]
names(rt)[wsp<-grep("sysbp",names(rt))[-  3   ]]
cbind( names(rt)[wdb],
       names(rt)[wdp],
       names(rt)[wsp] )


###################################################
### code chunk number 13: reshape.rnw:155-161
###################################################
BPr <- reshape( rt,
              idvar = "id",
               drop = names(rt)[-c(2,wdb,wdp,wsp)],
            varying = list(wdb,wdp,wsp),
            v.names = c("doVis","dia","sys"),
          direction = "long" )


###################################################
### code chunk number 14: reshape.rnw:167-169
###################################################
subset( rt , newid==91547 )[c(1,wdb,wdp,wsp)]
subset( BPr, newid==91547 )


###################################################
### code chunk number 15: reshape.rnw:173-175
###################################################
BPr <- subset( BPr, !is.na(doVis), select=-c(time,id) )
subset( BPr, newid==91547 )


###################################################
### code chunk number 16: reshape.rnw:182-184
###################################################
names(rt)[wda1c<-grep("d.hba",names(rt))]
names(rt)[wa1c <-grep("hba",  names(rt))]


###################################################
### code chunk number 17: reshape.rnw:189-191
###################################################
wa1c <- setdiff( wa1c, wda1c )
cbind( names(rt)[wda1c], names(rt)[wa1c] )


###################################################
### code chunk number 18: reshape.rnw:194-199
###################################################
A1cr <- reshape( rt,
               drop = names(rt)[-c(2,wda1c,wa1c)],
            varying = list(wda1c,wa1c),
            v.names = c("doVis","hba1c"),
          direction = "long" )


###################################################
### code chunk number 19: reshape.rnw:202-204
###################################################
subset( rt , newid==91547 )[c(1,wda1c,wa1c)]
subset( A1cr, newid==91547 )


###################################################
### code chunk number 20: reshape.rnw:208-210
###################################################
A1cr <- subset( A1cr, !is.na(doVis), select=-c(time,id) )
subset( A1cr, newid==91547 )


###################################################
### code chunk number 21: reshape.rnw:221-224
###################################################
intersect( names(BPr), names(A1cr) )
Vis <- merge( BPr, A1cr, all=TRUE )
subset( Vis, newid==91547 )


###################################################
### code chunk number 22: reshape.rnw:234-237
###################################################
Vis <- merge( Vis, rt[,c(2:7,104:110)], all.x=TRUE )
subset( Vis, newid==91547 )
str( Vis )


###################################################
### code chunk number 23: reshape.rnw:240-244
###################################################
cbind( 1:ncol(Vis), names(Vis) )
wh <- c(7:9,14,15)
for( i in wh ) Vis[,i] <- as.Date( Vis[,i], format="%m/%d/%Y" )
str( Vis )


###################################################
### code chunk number 24: reshape.rnw:248-250
###################################################
Vis <- cal.yr( Vis )
str( Vis )


###################################################
### code chunk number 25: reshape.rnw:263-265
###################################################
range( Vis$doDth )
range( Vis$doDth, na.rm=TRUE )


###################################################
### code chunk number 26: reshape.rnw:268-269
###################################################
Vis <- subset( Vis, doVis<2012 )


###################################################
### code chunk number 27: reshape.rnw:278-280
###################################################
junko <- function(x) c( x[-1], x[length(x)] )
junko


###################################################
### code chunk number 28: reshape.rnw:284-289
###################################################
Vis$doNxt <- ave( Vis$doVis, Vis$newid, FUN=junko )
subset( Vis, newid==91547 )
Vis$dox <- ifelse( Vis$doVis==Vis$doNxt,
                   pmin( Vis$doDth, 2012, na.rm=TRUE ),
                   Vis$doNxt )


###################################################
### code chunk number 29: reshape.rnw:291-299
###################################################
Lxr <- Lexis ( entry = list( date=doVis, age=doVis-doBth, dur=doVis-doDM ),
                exit = list( date=dox ),
         exit.status = factor( pmin(doDth,Inf,na.rm=TRUE) == dox,
                               labels=c("NoRet","Dead") ),
                  id = newid,
                data = Vis )
subset(Lxr, newid==91547)
length(unique(Vis$newid))


###################################################
### code chunk number 30: reshape.rnw:304-310 (eval = FALSE)
###################################################
## Rrcut <- subset( rt,
##                  !is.na(doRet) & ((doRet<doSev)|is.na(doSev)),
##                  select=c("newid","doRet"))
## names(Rrcut)<-c("lex.id","cut")
## Rrcut$new.state <- "Simplex"
## head(Rrcut)


###################################################
### code chunk number 31: reshape.rnw:312-326 (eval = FALSE)
###################################################
## Srcut<-subset( rt,
##                !is.na(doSev),
##                select=c("newid","doSev"))
## names(Srcut)<-c("lex.id","cut")
## Srcut$new.state<-"Prolif"
## head(Srcut)
## 
## c(nrow(Rrcut), nrow(Srcut))
## 
## clin.var <- c( "dia","sys",
##                "smoke","weight","bmi","hba1c",
##                "tc","ldl","hdl","tg")
## 
## Cxr <- cutLexis(Lxr, Rrcut, pre="NoRet")


###################################################
### code chunk number 32: reshape.rnw:330-339 (eval = FALSE)
###################################################
## Cxr[Cxr$date %in% Rrcut$cut,clin.var] <- NA
## str( Cxr )
## 
## Rxr <- cutLexis(Cxr, Srcut, pre=c("NoRet","Simplex") )
## #Rxr[Rxr$date %in% Srcut$cut,clin.var] <- NA
## str( Rxr )
## head(Rxr,20)
## Rxr$region <- factor( Rxr$category,
##            labels=c("DK","Europe","SubSAfri","MidEast","Asia","America"))


