data = pd.concat([a,b,c],axis = 1)
human = pd.DataFrame(data , columns= ['age','weight','height'])
print(human,'\n')

def main():
    ### 2. loc(), iloc() 함수를 이용하여 `age`를 추출
    print(human.loc[:,'age'],'\n')
    print(human.iloc[:,0],'\n')
    
    ### 3. loc(), iloc() 함수를 이용하여 `weight`와 `height`만 추출
    print(human.loc[:,'weight'],'\n')
    print(human.iloc[:,2],'\n')
     
    sex = ['F','M','F','M','F']
    ### 4.새로운 데이터 `sex`를 `human`에 추가
    human.loc[:,'sex'] = ['F','M','F','M','F']
    print(human,'\n')
    
    ### 5. `human`에서 `height`를 삭제
    tmp = human.drop(columns=['height'])
    print(tmp,'\n')


if __name__ == "__main__":
    main()