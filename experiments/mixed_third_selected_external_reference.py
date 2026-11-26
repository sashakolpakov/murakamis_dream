"""Import-safe four-leg reference enclosures for the third-selection test.

One fixed-seed floating proposal; full-box original residual certification.
No parameter cover, root retry, target scalar, or response derivative call.
Enclosures are conditional on actual inputs in their typed K domains.
"""
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PRECISION = 256
PINNED = {'notes/research_mixed_third_selected_implementation.md': '74c898dcb903dc09c3d907c1e2a197083ec5f7b09cd3595d1287a2927527e155',
 'notes/research_mixed_third_selected_center_comparison.md': '2e5305f3e37b3b50cfc5fdfae7d33b3a4b6cf7bf455381a635029c7ff7f5aff4',
 'notes/research_mixed_third_selected_two_vertex_diagnostic.md': '8c4b1d1af57b2fe416267c7759af32d7ec9ffd7957628169749f8fa5157c9515',
 'notes/research_mixed_cyclic_critical_height_bounds.md': '39dff66057a82bc974aa38d65e39a13f508024440bd4e3936783c1c37fe290a9',
 'notes/research_mixed_cyclic_critical_localization.md': 'ccb8b144e6068c434059b707cd13d9aed8bb88a40e7fa0cf0e6bc655bff7fa71',
 'notes/research_mixed_open_word_window_inheritance.md': 'b00b282d3258a42a4e5b6fe1af41b92d8a2c26cc31709b043a133dc27bbdf0ea',
 'notes/research_mixed_typed_last_row_envelopes.md': '5732f40ffc086acddb21632a5d6af3e4905ebad38f97e62e89953802b1bdd10d'}
QNAMES = ('u', 'z', 'v', 'b')
NAMES = ('a', 'u', 'z', 'v', 'b')
CENTERS = ((F(7,20),-F(1,100)),(F(3,10),-F(13,250)))
Q = tuple(map(F,('.23','.45','-.12','.12')))
FORMS = {
    'u+z':(1,1,0,0,0,0), 'a+u':(1,0,0,0,1,0), 'u':(1,0,0,0,0,0),
    'z+v':(0,1,1,0,0,0), 'z':(0,1,0,0,0,0),
    'v+b':(0,0,1,1,0,0), 'v':(0,0,1,0,0,0),
    'b+c':(0,0,0,1,0,1), 'b':(0,0,0,1,0,0),
}
_STATE = None


class Inconclusive(Exception):
    pass


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def initialize():
    global _STATE
    if not PINNED:
        raise ValueError('unfinished third-selection reference bindings')
    for name,digest in PINNED.items():
        if sha(ROOT/name)!=digest:
            raise ValueError('changed third-selection reference input: '+name)
    bindings=dict(PINNED)
    bindings[str(Path(__file__).resolve().relative_to(ROOT))]=sha(Path(__file__))
    _STATE={'bindings':bindings}
    return {'bindings':dict(bindings),'precision_bits':PRECISION,
            'seed_policy':'own typed centers; one proposal; no inherited or alternate seed',
            'coordinate_names':list(NAMES),'reference_unknown_names':list(QNAMES)}


def rat(x):
    x=F(x)
    return arb(x.numerator)/x.denominator


def ends(x):
    if not x.is_finite():raise Inconclusive('nonfinite real interval')
    return F(str(x.lower().fmpq())),F(str(x.upper().fmpq()))


def real_record(x):
    lo,hi=ends(x)
    return {'finite':True,'lower_rational':str(lo),'upper_rational':str(hi)}


def complex_record(z):
    if not z.is_finite():raise Inconclusive('nonfinite complex interval')
    return {'real':real_record(z.real),'imag':real_record(z.imag)}


def interval(lo,hi):
    lo,hi=F(lo),F(hi)
    if lo>hi:raise Inconclusive('empty interval')
    result=arb(rat((lo+hi)/2),rat((hi-lo)/2).upper())
    if not(ends(result)[0]<=lo<=hi<=ends(result)[1]):
        raise Inconclusive('outward interval reconstruction failed')
    return result


