"""Independent integral/action and literal physical-collar checks; not a packet audit."""
import argparse
from collections import Counter
import json
from pathlib import Path
import mpmath as mp
import sympy as sp

parser = argparse.ArgumentParser()
parser.add_argument('--output', type=Path,
                    default=Path(__file__).with_name('actual_cross_cofactor_marked_action_results.json'))
args = parser.parse_args()
mp.mp.dps = 75
counts = Counter()
errors = {}

def check(label, actual, expected, tol=mp.mpf('1e-34')):
    err = abs(actual-expected)
    errors[label] = max(errors.get(label, mp.mpf(0)), err)
    counts[label] += 1
    assert err < tol, (label, err, actual, expected)

# Independent elementary primitive used in the protected-middle constant check.
z, ss, cc, BB, CC = sp.symbols('z ss cc BB CC', nonzero=True)
rr = sp.sqrt(BB-CC*z*z)
primitive = sp.log((cc*z/rr-ss)/(cc*z/rr+ss))/(2*ss*cc)
res = sp.factor(sp.diff(primitive,z)-1/((z*z-ss*ss)*rr))
assert sp.simplify(res.subs(BB,cc*cc+CC*ss*ss)) == 0
counts['symbolic_b0_antiderivative'] += 1

def segment(fun, left, right):
    if left == right:
        return mp.mpf(0)
    return (right-left)*mp.quad(lambda t: fun(left+(right-left)*t), [0,mp.mpf('.5'),1])

def data(x,b,y,delta):
    A=x+y; sn=mp.sin(mp.pi*delta); co=mp.cos(mp.pi*delta)
    T=mp.sqrt(b*A+x*y+b*b*sn*sn)
    D=A*A-4*x*y*sn*sn
    Eb=A+2*b*sn*sn+2*sn*T
    mu=mp.atan(b*co/T)/mp.pi if b else mp.mpf(0)
    return A,sn,co,T,D,Eb,mu

def F(x,b,y,delta):
    A,sn,co,T,D,Eb,mu=data(x,b,y,delta)
    if not b and not x*y:
        return mp.log(A)/2
    w=-4*sn*sn
    def root(t):
        st=2*mp.sin(mp.pi*t); at=4*mp.cos(mp.pi*t)**2
        if not x*y:
            return st*st*A
        return (st*st*A+mp.sqrt(st**4*A*A+4*st*st*(at+w)*x*y))/2
    first=mu*mp.log(b)+segment(lambda t:mp.log(4*mp.cos(mp.pi*t)**2+w),0,mu) if b else 0
    return first+segment(lambda t:mp.log(root(t)),mu,mp.mpf('.5'))

def Q_source(x,b,y,delta):
    """Literal beta + original positive Jacobi determinant + half forced product."""
    mu=mp.mpf('.5')-delta
    I=lambda v:segment(lambda t:mp.log(2*mp.sin(mp.pi*t)),0,v)
    def jacobi_root(t):
        co=mp.cos(mp.pi*t); A=x+y
        E=A+2*b*co*co+2*co*mp.sqrt(b*b*co*co+b*A+x*y)
        return E/(4*co*co)
    forced=segment(lambda t:mp.log(x*x+y*y-2*x*y*mp.cos(2*mp.pi*t)),mu,1-mu)/4
    return I(2*mu)-2*I(mu)+segment(lambda t:mp.log(jacobi_root(t)),0,mu)+forced

def angles(x,b,y,delta):
    A,sn,co,T,D,Eb,mu=data(x,b,y,delta)
    def outer(xx,yy):
        den=(xx+b)*mp.sqrt(D)
        cosine=(xx*(yy-xx)+b*(yy+xx*mp.cos(2*mp.pi*delta)))/den
        sine=2*xx*co*T/den
        return -1j*mp.log(cosine+1j*sine)
    return outer(x,y), 2*mp.pi*mu, outer(y,x)

# Direct integration of the TWO independently specified actions. Include all
# allowed triangle zero types, unequal curvatures, and complex parameters.
triples=[(1,1,1),(2,3,5),(4,mp.mpf('.2'),1),(2,0,5),(0,3,5),(2,3,0),(0,0,5),(2,0,0)]
deltas=[mp.mpf('.017'),mp.mpf('.063'),mp.mpc('.031','.009')]
for vals in triples:
    x,b,y=map(mp.mpf,vals)
    for delta in deltas:
        check('independent_source_action_integrals',F(x,b,y,delta),Q_source(x,b,y,delta))

