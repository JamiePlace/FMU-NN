import fmpy

def simulate(fmu:str):
    results = fmpy.simulate_fmu(fmu)
    return results