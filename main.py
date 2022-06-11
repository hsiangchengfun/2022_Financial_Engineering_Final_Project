import pandas as pd


def main():

    # 4016.25, 4023.25, future
    # 4017.82, s&p500 index
    transaction_cost = 1
    df = pd.read_csv("data.csv")
    print(df)
    call_strike_list, call_last_list, put_strike_list, put_last_list = [], [], [], []
    for index, row in df.iterrows():
        if row['Type'] == 'Call':
            call_strike_list.append(float(row['Strike']))
            call_last_list.append(float(row['Last']))
        elif row['Type'] == 'Put':
            put_strike_list.append(float(row['Strike']))
            put_last_list.append(float(row['Last']))

    # Theorem 2:
    print("Thm2\n")
    print("for call\n")
    for i in range(len(call_strike_list)):
        for j in range(i + 1, len(call_last_list)):
            if (call_last_list[i]  + transaction_cost*4 < call_last_list[j]):
                print("Arbitrage (call) when i = ", i, " strike = ",call_strike_list[i])
                print("Arbitrage (call) when i = ", i, " last = ",call_last_list[i])
                print("Arbitrage (call) when j = ", j, " strike = ",call_strike_list[j])
                print("Arbitrage (call) when j = ", j, " last = ",call_last_list[j])
                print("Arbitrage strategies : buy the call with a higher strike price & write the call with a lower strike price")
                print("profit : = ",call_last_list[j] - call_last_list[i] - transaction_cost*4 + call_strike_list[j] - call_strike_list[i])
  
    for i in range(len(put_strike_list)):
        for j in range(i + 1, len(put_last_list)):
            if (put_last_list[i] > put_last_list[j] + transaction_cost*4):
                print("Arbitrage when i = ", i, " strike = ",put_strike_list[i])
                print("Arbitrage when j = ", j, " strike = ",put_strike_list[j])
                print("Arbitrage strategies : write the put with a lowerer strike price & buy the put with a higher strike price")
                print("profit : = ",put_last_list[i] - put_last_list[j] - transaction_cost*4 + put_strike_list[j] - put_strike_list[i])
              
    #Theorem 3:
    print("Thm3\n")
    sp_index = 4017.82
    sp_index_pv = 4017.82/(1+0.0184/30)
    for i in range(len(call_last_list)):
      if call_last_list[i] > sp_index + transaction_cost*2:
        print("Arbitrage(call) when i = ", i, " strike = ",
                      call_strike_list[i])
        print("Arbitrage strategies : long stock & short call")
        print("profit : = ",call_last_list[i] - sp_index - transaction_cost*2)
    for i in range(len(put_last_list)):
        if put_last_list[i] > put_strike_list[i]/(1+0.0184/30) + transaction_cost*2:
          print("Arbitrage(put) when i = ", i, " strike = ", put_strike_list[i])
          print("Arbitrage strategies : write put & borrow ", sp_index_pv)
          print("profit : = ", put_last_list[i] - put_strike_list[i]/(1+0.0184/30) - transaction_cost*2)

    #Theorem 4:
    print("Thm4\n")
    for i in range(len(call_strike_list)):
        if call_last_list[i] < max(sp_index - call_strike_list[i]/(1+0.0184/30), 0) - transaction_cost * 6:
            print("Arbitrage(call) when i = ", i, " strike = ",call_strike_list[i])
            print("Arbitrage strategies : long call, long zero bond with value(PV(X))) & short stock")
            print("profit : = ",max(sp_index - call_strike_list[i]/(1+0.0184/30), 0) - transaction_cost * 6 - call_last_list[i])                  
    #Theorem 5: X
    #Theorem 6:
    print("Thm6\n")
    for i in range(len(put_strike_list)):
        if put_last_list[i] < max(put_strike_list[i]/(1+0.0184/30) - sp_index, 0) - transaction_cost * 6:
            print("Arbitrage(put) when i = ", i, " strike = ",put_strike_list[i])
            print("Arbitrage strategies : long put, long stock & short zero bond with value(PV(X)))")
            print("profit : = ",max(put_strike_list[i]/(1+0.0184/30) - sp_index, 0) - transaction_cost * 6 - put_last_list[i])   
    #Theorem 7: X
    #Theorem 8: X
    #Theorem 9: X
    #Theorem 10: X
if __name__ == '__main__':
    main()