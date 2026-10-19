import subprocess
import re
import os

corners = ['tt', 'ff', 'ss', 'fs', 'sf']
voltages = [3.3, 2.7, 3.6]
temps = [-20, 27, 85]

results_file = "pvt_results.csv"

with open(results_file, "w") as f:
    f.write("Corner,Vdd(V),Temp(C),DC_Gain(dB),GBW(MHz),Phase_at_GBW(deg)\n")

total = len(corners) * len(voltages) * len(temps)
count = 0

for c in corners:
    for v in voltages:
        for t in temps:
            count += 1
            print(f"[{count}/{total}] Running {c.upper()} | {v}V | {t}C ...")
            
            sim_netlist = f"""* PVT Simulation
.lib /usr/local/share/pdk/sky130A/libs.tech/ngspice/sky130.lib.spice {c}
.include "dacc_core.spice"

.control
set filetype=ascii
alter v5 = {v}
set temp = {t}

ac dec 20 1 1G

meas ac a0 FIND vdb(vout) AT=1
meas ac f_gbw WHEN vdb(vout)=0
meas ac p_at_gbw FIND vp(vout) WHEN vdb(vout)=0

quit
.endc
.end
"""
            with open("sim_temp.spice", "w") as f:
                f.write(sim_netlist)

            proc = subprocess.run(
                ["ngspice", "-b", "sim_temp.spice"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            output = proc.stdout + "\n" + proc.stderr

            a0_match = re.search(r"a0\s*=\s*([+-]?\d+\.?\d*(?:[eE][+-]?\d+)?)", output)
            f_gbw_match = re.search(r"f_gbw\s*=\s*([+-]?\d+\.?\d*(?:[eE][+-]?\d+)?)", output)
            p_match = re.search(r"p_at_gbw\s*=\s*([+-]?\d+\.?\d*(?:[eE][+-]?\d+)?)", output)

            a0 = f"{float(a0_match.group(1)):.2f}" if a0_match else "FAIL"
            gbw = f"{float(f_gbw_match.group(1))/1e6:.3f}" if f_gbw_match else "FAIL"
            p_val = f"{float(p_match.group(1)):.2f}" if p_match else "FAIL"

            with open(results_file, "a") as f:
                f.write(f"{c},{v},{t},{a0},{gbw},{p_val}\n")

if os.path.exists("sim_temp.spice"):
    os.remove("sim_temp.spice")

print("\nFinished all 45 corners! Saved to pvt_results.csv")
