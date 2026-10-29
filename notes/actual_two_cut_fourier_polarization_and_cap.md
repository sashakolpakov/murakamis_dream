# Whole Fourier polarization of the actual second cut

Research theorem, 27 October 2026. The second identity wire admits an
exact change of polarization over its WHOLE actual coefficient ring.
It preserves the original source, every peripheral factor, both endpoint
defects and normal derivatives. Its Fourier variable is independent of
the old physical edge position. A bounded-band Gaussian statement gives
a character incidence, rather than an identification of these two bases.

## 1. The actual tensor and its unchanged source

Use the literal two-cut tensor of
[the port reconstruction](actual_two_cut_framing_port_reconstruction.md),

    T_(c,d;a,b),  0<=a,b,c,d<N.

The original pivots, caps, crossing scalars, preferred peripheral lifts
and zero-framing line are already in T. Opening an internal identity
edge supplies no new pivot. Its original source is

    Phi(T)=(1/N) sum_(a,c,b) T_(c,b;a,b).                 (1.1)

Thus the first cut retains its actual rank-one row, including all first
output bands. The second cut is an identity closure. For charge-zero
uninserted/scalar-Green tensors c+d=a+b; (1.1) then also equals the
double-diagonal sum/N. Current tensors require (1.1), not that restricted
formula.

Let R be the actual ring localized at the differences Q^i-Q^j, i!=j,
for 0<=i,j<N. Every such difference is a unit at a primitive Q_N.
Retain all other actual parameters, including q with q^2=Q, M,
Q^N, M^N and the original peripheral rational maps/lattices. Put

    y_j=Q^j,   V_(j,b)=y_j^b.

The determinant is the usual product of y_j-y_i. Elementary polynomial
interpolation gives the exact inverse

    (V^-1)_(b,j)=[X^b] L_j(X),
    L_j(X)=product_(m!=j) (X-y_m)/(y_j-y_m).             (1.2)

This is an isomorphism of finite free R-modules before taking jets.
Define

    T^V=(I tensor V) T (I tensor V^-1).

Partial trace on the second wire proves EXACTLY

    sum_j T^V_(c,j;a,j)=sum_b T_(c,b;a,b),
    Phi(T^V)=Phi(T).                                   (1.3)

All actual matrix products, inserted Green observables and Hopf rows
are transported by this same conjugation. For example the actual
two-port coproduct is (I tensor V) Delta(h) (I tensor V^-1), with
the original ordering and prefixes. It is not replaced by a scalar
left/right action on a reshaped diagonal array. An internal wire
requires V and V^-1 on its two sides, so arbitrary word composition,
cups/caps and all existing closure factors are preserved.

For original source maps psi and phi on that wire, a general boundary
source is transported as V psi and phi V^-1. Here the identity closure
is invariant, which explains (1.3). This is a basis change of the actual
state and source, not the definition of a replacement state.

At the primitive root, character orthogonality gives

    (V^-1)_(b,j)=Q_N^(-bj)/N.                          (1.4)

The RAW new two-variable array retaining the first source is

    Jtilde_(a,j)=sum_c T^V_(c,j;a,j),
    Phi(T)=(1/N)sum_(a,j) Jtilde_(a,j).                (1.5)

For charge-zero T this becomes the exact full-band formula

    Jtilde_(a,j)=(1/N) sum_(b,q)
                     Q_N^(jq) T_(a-q,b+q;a,b).        (1.6)

Only physically supported terms occur, with zero extension otherwise.
The 1/N in (1.6) is the Fourier inverse; it does NOT replace the
original 1/N in (1.5). The entire finite band range is transformed
before any Gaussian expansion.

At Q_N, if one instead fixes c=a in T^V, charge conservation forces d=b in
the old tensor. Consequently T^V_(a,j;a,j)=(1/N)sum_b T_(a,b;a,b),
independent of j. The new momentum coordinate survives because the
first source is retained, rather than replaced by a diagonal trace.

## 2. Exact whole clock and shift operators, including endpoints

On the old head let B=diag(Q^b), J=diag(b), and

    U=sum_(b<N-1) E_(b+1,b),
    Uflat=sum_(b>0) E_(b-1,b).

These are truncated shifts; U^-1 is not notation for Uflat. Put

    C=V B V^-1,    Y=diag(y_j),
    u_j=y_j^N,     v^t=e_(N-1)^t V^-1,
    uminus_j=y_j^-1, w^t=e_0^t V^-1.

Direct evaluation of a polynomial at the N nodes proves

    C_(i,j)=delta_(j,i+1)                         if i<N-1,
    C_(N-1,j)=L_j(Q^N),

    V U V^-1=Y-u v^t,
    V Uflat V^-1=Y^-1-uminus w^t.                     (2.1)

For example (V U)_(j,b)=y_j^(b+1), except for its missing last
column. Subtracting that column gives the rank-one correction.
The backward identity removes the missing first column. At Q_N,
C is the cyclic backward shift, u is the all-ones column,
v_j=y_j/N, and w_j=1/N. The WHOLE last row in (2.1) must be
retained before normal differentiation.

