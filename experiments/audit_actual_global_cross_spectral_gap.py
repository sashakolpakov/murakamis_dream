"""Finite algebra/source checks for the real CROSS spectral gap.
Rate comparisons are diagnostics, not a numerical proof of the upper theorem.
"""
import argparse,json
from pathlib import Path
import mpmath as mp
import sympy as sp


def symbolic():
    z,c,b,x,y=sp.symbols('z c b x y',positive=True)
    A=x+y;P=x*y;D=(x-y)**2
    count=0
    assert sp.expand(4*z*A*A+16*P*(c*c-z)-4*(4*P*c*c+D*z))==0;count+=1
    zs=c*c*b*b/((b+x)*(b+y))
    # Squared characteristic equation at the critical start, retaining pre-root sign separately.
    lam=4*b*(c*c-z)
    assert sp.factor((lam*lam-4*z*A*lam-16*z*P*(c*c-z)).subs(z,zs))==0;count+=1
    # At coalescence rho=A sin(pi t) for x=y, expressed via z.
    T=sp.Matrix([[2*sp.sqrt(z)*A,4*P*(c*c-z)],[1,0]])
    rho=sp.sqrt(z)*A+sp.sqrt(4*P*c*c+D*z)
    assert sp.simplify((T-rho*sp.eye(2)).det())==0;count+=1
    T0=T.subs({c:0,y:x});r0=2*x*sp.sqrt(z)
    assert sp.simplify((T0-r0*sp.eye(2))**2)==sp.zeros(2);count+=1
    return count


def action(x,b,y,delta):
    A=x+y;P=x*y
    if delta==mp.mpf('.5'): return mp.log(max(x,y,b))/2
    cc=mp.cos(mp.pi*delta)
    mu=mp.asin(cc*b/mp.sqrt((b+x)*(b+y)))/mp.pi if b else mp.mpf(0)
    def lam(t):
        ss=mp.sin(mp.pi*t)
        return 2*ss*(A*ss+mp.sqrt(4*P*cc*cc+(x-y)**2*ss*ss))
    val=(mu*mp.log(b) if b else 0)
    if mu: val+=mp.quad(lambda t:mp.log(4*(cc*cc-mp.sin(mp.pi*t)**2)),[0,mu])
    val+=mp.quad(lambda t:mp.log(lam(t)),[mu,(mu+mp.mpf('.5'))/2,mp.mpf('.5')])
    return max(val,mp.log(b)/2) if b else val


def run():
    mp.mp.dps=65
    counts={'symbolic_identities':symbolic(),'exact_start_decompositions':0,'exact_rescaled_tail_entries':0,'finite_characteristic_identities':0}
    profiles=[];err=mp.mpf(0)
    cases=[(1,1,1),(2,3,1),(1,0,1),(0,2,1),(0,0,2)]
    for N in (16,17,32,33,64,65):
        J=(N-1)//2;th=mp.pi/N
        ss=[2*mp.sin(j*th) for j in range(J+1)]
        for xx,bb,yy in cases:
            x,b,y=map(mp.mpf,(xx,bb,yy));A=x+y;P=x*y
            for delta in map(mp.mpf,('0','.08','.3','.5')):
                aa=[4*mp.cos((r+mp.mpf('.5'))*th)**2-4*mp.sin(mp.pi*delta)**2 for r in range(J+1)]
                seq=[];pref=mp.mpf(1)
                for j in range(J+1):
                    value=b**j*pref
                    if j:value+=ss[j]**2*A*seq[-1]
                    if j>1:value+=ss[j]*ss[j-1]*aa[j-1]*P*seq[-2]
                    seq.append(value);pref*=aa[j]
                parts=[];pref=mp.mpf(1)
                for i in range(J+1):
                    Kprev=mp.mpf(1);Kprev2=mp.mpf(0)
                    Lprev=mp.mpf(1);Lprev2=mp.mpf(0);sf=mp.mpf(1)
                    for j in range(i+1,J+1):
                        kval=ss[j]**2*A*Kprev+(ss[j]*ss[j-1]*aa[j-1]*P*Kprev2 if j>i+1 else 0)
                        lval=ss[j]*A*Lprev+aa[j-1]*P*Lprev2
                        sf*=ss[j]
                        ee=abs(kval-sf*lval)/max(1,abs(kval),abs(sf*lval));err=max(err,ee)
                        assert ee<mp.mpf('1e-52')
                        counts['exact_rescaled_tail_entries']+=1
                        Kprev2,Kprev=Kprev,kval;Lprev2,Lprev=Lprev,lval
                    parts.append(b**i*pref*Kprev);pref*=aa[i]
                total=mp.fsum(parts)
                ee=abs(total-seq[-1])/max(1,abs(total),abs(seq[-1]));err=max(err,ee)
                assert ee<mp.mpf('1e-50'),(N,xx,bb,yy,delta,ee)
                counts['exact_start_decompositions']+=1
                envelope=action(x,b,y,delta)
                abssum=mp.fsum(abs(v) for v in parts)
                profiles.append({'N':N,'faces':[xx,bb,yy],'delta':str(delta),'log_abs_start_sum_over_N_minus_envelope':float(mp.log(abssum)/N-envelope) if abssum else None})
                for j in (1,J):
                    p=ss[j]*A;q=P*aa[j-1]
                    disc=p*p+4*q
                    assert disc>=-mp.mpf('1e-55')
                    lp=(p+mp.sqrt(max(0,disc)))/2;lm=(p-mp.sqrt(max(0,disc)))/2
                    assert lp>=abs(lm)-mp.mpf('1e-55')
                    counts['finite_characteristic_identities']+=1
    return {'status':'PASS','precision_digits':mp.mp.dps,'counts':counts,'max_relative_identity_error':str(err),'rate_diagnostics':profiles,'scope':'Exact original cofactor recurrence/start decomposition and rescaling; discriminant and coalescing transfer algebra. Finite rate profiles are diagnostics only, not a proof of uniform asymptotics or shared coefficient sewing.'}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=Path(__file__).with_name('actual_global_cross_spectral_gap_results.json'));args=ap.parse_args()
    result=run();args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='rate_diagnostics'},indent=2));print('rate diagnostic cases:',len(result['rate_diagnostics']))
