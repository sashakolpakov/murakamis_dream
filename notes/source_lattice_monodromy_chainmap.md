# The actual source lattice, companion monodromy, and its normal cut

Research construction, 27 October 2026. This gives explicit maps from an
actual scalar quantum equation and its pointed source to the root
monodromy kernel, cokernel and first normal equation. It also identifies
the distinguished cut as a normal lattice functional, rather than
assuming it is a cyclic invariant line. No geometric-component or
regulator comparison is asserted.

## 1. The scalar source complex maps exactly to companion monodromy

Fix a primitive N-th root zeta, N>=2. Write E=k(Y), F=k(U), U=Y^N,
sigma f(Y)=f(zeta Y). Start with a specified actual scalar operator

    P(Q)=sum_(j=0)^d a_j(Q,Y) sigma_Q^j,
    sigma_Q f(Y)=f(QY),

regular at Q=zeta, with d>=1 and a_0 and a_d nonzero there. Laurent shift
operators can first be put in this form by a fixed shift. These choices
retain the actual source; they are not minimal-operator assumptions.
All maps below are initially over E and F, so no regularity at U=1 is
being silently imposed.

Let A be the solution companion matrix, so its first d-1 rows shift
coordinates and its last row is -(a_0,...,a_(d-1))/a_d. Put

    J(Q)f=(f,sigma_Q f,...,sigma_Q^(d-1)f)^t,
    T(Q)=A(Q,Y)^(-1) sigma_Q,
    r(Q)=A(Q,Y)^(-1)e_d/a_d(Q,Y),
    S_N(Q)=I+T(Q)+...+T(Q)^(N-1),
    M(Q)=T(Q)^N-I.

The following are exact identities of operators before specializing Q:

    (T-I)J=rP,
    M J=S_N r P.                                      (1.1)

Indeed sigma_Q J-AJ has only its last entry nonzero, equal to Pf/a_d.
The second identity is the geometric-series factorization. Thus the
actual scalar two-term complex maps to the monodromy complex by J in
degree zero and S_N r in degree one. The actual source is transported
by the displayed operator, including every coefficient and shift.

At the root write T_0,M_0,J_0,r_0,S_0 for these operators. They are
F-linear on E or E^d. Set

    K=ker_E M_0, C=coker_E M_0, pi:E^d -> C.

The operator T_0 acts on K and C, with N-th power identity. There are
canonical F-linear isomorphisms

    J_0:ker_F P_0 -> K^(T_0),                       (1.2)
    kappa:coker_F P_0 -> C^(T_0),
    kappa([h])=pi(S_0 r_0 h)/N.                    (1.3)

Here scalar kernels and cokernels are taken for P_0:E->E as an
F-linear operator. Equation (1.2) is the usual exact companion
reconstruction, with no loss of the scalar section.

For (1.3), first (T_0-I)J_0=r_0P_0 shows that r_0 induces an
isomorphism coker P_0 -> coker_F(T_0-I). To prove surjectivity, use
the first d-1 rows of sigma-A to eliminate the first d-1 coordinates
of any inhomogeneous equation; the remaining coordinate is e_d h/a_d.
If e_d h/a_d=(sigma-A)v, those same rows force v=J_0 f, hence h=P_0 f.
Multiplication by A^(-1) gives precisely r_0.

For an arbitrary F-linear T_0 the remaining map is

    E^d/(T_0-I)E^d -> C^(T_0), [v] |-> pi(S_0v)/N.

It is onto by averaging a lift of an invariant class. It is injective
because S_0=N+(T_0-I)R(T_0) for a polynomial R: if
S_0v=M_0w, then

    v=(T_0-I)(S_0w-R(T_0)v)/N.

This proves the claimed source-cokernel identification, including its
normalizing factor N. It requires no semisimplicity of M_0.

## 2. The first normal map commutes with this source identification

Put Q=zeta(1+epsilon). For every Q-dependent operator write subscripts
0,1 for its constant and first epsilon coefficients. In particular

    P_1=sum_j (a_(j,1) sigma^j+j a_(j,0) sigma^j D),
    D=Y partial_Y.

In ambient A[Y] notation the same physical derivation is

    D=Y partial_Y+N U partial_U;                    (2.1)

it preserves Y^N-U. A derivative at fixed U cannot replace it.

