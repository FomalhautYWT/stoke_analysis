from pytdx.hq import TdxHq_API

api = TdxHq_API()
stokes0 = []
stokes1 = []
daily_stoke = {}
all_daily = []
all_daily_index = {}

def fetch_stoke_data(daily_stokes, market_num):
    for i in range(len(daily_stokes)):
        stoke_code = daily_stokes[i]['code']
        #if stoke_code.startswith("300") or stoke_code.startswith("60") or stoke_code.startswith("00"):
        #if stoke_code.startswith("60") or stoke_code == "000001":
        if stoke_code == "000001" or stoke_code == '002173':
            res = api.get_security_bars(4,market_num, daily_stokes[i]['code'], 0, 10)
            #print("#####",stoke_code,res)
            for k in res:
                date_of_stoke = k['datetime'][:10]
                daily_stoke[date_of_stoke] = {}
                daily_stoke[date_of_stoke][stoke_code] = k
                if (stoke_code == '000001'):
                    all_daily.append(date_of_stoke)
                    all_daily_index[date_of_stoke] = len(all_daily) - 1
def check_limit_up(stoke_today, stoke_last_day):
    #print(stoke_today, stoke_last_day)
    if (stoke_today['close'] - stoke_last_day['close'] + 0.01) / stoke_last_day['close'] > 0.1:
        return True
    return False

with api.connect('119.147.212.81', 7709):  #get data
    print(api.get_security_count(0))
    print(api.get_security_count(1))

    for i in range(20): #主板
        rsp = api.get_security_list(0, i * 1000)                        
        if (rsp == None):
            break
        stokes0 += rsp
    for i in range(22): #其他板
        rsp = api.get_security_list(1, 516 + i * 1000)                        
        if (rsp == None):
            break
        stokes1 += rsp
    #print(stokes)
    #获取数据
    #print(stokes0)
    fetch_stoke_data(stokes0,0)
    fetch_stoke_data(stokes1,1)

    in_pool_days = 5
    stoke_pool = {}
    #print (all_daily)
    for i in range(len(all_daily)):
        date_of_today = all_daily[i]
        for j in daily_stoke[date_of_today]:
            if check_limit_up(daily_stoke[date_of_today][j], daily_stoke[all_daily[i-1]][j]) :
                stoke_pool[j] = in_pool_days
            
    #计算日k


    #绘制k线
    


    #for i in range(20): #主板
    #    print (i)
    #    rsp = api.get_security_list(1, i * 1000)                        
    #    if (rsp == None):
    #        break
    #    print (len(rsp))
    #print(rsp)


