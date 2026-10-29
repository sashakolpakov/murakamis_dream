# The actual crossing comparison retains a nontrivial normal insertion

Research proof, 27 October 2026. The full actual balanced crossing
can be compared coefficientwise between the q-normal integral color
and the aligned fixed-root meridian color. Away from nonzero sine
walls every aligned zero factor differs by an explicit bounded
holomorphic unit. The resulting crossing ratio is nonetheless not
a diagonal source/cut coboundary. It has a nonconstant finite normal
insertion, and the periodic boundary zeros and Frobenius centers
give further exact obstructions to a global fixed-fiber comparison.

This follows the actual finite formulas in
[the common-Verma construction](common_verma_two_wall_source.md),
not a replacement quantum dilogarithm. The scalar Gamma comparison
in [the whole frame profile](whole_gamma_frame_profile.md) remains
valid; it does not by itself intertwine the complete crossing.

## 1. The two actual colors and their full scalar conventions

Put c=2pi*i, n=N-1, and choose b in a fixed complex compact set.
Set

    H_0=c/N, H=H_0/(1-b/N),
    q=exp(H/2), q_0=exp(H_0/2),
    M=exp(Hb/2)=-q^N,
    M_0=exp(H_0b/2),
    x=-M/q, x_0=-M_0/q_0.                               (1.1)

The first head is the genuine integral-color quotient, with highest
weight alpha=n. The second head is the actual fixed-root nilpotent
color, with marked highest weight alpha_0=n+b. Both have the same
shifted interior E zero j=b. Their other boundary conditions differ.

The logarithms are fixed by

    Log x=c/2+H(b-1)/2=Hn/2,
    Log x_0=c/2+H_0(b-1)/2=H_0(n+b)/2.                  (1.2)

Hence x/x_0=exp[(H-H_0)(b-1)/2], without an unrecorded phase.
The common full positive Cartan factor and its negative inverse are

    C(H,alpha)=exp(H alpha^2/4).

For the raw full positive crossing their ratio is exactly

    C(H,n)/C(H_0,n+b)
         =exp[(Hn^2-H_0(n+b)^2)/4]
         ->exp(-cb/4).                                  (1.3)

That finite factor is retained. The specified auxiliary twist is

    theta(H,alpha)=exp[H(alpha^2/4-n alpha/2)],

because its stripped version is x^(-n). Thus the positive
zero-framing-normalized crossing is x^n R_+^0; the negative one
is x^(-n)R_-^0. The ratio of the full Cartan factors divided by
their matching twist ratio is precisely (x/x_0)^n=1+O(1/N).
No scalar in (1.3) is discarded; its cancellation uses that twist.

If the first side is closed with the ordinary integral-color twist
and pivot rather than the literal auxiliary ones, the exact route
adapter in the divided-color/source notes must be retained as well.
The two conventions are not identified by a basis change.

## 2. Literal positive and negative coefficients

Write P_H(s)=1-exp(Hs), and let i,j be the incoming indices.
For the positive checked crossing the output is (j+k,i-k), with
0<=k<=min(i,n-j). Its actual stripped coefficient is

    r_+^0(H,b;i,j,k)
      =(-1)^k x^(-i-j-k)
         exp{H[ij+(i-j)k-k(k+1)/2]}
         product_(r=1)^k P_H(j+r)/P_H(r)
         product_(r=0)^(k-1)P_H(b-i+r).                  (2.1)

For the negative crossing the output is (j-k,i+k), with
0<=k<=min(j,n-i), and

    r_-^0(H,b;i,j,k)
      =x^(i+j-k)exp(-Hij)
         product_(r=1)^k P_H(i+r)/P_H(r)
         product_(r=0)^(k-1)P_H(b-j+r).                  (2.2)

The Gaussian coefficients in the common-Verma formula are written
as finite products here. Their apparent denominators are units
at every displayed r<N, or cancel in the original polynomial
Gaussian. Full crossings multiply (2.1) by C(H,n), and (2.2)
by its inverse, with alpha_0 used on the root side. The original
Cartan half-character remains marked.

## 3. An exact holomorphic unit through every aligned zero

Let J(z)=2sinh(z/2)/z, J(0)=1, and DeltaH=H-H_0. The elementary
ratio has its exact removable form

    U_N(s)=P_H(s)/P_(H_0)(s)
          =(H/H_0)exp(DeltaH*s/2)J(Hs)/J(H_0s),
    U_N(0)=H/H_0.                                       (3.1)

