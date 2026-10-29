# Exact Newton twist equations, original source, and the parabolic Fricke graph

29 October 2026. The actual Newton crossing has a denominator-free finite
Weyl system. Its classical map is the genuine parabolic braid/Fricke map,
with the original four-plat cup and cap retained by an explicit matrix
intertwiner. Arbitrary rational words therefore have an actual complete-
meridian character gluing description without an unknown 6j frame.

The Newton clock is NOT the knot meridian or the Casimir eigenvalue.
This does not construct a generic-meridian A-curve or prove a sharp
asymptotic/survival theorem for all rational words. The exceptional cup
boundary and its normal source cannot be replaced by a regular torus
point. Those distinctions are made explicit below.

## 1. The exact kernel and its actual generic normalization

Use the [full Newton packet](actual_newton_turn_positive_gram.md):
q=exp(pi i/N), Q=q^2, d=N-1, kappa=q^(d^2/2). The actual full crossing
kernel is

    C_ij=kappa(-1)^i q^(i+j^2) [i choose j]_Q,
          0<=j<=i<=d;  C_ij=0 above the diagonal.         (1)

It is multiplication by the ORIGINAL checked R, including its common
Cartan, all Jordan derivatives, and the true q^(ij) half-clock phase.
The actual turn is the reversal P_rev and both original closures are
coordinate rows. None of these facts is an independent-eigenline model.

There is a useful analytic generic-q extension of(1), but its physical
scalar must remain. For zeta near q, put Q=zeta^2 and

    s_r^2(zeta)=(-1)^r zeta^[-r(r+1)](Q;Q)_r^2,
    c_j(zeta)=zeta^(2j+1)+zeta^(-2j-1),
    kappa(zeta)=zeta^(d^2/2).

The normalized Newton basis uses these s_r^2; multiplication by z is
the lower bidiagonal Z with diagonal c_j and subdiagonal

    b_j=Q^j+Q^(-j)-2.

The generic matrix (1) commutes with this Z by the same finite Gaussian
identities, and its diagonal is kappa nu_j, nu_j=(-1)^j zeta^[j(j+1)].
The literal generic highest-weight-d physical braiding, however, has
at the Casimir node c_a the highest-vector eigenvalue

    lambda_(d-a)=(-1)^(d-a)
                    zeta^[d^2/2-(d-a)(N+a)]
                =kappa gamma_N(zeta) nu_a,
    gamma_N(zeta)=(-1)^d zeta^(-Nd).                     (2)

Consequently its Newton matrix is gamma_N C, not just C. Generic
distinctness and equality of all nodal values prove the matrix identity;
regular specialization retains the full confluent polynomial. At the
root gamma_N(q)=1, but its normal derivatives are NONZERO. All q-normal
calculations must keep(2). This generic q deformation is not a deformation
of the knot meridian.

The inverse of the finite Gaussian kernel is also explicit:

    (C^-1)_ij=kappa^-1(-1)^i
                    q^[j^2-2ij-i] [i choose j]_Q.        (3)

This follows from the finite q-Pascal inverse and equals coefficient
conjugation of(1) at the original root. The physical generic inverse
has the additional scalar gamma_N^-1.

## 2. Finite Weyl equations, including the actual normal wall

Let X=Q^i,Y=Q^j on the kernel. Direct adjacent-factor cancellation gives

    (QX-Y) C_(i+1,j)=qY(1-QX)C_ij,
    (QY-1) C_(i,j+1)=q(X-Y)C_ij.                         (4)

These equations are CROSS-MULTIPLIED; they include the triangular
diagonal and its zero neighbors. One must not divide their vanishing
coefficients to change the support.

For the finite zero extension C_(N,j)=0, the first equation has the
explicit generic last-row current

    (QX-Y) C_(i+1,j)-qY(1-QX)C_ij
       =-qY(1-Q^N) delta_(i,d) C_(d,j).                  (5)

It vanishes at the root, but its first q-normal coefficient does not.
Multiplying by gamma_N preserves(4)--(5), with that scalar retained.
The backwards-j version is globally valid without another source:

    (Y-1)C_ij=q(X-Q^-1Y)C_(i,j-1), C_(i,-1)=0.          (6)

Together with triangular support and C_(i,0)=kappa(-q)^i, these are
finite pointed equations determining the actual kernel. They do not
identify an arbitrary cyclic-shift solution with the original one.

For strict forward shifts S f_i=f_(i+1), (6) gives the exact matrix
identity

    X C S=C Y S+q^-1 C(Y-I).                             (7)

The first equation similarly gives a cleared operator relation with
the wall(5). Inverting its factor S+q(1-QX) at the root is invalid:
that factor has a zero last diagonal entry. The finite source is part
of the operator identity, even when studying a regular classical chart.

