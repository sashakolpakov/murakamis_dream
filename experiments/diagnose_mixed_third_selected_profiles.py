#!/usr/bin/env python3
"""Eight fixed ordinary-window centers and 72 third-selection profile tests.

No parameter cover, finite quantum sum, alternate seed, or retry. Newton
and target optimization only propose exact rational centers/trials. The
original accretive residual bound certifies each retained reference;
Arb and rational support arithmetic certify only these prescribed inputs.
"""
import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PINNED = {'notes/research_mixed_third_selected_two_vertex_diagnostic.md': '8c4b1d1af57b2fe416267c7759af32d7ec9ffd7957628169749f8fa5157c9515', 'notes/research_mixed_plateau_window_concave_profiles.md': 'ba03fd9804c63274b8015532d3c176a044e9b7f0bdd34d69331f420522c88d19', 'notes/research_mixed_cyclic_critical_height_bounds.md': '39dff66057a82bc974aa38d65e39a13f508024440bd4e3936783c1c37fe290a9', 'notes/research_mixed_cyclic_critical_localization.md': 'ccb8b144e6068c434059b707cd13d9aed8bb88a40e7fa0cf0e6bc655bff7fa71', 'notes/research_mixed_open_word_window_inheritance.md': 'b00b282d3258a42a4e5b6fe1af41b92d8a2c26cc31709b043a133dc27bbdf0ea', 'notes/research_mixed_second_selected_outgoing_last_rows.md': 'd634f87205e3273ba5845f8f9586df3fe1a197fae8eae765d010278ff1809c91', 'notes/research_mixed_selected_outgoing_four_last_row_domination.md': '929aef4bcc8b0fbb5725d34405521e4cda787c546e5f2fa3cebdd0d3760c4525', 'repro/results/research-mixed-selected-outgoing-four-last-row-domination.json': '23f975f20c70e2f22a197c705d7225c37a30f175c13e92e59353410543d64eeb', 'notes/research_mixed_selected_three_left_rows.md': 'bb120efc92144f1a3ae6382d9023d1f71503b83f5a89d662791c6aa7f67b3bbc', 'notes/research_mixed_second_selected_outgoing_four_left_cut.md': 'd980491147fc9e2edfbe2e69148e390064215bd37f08f8df565609fd7c4f9a50', 'notes/research_mixed_second_selected_outgoing_four_half_row_completion.md': 'ce795f3dbf2cab22244994fa7e881ec3017387e4515f138a41809bfedd72aa75'}
NAMES = ('a', 'u', 'z', 'v', 'b')
QNAMES = ('u', 'z', 'v', 'b')
P = (F(11, 50), F(9, 20))
H = F(1, 100)
CENTERS = ((F(7, 20), -F(1, 100)), (F(3, 10), -F(13, 250)))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify():
    if not PINNED:
        raise ValueError('unfinished dependency bindings')
    for name, digest in PINNED.items():
        if sha(ROOT/name) != digest:
            raise ValueError('changed input: '+name)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    verify()
    # Arithmetic libraries are imported only after binding the proof inputs.
    import mpmath as mp
    import numpy as np
    from scipy.optimize import minimize
    from scipy.special import spence
    from flint import acb, arb, ctx
    ctx.prec = 192
    mp.mp.dps = 50
    pi, ii = arb.pi(), acb(0, 1)
    counts = {'reference_proposals': 0, 'reference_residual_certificates': 0,
              'target_proposals': 0, 'profile_interval_bounds': 0,
              'finite_quantum_sums': 0, 'parameter_subdivisions': 0,
              'alternate_seeds': 0}

    def rat(x):
        x = F(x)
        return arb(x.numerator)/arb(x.denominator)

    def endpoints(x):
        if not x.is_finite():
            raise ValueError('nonfinite real enclosure')
        return F(str(x.lower().fmpq())), F(str(x.upper().fmpq()))

    def record(x):
        lo, hi = endpoints(x)
        return {'finite': True, 'lower_rational': str(lo), 'upper_rational': str(hi)}

    def crecord(x):
        return {'real': record(x.real), 'imag': record(x.imag)}

    def ball(lo, hi):
        lo, hi = F(lo), F(hi)
        if lo > hi:
            raise ValueError('reversed interval')
        return arb(rat((lo+hi)/2), rat((hi-lo)/2))

    def exact(pair):
        return acb(rat(pair[0]), rat(pair[1]))

    def mpc(pair):
        return mp.mpc(mp.mpf(pair[0].numerator)/pair[0].denominator,
                      mp.mpf(pair[1].numerator)/pair[1].denominator)

    def rounded(x):
        return F(int(mp.nint(x*10**40)), 10**40)

    def mp_gp(w):
        if not 0 < w.real < 1:
            raise ValueError('proposal left original logarithmic strip')
        return mp.log(1-mp.exp(-2j*mp.pi*w))

    def mp_gpp(w):
        return mp.pi*mp.cot(mp.pi*w)-1j*mp.pi

    def equations(q, a, c, beta, gp, chirp):
        u, z, v, b = q
        return [gp(u+z)+gp(a+u)-3*gp(u)+chirp*a,
                gp(u+z)+gp(z+v)-3*gp(z)+chirp*v,
                gp(z+v)+gp(v+b)-(2+beta)*gp(v)+chirp*z,
                gp(v+b)+gp(b+c)-(2+beta)*gp(b)+chirp*c]

    def newton(a_pair, c_pair, beta):
        counts['reference_proposals'] += 1
        a, c = mpc(a_pair), mpc(c_pair)
        q = mp.matrix([mpc(CENTERS[1]), mpc(CENTERS[1]),
                       mpc(CENTERS[beta]), mpc(CENTERS[beta])])
        trace, message = [], 'maximum twenty steps reached'
        for iteration in range(20):
            try:
                f = mp.matrix(equations(q, a, c, beta, mp_gp, 2j*mp.pi))
                norm = max(abs(t) for t in f)
                trace.append({'iteration': iteration, 'residual_max_display': mp.nstr(norm, 18)})
                if norm < mp.mpf('1e-44'):
                    message = 'floating residual threshold reached'
                    break
                u, z, v, b = q
                k_uz, k_au, k_zv, k_vb, k_bc = [mp_gpp(w) for w in
                                               (u+z, a+u, z+v, v+b, b+c)]
                diagonal = [k_uz+k_au-3*mp_gpp(u), k_uz+k_zv-3*mp_gpp(z),
                            k_zv+k_vb-(2+beta)*mp_gpp(v), k_vb+k_bc-(2+beta)*mp_gpp(b)]
                jac = mp.diag(diagonal)
                for index, value in enumerate((k_uz, k_zv+2j*mp.pi, k_vb)):
                    jac[index,index+1] = jac[index+1,index] = value
                q -= mp.lu_solve(jac, f)
            except (ValueError, ZeroDivisionError) as error:
                message = 'proposal stopped: '+str(error)
                break
        return [(rounded(t.real), rounded(t.imag)) for t in q], trace, message

    class Primitive:
        def __init__(self):
            self.calls = {'g': 0, 'gp': 0}

        @staticmethod
        def regular(w):
            if not w.is_finite() or not (w.real > 0 and w.real < 1):
                raise ValueError('original logarithmic strip not enclosed')

        def gp(self, w):
            self.regular(w)
            self.calls['gp'] += 1
            result = (1-(-2*pi*ii*w).exp()).log()
            if not result.is_finite():
                raise ValueError('nonfinite original logarithm')
            return result

        def g(self, w):
            self.regular(w)
            self.calls['g'] += 1
            result = ((-2*pi*ii*w).exp().polylog(2)-pi*pi/6)/(2*pi*ii)
            if not result.is_finite():
                raise ValueError('nonfinite original primitive')
            return result

        def ordinary(self, s, a, b, beta):
            return (self.g(s+a)+self.g(s+b)-(2+beta)*self.g(s)-self.g(a)-self.g(b)+2*pi*ii*a*s,
                    self.gp(s+a)+self.gp(s+b)-(2+beta)*self.gp(s)+2*pi*ii*a,
                    self.gp(s+a)-self.gp(a)+2*pi*ii*s,
                    self.gp(s+b)-self.gp(b))

        def phase(self, q, alpha, beta):
            a, u, z, v, b = q
            left, right = self.ordinary(u, a, z, 1), self.ordinary(v, z, b, beta)
            value = left[0]+right[0]-alpha*self.g(a)/2-self.g(z)-beta*self.g(b)/2
            gradient = [left[2]-alpha*self.gp(a)/2, left[1],
                        left[3]+right[2]-self.gp(z), right[1], right[3]-beta*self.gp(b)/2]
            return value, gradient

    def certify(proposal, a_pair, c_pair, beta, details):
        counts['reference_residual_certificates'] += 1
        if not all(F(23,100) <= x <= F(9,20) and -F(3,25) <= y <= F(3,25)
                   for x, y in proposal):
            raise ValueError('rounded reference proposal is outside Q^4')
        p = Primitive()
        q0, a, c = [exact(t) for t in proposal], exact(a_pair), exact(c_pair)
        residual = equations(q0, a, c, beta, p.gp, 2*pi*ii)
        absolute = [record(abs(x)) for x in residual]
        maximum = max(F(x['upper_rational']) for x in absolute)
        radius = endpoints(8*rat(maximum)/pi)[1]
        details.update({'residual': [crecord(x) for x in residual], 'residual_moduli': absolute,
                        'residual_max_upper_rational': str(maximum),
                        'root_coordinate_radius_rational': str(radius),
                        'residual_primitive_calls': p.calls})
        roots = [acb(ball(x-radius, x+radius), ball(y-radius, y+radius)) for x,y in proposal]
        for index, w in enumerate(roots):
            own = 1 if index < 2 else beta
            rb = (F(6,25),F(9,25)) if own else (F(267,1000),F(433,1000))
            hb = (-F(51,500),-F(1,1000)) if own else (-F(13,200),F(17,250))
            if not (w.real > rat(rb[0]) and w.real < rat(rb[1])
                    and w.imag > rat(hb[0]) and w.imag < rat(hb[1])):
                details['raw_root_coordinates'] = dict(zip(QNAMES, map(crecord, roots)))
                raise ValueError('certified root enclosure does not fit the required typed domain')
        details['coordinates'] = dict(zip(NAMES, map(crecord, [a]+roots)))
        return [a]+roots

    def target_box(beta, left, right):
        result = [P, (F(1,8),F(1,2)), P,
                  (F(3,20) if beta == 0 else F(1,8),F(1,2)), P]
        if left != 'main':
            fixed = F(1,8) if left == 'left' else F(1,2)
            result[1] = (fixed,fixed)
        if right == 'half':
            result[3] = (F(1,2),F(1,2))
        return result

    def ng(w):
        return (spence(1-np.exp(-2j*np.pi*w))-np.pi**2/6)/(2j*np.pi)

    def ngp(w):
        return np.log(1-np.exp(-2j*np.pi*w))

    def nordinary(s,a,b,beta):
        return (ng(s+a)+ng(s+b)-(2+beta)*ng(s)-ng(a)-ng(b)+2j*np.pi*a*s,
                ngp(s+a)+ngp(s+b)-(2+beta)*ngp(s)+2j*np.pi*a,
                ngp(s+a)-ngp(a)+2j*np.pi*s,ngp(s+b)-ngp(b))

    def nphase(q,alpha,beta):
        a,u,z,v,b = q
        left,right = nordinary(u,a,z,1),nordinary(v,z,b,beta)
        return (left[0]+right[0]-alpha*ng(a)/2-ng(z)-beta*ng(b)/2,
                np.array([left[2]-alpha*ngp(a)/2,left[1],left[3]+right[2]-ngp(z),
                          right[1],right[3]-beta*ngp(b)/2]))

    def objective(x, r, alpha, beta, left, right, nu):
        q = np.array(x,dtype=complex)+1j*r.imag
        q[2] = x[2]+1j*float(H)
        if left != 'main':
            q[1] = x[1]+0j
        if right == 'half':
            q[3] = .5+0j
        value,gradient = nphase(q,alpha,beta)
        ref,refgrad = nphase(r,alpha,beta)
        value -= ref+refgrad[0]*(q[0]-r[0])+refgrad[4]*(q[4]-r[4])
        gradient[0] -= refgrad[0]
        gradient[4] -= refgrad[4]
        value += (1-nu)*ng(q[2])-2*np.pi*float(H)*nu
        gradient[2] += (1-nu)*ngp(q[2])
        if left != 'main':
            gradient[1] = 0
        if right == 'half':
            gradient[3] = 0
        return -float(value.real), -gradient.real

    def evaluate(r, alpha, beta, left, right, nu, trial):
        counts['profile_interval_bounds'] += 1
        box = target_box(beta,left,right)
        assert len(trial) == 5 and all(lo <= x <= hi for x,(lo,hi) in zip(trial,box))
        p = Primitive()
        q = [acb(rat(x),w.imag) for x,w in zip(trial,r)]
        q[2] = acb(rat(trial[2]),rat(H))
        if left != 'main':
            q[1] = acb(rat(trial[1]))
        if right == 'half':
            q[3] = acb(rat(F(1,2)))
        reference,refgrad = p.phase(r,alpha,beta)
        value,gradient = p.phase(q,alpha,beta)
        value -= reference+refgrad[0]*(q[0]-r[0])+refgrad[4]*(q[4]-r[4])
        gradient[0] -= refgrad[0]
        gradient[4] -= refgrad[4]
        value += (1-nu)*p.g(q[2])-2*pi*rat(H)*nu
        gradient[2] += (1-nu)*p.gp(q[2])
        support = []
        for name,x,(lo,hi),slope in zip(NAMES,trial,box,gradient):
            gl,gh = endpoints(slope.real)
            products = [gl*(lo-x),gh*(lo-x),gl*(hi-x),gh*(hi-x)]
            support.append({'name':name,'trial':str(x),'lower':str(lo),'upper':str(hi),
                            'gradient':record(slope.real),'corner_products':list(map(str,products)),
                            'upper_rational':str(max(products))})
        upper = endpoints(value.real)[1]+sum(F(t['upper_rational']) for t in support)
        return {'trial':list(map(str,trial)),'trial_defect':record(value.real),
                'incoming_marginal':crecord(refgrad[0]),'outgoing_marginal':crecord(refgrad[4]),
                'support_terms':support,'upper_rational':str(upper),
                'upper_decimal_display':float(upper),'primitive_calls':p.calls}

    results, unexpected = [], None
    for alpha,beta,sigma in itertools.product((0,1),repeat=3):
        row = {'alpha':alpha,'beta':beta,'external_right_type_flag':sigma,
               'external_a':list(map(str,CENTERS[alpha])),
               'external_c':list(map(str,CENTERS[sigma])), 'profiles':[]}
        results.append(row)
        try:
            proposal,trace,message = newton(CENTERS[alpha],CENTERS[sigma],beta)
            row.update({'proposal_centers':dict(zip(QNAMES,[list(map(str,t)) for t in proposal])),
                        'proposal_trace':trace,'proposal_message':message})
            details = {}
            row['reference_certificate'] = details
            r = certify(proposal,CENTERS[alpha],CENTERS[sigma],beta,details)
            row['status'] = 'fixed canonical reference certified'
            numeric_r = np.array([complex(float(x),float(y)) for x,y in [CENTERS[alpha]]+proposal])
            for left,right,nu in itertools.product(('main','left','half'),
                                ('main','half') if beta == 0 else ('main',),(0,1)):
                profile = {'incoming_profile':left,'outgoing_profile':right,'nu':nu}
                row['profiles'].append(profile)
                counts['target_proposals'] += 1
                box = target_box(beta,left,right)
                nbox = [(float(lo),float(hi)) for lo,hi in box]
                initial = np.clip(numeric_r.real,[a for a,b in nbox],[b for a,b in nbox])
                fixed = (numeric_r,alpha,beta,left,right,nu)
                opt = minimize(objective,initial,args=fixed,jac=True,bounds=nbox,method='L-BFGS-B',
                               options={'ftol':1e-14,'gtol':1e-10,'maxiter':200,'maxls':40})
                profile['proposal'] = {'success':bool(opt.success),'message':str(opt.message),
                    'iterations':int(opt.nit),'evaluations':int(opt.nfev),
                    'candidate_maximum':float(-opt.fun),'candidate_targets':opt.x.tolist()}
                test = np.array([(lo+hi)/2 for lo,hi in nbox])
                slope = objective(test,*fixed)[1]
                errors = []
                for j,(lo,hi) in enumerate(nbox):
                    if lo == hi:
                        continue
                    step = np.zeros(5); step[j] = 1e-6
                    diff = (objective(test+step,*fixed)[0]-objective(test-step,*fixed)[0])/2e-6
                    errors.append(abs(float(diff-slope[j])))
                profile['gradient_difference_max_error'] = max(errors)
                trial = [min(hi,max(lo,F(f'{float(x):.12f}'))) for x,(lo,hi) in zip(opt.x,box)]
                profile.update(evaluate(r,alpha,beta,left,right,nu,trial))
        except ValueError as error:
            row['status'] = 'arithmetic or proposal inconclusive'
            row['reason'] = str(error)
        except Exception as error:
            row['status'] = 'unexpected error'
            row['reason'] = repr(error)
            unexpected = repr(error)
            break
        print(json.dumps({'completed_case':[alpha,beta,sigma],'status':row['status'],
                          'profiles':len(row['profiles'])}),flush=True)
    verify()
    result = {'status':'fixed eight-center diagnostic completed' if unexpected is None and len(results)==8 else 'stopped with unexpected error',
              'diagnostic':True,'scope':'eight canonical external centers only; no product-domain or actual-word assertion',
              'precision_bits':192,'proposal_decimal_digits':50,'proposal_max_steps':20,
              'target_proposal_max_iterations':200,'maximum_reference_proposals':8,
              'maximum_profile_bounds':72,'height_rational':str(H),'input_sha256':PINNED,
              'script_sha256':sha(Path(__file__)),'counts':counts,'references':results,
              'unexpected_error':unexpected,'whole_domain_claimed':False,
              'finite_word_realization_claimed':False}
    assert counts['reference_proposals'] <= 8 and counts['target_proposals'] <= 72
    profiles = [p for r in results for p in r['profiles'] if 'upper_rational' in p]
    if profiles:
        result['largest_support_upper_rational'] = str(max(F(p['upper_rational']) for p in profiles))
        result['largest_trial_lower_rational'] = str(max(F(p['trial_defect']['lower_rational']) for p in profiles))
        result['max_gradient_difference_error'] = max(p['gradient_difference_max_error'] for p in profiles)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as stream:
        json.dump(result,stream,sort_keys=True,indent=2)
        stream.write('\n')
    print(json.dumps({'status':result['status'],'counts':counts,
          'largest_support_upper':float(F(result['largest_support_upper_rational'])) if profiles else None,
          'output_sha256':sha(args.output)}),flush=True)


if __name__ == '__main__':
    main()