It is an explicitly defined unit through the common zero s=0;
no division of two zero coefficients is needed. On any fixed
strip |Re(s/N)|<=1-delta, with bounded Im s and bounded b,
all J arguments avoid their nonzero zeros for sufficiently large
N. Both U_N and its inverse are holomorphic and uniformly bounded.

Define

    A_+=ij+(i-j)k-k(k+1)/2-(b-1)(i+j+k)/2,
    A_-=-ij+(b-1)(i+j-k)/2.

The exact continued coefficient ratios are

    r_+^0(H)=Z_+ r_+^0(H_0),
    Z_+=exp(DeltaH*A_+)
        product_(r=1)^k U_N(j+r)/U_N(r)
        product_(r=0)^(k-1)U_N(b-i+r),

    r_-^0(H)=Z_- r_-^0(H_0),
    Z_-=exp(DeltaH*A_-)
        product_(r=1)^k U_N(i+r)/U_N(r)
        product_(r=0)^(k-1)U_N(b-j+r).                   (3.2)

These are equalities of holomorphic coefficients even where the
shared P_H(b-i+r) or P_H(b-j+r) factor is zero. Under the stated
sine-safe strip condition, Z_+ and Z_- and their inverses are
bounded uniformly in N. There are O(N) factors, but the logarithm
of each U_N factor is O(1/N), not O(1).

There is a finite one-index factorial form which makes the
potential diagonal pieces visible. Put

    G_l=product_(r=1)^l U_N(r),
    L_l=product_(r=1)^l U_N(b-r).

Then

    Z_+=exp(DeltaH*A_+) L_i/L_(i-k)
                               *G_(j+k)/(G_j G_k),
    Z_-=exp(DeltaH*A_-) L_j/L_(j-k)
                               *G_(i+k)/(G_i G_k).       (3.3)

The remaining transfer factorial G_k and Gaussian factor belong
to the crossing. They are not removed merely by identifying a
scalar half-adapter on one color.

## 4. The geometric bulk limit is a finite normal insertion

Let u=i/N, v=j/N, t=k/N, and assume a compact sine-safe flow
region. For example on the positive crossing take
i/N<=1-delta and (j+k)/N<=1-delta; on the negative take
j/N<=1-delta and (i+k)/N<=1-delta. Aligned zeros at the origin
remain allowed by (3.1).

Define the holomorphic removable function

    h(y)=cy exp(cy)/(exp(cy)-1), h(0)=1.                  (4.1)

Uniformly on such regions and compact b-sets,

    Log Z_+=b I_+(u,v,t)+O(1/N),
    I_+=c[uv+(u-v)t-t^2/2]
       +integral_0^t[h(v+x)-h(x)+h(-u+x)]dx,

    Log Z_-=b I_-(u,v,t)+O(1/N),
    I_-=-cuv
       +integral_0^t[h(u+x)-h(x)+h(-v+x)]dx.              (4.2)

The logarithms are the ones furnished by (3.1)--(3.2), rather
than arbitrary logarithms of the final coefficient. They remain
defined through the aligned coefficient zeros. The auxiliary
zero-framing scalar ratio is 1+O(1/N), so has the same bulk limit.
The raw full Cartan factor adds the explicitly specified term
-cb/4 positively, +cb/4 negatively.

Proof: DeltaH=cb/N^2+O(N^-3). On the relevant strips, Taylor
expansion of (3.1) gives

    Log U_N(Ny+O(1))=(b/N)h(y)+O(N^-2).                 (4.3)

The expression is uniform at y=0 by the removable formula.
Riemann summation in (3.2), followed by the elementary quadratic
limits A_+/N^2 and A_-/N^2, proves (4.2). Thus the ratio is an
O(1) normal transport insertion. It does not alter the common
N-leading local action.

There is an action interpretation with all branches retained.
If the actual leading local coefficient is exp(S(x,y,z)/H),
with x=Hi,y=Hj,z=Hk, differentiation at fixed integer indices
gives precisely

    b I=(b/c)[-S+xS_x+yS_y+zS_z].                       (4.4)

Equivalently I=c partial_s[S(su,sv,st)/s]_(s=c).
The constant/linear lift terms are the ones of the actual
coefficient, not freely chosen phases. Passing from this local
identity to a closed stationary network requires its original
cut, pivots, twists and source: their Euler terms must be
included. It does not by itself select a finite geometric cycle.