def rectangle(box):
    return acb(interval(box[0],box[1]),interval(box[2],box[3]))


def cp(pair):
    return acb(rat(pair[0]),rat(pair[1]))


def squared_modulus_upper(z):
    re,im=ends(z.real),ends(z.imag)
    return max(abs(re[0]),abs(re[1]))**2+max(abs(im[0]),abs(im[1]))**2


def sqrt_upper(value):
    value=F(value)
    if value<0:raise ValueError('negative squared bound')
    return ends(rat(value).sqrt())[1] if value else F(0)


def modulus_upper(z):
    return sqrt_upper(squared_modulus_upper(z))


def terms(beta):
    return [((1,'u+z'),(1,'a+u'),(-3,'u')),
            ((1,'u+z'),(1,'z+v'),(-3,'z')),
            ((1,'z+v'),(1,'v+b'),(-(2+beta),'v')),
            ((1,'v+b'),(1,'b+c'),(-(2+beta),'b'))]


def arguments(q,a,c):
    values=list(q)+[a,c]
    return {name:sum((n*w for n,w in zip(row,values)),0) for name,row in FORMS.items()}


def gradient(q,a,c,beta,gp,pi,ii):
    u,z,v,b=q
    return [gp(u+z)+gp(a+u)-3*gp(u)+2*pi*ii*a,
            gp(u+z)+gp(z+v)-3*gp(z)+2*pi*ii*v,
            gp(z+v)+gp(v+b)-(2+beta)*gp(v)+2*pi*ii*z,
            gp(v+b)+gp(b+c)-(2+beta)*gp(b)+2*pi*ii*c]


def jacobian(k,beta,pi,ii):
    h=[[0 for _ in range(4)] for _ in range(4)]
    diag=(k['u+z']+k['a+u']-3*k['u'],k['u+z']+k['z+v']-3*k['z'],
          k['z+v']+k['v+b']-(2+beta)*k['v'],k['v+b']+k['b+c']-(2+beta)*k['b'])
    for j,x in enumerate(diag):h[j][j]=x
    for j,x in enumerate((k['u+z'],k['z+v']+2*pi*ii,k['v+b'])):
        h[j][j+1]=h[j+1][j]=x
    return h,[k['a+u']+2*pi*ii,0,0,0],[0,0,0,k['b+c']+2*pi*ii]


def propose(amid,cmid,beta,counts):
    import mpmath as mp
    counts['proposal_calls']+=1
    with mp.workdps(50):
        def mr(x):return mp.mpf(x.numerator)/x.denominator
        def mc(pair):return mp.mpc(mr(pair[0]),mr(pair[1]))
        def gp(w):
            if not(0<w.real<1):raise Inconclusive('floating proposal left the original regular strip')
            result=mp.log(1-mp.exp(-2*mp.pi*mp.j*w))
            if not mp.isfinite(result):raise Inconclusive('nonfinite floating original logarithm')
            return result
        def hj(q,a,c):
            k={name:mp.pi*mp.cot(mp.pi*w)-mp.pi*mp.j for name,w in arguments(q,a,c).items()}
            h,fa,fc=jacobian(k,beta,mp.pi,mp.j)
            return mp.matrix(h),mp.matrix(fa),mp.matrix(fc)
        a,c=mc(amid),mc(cmid)
        q=mp.matrix([mc(CENTERS[1]),mc(CENTERS[1]),mc(CENTERS[beta]),mc(CENTERS[beta])])
        trace=[];stopped=False
        for iteration in range(20):
            f=mp.matrix(gradient(q,a,c,beta,gp,mp.pi,mp.j))
            counts['floating_gradient_calls']+=1
            maximum=max(abs(x) for x in f)
            trace.append({'iteration':iteration,'residual_max_display':mp.nstr(maximum,20)})
            if maximum<mp.mpf('1e-42'):
                stopped=True;break
            try:
                h,_,_=hj(q,a,c)
                correction=mp.lu_solve(h,f)
            except ZeroDivisionError as error:
                raise Inconclusive('singular floating Newton proposal') from error
            q-=correction;counts['newton_steps']+=1
        scale=10**40
        def rounded(x):
            if not mp.isfinite(x):raise Inconclusive('nonfinite floating predictor')
            return (F(int(mp.nint(x.real*scale)),scale),F(int(mp.nint(x.imag*scale)),scale))
        q0=[rounded(x) for x in q]
        try:
            h,fa,fc=hj([mc(x) for x in q0],a,c)
            ta=-mp.lu_solve(h,fa);tc=-mp.lu_solve(h,fc)
        except ZeroDivisionError as error:
            raise Inconclusive('singular floating affine predictor') from error
        counts['floating_predictor_solves']+=2
        return q0,[rounded(x) for x in ta],[rounded(x) for x in tc],{
            'precision_decimal_digits':50,'maximum_newton_steps':20,'rounding_decimal_places':40,
            'stopped_below_proposal_tolerance':stopped,'proposal_tolerance':'1e-42',
            'trace':trace,'convergence_used_as_certificate':False}


