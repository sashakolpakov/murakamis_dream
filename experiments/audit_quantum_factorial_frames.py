"""Independent frame, whole-period and eigenflag-boundary checks.

These supplement the general proofs in the associated note. They do
not compute a knot's selected regulator norm or volume asymptotic.
"""
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp
import sympy as sp


def symbolic_shears():
    v, a, s = sp.symbols('v a s', nonzero=True)
    T = v*a
    r = sp.exp(s*(1-T)/2)
    vv, aa = r*v, a/r
    jac = sp.diff(vv, v)*sp.diff(aa, a)-sp.diff(vv, a)*sp.diff(aa, v)
    assert sp.simplify(jac-1) == 0
    assert sp.simplify(vv*aa-T) == 0
    t = sp.symbols('T', real=True)
    m = sp.exp(s/2)
    k = m*sp.exp(-s*t)
    e = (sp.exp(s*t/2)-sp.exp(-s*t/2))/v
    f = v*(sp.exp(s*(1-t)/2)-sp.exp(-s*(1-t)/2))
    assert sp.simplify(e*f-(m+1/m-k-1/k)) == 0
    assert sp.simplify((m-k)/e-sp.exp(s*(1-t)/2)*v) == 0
    flagminus = -sp.exp(-s*t/2)*sp.sinh(s*(1-t)/2)/sp.sinh(s*t/2)*v
    assert sp.simplify(((1/m-k)/e-flagminus).rewrite(sp.exp)) == 0
    W = s*(t/2-t*t/4)
    assert sp.simplify(sp.diff(W, t)-s*(1-t)/2) == 0
    return {'symplectic_shear': True, 'clock_preserved': True,
            'Casimir_and_both_marked_flags': True, 'quadratic_generator': True}


def bfun(lam, x):
    if not lam or not x:
        return mp.mpf(1)
    if lam*x == 1:
        return mp.mpf(0)
    return mp.sin(mp.pi*lam*x)/(mp.pi*lam*x)


def period(lam, T):
    if not lam or not T:
        return mp.mpf(0)
    s = 2j*mp.pi*lam
    def primitive(x):
        if not x:
            return mp.pi**2/(6*s)
        term = mp.polylog(2, mp.exp(-s*x))
        return s*x*x/4+term/s-x*mp.log(s*x)+x
    value = primitive(1)-primitive(1-T)
    assert abs(mp.im(value)) < mp.mpf('1e-65')
    return mp.re(value)


