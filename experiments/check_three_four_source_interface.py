#!/usr/bin/env python3
"""Exact interface identities and a validated alternating 3/4 geometry.

Checks no quantum contour or asymptotic coefficient. The quartic root is
isolated by a complex Newton contraction, and its original logarithmic
period lifts are selected from exact squared identities and strict bounds.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

from flint import acb, arb, ctx
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=192)
    ap.add_argument('--output', type=Path,
                    default=ROOT/'repro/results/research-three-four-source-interface.json')
    args = ap.parse_args()
    ctx.prec = args.precision

    def rat(x):
        x = Fraction(x)
        return arb(x.numerator)/x.denominator

    exact = []
    a, X, Y, Z = sp.symbols('a X Y Z')
    p = 4*a**4-6*a**3+4*a**2-2*a+1
    A = a*a
    B = A*(2*a-1)**2/(2*(a-1))
    sextic = 16*a**6-24*a**5+8*a**4-4*a**3+8*a**2-2*a-1

    def identity(name, expression):
        assert sp.cancel(expression) == 0, name
        exact.append(name)

    identity('power-three squared return identity',
             B*(1-A)+A*(4*a**3-3*a+1)/2)
    identity('power-four squared return factorization',
             A*(1-B)+B*(2*B-1)**2-A*p*sextic/(2*(a-1)**3))
    C = 1-2*A*B/(A+B)
    identity('original wire gradient exponential',
             (C+2*A-1)*(C+2*B-1)-(1-C)**2)
    kk = A*B/(A+B)
    identity('fixed-wire return agrees with edge return',
             kk*(1-A)/(A-kk)-B*(1-A)/A)
    identity('crossing bulk derivative cannot be one',
             Y*(1-Z)/(1-Y*Z)-1-(Y-1)/(1-Y*Z))
    identity('power-four fixed-wire period factorization',
             Z**4*(1+X*Z)*(1+Y*Z)-(X+Z)*(Y+Z)
             -(Z**2-1)*(X*Y*Z**4+(X+Y)*Z**3+(1+X*Y)*Z**2+(X+Y)*Z+X*Y))
    WW = sp.symbols('W')
    identity('power-four diagonal selected root',
             (X*X*WW**2+2*X*WW+1-X*X).subs(WW,1-1/X))

    # These are original finite matrices, with their actual level scalar.
    q = (1+sp.I*sp.sqrt(3))/2
    kappa = sp.expand(q*q)
    sine = [sp.Integer(1), sp.sqrt(3), sp.Integer(3)]
    M = sp.zeros(3)
    for i in range(3):
        for j in range(i+1):
            M[i,j] = sp.simplify(kappa*(-1)**i*q**(i*(j+1))
                                *sine[i]/(sine[j]*sine[i-j]))
    J = sp.zeros(3)
    for i in range(3):
        J[i,2-i] = 1
    A3, A4 = sp.simplify(J*M**3), sp.simplify(J*M**4)
    assert sp.simplify(M.T*J-J*M) == sp.zeros(3)
    assert sp.simplify(A3*M-A4) == sp.zeros(3)
    assert sp.simplify(M.T*A3-A4) == sp.zeros(3)
    exact.extend(['original Frobenius adjoint', 'right crossing gives A4',
                  'left transposed crossing gives A4'])
    spectral = []
    for label, mat, claimed in [
        ('A4', A4, (4854+127*sp.I*sp.sqrt(3))/6241),
        ('A3A4', A3*A4, (2462214+14347*sp.I*sp.sqrt(3))/2588881),
    ]:
        tr = sp.simplify(sp.trace(mat))
        tr2 = sp.simplify(sp.trace(mat*mat))
        assert tr != 0
        identity(label+' exact trace ratio', sp.expand_complex(tr2/tr**2)-claimed)
        assert sp.im(claimed).is_positive
        spectral.append({'matrix':label, 'trace':str(tr), 'trace_square':str(tr2),
                         'ratio':str(claimed), 'imaginary_part':str(sp.im(claimed))})

    # One exact rational replay of the interface, independent of its proof
    # by the general binomial formula. Clear the common c_x c_y kappa.
    QQ = sp.expand(q*q)
    row_variable = sp.symbols('z')
    for j in range(3):
        row = sum(M[j,k]*row_variable**k for k in range(j+1))
        product = kappa*(-q)**j*sp.prod(1+q*row_variable*QQ**k for k in range(j))
        assert sp.simplify(sp.expand(row-product)) == 0
        exact.append(f'N3 row generating polynomial {j}')
        for ell in range(j):
            assert sp.simplify(sp.prod(1-QQ**(-ell+k) for k in range(j))) == 0
            exact.append(f'N3 vanished Fourier entry {j},{ell}')
    hx = sp.Matrix([(-1/q)**i/(1-X*QQ**(-i)) for i in range(3)])
    hy = sp.Matrix([(-1/q)**i/(1-Y*QQ**(-i)) for i in range(3)])
    rhs = 0
    for i in range(3):
        num = sp.prod(1-QQ**(-j) for j in range(1,i+1))
        den = sp.prod(1-Y*QQ**(-j) for j in range(i+1))
        rhs += Y**i*num/((1-X*QQ**(-i))*den)
    # Work over Q(i,sqrt3), avoiding an approximate root of unity.
    expr = sp.together((hx.T*M*hy)[0]/kappa-rhs)
    assert sp.simplify(sp.expand(expr)) == 0
    exact.append('N3 rational one-crossing interface')

    # A disk contraction is bounded on its enclosing coordinate square.
    cr = '.772606299919327105862744779296'
    ci = '.357976514994011533180925612135'
    radius = rat('1e-26')
    center = acb(rat(cr),rat(ci))
    box = acb(center.real+arb(0,radius), center.imag+arb(0,radius))

    def poly(z):
        return (((4*z-6)*z+4)*z-2)*z+1

    def deriv(z):
        return ((16*z-18)*z+8)*z-2

    inverse = 1/deriv(center)
    residual = abs(inverse*poly(center))
    contraction = abs(1-inverse*deriv(box))
    checks = []

    def positive(name, value):
        assert value > 0, (name,str(value))
        checks.append({'name':name, 'margin':str(value)})

    positive('Newton contraction below one', 1-contraction)
    positive('Newton disk strict self map', radius-residual-contraction*radius)
    pi, ii = arb.pi(), acb(0,1)
    aa = box
    BB = aa**2*(2*aa-1)**2/(2*(aa-1))
    bb = BB.sqrt()
    t, u = 2*aa.acos(), 2*bb.acos()
    wire = (aa**2*BB/(aa**2+BB)).sqrt().asin()/pi
    xh = acb(arb(1)/6,arb(2).log()/(2*pi))
    for name, z, rr, hh in [
        ('t3',t,('1.61266','1.61268'),('.95522','.95524')),
        ('t4',u,('1.43876','1.43878'),('.69705','.69707')),
    ]:
        positive(name+' real lower',z.real-rat(rr[0]))
        positive(name+' real upper',rat(rr[1])-z.real)
        positive(name+' height lower',-z.imag-rat(hh[0]))
        positive(name+' height upper',rat(hh[1])+z.imag)
    for label,z,lo,hi in [('wire real',wire.real,'.18299','.18301'),
                         ('wire height',wire.imag,'.07871','.07873')]:
        positive(label+' lower',z-rat(lo))
        positive(label+' upper',rat(hi)-z)
    v,w = (t/2).tan(),(u/2).tan()
    q0 = (1+v*v+w*w).sqrt()
    positive('positive original edge branch',q0.real)
    positive('all eight original shapes positive',q0.real**2-v.real**2-w.real**2)
    returns = [(v*bb).asinh(),(w*aa).asinh()]
    candidates = [ii*(3*t-2*pi)/4,ii*(4*u-2*pi)/4]
    for i,(ret,candidate) in enumerate(zip(returns,candidates)):
        for label,z in [('actual return',ret),('period candidate',candidate)]:
            positive(f'{i} {label} real',z.real)
            positive(f'{i} {label} imaginary lower',z.imag+pi/2)
            positive(f'{i} {label} imaginary upper',-z.imag)
    positive('wire in upper quarter strip lower',wire.real)
    positive('wire in upper quarter strip upper',arb(1)/4-wire.real)
    for name,angle in [('t3',t),('t4',u)]:
        positive(name+' regular factorial lower',arb(1)/2-wire.real-angle.real/(2*pi))
        positive(name+' opposite factorial lower',arb(1)/2-wire.real+angle.real/(2*pi))
        positive(name+' opposite factorial upper',arb(1)/2+wire.real-angle.real/(2*pi))
    positive('distance from old center greater than .035',abs(wire-xh)-rat('.035'))
    positive('outside old directed tube in real part',
             wire.real-(arb(1)/6+rat('.013')))
    wire_gradients = []
    for angle in (t,u):
        cp,cm = (pi*wire+angle/2).cos(),(pi*wire-angle/2).cos()
        positive('regular first cosine real part',cp.real)
        positive('regular second cosine real part',cm.real)
        val = cp.log()+cm.log()-2*(pi*wire).sin().log()
        wire_gradients.append(val)
    g3,g4 = wire_gradients
    for label,val,lo,hi in [('g3 real',g3.real,'.0462','.0463'),
                          ('g3 imaginary',g3.imag,'.2967','.2969'),
                          ('g4 real',g4.real,'-.0463','-.0462'),
                          ('g4 imaginary',g4.imag,'-.2969','-.2967')]:
        positive(label+' lower',val-rat(lo))
        positive(label+' upper',rat(hi)-val)
    positive('wire lift sum exceeds minus pi',(g3+g4).imag+pi)
    positive('wire lift sum below pi',pi-(g3+g4).imag)
    XX = (2*pi*ii*wire).exp()
    # Algebraic equality is proved in the note via the original wire equation;
    # this outward enclosure also selects the intended quadratic branch.
    fixed_wire_periods = []
    phase_hessians = []
    positive('selected power-four quadratic root positive real',(2*u.cos()).real)
    positive('other diagonal quadratic root negative real',-(-1-1/XX).real)
    for n,angle,ret,lower in [(3,t,returns[0],7),(4,u,returns[1],9)]:
        rp = ((pi*wire-angle/2).cos().log()
              -(pi*wire+angle/2).cos().log())/2
        for label,z in [('fixed-wire return',rp),('edge return',ret)]:
            positive(f'n{n} {label} positive real',z.real)
            positive(f'n{n} {label} negative imaginary',-z.imag)
            positive(f'n{n} {label} above minus pi/2',z.imag+pi/2)
        pp,pm = (pi*wire+angle/2).tan(),(pi*wire-angle/2).tan()
        dd = -pi*(pp+pm)-2*pi/(pi*wire).tan()
        ee = (pm-pp)/2
        ff = -(pp+pm)/(2*pi)+ii*n/(2*pi)
        positive(f'n{n} angular Hessian nonzero',abs(ff))
        ev1,ev2 = -dd.real,-(dd-2*ee**2/ff).real
        positive(f'n{n} antisymmetric Schur eigenvalue',ev1-lower)
        positive(f'n{n} symmetric Schur eigenvalue',ev2-lower)
        fixed_wire_periods.append({'power':n,'fixed_wire_return':str(rp),
                                   'period_enclosure':str(n*angle+4*ii*rp-2*pi)})
        phase_hessians.append({'power':n,'angular_hessian':str(ff),
                               'negative_real_schur_eigenvalues':[str(ev1),str(ev2)]})

    deps = [
        'notes/research_three_four_source_interface.md',
        'notes/research_traced_three_vertex_endpoint.md',
        'notes/research_positive_three_crossing_cycle.md',
        'notes/research_positive_edge_global_monotonicity.md',
        'notes/research_positive_path_real_wire_order.md',
        'notes/research_unsummed_network_phase_coercivity.md',
        'notes/research_three_vertex_directed_packet.md',
        'notes/research_boundary_crossing_packet_preservation.md',
        'notes/research_bare_kernel_power_three_obstruction.md',
    ]
    result = {
        'status':'passed','precision_bits':args.precision,
        'scope':'Exact original matrix/rational identities and validated periodic positive 3/4 geometric reference, including logarithmic lifts. No asymptotic source coefficient, finite-path localization, or quantum contour is checked.',
        'exact_identities':exact,'exact_identity_count':len(exact),
        'positive_similarity_obstructions':spectral,
        'strict_comparison_count':len(checks),'comparisons':checks,
        'root_certificate':{'center':[cr,ci],'complex_disk_radius':'1/100000000000000000000000000',
                            'residual':str(residual),'contraction_upper':str(contraction),
                            'a_enclosure':str(aa),'b_enclosure':str(bb)},
        'geometric_enclosures':{'t3':str(t),'t4':str(u),'wire':str(wire),
                                'return3':str(returns[0]),'return4':str(returns[1]),
                                'gradient3':str(g3),'gradient4':str(g4)},
        'fixed_wire_periods':fixed_wire_periods,'local_angular_schur_hessians':phase_hessians,
        'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},
    }
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','exact_identity_count','strict_comparison_count']},indent=2))
    print('Geometric wire:',wire)
    print('Distance from homogeneous-three wire:',abs(wire-xh))


if __name__ == '__main__':
    main()