Differentiate (1.1), restrict to f in ker P_0, and project to C.
The terms M_0 J_1 f and (S_Nr)_1P_0f disappear. Hence

    pi(M_1 J_0 f)=pi(S_0r_0P_1f).                  (2.2)

Consequently the canonical first quantum-normal operator of
[the monodromy construction](first_quantum_normal_connection.md) obeys

    D_N(J_0 f)=kappa([P_1 f])/N.                  (2.3)

This is an exact scalar-to-companion normal-source map. In particular,
if the supplied whole Q-germ has

    P(Q)f(Q)=epsilon h_1+O(epsilon^2),

then [P_1f_0]=[h_1] in coker P_0 and

    D_N(J_0f_0)=kappa([h_1])/N,
    s=S_0r_0h_1.                                 (2.4)

The actual off-root section is not assumed P-horizontal. Its first
coefficient f_1 is retained in P_0f_1+P_1f_0=h_1. The source class is
independent of changing f_1; the selected section and cut are not
replaced by this class alone.

For example the central derivative of the actual finite-sum lift
constructs h_1 in the cited first-normal note. Equations (2.3)--(2.4)
transport that actual source, rather than positing an abstract one.

There is also a useful scalar form of the connection symbol. Put
W_P=sum_j j a_(j,0)sigma^j. For f in ker P_0,

    kappa([W_P f])=iota(J_0 f),                    (2.5)

where iota:K->C is inclusion followed by quotient. To see this,
apply (2.3) to g(U)f and subtract g times the equation for f. Since
[P_1,g]=N U g'(U) W_P, comparison with the monodromy Leibniz rule
gives (2.5), for instance by taking g=U. Thus the correct scalar
symbol is the shift derivative W_P and not an assumed invertible
scalar. Jordan degeneracies remain visible in iota.

## 3. Keeping the actual source lattice and the companion cut

At the root put A_0=k[U,U^(-1)], B=k[Y,Y^(-1)] and use the lattice

    L=(1-Y)A_0[X], X=Y+Y^(-1),
    (U^2-1)B subset L subset B,

from [whole-source Newton transport](whole_source_newton_transport.md).
Actual reciprocity gives f_N=(1-Y)F_N in L, and an actual invariant
annihilator acts on L by the banded matrices proved there.

The map J_0 embeds L into the companion space by its literal shifted
coordinates. It need not embed it into a preselected regular power
lattice if a companion denominator vanishes at the cut. Keep the
fractional lattice J_0(L) and the source image S_0r_0(L), or retain the
undivided scalar complex. In particular, localization by a_d followed
by evaluation at U=1 is not an integral comparison theorem.

The original cut transfers without ambiguity to J_0(L):

    cut_comp(J_0f)=-[D(pr_0 J_0f)]_(Y=1)
                 =cut(f),                         (3.1)

because the first component of J_0f is exactly f. The derivative is
the physical one (2.1). This is a normal co-source, not evaluation
of the first component in the ambient reduced fiber.

More intrinsically, localize A_0 at w=U-1. Then wB subset L, and the
cut is a well-defined functional on the thickened module B/wL,

    ell_B([b])=-[Db]_(Y=1).                       (3.2)

It kills wL because every element of L vanishes at Y=1. The source
fiber L/wL injects into B/wL and (3.2) restricts to its actual cut.
This retains precisely the extra normal classes lost by B/wB.
The same construction in the first companion coordinate transports
this normal co-source through (1.1); no inverse of a vanishing
peripheral factor is used to define it.

There is a canonical Bockstein description. If f in L has zero
ambient fiber, write f=wb. The map

    ker(L/wL -> B/wB) -> (B/wB)/im(L/wL),
    [f] |-> [b]                                  (3.3)

is an isomorphism. Changing f by wL changes b by L. Surjectivity
uses wB subset L. On this kernel the marked cut is

    cut(f)=-N b(1).                               (3.4)

This is a normal-lattice source map, not an unproved invariant line
in the actual monodromy kernel.

## 4. The distinguished X=2 normal sector

On L/wL the characteristic and minimal polynomials of X are
C_N(x)-2, where C_N(Y+Y^(-1))=Y^N+Y^(-N). The root x=2 is simple
since C_N'(2)=N^2. Thus

    e_2(X)=(C_N(X)-2)/(N^2(X-2))                 (4.1)

is a canonical rank-one projector on this abstract fiber. The right
side is a polynomial. The cut satisfies ell X=2ell and ell(v_0)=1,
so ell e_2=ell and identifies this line with k.