For 1<=m<N the complete higher forward carry is

    V U^m V^-1=Y^m
       -sum_(b=N-m)^(N-1) (y_j^(b+m))_j e_b^t V^-1.  (2.2)

In particular the transform does not cyclically identify the original
finite head or its Green tails. The finite relative head/tail module
is carried along by the same isomorphism. Unwrapped tails are not
discarded or aliased by using (1.4); their exact independent-power
Fourier cap is recorded in
[the finite Fourier theorem](finite_band_fourier_cap_and_independent_clock.md).

The actual balanced finite matrices, as literal compressed matrices
for whole Q,M, are

    F=U(I-QB),
    Ecal=Uflat(M B^-1-M^-1 I),
    K=x B^-1,   x=-M/q.

Their exact transforms are

    F^V=Y(I-QC)-(1-Q^N)u v^t,
    Ecal^V=Y^-1(M C^-1-M^-1 I)
                         -(M-M^-1)uminus w^t,
    K^V=x C^-1.                                       (2.3)

Indeed v^t C=Q^(N-1)v^t and w^t C^-1=w^t. These identities
prove (2.3), including its signs. Thus the two actual endpoint
defects delta=1-Q^N and kappa=M-M^-1 remain distinct. At the
complete root both vanish, but

    D_Q[-delta u v^t]_(Q_N)=N u v^t,
    D_M[-kappa uminus w^t]_(M=1)=-2 uminus w^t.        (2.4)

Here D_Q=Q partial_Q and D_M=M partial_M with the other parameter
fixed. The simultaneous integral-color path must subsequently be
pulled back with its actual q/M relation. These normal terms cannot
be removed by specializing (2.3) prematurely.

Likewise

    C^N=V diag(Q^(Nb)) V^-1,
    C^N|_(Q_N)=I,
    D_Q(C^N)|_(Q_N)=N V J V^-1.                       (2.5)

The cyclic root value does not identify its whole normal clock.

## 3. The normal connection of this actual basis change

For fixed N, the matrix

    A_Q=(D_Q V)V^-1=J_eval (V J V^-1),
    J_eval=diag(j),                                   (3.1)

is regular at the primitive root. Differentiating an arbitrary
whole transported matrix gives

    D_Q T^V=(I tensor V)(D_Q T)(I tensor V^-1)
                                   +[I tensor A_Q,T^V].       (3.2)

Every normal jet follows by the product rule; the connection term
is forced. Partial trace of its commutator is zero entrywise on
the first wire, so it preserves the full original source also at
first normal order. Invariant functions or extra source-dependent
coupons must themselves be transported, rather than commuted past
V without their endpoint terms.

In the usual complex root metric V/sqrt(N) is unitary. Hence

    ||A_Q||_op <= (N-1)^2.                            (3.3)

This is a polynomial bound for the forced FIRST normal basis term,
not a bound for the actual entire knot state. Regularity holds in
a root-dependent neighborhood for each N. It does not produce a
single meromorphic family at the accumulation point Log Q=0.

The same statements hold with the original full ADO peripheral line

    d_N(M)=epsilon_N (M-M^-1)/(M^N-M^-N)

retained as its actual rational map/source lattice. Nothing here
replaces it by its complete value epsilon_N/N before derivatives.

## 4. Independent band and position variables before polarization

Write J^(p,q)_(a,b)=T_(a+p,b+q;a,b) and

    F(x,y;xi,eta)=sum J^(p,q)_(a,b) x^a y^b xi^p eta^q.

The coupling variables x,y generate position weights. The physical
input clock at the second cut is B=Q^b, while eta generates the
OUTPUT OFFSET q. Direct index identities give

    B_input:        y -> Qy,
    B_output:       (y,eta) -> (Qy,Qeta),
    q moment:       E_eta=eta partial_eta,
    Phi(T)=(1/N) CT_eta F(1,1;1,eta).                 (4.1)

These are different commuting coordinates before a polarization.
The last cap closes the band and leaves the physical b sum intact.
The finite root average and unwrapped alias corrections are exact
in [the independent-clock cap theorem](finite_band_fourier_cap_and_independent_clock.md).
Equations (1.2)--(1.6) instead change the actual wire basis: the
old physical b is summed internally, and j becomes an external
spectral coordinate. This is a source-preserving change of
polarization, rather than the substitution B=eta.

For a finite Laurent test h(eta)=sum h_n eta^n, its literal cap
coupon is

    X_h=sum_(n>=0) h_n U^n +sum_(n<0) h_n Uflat^(-n),

with unsupported shifts zero. Indeed CT selects q=-n, and
(X_h)_(b,b+q)=h_(-q). Thus CT h F is the original source with
X_h inserted on the identity wire. The Toeplitz coupon map is not
multiplicative at finite endpoints. Its original Ward row must be
retained. The actual negative-band moment calculation in
[the boundary-current note](actual_negative_band_boundary_moment_and_ward_atom.md)
gives explicit signed-crossing examples where this insertion is
nonzero although the uninserted source is zero.

