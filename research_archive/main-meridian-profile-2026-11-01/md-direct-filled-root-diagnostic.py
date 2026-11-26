"""Check the moving trace against its complete first normal, at 80 digits.

This is a numerical diagnostic of the local meridian ratio, not a proof of
the asymptotic statement or the filled knot volume limit.
"""
import json
from pathlib import Path
import mpmath as mp

mp.mp.dps = 80
rows = []
for N in (40, 41, 80, 81, 160, 161):
    k = int(mp.mpf('.31') * N)
    d = N - 1
    eta = (-1) ** d
    centers = [2 * mp.cos((2*j+1)*mp.pi/N) for j in range(k)]
    scale = mp.fprod(2*mp.sin(j*mp.pi/N) for j in range(1,k+1)) ** 2
    def newton(t):
        z = -2*mp.cos(t)
        value, derivative = mp.mpc(1), mp.mpc(0)
        for c in centers:
            derivative = derivative * (c-z) - value
            value *= c-z
        return value/scale, derivative/scale
    for n in (6, -6, 10):
        normals = []
        for r in range(N):
            t = 2*mp.pi*(mp.mpf(d)/2-r)/N
            value, dz = newton(t)
            normals.append(mp.exp(1j*n*N*t*t/(4*mp.pi)) * (
                mp.cos(t)*value + 2*mp.sin(t)**2*dz
                + 1j*n*N/(2*mp.pi)*t*mp.sin(t)*value))
        complete_without_cartan = eta * mp.fsum(normals)
        for s in (mp.mpc('.23','.11'), mp.mpc('.72','.09')):
            values = []
            for r in range(N):
                t = 2*mp.pi*(mp.mpf(d)/2+s-r)/N
                value, _ = newton(t)
                values.append(mp.sin(t)*value*mp.exp(1j*n*N*t*t/(4*mp.pi)))
            moving_without_cartan = eta*N/mp.sin(2*mp.pi*s)*mp.fsum(values)
            error = abs(moving_without_cartan/complete_without_cartan-1)
            rows.append({'N':N,'k':k,'n':n,'s':str(s),
                         'ratio_error':mp.nstr(error,18),
                         'log_error_per_N':mp.nstr(mp.log(error)/N,18)})
result = {'precision':mp.mp.dps,'scope':'Local diagnostic only; no whole-source conclusion.',
          'formula':'Cartan factors divided out; the complete trace uses the exact first normal.',
          'rows':rows}
Path('/private/tmp/md-direct-filled-root-diagnostic-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
