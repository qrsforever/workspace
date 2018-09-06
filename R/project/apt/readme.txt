sudo apt-get install r-base r-base-dev

# 安装rstudio
sudo apt-get install gdebi-core
sudo apt-get install libapparmor1

https://www.rstudio.com/

官网(安装最新版本):
    https://www.r-project.org/
    sudo apt-get install gfortran libreadline6-dev libxt-dev
    ./configure --enable-R-shlib

jupyter support:
   https://github.com/IRkernel/IRkernel
   1. R
   2. install.packages('devtools')
   3. devtools::install_github('IRkernel/IRkernel')
   4. IRkernel::installspec() or IRkernel::installspec(name = 'ir34', displayname = 'R 3.4')
