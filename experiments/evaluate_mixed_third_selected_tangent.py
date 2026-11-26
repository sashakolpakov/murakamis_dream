"""Original third-selection profile supports and centered boundary values.

Import-safe; no reference solve, parameter cover or adaptive trial search.
A numerical target proposal is optional proof input. Only exact rational
trials, outward original primitives and Cartesian endpoint arithmetic
enter the returned compensated upper bound.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from flint import acb,arb,ctx

ROOT=Path(__file__).resolve().parents[1]
PINNED = {'notes/research_mixed_third_selected_implementation.md': '74c898dcb903dc09c3d907c1e2a197083ec5f7b09cd3595d1287a2927527e155',
 'notes/research_mixed_third_selected_center_comparison.md': '2e5305f3e37b3b50cfc5fdfae7d33b3a4b6cf7bf455381a635029c7ff7f5aff4',
 'notes/research_mixed_third_selected_two_vertex_diagnostic.md': '8c4b1d1af57b2fe416267c7759af32d7ec9ffd7957628169749f8fa5157c9515',
 'notes/research_mixed_cyclic_critical_height_bounds.md': '39dff66057a82bc974aa38d65e39a13f508024440bd4e3936783c1c37fe290a9',
 'notes/research_mixed_cyclic_critical_localization.md': 'ccb8b144e6068c434059b707cd13d9aed8bb88a40e7fa0cf0e6bc655bff7fa71',
 'notes/research_mixed_open_word_window_inheritance.md': 'b00b282d3258a42a4e5b6fe1af41b92d8a2c26cc31709b043a133dc27bbdf0ea',
 'notes/research_mixed_typed_last_row_envelopes.md': '5732f40ffc086acddb21632a5d6af3e4905ebad38f97e62e89953802b1bdd10d',
 'notes/research_mixed_plateau_window_concave_profiles.md': 'ba03fd9804c63274b8015532d3c176a044e9b7f0bdd34d69331f420522c88d19',
 'notes/research_mixed_second_selected_outgoing_last_rows.md': 'd634f87205e3273ba5845f8f9586df3fe1a197fae8eae765d010278ff1809c91',
 'notes/research_mixed_selected_outgoing_four_last_row_domination.md': '929aef4bcc8b0fbb5725d34405521e4cda787c546e5f2fa3cebdd0d3760c4525',
 'repro/results/research-mixed-selected-outgoing-four-last-row-domination.json': '23f975f20c70e2f22a197c705d7225c37a30f175c13e92e59353410543d64eeb',
 'notes/research_mixed_selected_three_left_rows.md': 'bb120efc92144f1a3ae6382d9023d1f71503b83f5a89d662791c6aa7f67b3bbc',
 'notes/research_mixed_second_selected_outgoing_four_left_cut.md': 'd980491147fc9e2edfbe2e69148e390064215bd37f08f8df565609fd7c4f9a50',
 'notes/research_mixed_second_selected_outgoing_four_half_row_completion.md': 'ce795f3dbf2cab22244994fa7e881ec3017387e4515f138a41809bfedd72aa75',
 'notes/research_stationary_reference_signed_boundary_compensation.md': '1f3d83f4e29ce9cc26f5c1d053f1726844b1e27af281fc6134155e17b17606f6',
 'notes/research_mixed_second_selected_horizontal_concavity.md': 'dac208b242a8dd24f1ce0c29e15775bd343554e0cb0141e2ad84c0fe64312ca8',
 'notes/research_mixed_four_left_cut_extension.md': 'b8a496417f6c6b619508d2ad644eaef47d7fd4408d412bc28a3e92b09d98b96b',
 'notes/research_mixed_half_index_contour.md': 'ed8d13779e734803090f778d01ddc334469cbfb7a35154ba48d6eb462c28c57e',
 'notes/research_mixed_horizontal_zero_mode_support.md': '8cc704f6145773e9267a8fade870192dac729fb2ecd33ee8d6c854ce7deb5fa9',
 'repro/results/research-mixed-third-selected-eight-center-diagnostic.json': '69ea662427dd1499aea1451df25da519d0249dc3604b55afd0bdd55c7da4812a',
 'repro/results/research-mixed-third-selected-eight-center-saved-audit.json': '14e3f08a8113a501b3073298fff532c9f9c4c4b2552c84f6d8aaecc6d43b9d14',
 'experiments/check_mixed_third_selected_eight_center_record.py': '347d1015bce33c1761609467ce9e96e331fb5f81107ba37dc62933230ee48998',
 'experiments/diagnose_mixed_third_selected_profiles.py': '4edf2a5f7946d35968acc9492757e69c09a87320fbf2d40fdf883d0f852760e8'}
PRECISION=256
NAMES=('a','u','z','v','b')
P=(F(11,50),F(9,20))
H=F(1,100)
_STATE=None


class Inconclusive(Exception):
    pass


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def initialize():
    global _STATE
    if not PINNED:raise ValueError('unfinished third-selection tangent bindings')
    for name,digest in PINNED.items():
        if sha(ROOT/name)!=digest:raise ValueError('changed third-selection tangent input: '+name)
    bindings=dict(PINNED)
    bindings[str(Path(__file__).resolve().relative_to(ROOT))]=sha(Path(__file__))
    _STATE={'bindings':bindings}
    return {'bindings':dict(bindings),'precision_bits':PRECISION,'target_coordinates':list(NAMES),
            'proposal_role':'one numerical target proposal; exact support bound supplies the proof'}


def rat(value):
    value=F(value)
    return arb(value.numerator)/value.denominator


def ends(value):
    if not value.is_finite():raise Inconclusive('nonfinite real enclosure')
    return F(str(value.lower().fmpq())),F(str(value.upper().fmpq()))


def rrecord(value):
    lo,hi=ends(value)
    return frecord((lo,hi))


def frecord(bounds):
    lo,hi=map(F,bounds)
    if lo>hi:raise ValueError('reversed exact interval')
    return {'finite':True,'lower_rational':str(lo),'upper_rational':str(hi)}


def crecord(value):
    return {'real':rrecord(value.real),'imag':rrecord(value.imag)}


def bounds(row):
    if row.get('finite') is not True:raise Inconclusive('input interval is not finite')
    lo,hi=F(row['lower_rational']),F(row['upper_rational'])
    if lo>hi:raise ValueError('reversed saved interval')
    return lo,hi


def read_real(row):
    lo,hi=bounds(row)
    result=arb(rat((lo+hi)/2),rat((hi-lo)/2).upper())
    if not(ends(result)[0]<=lo<=hi<=ends(result)[1]):raise Inconclusive('outward reconstruction failed')
    return result


def read_complex(row):
    return acb(read_real(row['real']),read_real(row['imag']))


def payload(record,alpha,beta,anchor=False):
    if record.get('alpha')!=alpha or record.get('beta')!=beta:
        raise ValueError('reference type association mismatch')
    if anchor:
        if record.get('status')!='fixed canonical reference certified':raise ValueError('uncertified center anchor')
        result=record['reference_certificate']['coordinates']
    else:
        if record.get('status')!='enclosed':raise ValueError('reference is not enclosed')
        result=record['coordinates']
    if set(result)!=set(NAMES):raise ValueError('incorrect reference coordinate inventory')
    return result


def target_box(beta,left,right):
    if beta not in(0,1) or left not in('main','left','half'):
        raise ValueError('unsupported incoming profile')
    if right not in('main','half') or(beta==1 and right!='main'):
        raise ValueError('unsupported outgoing profile')
    box=[P,(F(1,8),F(1,2)),P,(F(3,20) if beta==0 else F(1,8),F(1,2)),P]
    if left!='main':
        fixed=F(1,8) if left=='left' else F(1,2)
        box[1]=(fixed,fixed)
    if right=='half':box[3]=(F(1,2),F(1,2))
    return box


class Primitive:
    def __init__(self):
        self.pi,self.ii=arb.pi(),acb(0,1)
        self.calls={'g':0,'gp':0}

    @staticmethod
    def regular(w):
        if not w.is_finite() or not(w.real>0 and w.real<1):
            raise Inconclusive('original regular strip not enclosed')

    def g(self,w):
        self.regular(w);self.calls['g']+=1
        value=((-2*self.pi*self.ii*w).exp().polylog(2)-self.pi*self.pi/6)/(2*self.pi*self.ii)
        if not value.is_finite():raise Inconclusive('nonfinite original primitive')
        return value

    def gp(self,w):
        self.regular(w);self.calls['gp']+=1
        value=(1-(-2*self.pi*self.ii*w).exp()).log()
        if not value.is_finite():raise Inconclusive('nonfinite original logarithm')
        return value

    def ordinary(self,s,a,b,beta):
        value=self.g(s+a)+self.g(s+b)-(2+beta)*self.g(s)-self.g(a)-self.g(b)+2*self.pi*self.ii*a*s
        ds=self.gp(s+a)+self.gp(s+b)-(2+beta)*self.gp(s)+2*self.pi*self.ii*a
        da=self.gp(s+a)-self.gp(a)+2*self.pi*self.ii*s
        db=self.gp(s+b)-self.gp(b)
        return value,ds,da,db

    def phase(self,q,alpha,beta):
        a,u,z,v,b=q
        left,right=self.ordinary(u,a,z,1),self.ordinary(v,z,b,beta)
        value=left[0]+right[0]-alpha*self.g(a)/2-self.g(z)-beta*self.g(b)/2
        grad=[left[2]-alpha*self.gp(a)/2,left[1],left[3]+right[2]-self.gp(z),
              right[1],right[3]-beta*self.gp(b)/2]
        return value,grad

    def marginals(self,q,alpha,beta):
        a,u,_,v,b=q
        return (self.gp(a+u)-rat(1+F(alpha,2))*self.gp(a)+2*self.pi*self.ii*u,
                self.gp(v+b)-rat(1+F(beta,2))*self.gp(b))


def subtract(x,y):return x[0]-y[1],x[1]-y[0]

def add(x,y):return x[0]+y[0],x[1]+y[1]

def multiply(x,y):
    products=[a*b for a in x for b in y]
    return min(products),max(products)


def complex_difference(x,y):
    return {part:frecord(subtract(bounds(x[part]),bounds(y[part]))) for part in('real','imag')}


def compensation_record(current,anchor,current_hash,anchor_hash):
    pieces={}
    for side,pname,qname in(('left','pL','a'),('right','pR','b')):
        dp=complex_difference(current[pname],anchor[pname])
        dq=complex_difference(current[qname],anchor[qname])
        real_product=multiply(bounds(dp['real']),bounds(dq['real']))
        imag_product=multiply(bounds(dp['imag']),bounds(dq['imag']))
        total=add(real_product,imag_product)
        pieces[side]={'delta_marginal':dp,'delta_coordinate':dq,
                      'real_times_real':frecord(real_product),'imag_times_imag':frecord(imag_product),
                      'real_product':frecord(total)}
    total=add(bounds(pieces['left']['real_product']),bounds(pieces['right']['real_product']))
    total=(total[0]/2,total[1]/2)
    return {'current':current,'anchor':anchor,**pieces,'C0':frecord(total),
            'reference_coordinate_sha256':current_hash,'anchor_coordinate_sha256':anchor_hash,
            'formula':'one half Re[(pL-pL0)conj(a-a0)+(pR-pR0)conj(b-b0)]'}


def propose_trial(reference,alpha,beta,left,right,nu):
    """One bounded floating proposal, returned as an exact rational trial."""
    if _STATE is None:initialize()
    if alpha not in(0,1) or nu not in(0,1):raise ValueError('invalid type or Fourier flag')
    coordinates=payload(reference,alpha,beta)
    box=target_box(beta,left,right)
    import numpy as np
    from scipy.optimize import minimize
    from scipy.special import spence
    r=np.array([complex(float(sum(bounds(coordinates[name]['real']))/2),
                        float(sum(bounds(coordinates[name]['imag']))/2)) for name in NAMES])
    def g(w):return(spence(1-np.exp(-2j*np.pi*w))-np.pi**2/6)/(2j*np.pi)
    def gp(w):return np.log(1-np.exp(-2j*np.pi*w))
    def ordinary(s,a,b,flag):
        return(g(s+a)+g(s+b)-(2+flag)*g(s)-g(a)-g(b)+2j*np.pi*a*s,
               gp(s+a)+gp(s+b)-(2+flag)*gp(s)+2j*np.pi*a,
               gp(s+a)-gp(a)+2j*np.pi*s,gp(s+b)-gp(b))
    def phase(q):
        a,u,z,v,b=q;l,rr=ordinary(u,a,z,1),ordinary(v,z,b,beta)
        return(l[0]+rr[0]-alpha*g(a)/2-g(z)-beta*g(b)/2,
               np.array([l[2]-alpha*gp(a)/2,l[1],l[3]+rr[2]-gp(z),rr[1],rr[3]-beta*gp(b)/2]))
    ref,refgrad=phase(r)
    def objective(x):
        q=np.array(x,dtype=complex)+1j*r.imag
        q[2]=x[2]+1j*float(H)
        if left!='main':q[1]=x[1]+0j
        if right=='half':q[3]=.5+0j
        value,grad=phase(q)
        value-=ref+refgrad[0]*(q[0]-r[0])+refgrad[4]*(q[4]-r[4])
        grad[0]-=refgrad[0];grad[4]-=refgrad[4]
        value+=(1-nu)*g(q[2])-2*np.pi*float(H)*nu
        grad[2]+=(1-nu)*gp(q[2])
        if left!='main':grad[1]=0
        if right=='half':grad[3]=0
        return -float(value.real),-grad.real
    nbox=[(float(lo),float(hi)) for lo,hi in box]
    start=np.clip(r.real,[lo for lo,hi in nbox],[hi for lo,hi in nbox])
    result=minimize(objective,start,jac=True,bounds=nbox,method='L-BFGS-B',
                    options={'ftol':1e-14,'gtol':1e-10,'maxiter':200,'maxls':40})
    if not np.isfinite(result.fun) or not all(np.isfinite(x) for x in result.x):
        raise Inconclusive('nonfinite numerical target proposal')
    trial=tuple(str(min(hi,max(lo,F(f'{float(x):.12f}')))) for x,(lo,hi) in zip(result.x,box))
    metadata={'success':bool(result.success),'message':str(result.message),'iterations':int(result.nit),
              'evaluations':int(result.nfev),'maximum_iterations':200,'proposal_calls':1,
              'candidate_maximum':float(-result.fun),'candidate_targets':result.x.tolist(),
              'acceptance_role':'none; only the exact trial and outward support bound are used'}
    return trial,metadata


def evaluate(reference,anchor,alpha,beta,left,right,nu,trial):
    """Return a single original support bound minus its same-reference C0."""
    if _STATE is None:initialize()
    result={'status':'inconclusive','alpha':alpha,'beta':beta,'left':left,'right':right,'nu':nu,
            'precision_bits':PRECISION}
    p=None
    try:
        if alpha not in(0,1) or nu not in(0,1):raise ValueError('invalid type or Fourier flag')
        if ctx.prec!=PRECISION:raise ValueError('caller must set interval precision to 256 bits')
        box=target_box(beta,left,right)
        trial=tuple(map(F,trial))
        if len(trial)!=5 or not all(lo<=x<=hi for x,(lo,hi) in zip(trial,box)):
            raise ValueError('trial is outside the original target box')
        result['trial']=list(map(str,trial))
        current_payload=payload(reference,alpha,beta)
        anchor_payload=payload(anchor,alpha,beta,anchor=True)
        current_hash,anchor_hash=canonical_hash(current_payload),canonical_hash(anchor_payload)
        result['reference_coordinate_sha256']=current_hash
        result['anchor_coordinate_sha256']=anchor_hash
        r=[read_complex(current_payload[name]) for name in NAMES]
        r0=[read_complex(anchor_payload[name]) for name in NAMES]
        p=Primitive()
        # These broad containing gates are the actual reference/target
        # concavity domains. The provider separately records tighter necessary
        # typed intersections; no clipping is performed here.
        for name,w in zip(NAMES,r):
            real,imag=ends(w.real),ends(w.imag)
            if not(F(11,50)<real[0]<=real[1]<F(9,20)
                   and -F(3,25)<imag[0]<=imag[1]<F(3,25)):
                raise Inconclusive('current reference is outside the broad target product: '+name)
        q=[acb(rat(x),w.imag) for x,w in zip(trial,r)]
        q[2]=acb(rat(trial[2]),rat(H))
        if left!='main':q[1]=acb(rat(trial[1]))
        if right=='half':q[3]=acb(rat(F(1,2)))
        ref,refgrad=p.phase(r,alpha,beta)
        value,grad=p.phase(q,alpha,beta)
        value-=ref+refgrad[0]*(q[0]-r[0])+refgrad[4]*(q[4]-r[4])
        grad[0]-=refgrad[0];grad[4]-=refgrad[4]
        value+=(1-nu)*p.g(q[2])-2*p.pi*rat(H)*nu
        grad[2]+=(1-nu)*p.gp(q[2])
        result['reference_action']=crecord(ref)
        result['trial_defect']=rrecord(value.real)
        result['incoming_marginal']=crecord(refgrad[0]);result['outgoing_marginal']=crecord(refgrad[4])
        support=[]
        for name,x,(lo,hi),slope in zip(NAMES,trial,box,grad):
            gl,gh=ends(slope.real)
            products=[gl*(lo-x),gh*(lo-x),gl*(hi-x),gh*(hi-x)]
            support.append({'name':name,'trial':str(x),'lower':str(lo),'upper':str(hi),
                'gradient':rrecord(slope.real),'corner_products':list(map(str,products)),
                'upper_rational':str(max(products))})
        upper=ends(value.real)[1]+sum((F(t['upper_rational']) for t in support),F(0))
        result['support_terms']=support
        result['upper_rational']=str(upper)
        pl0,pr0=p.marginals(r0,alpha,beta)
        current={'pL':crecord(refgrad[0]),'pR':crecord(refgrad[4]),'a':crecord(r[0]),'b':crecord(r[4])}
        anchored={'pL':crecord(pl0),'pR':crecord(pr0),'a':crecord(r0[0]),'b':crecord(r0[4])}
        compensation=compensation_record(current,anchored,current_hash,anchor_hash)
        compensated=upper-F(compensation['C0']['lower_rational'])
        result['compensation_record']=compensation
        result['compensated_upper_rational']=str(compensated)
        result['compensated_upper_decimal_display']=float(compensated)
        result['status']='enclosed'
    except Inconclusive as error:
        result['reason']=str(error)
    except Exception as error:
        result['status']='error';result['reason']=repr(error)
    result['primitive_calls']=dict(p.calls) if p else {'g':0,'gp':0}
    return result