## 5. Principal incidence and the first bounded-test correction

This section is a LOCAL formal Gaussian theorem with bounded band
tests. It is separate from the exact whole finite transform above.

Keep the old physical exterior positions (A,B) fixed. Use the actual
integral tree extension of the port-offset lattice in
[the port theorem](actual_two_cut_framing_port_reconstruction.md).
For charge-zero offsets (p,q)=(-q,q), let nu=Hq be the small
continuous boundary displacement. The resulting enlarged actual
phase and amplitude are S(u,nu), a_0(u,nu), with u transverse.
They come from those original coefficient atoms, including Cartan,
pivot and half-step terms. Work at a regular critical point with
S_u=0, invertible S_uu, and nonzero a_0. Let u(nu) be its formal
critical continuation and put

    W(nu)=S(u(nu),nu),
    A_0(nu)=a_0(u(nu),nu)/sqrt(det(-S_uu(u(nu),nu))),
    p_e=exp(W'(0)),
    alpha=(partial_nu log A_0)(0),
    beta=W''(0)/2.                                  (5.1)

The square-root line is the original fixed Gaussian line; its
constant choice cancels in the ratio. If a varying lattice measure
is needed, it is included in a_0. The chosen affine integral tree
coordinates have fixed measure. Formal stationary phase gives,
for EACH fixed q,

    Z_q/Z_0=p_e^q[1+H(q alpha+q^2 beta)+O(H^2)].      (5.2)

Proof: write the actual formal block as
exp(W(nu)/H) A_0(nu)[1+H z_1(nu)+O(H^2)] and substitute nu=Hq.
Taylor expansion gives (5.2). The first Gaussian correction z_1
cancels from this normalized ratio at order H; its difference
z_1(Hq)-z_1(0) first contributes at order H^2. All constant
base lines cancel too. This proof neither estimates a saddle
remainder nor sums q growing with N.

For an explicit contraction form let G=S_uu^-1, g=d_u log a_0,
ell=S_nu, and

    b^i=-G^(ij)g_j+(1/2)G^(il) S_(ljk)G^(jk).

Implicit differentiation and the determinant rule give exactly

    alpha=partial_nu log a_0+b^i ell_i
                                      -(1/2)G^(ij)ell_(ij),
    beta=(S_(nu nu)-ell_i G^(ij)ell_j)/2,            (5.3)

all evaluated at nu=0,u(0). This also derives (5.2) directly
with covariance -HG. Actual bounded changes of the chosen tree
particular solution translate u and give the same block ratios.
Flattening/period marks are held fixed; an N-dependent log-deck
move is not such a bounded translation.

Now interpret Delta(t)=sum_(q in Z)t^q as a FORMAL Laurent
distribution, paired only with finite Laurent tests. It is not
an ordinary function to evaluate at t=1. Equations (5.2) yield

    Zhat(eta)=Z_0{Delta(eta p_e)
       +H(alpha E_eta+beta E_eta^2)Delta(eta p_e)+O(H^2)}.

For every fixed Laurent polynomial h, finite coefficient extraction
therefore gives the rigorous bounded-test identity

    CT_eta h(eta) Zhat(eta)
      =Z_0{h(p_e^-1)
              +H{-alpha E_eta h+beta E_eta^2 h}_(eta=p_e^-1)
              +O(H^2)}.                            (5.4)

Each test uses only finitely many fixed bands, so the port theorem
and Gaussian contraction suffice. The principal Fourier incidence
is eta p_e=1. It does not eliminate the physical B coordinate.
For the ACTUAL identity cap h=1, the right side is Z_0 exactly,
including all corrections: only q=0 is extracted. The remaining
physical position sum and its original support/tails persist.
If beta!=0, (5.4) has a second derivative on test functions;
an ordinary coordinate substitution plus a scalar unit has only
a first derivative at this order and cannot reproduce this map.

The principal geometric chart eta_geo=p_e^-1 and its rational
boundary residues can still be studied. They are NOT images of
the original finite cap eta=0 merely by (5.2) or (5.4). In
particular [the exact first Gaussian calculation](figure_eight_first_loop_cap_residue.md)
is a calculation on that candidate geometric incidence boundary,
not a proof of the cap-cycle pushforward. A whole open-phase
Fourier stationary construction must use (1.2)--(1.6), its full
support and source before any local reduction.

## 6. Audit and scope

[The exact operator/source audit](../experiments/audit_actual_two_cut_fourier_polarization.py)
and [saved results](../experiments/actual_two_cut_fourier_polarization_results.json)
check generic/root Vandermonde inverse and carries, the forced
normal connection, both actual boundary terms, full source and
actual signed-braid tensors. The bounded-test formulas are
independently checked on quadratic non-diagonal Gaussian models.

This theorem supplies a genuine whole change of polarization of
the actual pointed finite state. It proves no global geometric
cycle comparison, no nonzero selected geometric block, and no
hyperbolic-volume limit. Those require transporting the actual
source through the remaining geometric/cyclotomic construction.
