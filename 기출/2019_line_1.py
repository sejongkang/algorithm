def run(t):
    if(t == 1):
        return 1
    return run(t-1) + t

def catch(x, y):
    run_x = run()

run(4) +