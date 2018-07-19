#include <stdio.h>
#include <signal.h>
#include <time.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
 
#if 0
#define CLOCKID CLOCK_REALTIME
 
void timer_thread(union sigval v)
{
	printf("timer_thread function! %d\n", v.sival_int);
}
 
int main(int argc, char **argv)
{
	// XXX int timer_create(clockid_t clockid, struct sigevent *evp, timer_t *timerid);
	// clockid--值：CLOCK_REALTIME,CLOCK_MONOTONIC,CLOCK_PROCESS_CPUTIME_ID,CLOCK_THREAD_CPUTIME_ID
	// evp--存放环境值的地址,结构成员说明了定时器到期的通知方式和处理方式等
	// timerid--定时器标识符
	timer_t timerid;
	struct sigevent evp;
	memset(&evp, 0, sizeof(struct sigevent));	//清零初始化
 
	evp.sigev_value.sival_int = 111;		//也是标识定时器的，这和timerid有什么区别？回调函数可以获得
	evp.sigev_notify = SIGEV_THREAD;		//线程通知的方式，派驻新线程
	evp.sigev_notify_function = timer_thread;	//线程函数地址
 
	if (timer_create(CLOCKID, &evp, &timerid) == -1)
	{
		perror("fail to timer_create");
		exit(-1);
	}
 
	// XXX int timer_settime(timer_t timerid, int flags, const struct itimerspec *new_value,struct itimerspec *old_value);
	// timerid--定时器标识
	// flags--0表示相对时间，1表示绝对时间，通常使用相对时间
	// new_value--定时器的新初始值和间隔，如下面的it
	// old_value--取值通常为0，即第四个参数常为NULL,若不为NULL，则返回定时器的前一个值
	
	//第一次间隔it.it_value这么长,以后每次都是it.it_interval这么长,就是说it.it_value变0的时候会装载it.it_interval的值
	//it.it_interval可以理解为周期
	struct itimerspec it;
	it.it_interval.tv_sec = 1;	//间隔1s
	it.it_interval.tv_nsec = 0;
	it.it_value.tv_sec = 1;		
	it.it_value.tv_nsec = 0;
 
	if (timer_settime(timerid, 0, &it, NULL) == -1)
	{
		perror("fail to timer_settime");
		exit(-1);
	}

    while(1);
 
	return 0;
}
/*
 * int timer_gettime(timer_t timerid, struct itimerspec *curr_value);
 * 获取timerid指定的定时器的值，填入curr_value
 *
 */
#endif

int GetNDaysGapDate(int iNowDate, int iNum)
{
    struct tm ptm;
    ptm.tm_year = iNowDate / 10000 % 10000 - 1900;
    ptm.tm_mon  = iNowDate / 100 % 100 - 1;
    ptm.tm_mday = iNowDate % 100;
    ptm.tm_hour = 0;
    ptm.tm_min  = 0;
    ptm.tm_sec  = 0;
 
    time_t timep;
    timep = mktime(&ptm);
    timep += iNum * 24 * 60 * 60;
 
    ptm = *localtime(&timep);
 
    return (ptm.tm_year + 1900) * 10000 + (ptm.tm_mon + 1) * 100 + ptm.tm_mday;
}

#if 0

private int getDay(int year, int month) {
    int day = 30;
    boolean flag = false;
    // if((y%400==0)||(y%4==0)&&(y%100!=0))  
    switch (year % 4) { //余0等于闰年
        case 0:
            flag = true;
            break;
        default:
            flag = false;
            break;
    }
    switch (month) {
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12:
            day = 31;
            break;
        case 2:
            day = flag ? 29 : 28; //闰年2月是29天
            break;
        default:
            day = 30;
            break;
    }
    return day;
}

#endif
 
int main(int argc, char **argv)
{
    // int iDate = 20170120;
    // int n = 30;
    // int iPre30Date = GetNDaysGapDate(iDate, (-1)*n); //获取 iDate 30天前的日期
 
    struct tm ptm;
    ptm.tm_year = 2018 - 1900;
    // ptm.tm_mon  = 7 - 1;
    // ptm.tm_mday = 10;
    ptm.tm_wday = 1;
    ptm.tm_hour = 0;
    ptm.tm_min  = 0;
    ptm.tm_sec  = 0;
 
    time_t timep;
    timep = mktime(&ptm);

    ptm = *localtime(&timep);
    printf("############ %d %d %d %d\n", ptm.tm_year + 1900, ptm.tm_mon + 1, ptm.tm_mday, ptm.tm_wday + 1);
    return 0;
}
 
#if 0
//距9：30的分钟数可以表示成：
    min =  ptm.tm_hour*60 + ptm.tm_min - （9*60 + 30）;
 
// long 型可直接赋值给 time_t 对象
long lTime = 1513318455;
time_t timestamp = 1513318455;
struct tm ptm;
ptm = *localtime(&timestamp);
 
//获取当前时间戳
time_t timep;
time(&timep);
cout << timep << endl;
#endif