# Differentiate the actual integral, not the target formula. Logarithmic face
# derivatives check the outer/common-scale normalization as well as the middle.
hh=mp.mpf('1e-20')
for vals in triples[:6]:
    x,b,y=map(mp.mpf,vals); delta=mp.mpc('.027','.006')
    A,sn,co,T,D,Eb,mu=data(x,b,y,delta)
    actual=(F(x,b,y,delta+hh)-F(x,b,y,delta-hh))/(2*hh)
    check('integral_spectral_force',actual,-mp.log(Eb/mp.sqrt(D)),mp.mpf('1e-32'))
    if x and y:
        th=angles(x,b,y,delta)
        for pos,var in enumerate((x,b,y)):
            if not var:
                continue
            plus=[x,b,y]; minus=[x,b,y]
            plus[pos]*=mp.exp(hh); minus[pos]*=mp.exp(-hh)
            force=(F(*plus,delta)-F(*minus,delta))/(2*hh)
            check('integral_face_force',force,th[pos]/(2*mp.pi),mp.mpf('1e-32'))

# Literal Gauss heads from the physical H/(bc)^(d/2) adapter, then independent
# whole product and both collar legs. No diagonalizing-conjugation shortcut.
def head(X,S):
    K=-1/X; ff=S*(1-X); ee=(1/X-1)/S
    return mp.matrix([[K,ee],[ff*K,ff*ee+1/K]]),mp.matrix([[1,0],[-K*ff,K]])

for vals in ((1,2,3,1),(2,3,5,7),(4,9,1,1),(1,mp.mpf('.3'),4,2)):
    x,b,c,y=map(mp.mpf,vals)
    for delta in (mp.mpf('.012'),mp.mpf('.057'),mp.mpc('.023','.008')):
        tb=angles(x,b,y,delta);tc=angles(x,c,y,delta)
        gi=mp.mpc('.7','.23'); pin=mp.exp(-1j*tb[1]); pout=mp.exp(1j*tc[1])
        go=gi*mp.exp(1j*(tb[2]+tc[2]))
        Ain,L=head(-x/b,-gi*pin);G,_=head(-b/y,gi);Bin=L**-1*G*L
        Aout,Lo=head(-x/c,-go*pout);Go,_=head(-c/y,go);Bout=Lo**-1*Go*Lo
        P=Bin*Ain; Po=Bout*Aout
        sigma=-2*mp.cos(2*mp.pi*delta)
        check('physical_casimir',mp.trace(P) if hasattr(mp,'trace') else P[0,0]+P[1,1],sigma)
        for actual,expected in zip(P,Po):check('whole_ordered_product',actual,expected)
        Db=data(x,b,y,delta);Dc=data(x,c,y,delta)
        R0=Db[5]*Dc[5]/Db[4];J=-mp.exp(-2j*mp.pi*delta)
        C=mp.eye(2)+(R0-1)/(J-1/J)*(P-mp.eye(2)/J)
        for actual,expected in zip(C*Ain*C**-1,Aout):check('primitive_first_collar',actual,expected)
        for actual,expected in zip(C*Bin*C**-1,Bout):check('primitive_second_collar',actual,expected)
        check('primitive_collar_determinant',mp.det(C),R0)
        check('physical_conic',2+(pin-1)**2/pin*(b+x)*(b+y)/b**2,sigma)

# This is an algebraic change of polarization, not a new volume assertion.
for U,V in ((mp.mpc('.2','.3'),mp.mpc('-.1','.4')),
            (mp.mpc('-.07','.13'),mp.mpc('.11','-.05'))):
    # 2pi Re(S_core-A)= Im(UV)/2 under the exact Legendre relation.
    difference=mp.im(U*V)/2
    meridian_correction=mp.re(U)*mp.im(V)/2
    longitude_correction=-mp.im(U)*mp.re(V)/2
    check('polarization_boundary_correction',meridian_correction-difference,longitude_correction)

for pp,ell,V in ((7,1,mp.mpc('.03','.11')),(-9,1,mp.mpc('-.02','.09')),
                 (11,2,mp.mpc('.05','-.07'))):
    U=-pp*V-2j*mp.pi*ell
    correction=-mp.im(U)*mp.re(V)/2+mp.im(-pp*V*V/4-1j*mp.pi*ell*V)
    check('full_gaussian_critical_boundary_cancellation',correction,0)

out={'status':'PASS','precision':mp.mp.dps,'counts':dict(counts),
     'maximum_errors':{k:str(v) for k,v in errors.items()},
     'scope':'Independent actual-source integral normalization, its full physical derivatives, literal whole Gauss products and primitive collar. No ordinary-middle relative packet, global coefficient saddle, or filling-cycle estimate.'}
args.output.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
