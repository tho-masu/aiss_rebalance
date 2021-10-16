import math


def buy():
    flag = False
    global A, t, beta, bought
    if beta <= 0:
        return False
    alpha, a = calc_alpha_a(A)
    dif = sub(mul(alpha+beta, t), mul(alpha, a))
    dist = []
    for veci in dif:
        if veci > 0:
            dist.append(veci)
            flag = True
        else:
            dist.append(0)
    l1_dist = l1(dist)
    beta_dist = [beta*l1_disti for l1_disti in l1_dist]
    A = add(A, beta_dist)
    beta -= sum(beta_dist)
    bought = add(bought, beta_dist)
    return flag


def sell():
    global A, fundarr, f, t, sold, sold_flag, c, delta, beta
    if delta <= 0:
        return False
    step = max(int(sum(fundarr)/20),1)
    max_sellvalue_cossim = []
    rangearr = fundarr
    if sold_flag.count(True) >= c:
        rangearr = [fundarr[i] if sold_flag[i]
                    == True else 0 for i in range(len(sold_flag))]
    for i, fund in enumerate(rangearr):
        if(fund > 0):
            cossim_list = []
            for sellvalue in range(step, int(fund)+1, step):
                A_dash = sub(A, mul(sellvalue, f[i]))
                cossim_list.append((i, sellvalue, cossim(A_dash, t), A_dash))
            # このファンドに対して最もコサイン類似度が高くなるケースの(ファンド番号,売却額,コサイン類似度,リバランス後の配分)
            # のタプルを代入・append
            if cossim_list:
                fund_max_sellvalue_cossim = max(
                    cossim_list, key=lambda element: element[2])
                max_sellvalue_cossim.append(fund_max_sellvalue_cossim)
    # 全てのケースの中から最もコサイン類似度が高くなるケースの(ファンド番号,売却額,コサイン類似度,リバランス後の配分)のタプルを代入
    if max_sellvalue_cossim:
        operation = max(max_sellvalue_cossim,
                        key=lambda element: (element[2], -element[1]))
    else:
        operation = None
    # もしどのファンドの売りも元のコサイン類似度A・t/|A||t|よりも値が大きくならないならこの売りは中断
    if operation[2] <= cossim(A, t) or operation is None:
        return False
    # 残りの売却上限額を超えるなら上限額ちょうどまで売る
    if operation[1] > delta:
        A_dashdash = sub(A, mul(delta, f[operation[0]]))
        operation = (operation[0], delta, cossim(A_dashdash, t), A_dashdash)
    # 売り実行
    A = operation[3]
    sold[operation[0]] += operation[1]
    fundarr[operation[0]] -= operation[1]
    sold_flag[operation[0]] = True
    delta -= operation[1]
    beta += operation[1]
    return True


def iprod(vec0, vec1):
    return sum([vec0i*vec1i for vec0i, vec1i in zip(vec0, vec1)])


def mul(a, vec):
    return [a*veci for veci in vec]


def add(vec0, vec1):
    return [vec0i+vec1i for vec0i, vec1i in zip(vec0, vec1)]


def sub(vec0, vec1):
    return [vec0i-vec1i for vec0i, vec1i in zip(vec0, vec1)]


def l1(vec):
    return [veci/sum(vec) for veci in vec]


def l2norm(vec):
    squaresum = 0
    for veci in vec:
        squaresum += veci**2
    return math.sqrt(squaresum)


def cossim(vec0, vec1):
    return iprod(vec0, vec1) / (l2norm(vec0)*l2norm(vec1))


def calc_fund_to_A(fundarr):
    resultA = [0, 0, 0, 0]
    for i, fund in enumerate(fundarr):
        resultA = add(resultA, mul(fund, f[i]))
    return resultA


def calc_alpha_a(A):
    return (sum(A), l1(A))


bought = [0, 0, 0, 0]
sold = [0, 0, 0, 0, 0, 0, 0]
sold_flag = [False, False, False, False, False, False, False]
c = 2
delta = 50
beta = 100

f = ((1, 0, 0, 0),  # ファンド1
     (0, 1, 0, 0),  # ファンド2
     (0, 0, 1, 0),  # ファンド3
     (0, 0, 0, 1),  # ファンド4
     (0, 0.5, 0, 0.5),  # ファンド5
     (0.3, 0.2, 0.3, 0.2),  # ファンド6
     (0.1, 0.1, 0.4, 0.4))  # ファンド7

t = (0.4, 0.1, 0.4, 0.1)

fundarr = [20, 50, 70, 10, 200, 90, 30]

A = calc_fund_to_A(fundarr)


# ----------------------operation_start----------------------

print()
print("----------------------START----------------------")
print("資産クラス配分:", A,"\n")
print("保有ファンド:", fundarr, "\n")
print("購入残り:", beta)
print("資産クラス購入額一覧:", bought)
print("売却残り:", delta)
print("ファンド売却額一覧:", sold, "\n")
print("コサイン類似度:", cossim(A, t), "\n")
print("資産保有総額:", sum(A)+beta, "\n")

pre = True
cur = True
count = 0

while pre or cur:
    pre = cur
    if count % 2 == 0:
        cur = buy()
    else:
        cur = sell()
    print("----------------------"+str(cur)+"----------------------")
    print("資産クラス配分:", A,"\n")
    print("保有ファンド:", fundarr, "\n")
    print("購入残り:", beta)
    print("資産クラス購入額一覧:", bought)
    print("売却残り:", delta)
    print("ファンド売却額一覧:", sold, "\n")
    print("コサイン類似度:", cossim(A, t), "\n")

    count += 1

print("----------------------RESULT----------------------")
print("資産クラス配分:", A,"\n")
print("保有ファンド:", fundarr, "\n")
print("購入残り:", beta)
print("資産クラス購入額一覧:", bought)
print("売却残り:", delta)
print("ファンド売却額一覧:", sold, "\n")
print("コサイン類似度:", cossim(A, t), "\n")
print("資産保有総額:", sum(A), "\n")
