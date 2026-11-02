"""Independent limited counterchecks, never certificates for uniform limits."""
from pathlib import Path
import json, math
import mpmath as mp
import sympy as sp
from scipy.integrate import quad, IntegrationWarning
import warnings
warnings.filterwarnings("error", category=IntegrationWarning)

HERE = Path(__file__).resolve().parent
mp.mp.dps = 70

# Exact, generic Hessian calculation for the three positive loads.
x, y, z = sp.symbols('x y z', positive=True)
w = [x, y, z]
D = sp.sqrt(x*y+y*z+z*x)
loads = [sp.atan(a/D)/sp.pi for a in w]
hessian = []
for i in range(3):
    for j in range(3):
        derived = sp.diff(loads[i], w[j])*w[j]
        proposed = (-w[i]*w[j]/(2*sp.pi*D*(w[i]+w[j])) if i != j else
                    sum(w[i]*w[k]/(2*sp.pi*D*(w[i]+w[k]))
                        for k in range(3) if k != i))
        assert sp.simplify(derived-proposed) == 0
        hessian.append([i,j])

def integral_a(t, delta):
    if not t or t == .5:
        return 0.0
    if delta == .5:
        return 2*t*(math.log(t)-1)+quad(
            lambda v: math.log(4*math.pi**2*(math.sin(math.pi*v)/(math.pi*v) if v else 1)**2),
            0,t,epsabs=2e-10)[0]
    if delta == 0:
        return quad(lambda v: math.log(4)+2*math.log(math.cos(math.pi*v)),0,t,epsabs=2e-10)[0]
    root=.5-delta
    primitive=lambda v: v*(math.log(abs(v))-1) if v else 0.0
    singular=primitive(t-root)-primitive(-root)
    def smooth(v):
        z=v-root
        sinc=math.sin(math.pi*z)/(math.pi*z) if z else 1.
        return math.log(abs(4*math.pi*sinc*math.cos(math.pi*(v-delta))))
    return singular+quad(smooth,0,t,epsabs=2e-10)[0]

def integral_lambda(t, delta, x, y):
    if not t:
        return 0.0
    A,P=x+y,x*y
    if not P or delta == .5:
        def smooth(v):
            sinc=math.sin(math.pi*v)/(math.pi*v) if v else 1.
            return math.log(4*max(x,y)*math.pi**2*sinc*sinc)
        return 2*t*(math.log(t)-1)+quad(smooth,0,t,epsabs=2e-10)[0]
    def smooth(v):
        s=math.sin(math.pi*v)
        sinc=s/v if v else math.pi
        return math.log(2*sinc*(A*s+math.sqrt((x-y)**2*s*s+4*P*math.cos(math.pi*delta)**2)))
    return t*(math.log(t)-1)+quad(smooth,0,t,epsabs=2e-10)[0]

envelopes=[]
for x,y,b,c in [(1.,1.,1.,1.),(0.,2.,.3,5.),(2.,0.,0.,3.),
                (1.,3.,0.,.25),(1.,1.,10.,100.),(1.,4.,.2,.7)]:
    A,P=x+y,x*y
    mu0 = math.atan(b/math.sqrt(b*A+P))/math.pi if b else 0.
    qb0=(mu0*math.log(b) if b else 0.)+integral_a(mu0,0.)+(
        integral_lambda(.5,0.,x,y)-integral_lambda(mu0,0.,x,y))
    bound=max(math.log(c),qb0+.5*math.log(c))
    worst=-math.inf
    witness=None
    for delta in [0.,.1,.3,.49,.5]:
        grid=sorted(set([i/64 for i in range(33)]+([mu0] if delta==0 else [])))
        B=[integral_lambda(t,delta,x,y)-integral_a(t,delta) for t in grid]
        for i,mu in enumerate(grid):
            if not b and mu:
                continue
            for j in range(i,len(grid)):
                nu=grid[j]
                value=(mu*math.log(b) if b else 0.)+(1-nu)*math.log(c)+B[j]-B[i]
                if value>worst:
                    worst,witness=value,[delta,mu,nu]
    assert worst<=bound+2e-8, (x,y,b,c,worst,bound,witness)
    assert abs(worst-bound)<2e-8, (worst,bound)
    envelopes.append({'weights':[x,y,b,c],'sampled_max':worst,'formula':bound,
                      'witness':witness,'status':'finite diagnostic only'})

def cofactor_jets(N, x, y, b):
    x,y,b=map(mp.mpf,(x,y,b)); A,P=x+y,x*y
    theta=mp.pi/N
    s=lambda j:2*mp.sin(j*theta)
    a=lambda j:4*mp.cos((j+mp.mpf('.5'))*theta)**2
    values=[mp.mpf(1)]; derivs=[mp.mpf(0)]
    prefix,dprefix=mp.mpf(1),mp.mpf(0)
    for j in range(1,N//2+1):
        dprefix,prefix=dprefix*a(j-1)+prefix,prefix*a(j-1)
        val=b**j*prefix+s(j)**2*A*values[-1]
        der=b**j*dprefix+s(j)**2*A*derivs[-1]
        if j>=2:
            coeff=s(j)*s(j-1)*P
            val+=coeff*a(j-1)*values[-2]
            der+=coeff*(values[-2]+a(j-1)*derivs[-2])
        values.append(val);derivs.append(der)
    return values,derivs

jets=[]
for x,y,b in [(1,1,1),(1,1,0),(0,2,3),(2,0,0)]:
    target=-2*mp.pi*mp.sqrt(b*(x+y)+x*y)/(x+y)
    row={'weights':[x,y,b],'target':float(target),'samples':[]}
    for N in [80,81,160,161,320,321,640,641]:
        values,ders=cofactor_jets(N,x,y,b)
        # u(delta)''|0=-8*pi^2; no finite-difference differentiation.
        computed=-8*mp.pi**2*ders[-1]/(N*values[-1])
        row['samples'].append({'N':N,'normalized_log_second_derivative':float(computed),
                               'error':float(computed-target)})
    jets.append(row)

out={'scope':'Exact symbolic Hessian identities; finite quadrature falsification tests '
             'of the envelope; derivative convergence diagnostics at listed levels. '
             'No numerical test proves uniformity, zero exclusion, a complement gap, '
             'an asymptotic expansion or a volume theorem.',
     'exact_hessian_entries':hessian,'continuum_envelope_diagnostics':envelopes,
     'actual_cofactor_derivative_diagnostics':jets}
(HERE/'counterchecks.json').write_text(json.dumps(out,indent=2)+'\n')
print('9 exact generic Hessian entries, 6 sampled envelope comparisons, 32 exact-recurrence jet diagnostics saved.')
