from ds1 import Stack, Queue


def hotPotato(namelist, num):
    simqueue=Queue()
    for name in namelist:
        simqueue.enqueue(name)
    while simqueue.size()>1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())# transfer the potato
        simqueue.dequeue()#delete the one who lose
    return simqueue.dequeue()



if __name__ == "__main__":
    print(hotPotato(['tm','tn','tb','tv','tc','tx'],7))