def finite_frames_and_periods():
    mp.mp.dps = 80
    results = []
    for N in (5, 12, 24, 64, 192):
        n = N-1
        for lam in map(mp.mpf, ('0', '0.2', '0.5', '0.97', '1')):
            q = mp.exp(mp.pi*1j*lam/N)
            qnum = lambda k: mp.mpf(k) if not lam else mp.sin(mp.pi*lam*k/N)/mp.sin(mp.pi*lam/N)
            R = [mp.mpf(1)]
            for j in range(n):
                R.append(R[-1]*qnum(n-j)/(n-j))
            max_error = mp.mpf(0)
            for j in sorted(set((0, 1, N//4, N//2, n))):
                exact = mp.log(R[j])/N
                expected = period(lam, mp.mpf(j)/N)
                error = abs(exact-expected)
                max_error = max(max_error, error)
                assert N*error < 4*mp.log(N)+10
                if j < n:
                    ratio = bfun(lam, mp.mpf(n-j)/N)/bfun(lam, mp.mpf(1)/N)
                    assert abs(R[j+1]/R[j]-ratio) < mp.mpf('1e-65')
            # This is the actual finite similarity for both off-diagonal
            # generator entries. The scalar rho cancels from the test.
            for j in range(n+1):
                if j:
                    E_sym = qnum(j)
                    E_ord = qnum(j)*qnum(N-j)/(N-j)
                    assert abs(E_sym*R[j]/R[j-1]-E_ord) < mp.mpf('1e-60')
                if j < n:
                    F_sym = qnum(n-j)
                    F_ord = n-j
                    assert abs(F_sym*R[j]/R[j+1]-F_ord) < mp.mpf('1e-60')
            results.append({'N':N,'lambda':str(lam),'max_normalized_period_error':float(max_error)})
    for lam in map(mp.mpf, ('0.1', '0.4', '0.99', '1')):
        for T in map(mp.mpf, ('0.13', '0.47', '0.91')):
            deriv = mp.diff(lambda t: period(lam, t), T)
            assert abs(deriv-mp.log(bfun(lam, 1-T))) < mp.mpf('1e-60')
    assert abs(period(mp.mpf(1), mp.mpf(1))-(1-mp.log(2*mp.pi))) < mp.mpf('1e-65')
    cond = []
    target = mp.log(2*mp.pi)-1
    previous_error = mp.inf
    for N in (16, 32, 64, 128, 256, 512):
        sineprod = mp.fprod(mp.sin(mp.pi*k/N) for k in range(1,N))
        assert abs(sineprod/(mp.mpf(N)/2**(N-1))-1) < mp.mpf('1e-65')
        log_min = mp.log(N)-(N-1)*mp.log(2*mp.sin(mp.pi/N))-mp.loggamma(N)
        rate = -log_min/N
        error = abs(rate-target)
        assert error < previous_error
        previous_error = error
        cond.append({'N':N,'conditioning_rate':float(rate),'target':float(target)})
    return {'finite_frame_cases':results,'conditioning_rates':cond,
            'marked_dilogarithm_and_derivative':True}


def inverse_flag_currents():
    mp.mp.dps = 80
    def u(lam, T):
        if not T:
            return mp.mpf(1)
        if T == 1:
            return mp.mpf(0)
        aa = T*mp.sin(mp.pi*lam*(1-T))**2
        bb = (1-T)*mp.sin(mp.pi*lam*T)**2
        return aa/(aa+bb)
    test_derivatives = [
        ('1',lambda t:mp.mpf(1),lambda t:mp.mpf(0)),
        ('T',lambda t:t,lambda t:mp.mpf(1)),
        ('T^2',lambda t:t*t,lambda t:2*t),
        ('exp(T)',mp.exp,mp.exp),
    ]
    records = []
    previous = None
    for eps in map(mp.mpf, ('0.1', '0.01', '0.001', '0.0001')):
        lam = 1-eps
        # Resolve the epsilon^2 current layers at both poles.
        tscale = eps*eps
        grid = [0,tscale/100,tscale/10,tscale,10*tscale,mp.mpf('0.1'),
                mp.mpf('0.5'),mp.mpf('0.9'),1-10*tscale,1-tscale,
                1-tscale/10,1-tscale/100,1]
        grid = sorted(set(t for t in grid if 0 <= t <= 1))
        errs = []
        for label, h, hp in test_derivatives:
            actual = -h(0)-mp.quad(lambda t:hp(t)*u(lam,t),grid)
            predicted = mp.quad(h,[0,1])-h(0)-h(1)
            err = abs(actual-predicted)
            errs.append(err)
            records.append({'epsilon':str(eps),'test':label,'pairing':float(actual),
                            'limiting_pairing':float(predicted),'error':float(err)})
        largest = max(errs)
        if previous is not None:
            assert largest < previous
        previous = largest
    # Both genuine marked eigenline bubble profiles have negative degree.
    profiles = []
    zeta = mp.mpc('0.7','0.4')
    def minusflag(lam,v):
        T = abs(v)**2/(1+abs(v)**2)
        return -mp.exp(-mp.pi*1j*lam*T)*mp.sin(mp.pi*lam*(1-T))/mp.sin(mp.pi*lam*T)*v
    previous = None
    for eps in map(mp.mpf, ('0.01','0.001','0.0001','0.00001')):
        north = minusflag(1-eps,eps*zeta)
        south = minusflag(1-eps,1/(eps*zeta))
        error = max(abs(north+1/mp.conj(zeta)),abs(south-mp.conj(zeta)))
        if previous is not None:
            assert error < previous
        previous = error
        profiles.append({'epsilon':str(eps),'max_profile_error':float(error)})
    assert previous < mp.mpf('0.0001')
    return {'weak_current_tests':records,'negative_bubble_profiles':profiles,
            'total_degree_before_root':-1,'root_main_degree':1,'bubble_degrees':[-1,-1]}


def exact_quantum_shear():
    mp.mp.dps = 80
    q = sp.symbols('q',nonzero=True)
    T = sp.symbols('T')
    cases = 0
    for N in range(2,9):
        n = N-1
        m = q**N
        U = [q**(N*j-j*(j+1)//2) for j in range(N)]
        # Sum in T; the a and b regular factors remove both polar
        # chart divisions, rather than testing only a torus symbol.
        asum = sum(sp.binomial(n,j)*T**j*(1-T)**(n-j)*sp.Rational(j,n)*U[j-1]/U[j]
                   for j in range(1,N))
        bsum = sum(sp.binomial(n,j)*T**j*(1-T)**(n-j)*sp.Rational(n-j,n)*U[j+1]/U[j]
                   for j in range(n))
        assert sp.cancel(asum-m**(-1)*q*T*(1+(q-1)*T)**(n-1)) == 0
        assert sp.cancel(bsum-m/q*(1-T)*(1+(q**(-1)-1)*T)**(n-1)) == 0
        qnum = lambda k:(q**k-q**(-k))/(q-q**(-1))
        for j in range(N):
            qbinom = sp.prod(qnum(N-r)/qnum(r) for r in range(1,j+1))
            D = (-1)**j*q**(j*(j+1)//2)/qbinom
            assert sp.cancel(D*U[j]-(-m)**j/qbinom) == 0
        assert U[n] == q**(N*n//2)
        cases += 1
    rootcases = []
    for N in range(2,21):
        qN = mp.exp(mp.pi*1j/N)
        n = N-1
        eps = (1j)**(N+3)
        for j in range(N):
            Uj = qN**(N*j-j*(j+1)//2)
            Dj = (-1)**j*qN**(j*(j+1)//2)
            assert abs(Uj*Dj-1) < mp.mpf('1e-65')
            assert abs(abs(Uj)-1) < mp.mpf('1e-65')
        assert abs(qN**(N*n//2)-eps) < mp.mpf('1e-65')
        rootcases.append(N)
    return {'exact_generic_symbol_and_residual_gauge_levels':cases,
            'unitary_root_frame_and_original_phase_levels':rootcases,
            'actual_root_source_coupon_conjugation':'U e U^-1',
            'finite_map':'inner star automorphism, not literal finite symbol pullback'}


def main():
    result = {'symbolic':symbolic_shears(), 'whole_frame_period':finite_frames_and_periods(),
              'marked_inverse_flag':inverse_flag_currents(), 'quantum_shear':exact_quantum_shear()}
    target = Path(__file__).with_name('quantum_factorial_frames_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'symbolic':'pass','finite_frame_cases':len(result['whole_frame_period']['finite_frame_cases']),
                      'marked_current_cases':len(result['marked_inverse_flag']['weak_current_tests']),
                      'exact_quantum_shear_generic_levels':result['quantum_shear']['exact_generic_symbol_and_residual_gauge_levels'],
                      'root_boundary_degree':-2,'results':str(target)},indent=2))


if __name__ == '__main__':
    main()