## 3. The regular canonical graph and its preserved Casimir

For i/N=x,j/N=y in 0<y<x<1 the leading exponent of(1) is

    Phi(x,y)=J(x)-J(y)-J(x-y)+pi i(xy+x+1/2),
    J'(x)=log(2sin pi x).

The common Cartan produces the displayed pi i/2; the remaining known
subleading phase is retained in the finite kernel. Put

    X=exp(2pi i x), Y=exp(2pi i y),
    U=exp(Phi_x), V=exp(-Phi_y).

The negative sign in the INPUT momentum is essential for composing
kernel critical equations. Equations(4) give precisely

    X=Y+(Y-1)/V,  U=-Y(1+V),
    equivalently XV+U+1=0, Y(V+1)+U=0.                  (8)

It preserves dlog U wedge dlog X. Indeed 2pi i Phi is a generating
function with differential log U dlog X-log V dlog Y. The same graph
comes from the exact cleared equations, not merely a guessed phase.

The actual Newton multiplication-Casimir symbol is

    A(X,U)=X+X^-1+(X+X^-1-2)/U.                         (9)

Substitution in(8) proves A(output)=A(input). The turn has the exact
root clock relation P_rev X P_rev=Q^-1 X^-1 and interchanges strict
forward and backward shifts. Its principal graph is
(X,U)->(X^-1,U^-1). Thus the second trace symbol is

    B(X,U)=X+X^-1+(X+X^-1-2)U.

With {log X,log U}=-1, define the ordered third trace

    C(X,U)=(8-AB+{A,B})/2
          =2-(X-1)^2(U+1)^2/U.                          (10)

Direct algebra gives the ACTUAL parabolic Fricke equation

    A^2+B^2+C^2+ABC-8(A+B+C)+28=0.                      (11)

On these trace coordinates, the active point map(8) is

    (A,B,C)->(A,C,8-AC-B).                              (12)

The inverse occurs on observables: Ad(R) is pullback by the inverse
state map. Thus(12) agrees with the actual positive braid formula
Ad(R):(A,B,C)->(A,8-AB-C,B), rather than reversing a physical crossing
based on an isolated eigenphase.

## 4. Actual quantum trace matrices and original source matching

This graph has an exact physical source realization. In the already
audited three-head complete multiplicity basis let

    A_phys=Omega_12,
    B_phys e_j=c_j e_j+b_j e_(j-1).

A_phys is the original symmetric tridiagonal matrix with

    (A_phys)_jj=4qQ^j-q(1+Q)Q^(2j),
    (A_phys)_(j-1,j)=(A_phys)_(j,j-1)=-(1-Q^j)^2.         (13)

The actual R_23 is C^T, by multiplication functional calculus in the
upper-bidiagonal B_phys. Finite Gaussian cancellation gives the FULL
matrix identity

    R_23^-1 A_phys R_23=B_phys^T.                        (14)

For an entrywise proof substitute(1) transposed in
A_phys C^T=C^T B_phys^T. On the interior the needed three ratios are

    U_(i-1,j)/U_ij=q^(-2i+1)(1-Q^i)/(1-Q^(j-i+1)),
    U_(i+1,j)/U_ij=q^(2i+1)(1-Q^(j-i))/(1-Q^(i+1)),
    U_(i,j+1)/U_ij=-q(1-Q^(j+1))/(1-Q^(j-i+1)).

Cross multiplication proves the identity, including the adjacent zero
diagonal. The end terms vanish by b_0=b_N=0 and (1-Q^N)^2=0 at the
root. No nodal or semisimple substitution is used in(14).

Set the explicit source intertwiner

    S_source=P_rev R_23^-1.

Then EXACTLY

    S_source B_phys S_source^-1=Z_lower,
    S_source A_phys S_source^-1=Z_upper=Z_lower^T.        (15)

The original cup slide gives R_23^-1 p=N kappa^-1 e_d. Moreover
ell_i=x^i/N, x=q^d=-q^-1, and the finite q-binomial identity gives

    ell R_23=(kappa/N)e_0^T,
    S_source p=N kappa^-1 e_0,
    ell S_source^-1=(kappa/N)e_d^T.                      (16)

For the first formula the j-th component is
kappa(-q)^j/N times sum_i [j choose i]_Q(-1)^iQ^[i(i-1)/2],
namely kappa(-q)^j(1;Q)_j/N. It is zero for j>0. Thus the original
N and kappa factors cancel in the WHOLE marked four-plat scalar:

    ell W_phys p=e_d^T W_Newton e_0,
    W_Newton=S_source W_phys S_source^-1.                (17)