Its literal generator before specialization is

    e_2(X)v_0
      =-Y(U-1)sum_(j=0)^(N-1)Y^j/(N^2 U).      (4.2)

It has zero ambient fiber. Its divided-normal value at Y=1 is -1/N,
so (3.4) gives cut=1. The selected sector therefore sits in the
normal defect, and disappears if L/wL is replaced by its ambient
image.

Over the completed central ring k[[w]], the marked branch Y=1
determines a canonical etale idempotent e_0 in Bhat. It satisfies

    e_0 Lhat=w e_0 Bhat.                          (4.3)

Indeed every source vanishes on this branch at w=0, and wBhat
is contained in Lhat. Thus this is a rank-one direct summand of
the completed source lattice; its fiber is the line (4.1).
The physical connection D/N preserves etale idempotents. On this
summand its logarithmic residue is +1, and dividing by w identifies
it with the regular trivial branch line. The cut is -N times the
constant coefficient in this divided-normal trivialization.

This supplies an exact local normal sector. It does not imply that
an actual annihilator, companion connection, or crossing transport
preserves it. Nor does it automatically extend to a rational line
over the whole central U-curve: the generic algebra B tensor F is
the field F(Y), Y^N=U, and has no nontrivial idempotents. The branch
projector becomes algebraic after the marked Kummer splitting cover
and exists canonically in the completion at U=1; cyclic deck shifts
permute those generic branches. Descent of one chosen branch is
additional data, rather than a consequence of its simple special
eigenvalue.

Already at N=3, writing zeta^2+zeta+1=0,

    ell(v_0)=1, ell(v_1)=3,
    S v_0=-zeta^2 v_0, S v_1=2zeta^2 v_1.

Therefore ell S is not a scalar multiple of ell. The cut is not
even a common quotient character of the full banded algebra.
Transport over the actual A-curve still requires a proved map of
the actual scalar/source complexes, not just this boundary projector.

## 5. The exact cyclic envelope has a parity defect

Let L_cyc=sum_(j=0)^(N-1) sigma^j L inside B. This is stable under
sigma. The exact result is

    N even: L_cyc=B,
    N odd:  L_cyc=sum_(j != j_0) A_0 Y^j
                    direct_sum (U-1)A_0Y^(j_0),
            j_0=(N+1)/2.                         (5.1)

Thus cyclic saturation is not always the ordinary power lattice.
For the proof use the Fourier projectors
E_j=(1/N)sum_l zeta^(-jl)sigma^l. Each character coefficient ideal
is generated by the coefficients of the v_n.

For 1<=j<=floor(N/2), the highest term -Y^j of v_(j-1) has no
other exponent congruent to j modulo N. It gives the unit generator.
For j>(N+1)/2 the lowest term Y^(j-N) of v_(N-j) does the same.
The constant character is present in v_0. These exhaust the even
case and all but j_0 in the odd case.

For N=2m+1 the highest and lowest terms of v_m are the only terms
with residue j_0=m+1; their coefficient is U^(-1)-1. Conversely
the congruence Jf=f modulo U^2-1 implies that the j_0 coefficient
of every f in L vanishes at U=1: the weighted reflection acts by
-1 on this character there. All its coefficients are therefore
divisible by U-1. This proves (5.1).

Neither enlargement makes the cut descend to an ordinary ambient
fiber: the row (3.2) still retains the normal direction. Bare sigma
does not preserve L, and the parity defect is an additional reason
to avoid assuming a cyclic invariant cut line.

## 6. What the construction reduces, and what remains

The actual scalar equation, its first-normal source and its cut now
have explicit maps to companion monodromy, with the exact cyclic
normalization (1.3), (2.3), and the normal co-source (3.1)--(3.4).
Thus an actual-to-geometric comparison may be checked directly on
these pointed two-term complexes. It is not necessary to guess a
global quantum connection or discard the source in order to make
that comparison.

The remaining issue is substantive: construct a geometric complex
and a map matching the actual scalar source class and this marked
normal row, including its integral lattice at U=1. No general
invariance of the X=2 sector, regulator identity, or selected norm
formula follows from boundary algebra alone.

[Exact audit](../experiments/audit_source_lattice_monodromy_chainmap.py).
[Results](../experiments/source_lattice_monodromy_chainmap_results.json).
