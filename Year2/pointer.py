def main():
    person={'name':'','id':0}
    team=list()
    for i in range(3):
        team.append(person)
    team[0]['name']='Jack'
    team[1]['name']='Pony'
    team[2]['name']='Crossin'
    for i in range(3):
        team[i]['id']=i
        
    return team
    
if __name__ == "__main__":
    print(main())


