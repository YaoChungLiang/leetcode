import time, threading, concurrent.futures
start = time.perf_counter()

def do_something(sec):
    print(f'sleep for {sec} seconds')
    time.sleep(sec)
    print('Done sleeping')
    
threads= []
for _ in range(10):
    t = threading.Thread(target=do_something,args=[2.0])
    t.start()
    threads.append(t)

for t in threads:
    t.join()
    
finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} seconds')    
    
    
# newer way 

def do_newThings(sec):
    print(f'sleep for {sec} seconds')
    time.sleep(sec)
    return f'Done sleeping...{sec} '    

start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_newThings, 1.2)
    print(f1.result()) # return a future object basically encapsulate a 
finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} seconds')  

start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(do_newThings, 1.2) for _ in range(10)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())     
finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} seconds')  

        
start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = [executor.submit(do_newThings, sec) for sec in secs]
    for f in concurrent.futures.as_completed(results):
        print(f.result())   
finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} seconds')  




start = time.perf_counter()        
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs= [5,4,3,2,1]
    results = executor.map(do_newThings, secs)
    for result in results:
        print(result)  
finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} seconds')