def common(values,label,details):
    check={}
    for name,z in values.items():
        re,im=ends(z.real),ends(z.imag)
        passed=Q[0]<=re[0]<=re[1]<=Q[1] and Q[2]<=im[0]<=im[1]<=Q[3]
        check[name]={'coordinate':complex_record(z),'contained':passed}
        if not passed:
            details.setdefault('common_product_checks',{})[label]=check
            raise Inconclusive(label+' is outside common Q: '+name)
    details.setdefault('common_product_checks',{})[label]=check


def regular(args,label,details):
    check={}
    for name,w in args.items():
        lo,hi=ends(w.real)
        passed=0<lo<=hi<1
        check[name]={'argument':complex_record(w),'regular_strip':passed}
        if not passed:
            details.setdefault('regular_strip_checks',{})[label]=check
            raise Inconclusive(label+' original strip failed: '+name)
    details.setdefault('regular_strip_checks',{})[label]=check


def clipped_record(z,bounds,name,details):
    old=(*ends(z.real),*ends(z.imag))
    new=(max(old[0],bounds[0]),min(old[1],bounds[1]),max(old[2],bounds[2]),min(old[3],bounds[3]))
    details.setdefault('necessary_intersections',{})[name]={
        'raw_box':list(map(str,old)),'necessary_box':list(map(str,bounds)),
        'intersection_box':list(map(str,new))}
    if new[0]>new[1] or new[2]>new[3]:raise Inconclusive('empty necessary actual-reference intersection: '+name)
    result=rectangle(new)
    details['necessary_intersections'][name]['outward_coordinate']=complex_record(result)
    return result