## 5. A diagonal Gamma or cut coboundary cannot remove the insertion

There is an exact test independent of asymptotics. At k=0,i=j
the positive checked crossing has the diagonal entry (i,i)->(i,i).
Its continued auxiliary-normalized ratio is

    exp{DeltaH[i^2-(b-1)i+n(b-1)/2]}.                    (5.1)

Every diagonal similarity leaves every such diagonal entry
unchanged. Multiplying by an external scalar cannot fix the
problem: for two different i values their ratio is

    exp{DeltaH(i_1-i_2)(i_1+i_2-b+1)},                   (5.2)

which is generically nontrivial. At distinct bulk values u_1,u_2,
it tends exp[cb(u_1^2-u_2^2)]. This applies to arbitrary diagonal
leg or pair gauges, including the retained Gamma/frame factors.

Therefore a comparison of this same-fiber type is not a pure
diagonal/cut coboundary. A non-diagonal or base/normal/Fock
transport is not ruled out by this test; it must account for
the actual surviving insertion. Separate spectral multiplicity
tests can obstruct even a non-diagonal fixed-fiber similarity.

## 6. Periodic boundary zeros and the Frobenius center also differ

The bounded-unit statement cannot be extended over nonzero sine
walls. Take b=-1, H=c/(N+1), and the positive entry i=n,j=0,k=1.
At the fixed root its Pochhammer factor is

    P_(H_0)(b-i)=P_(H_0)(-N)=0.

On the integral-color side the corresponding factor is
1-exp[-cN/(N+1)]!=0; all its other factors are units. Hence the
root coefficient vanishes while the moving-q coefficient does not.
These are periodic root aliases, not the aligned s=0 zero treated
by (3.1). On this same example Ecal has different ranks on the
two heads, so no regular color-module intertwiner can identify them.
This does not say that their selected knot scalars disagree;
ordinary-color subquotients can kill the extra directions.

There is also a generic root-central-power residual. Let
gamma=(-1)^(N-1).
On the moving-q head,

    (K_H^N)_i=gamma exp[Hb(n/2-i)],

whereas on the fixed-root meridian head,

    K_0^N=gamma exp(cb/2) I.                              (6.1)

Their eigenvalue ratio is exactly

    exp[Hb((b-1)/2-i)] -> exp(-cbu).                      (6.2)

Thus the moving-q central power retains the bulk clock and is
not a scalar Frobenius character on that normal family. An
extension must transport this center/base or a genuine normal
source sector; the scalar Gamma half-line is not the whole module.
The moving-q power K_H^N is not asserted central away from the
root; it is the continuation of the root-central generator whose
non-scalar operator is being compared.

## 7. Meaning of the result

Equations (2.1)--(3.3) are finite whole-source formulas with
aligned zero divisors and full scalar conventions. Equation
(4.2) gives their uniform bulk insertion. Equations (5.1)--(6.2)
show concretely what remains after scalar/frame normalization.
The result holds for every allowed crossing, independent of
which knot braid later composes it.

The whole-knot Euler cancellation and its geometric normal action
are proved with the actual closure and source adapter in
[the closed bulk-response theorem](quantum_normal_crossing_bulk_response.md).
Its marked geometric transverse block has multiplier exp(-a S_geo/c),
with the preferred regulator action and all original base factors
retained. This is a formal calculation on the marked geometric branch,
not a proof
that the original finite cycle has that branch coefficient.

The [full-head Gamma source transport](full_head_gamma_source_transport.md)
also repairs the naive upper-half scalar source by its actual Weyl
complement. It does not remove the crossing periodic-wall example
or the Frobenius clock residual in Section 6. Thus the entry
comparison still does not control those sectors or the selected
trace norm. Those are precisely the sectors lost
by treating an interior bounded unit as a global quantum-source
isomorphism.

The independent [whole checked-crossing spectrum calculation](crossing_normal_spectra_obstruction.md)
strengthens the fixed-fiber obstruction: its generic channel
multiplicities differ for every N, excluding even a nondiagonal
similarity up to a scalar. This leaves relative source and base
transport open rather than identifying the two full crossings.

The [exact audit](../experiments/audit_actual_crossing_q_normal_meridian_ratio.py)
checks both finite ratios, aligned zeros, full Cartan/twist
cancellation, diagonal obstruction, periodic-wall rank example,
central powers and the uniform bulk normal insertion.