The original enhancement/framing line multiplies both sides unchanged.
In the complete four-head invariant reduction, physical generators1
and3 use A_phys and generator2 uses B_phys. Therefore they become
P_rev T_1 P_rev and T_1, respectively, with literal signed inverses.
This is a complete source-exact alphabet for ANY original four-plat
word, including all composite/even levels and all Casimir normals.
No unknown Racah eigenframe is present.

The exact quantum trace triple in these coordinates is
Z_lower,Z_upper, and the tridiagonal matrix(13). Expanding its band
entries gives the denominator-free quantum Fricke identities from
[the actual adjacent-trace theorem](actual_adjacent_twist_character_and_source.md)
with single/total Casimirs -2 and central coefficients8. In particular
it is the actual physical character slice, not an arbitrary surface
inferred only from(11). Equation(14), or its transpose, fixes the
braid orientation on the full matrices. At N=2 no division by
q+q^-1 is allowed; the same explicit matrix identities still hold.

## 5. The original cap is an exceptional curve, not a torus point

Both exact boundary vectors in(17) have the correct source eigencondition:

    Z_upper e_0=c_0 e_0,
    e_d^T Z_upper=c_d e_d^T=c_0 e_d^T.                   (18)

Consequently their reduced classical cap is B=2. The Fricke equation
then gives C=4-A on its reduced locus, but has a NONREDUCED normal
there. The exact finite source(16)--(18) retains that normal data.

Naively putting X=1 with finite nonzero U in(9)--(10) collapses all
three traces to2. It loses the real cup family. To retain a finite
free A!=2 one must resolve the actual corner by

    U ~ (X-1)^2/[X(A-2)] as X->1.

Then B->2 and C->4-A. Thus the correct cap is an exceptional divisor
of the Newton chart. It cannot be removed from an endpoint estimate
by calling it a regular stationary point on (C*)^2.

There is a direct group certificate on this cap. For z=A-2 use

    mu_1=-[[1,1],[0,1]], mu_2=-[[1,0],[z,1]],
    mu_3=mu_2^-1, mu_4=mu_1^-1.                         (19)

Their total product is identity, all meridian traces are -2, and
their trace triple is (A,2,4-A). For z!=0 it is irreducible. Actual
Hurwitz propagation of(19) gives the trace dynamics(12), with its
direction fixed by the finite conjugation identities. On an irreducible
four-punctured representation, a terminal cap trace2 forces the actual
inverse pair matrices: if their product were a nontrivial unipotent,
both meridian pairs would share its flag and the whole representation
would be reducible. This is the four-port case of
[the faithful cap certificate](actual_parabolic_cap_trace_certificate.md).

Thus any REGULAR irreducible intersection of the transported cap with
the closing cap is an actual representation of the ORIGINAL rational
word closure. This is global parabolic character gluing for arbitrary
rational words, not merely a formal cubic at each isolated crossing.
Reducible and escaping/normal intersections are not discarded, and
their source contributions require separate analytic control.

## 6. Exact limits of the statement

The Newton clock X is exp(2pi i times a NEWTON INDEX/N). The spectral
Casimir is the function(9), and the geometric eigenvalue w is obtained
only by solving w+w^-1=A. Neither is the physical meridian M.

This theorem fixes the actual COMPLETE-meridian slice M=1, with
meridian trace-2 and the original source framing. It does not create
the generic M-dependent quantum A-module. That requires the actual
meromorphic color/dual/turn family and its peripheral currents; the
generic q scalar(2) is not a substitute for that meridian deformation.
The older [actual-color Newton transform](newton_actual_source_canonical_transform.md)
uses different nodes Q^j+Q^-j and the knot's meridian variable. The two
Newton transforms must not be identified by their names.

The reversal identity is exact at the original root. Its actual
generic-q turn family need not be the same reversal matrix off the
root, so whole normal derivatives of a turned circuit must retain
that family. Likewise(5) is not deleted in a q-normal recurrence.

Finally actual character support and an explicit source alphabet do
not prove that the geometric branch is accessible, noncanceling, or
largest in the complete finite source. A sharp coherent action bound
and a nonzero full-source coefficient remain necessary. This result
provides the exact finite recurrence, actual braid graph and pointed
boundary data for that next analysis; it does not infer a new universal
volume equality from a principal curve alone.

## 7. Focused verification

[The new exact audit](../experiments/audit_actual_newton_twist_canonical_graph.py)
passes symbolic symplectic/Fricke/inverse-Hurwitz and resolved-cap group
identities; six generic physical families using the literal full-Cartan
universal R and its gamma_N scalar; and seven original root families
N=2,...,8. The latter include every finite Weyl boundary equation, the
physical three-head Hom action, all quantum Fricke relations/cubic,
the source intertwiner, and twenty-one full marked four-plat words
using all three physical braid generators. Finite-field arithmetic is
exact. These checks supplement the all-entry proofs and do not claim
an asymptotic or a meridian deformation from finite tests.
