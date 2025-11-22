# Pile, hammer, PDA, and environmental parameters

Use the parameters below for the Project Part 3 analysis.
Per the project requirements, users should be able to adjust these parameters, if desired from within the notebook. Do not overwrite the parameters in the support code files.

## Pile parameters

| Parameter | Description | Default value |
|----------|-----|-----:|
| $L$ | Total pile length | 150 feet |
| $A$ | Pile cross-sectional area | 477 square inches |
| $b$ | Pile perimeter | 56 inches |
| $E$ | Pile modulus | 6,807,000 psi |
| $c$ | Pile wave speed | 14450 feet/second |
| $\rho$ | Pile mass density | 2403 kg/m^3 |
| $\nu$ | Poisson's ratio | 0.2 |

## Hammer parameters

| Parameter | Description | Default value |
|----------|-----|-----:|
| $W$ | Hammer ram weight| 20,000 pounds |
| $a$ | $S_o$ equation efficiency| 0.4 |
| $h_{0}$ | piston height at the start of Phase 1 | varies | 
| $m_{piston}$ | piston mass  | 9072 kg |
| $A_{piston}$ | piston cross-sectional area| 0.75 m |
| $V_{min}$ | minimum volume of the combustion chamber when piston height is zero | 7.5e-4 m^3|
| $h_{exhaust}$ | exhaust port height| 0.5 m |
| $V_{fuel}$ | volume of fuel injected per cycle  | varies|
| $\rho_{fuel}$ | fuel density | 832 kg/m^3|
| $Q_{fuel}$ | specific energy content of fuel  | 44 MJ/kg|
| $\eta_{combustion}$ | combustion efficiency  | 0.4 |
| $T_{ignition}$ | ignition temperature  | 500 K|
| $T_{ambient}$ | ambient temperature  | 300 K|
| $P_{atm}$ | ambient temperature  | 101 kPa|
| $g$ | gravitational acceleration   | 9.81 m/s/s or 32.2 ft/s/s|

## PDA parameters

| Parameter | Description | Default value |
|----------|-----|-----:|
| $L_{pda}$ | Distance from PDA instruments to pile toe | 128.8 feet | 
| $J$ | Case method soil damping | 0.5 | 
| $d_{2813}$ | Pile tip depth at blow 2813| 113 feet |
| $d_{3701}$ | Pile tip depth at blow 3701| 132 feet |
| $t_{imp,2813}$ | Time of start of blow impact for blow 2813 | 29.4 milliseconds |
| $t_{imp,3701}$ | Time of start of blow impact for blow 3701| 29.0 milliseconds |

## Environmental parameters

| Parameter | Description | Default value |
|----------|-----|-----:|
| $c_{air}$ | Speed of sound in air | 1125 feet/second | 
| $c_{water}$ | Speed of sound in water | 4920 feet/second |
| $\rho_{air}$ | Density of air | 1.225 kg/m^3 | 
| $\rho_{water}$ | Density of water | 1025 kg/m^3 |
| $p_{ref,air}$ | Acoustic reference pressure for air | 20 $\mu$Pa | 
| $p_{ref,water}$ | Acoustic reference pressure for water | 1 $\mu$Pa|