def evaluate(alpha,beta,abox,cbox):
    """Certify the original four-leg image over a full external rectangle."""
    if _STATE is None:initialize()
    counts=Counter();details={}
    result={'status':'inconclusive','alpha':alpha,'beta':beta,'precision_bits':PRECISION,
            'coordinates':{},'diagnostics':details,'counts':{},
            'scope':'actual a in K_(3+alpha), c in K3 union K4, intersected with the original supplied boxes'}
    try:
        if alpha not in(0,1) or beta not in(0,1):raise ValueError('invalid type flag')
        if ctx.prec!=PRECISION:raise ValueError('caller must set interval precision to 256 bits')
        abox,cbox=tuple(map(F,abox)),tuple(map(F,cbox))
        if len(abox)!=4 or len(cbox)!=4:raise ValueError('external boxes must have four exact endpoints')
        details['input_abox']=list(map(str,abox));details['input_cbox']=list(map(str,cbox))
        a,c=rectangle(abox),rectangle(cbox)
        common({'a':a,'c':c},'full external boxes',details)
        amid=((abox[0]+abox[1])/2,(abox[2]+abox[3])/2)
        cmid=((cbox[0]+cbox[1])/2,(cbox[2]+cbox[3])/2)
        details['external_midpoints']={'a':list(map(str,amid)),'c':list(map(str,cmid))}
        q0_pairs,ta_pairs,tc_pairs,proposal=propose(amid,cmid,beta,counts)
        details['proposal']=proposal
        details['exact_affine_model']={'q0':dict(zip(QNAMES,[list(map(str,x)) for x in q0_pairs])),
            'Ta':dict(zip(QNAMES,[list(map(str,x)) for x in ta_pairs])),
            'Tc':dict(zip(QNAMES,[list(map(str,x)) for x in tc_pairs]))}
        q0,ta,tc=list(map(cp,q0_pairs)),list(map(cp,ta_pairs)),list(map(cp,tc_pairs))
        a0,c0=cp(amid),cp(cmid)
        da=rectangle((abox[0]-amid[0],abox[1]-amid[0],abox[2]-amid[1],abox[3]-amid[1]))
        dc=rectangle((cbox[0]-cmid[0],cbox[1]-cmid[0],cbox[2]-cmid[1],cbox[3]-cmid[1]))
        details['external_displacements']={'a':complex_record(da),'c':complex_record(dc)}
        affine=[q0[j]+ta[j]*da+tc[j]*dc for j in range(4)]
        details['full_affine_coordinates']=dict(zip(QNAMES,map(complex_record,affine)))
        common(dict(zip(QNAMES,affine)),'full affine unknowns',details)
        args0=arguments(q0,a0,c0);fullargs=arguments(affine,a,c)
        regular(args0,'midpoint',details);regular(fullargs,'full affine',details)
        pi,ii=arb.pi(),acb(0,1)
        def gp(w):
            counts['original_logarithms']+=1
            value=(1-(-2*pi*ii*w).exp()).log()
            if not value.is_finite():raise Inconclusive('nonfinite original logarithm')
            return value
        direct=None;taylor=None
        try:
            counts['direct_residual_evaluations']+=1
            residual=gradient(affine,a,c,beta,gp,pi,ii)
            direct=[modulus_upper(x) for x in residual]
            details['direct_residual']={'values':list(map(complex_record,residual)),
                                        'row_modulus_uppers':list(map(str,direct))}
        except Inconclusive as error:
            details['direct_residual_failure']=str(error)
        try:
            counts['taylor_residual_evaluations']+=1
            f0=gradient(q0,a0,c0,beta,gp,pi,ii)
            k={}
            for name,w in args0.items():
                sine=(pi*w).sin()
                if not sine.is_finite():raise Inconclusive('nonfinite midpoint sine')
                inverse=1/sine
                if not inverse.is_finite():raise Inconclusive('midpoint sine inverse unresolved')
                k[name]=pi*(pi*w).cos()*inverse-pi*ii
            h,fa,fc=jacobian(k,beta,pi,ii)
            la=[sum((h[i][j]*ta[j] for j in range(4)),acb(0))+fa[i] for i in range(4)]
            lc=[sum((h[i][j]*tc[j] for j in range(4)),acb(0))+fc[i] for i in range(4)]
            linear=[f0[i]+la[i]*da+lc[i]*dc for i in range(4)]
            details['midpoint_residual']=list(map(complex_record,f0))
            details['midpoint_jacobian']=[[complex_record(acb(x)) for x in row] for row in h]
            details['midpoint_external_derivatives']={'a':list(map(lambda x:complex_record(acb(x)),fa)),
                                                       'c':list(map(lambda x:complex_record(acb(x)),fc))}
            details['linear_defect']={'a':list(map(complex_record,la)),'c':list(map(complex_record,lc)),
                                      'whole_linear_residual':list(map(complex_record,linear))}
            form_terms={};remainder_records={}
            for name,coefficients in FORMS.items():
                ka=sum((coefficients[j]*ta[j] for j in range(4)),acb(coefficients[4]))
                kc=sum((coefficients[j]*tc[j] for j in range(4)),acb(coefficients[5]))
                increment=ka*da+kc*dc
                inc_squared=squared_modulus_upper(increment)
                sine=(pi*fullargs[name]).sin()
                re,im=ends(sine.real),ends(sine.imag)
                separation=max(F(0),re[0],-re[1],im[0],-im[1])
                if separation<=0:raise Inconclusive('full affine sine rectangle does not exclude zero: '+name)
                inverse=1/sine
                third=-pi*pi*inverse*inverse
                third_upper=modulus_upper(third)
                contribution=third_upper*inc_squared/2
                form_terms[name]=contribution
                remainder_records[name]={'argument':complex_record(fullargs[name]),
                    'coefficient_a':complex_record(ka),'coefficient_c':complex_record(kc),
                    'increment':complex_record(increment),'increment_modulus_squared_upper':str(inc_squared),
                    'sine':complex_record(sine),'cartesian_separation_lower':str(separation),
                    'third_derivative':complex_record(third),'third_derivative_modulus_upper':str(third_upper),
                    'single_log_remainder_upper':str(contribution)}
            details['taylor_log_remainders']=remainder_records
            row_remainders=[sum((abs(coefficient)*form_terms[name] for coefficient,name in row),F(0))
                            for row in terms(beta)]
            linear_moduli=[modulus_upper(x) for x in linear]
            taylor=[linear_moduli[i]+row_remainders[i] for i in range(4)]
            details['taylor_residual']={'linear_modulus_uppers':list(map(str,linear_moduli)),
                'quadratic_remainder_uppers':list(map(str,row_remainders)),
                'row_modulus_uppers':list(map(str,taylor))}
        except Inconclusive as error:
            details['taylor_residual_failure']=str(error)
        if direct is None and taylor is None:raise Inconclusive('neither original residual enclosure succeeded')
        selected=[min(x[i] for x in(direct,taylor) if x is not None) for i in range(4)]
        square=sum((x*x for x in selected),F(0))
        radius_squared=F(200,157)**2*square
        radius=sqrt_upper(radius_squared)
        details['residual_certificate']={'selected_row_modulus_uppers':list(map(str,selected)),
            'squared_norm_upper':str(square),'pi_lower_rational':'157/50',
            'radius_squared_target':str(radius_squared),'coordinate_radius_rational':str(radius),
            'radius_squared_margin_rational':str(radius*radius-radius_squared),
            'method':'original canonical existence plus pi/4 accretivity; no certified inverse'}
        raw=[]
        for w in affine:
            re,im=ends(w.real),ends(w.imag)
            raw.append(rectangle((re[0]-radius,re[1]+radius,im[0]-radius,im[1]+radius)))
        details['raw_root_coordinates']=dict(zip(QNAMES,map(complex_record,raw)))
        incoming=tuple(map(F,('.267','.433','-.072','.068'))) if alpha==0 else tuple(map(F,('.24','.36','-.108','-.001')))
        out=[clipped_record(a,incoming,'a',details)]
        for j,(name,w) in enumerate(zip(QNAMES,raw)):
            own=1 if j<2 else beta
            bounds=tuple(map(F,('.24','.36','-.102','-.001'))) if own else tuple(map(F,('.267','.433','-.065','.068')))
            out.append(clipped_record(w,bounds,name,details))
        common(dict(zip(NAMES,out)),'actual-reference images after necessary intersections',details)
        result['coordinates']=dict(zip(NAMES,map(complex_record,out)))
        result['coordinate_canonical_sha256']=canonical_hash(result['coordinates'])
        result['status']='enclosed'
    except Inconclusive as error:
        result['reason']=str(error)
    except Exception as error:
        result['status']='error';result['reason']=repr(error)
    result['counts']=dict(counts)
    return result
