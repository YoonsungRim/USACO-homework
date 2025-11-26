def solve():
    N, C, P = map(int, input().split())
    nouns, tverbs, iverbs, conjs = [], [], [], []#noun은 noun에 담고, tverbs는 tverbs에 담기위해 list를 만든다
    for _ in range(N):#단어 개수만큼 반복 (리스트에 단어를 담기 위해)
        word, t = input().split()
        if t[0] == "n":# noun이면
            nouns.append(word)
        if t[0] == "t":# transitive이면
            tverbs.append(word)
        if t[0] == "i":# intransitive이면
            iverbs.append(word)
        if t[0] == "c":# conjunction이면
            conjs.append(word)
    ans = (0, 0, 0, 0)
    for n_tverb in range(len(tverbs) + 1):
        n_iverb = min(len(iverbs), len(nouns) - 2 * n_tverb)#전체명사 수 - tverb문장 명사 수(tverb*2)= iverb문장 명사 수/ 그중에서 작은숫자가 iverb 문장 수여야 함. 왜냐하면 iverb가 아무리 많아도 명사가 n개라면 n개밖에 문장을 못만들기 때문임. 
        #위에서는 최대 사용가능한 iverb의 개수를 구함
        while n_iverb >= 0:
            n_conj = min(len(conjs), (n_tverb + n_iverb) // 2)#쓸수 있는 접속사의 개수는 총 문장 개수의 절반(문장 두개당 하나 사용가능하기 때문임.) 만약에 input으로 받는 conj의 개수가 더 크다면, 문장에 다 넣을수 없으므로 (n_tverb + n_iverb) // 2 가 conj의 개수가 되는것이고, (n_tverb + n_iverb) // 2 보다 input이 더 작은거라면 그냥 input을 conj 개수로 사용한다.
            #위에서는 최대 사용가능한 conj의 개수를 구함 
            if n_tverb + n_iverb - n_conj <= P:#P는 마침표 개수임. 저 식은 만들어진 문장의 총 개수를 뜻하는 것임 그말인즉슨 적어도 저 양(n_tverb + n_iverb - n_conj)만큼의 마침표는 사용되어야 한다는 뜻임. 
                break#조건에 맞으니 끊음
            n_iverb -= 1#조건에 안맞으니 맞을때까지 문장을 한개씩 없앰(그래야 원하는 마침표개수만큼의 문장이 만들어지니깐)
        if n_iverb < 0:#iverb 개수가 음수가 됐다는것은 == 조건을 만족하는 iverb 문장의 수를 찾지 못한것임.
            continue #iverb문장은 이제 뺄게 없으니 tverb로 넘어감
        extra_nouns = min(C, len(nouns) - (n_iverb + 2 * n_tverb))#쓸수 있는 남은 명사 수를 구하는것임. 전체 명사의 개수(len(nouns))에서 iverb와 tverb에서 쓴 동사를 뺀거임(n_iverb + 2 * n_tverb) 근데 tverb문장이 하나도 없으면, 더 붙일게 없으므로 extra nouns는 0.
        if n_tverb == 0:# 추가 명사(extra nouns)는 tverb 뒤에만 붙을수 있음. 왜냐면 iverb뒤에는 명사가 안오니깐. 근데 tverb문장이 하나도 없으면, 더 붙일게 없으므로 extra nouns는 0.
            extra_nouns = 0
        n_words = 3 * n_tverb + 2 * n_iverb + n_conj + extra_nouns# 총 사용하는 모든 단어들의 수를 구하는 식. tverb는 주어, 동사, 목적어 이렇게 3개이고, iverb는 주어, 동사 이렇게 2개이고, conj 개수도 세주고, extra noun도 잊지말고 더해주자.
        ans = max(ans, (n_words, n_tverb, n_iverb, n_conj))#원래 있던 ans보다 새로운 조합이 더 큰지

    n_words, n_tverb, n_iverb, n_conj = ans# ans에 있던 최댓값을 각각에 할당하기
    print(n_words)
    basic_sentences = [nouns.pop() + " " + iverbs.pop() for _ in range(n_iverb)] + [
        nouns.pop() + " " + tverbs.pop() + " " + nouns.pop() for _ in range(n_tverb)
    ]
    #첫번째줄: iverb의 문장(subject + iverb)을 for loop를 사용해서 만든다.(iverb 개의 문장을 만들어냄)
    #두번째줄: tverb의 문장(subject + tverb + noun)을 for loop를 사용해서 만든다. (tverb 개의 문장을 만들어냄)

    while n_tverb > 0 and C > 0 and len(nouns) > 0:#extra nouns를 붙이는 단계/ tverb문장이 한개 이상 있고 comma도 한개 이상 있을때, 그리고 명사의 개수가 1개 이상일때
        basic_sentences[-1] += ", " + nouns.pop()# tverb 문장을 iverb보다 나중에 만들어서 [-1]인덱싱하면 tverb 문장 나옴. comma를 붙이고 noun을 붙이면 됨.
        C -= 1# 가능한 commma 개수 하나 사라짐

    compound_sentences = [
        basic_sentences.pop() + " " + conjs.pop() + " " + basic_sentences.pop()
        for _ in range(n_conj)
    ]#conjunction을 써서 문장을 합쳐보자
    #basic문장 + conjunction + basic문장
    sentences = [sentence + "." for sentence in basic_sentences + compound_sentences]#모든 문장들이 들어있는 두개의 리스트를 더하고, 그거를 for loop를 돌면서 마침표를 찍는거임
    print(" ".join(sentences))#문장 사이에 간격 넣기)


T = int(input())
for t in range(T):
    solve()