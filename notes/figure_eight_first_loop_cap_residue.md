# The actual figure-eight first Gaussian correction retains a relative endpoint term

Research calculation, 27 October 2026. For the ACTUAL balanced
figure-eight coefficient model, use the two physical external
positions (a_0,a_2), not an arbitrary transverse slice. At the
framing slice s=1 the complete relative first Gaussian correction
is a nonconstant rational function z_1(r) over the exact Riley
field. It is holomorphic at BOTH candidate geometric boundary points
defined by eta_geo=p_e^(-1). All its
finite poles are projection caustics, and z_1(r)dr has an explicit
rational primitive. That primitive has nonzero marked endpoint
differences.
Here "first correction" means the coefficient of H AFTER the
leading determinant/Gaussian factor, as defined in (2.2).

These are exact statements about the actual transverse formal
block on this slice. They neither assert vanishing at every loop
or every s nor identify eta_geo with the independent Fourier cap
variable eta_F. The original CT_(eta_F) cap still leaves the physical
second-position sum intact. The exact distinction and an actual
whole source-preserving Fourier basis change are proved in
[the two-cut polarization note](actual_two_cut_fourier_polarization_and_cap.md).
A source-normalization guard for the
endpoint differences is retained in Section 6.

## 1. Actual critical field, source and two physical coordinates

Take the action-order braid

    (sigma_1,sigma_2^(-1),sigma_1,sigma_2^(-1)).

Put t=(1-sqrt(-3))/2, t^2-t+1=0. The original developed meridians
may be taken as

    A=[[1,1],[0,1]], B=[[1,0],[t,1]],
    C=A^(-1) B A B^(-1) A.

They are the exact fixed triple used in
[the original stationary calculation](actual_geometric_normal_period.md).
They agree with the newer prefix convention u=-t because
C=B A^(-1)B A B^(-1) in this field. The actual framing is
F(r,s)=[[r,1-r],[s,-s]]. Local Gauss states are reconstructed
from BOTH signed developed prefixes, with their actual signs.

Let k_1,...,k_4 be the original transfers. The exact integral
closure solver gives initial positions

    a_1=a_0-k_1+k_2-k_4,
    a_2=a_0+k_2-k_3.

Keep the two ACTUAL positions (a_0,a_2) external. The transverse
variables are (k_1,k_3,k_4), with

    k_2=a_2-a_0+k_3.                              (1.1)

This has determinant one on the original flow lattice. The
corresponding three transverse tangent columns in the original
five coordinates (a_0,k_1,k_2,k_3,k_4) are

    T=[(0,1,0,0,0),(0,0,1,1,0),(0,0,0,0,1)].

All following phase/amplitude derivatives use these columns.
Only AFTER those flow derivatives are formed do we evaluate the
critical point at s=1. No derivative in a fixed framing r slice
is substituted for a transverse flow derivative.

The original cut 1/N, full Cartan line, closed pivots, color
half-step x=-M exp(-H/2), writhe and fixed compact factor are
retained, with H=Log Q. The base-only line C_beta(H) is kept
separate, as in the original normal-period construction.

## 2. The actual first-loop formula is rational

Write the actual interior coefficient as

    C_beta(H) exp(S/H) a_0(u)[1+H a_1(u)+O(H^2)].

For a positive crossing its shape arguments are
(B,C,Y/A,BC,YC/A); for a negative one they are
(A,C,Y/B,AC,YC/B). Their phase signs are
epsilon=(1,1,1,-1,-1). The actual compact-factor equation gives

    [H]log P_Q(Q^alpha z)=B_2(alpha)Li_0(z)/2.

Here alpha is only 0 or 1 because Qx^2=Y. Both have coefficient
Li_0(z)/12. The variable first relative coefficient is therefore

    a_1=sum_(all20atoms) epsilon Li_0(z)/12.        (2.1)

No variable H term is lost from the Cartan/color monomials. Their
principal half-amplitudes are (log A+log B)/2 positively and
(log C-log A-log B)/2 negatively. Closed pivot gradients are
EXACTLY minus the two initial closed-position gradients.

The half-log coefficients of log(1-z) in log a_0 are, for either
ordered shape list,

    alpha=(-1,-1,1,1,-1)/2.

The squared amplitudes and exact half-step checks are those in
[the actual normal calculation](actual_geometric_normal_period.md),
not an independently chosen torsion density.

Let G=(S_perp'')^(-1), so the Gaussian covariance for exp(S/H)
is -HG. Direct Wick expansion gives the COMPLETE relative
correction

    z_1=a_1-(1/2)G_ij(a_0,ij/a_0)
      +(1/2)(a_0,l/a_0)S_ijk G_ij G_kl
      +(1/8)S_ijkl G_ij G_kl
      -(1/12)S_ijk S_lmn G_il G_jm G_kn
      -(1/8)S_ijk S_lmn G_ij G_lm G_kn.            (2.2)

The tensor sums are evaluated in Q(t)(r). For an atom with
integer transverse exponent vector v, its contributions are

    S_3: epsilon z/(1-z)^2 v^tensor3,
    S_4: epsilon z(1+z)/(1-z)^3 v^tensor4,
    grad log a_0: -alpha z/(1-z) v,
    Hess log a_0: -alpha z/(1-z)^2 v^tensor2.

The quadratic Cartan phase has no third or fourth derivative.
These formulas make (2.2) an EXACT rational calculation; no
dilogarithm evaluation or numerical differentiation is required.
The independent [Wick/atom audit](wick_first_loop_actual_atom_independent_audit.md)
checks every coefficient and the original normalization terms.

## 3. The complete correction and its actual projection caustics

At s=1 the signed physical prefix minors for the third initial
position are

    V(r)=2+t-tr^2,
    U(r)=4-t-(1+t)(r+r^2),
    k(r)=U(r)/V(r)=1/A_2.

Their Jacobian numerator is

    J(r)=U'V-UV'=(1-2t)r^2-2tr-(1+4t).           (3.1)

The exact result of (2.2) satisfies

    z_1(r)=P_10(r,t)/[216 J(r)^4],                (3.2)

where P_10 is the degree-ten polynomial recorded by the exact
artifact. Multiplication of the separately computed Wick result
by J^4 is checked to be polynomial; this is an identity of the
whole rational function, not an interpolation.

The only FINITE poles are the two physical projection caustics

    r_c1=2t-1=-sqrt(-3),
    r_c2=-(1+4t)/3=-1+2sqrt(-3)/3.

Both poles have order four, and both have zero SIMPLE residue.
The other displayed Gauss-chart denominators, including V=0,
cancel from the final z_1. There is also an order-two pole at
r=infinity. That compactification boundary must not be mislabeled
as a finite projection caustic.

For comparison, writing z_1=a(r)+t b(r) over Q(r), the denominator
factors are respectively

    216(r^2+3)^4(3r^2+6r+7)^4,
    108(r^2+3)^4(3r^2+6r+7)^4.

Their common quartic is Norm_(Q(t)/Q) J. The conjugate caustic
factor cancels when the two field components are combined, giving
(3.2). In particular z_1 is NOT constant in r.

## 4. Both candidate geometric boundary residues vanish exactly

The two k=1 points at s=1, labeled by the candidate geometric
incidence coordinate eta_geo=p_e^(-1), are

    r_cap0=-2, r_capinfinity=1-t.

Neither is a zero of J: its values are 3-8t and -5-3t. Thus the
COMPLETE z_1 is holomorphic at both geometric boundary points.
The eta_geo=p_e^(-1) coordinate has a nonzero local derivative at
the marked first point, by the exact prefix/Jacobian calculation in
[the identity-cap note](identity_cut_orientation_cover_and_marked_source.md).
Hence ordinary residues can be computed in r.

The bare density on this slice is

    Omega_cut=-dr wedge ds/[s(1+s)].

Therefore, with its original base-line multiplier retained,

    Res_(eta_geo=0)(Omega_cut z_1)=0,
    Res_(other geometric boundary)(Omega_cut z_1)=0.   (4.1)

This is stronger than a cancellation of a simple residue: the
total relative correction is regular there. Each of the six
separate Wick pieces in (2.2), however, has a DOUBLE pole at
r=-2. Their exact simple residues are recorded in the artifact;
they sum to zero, and their double-pole terms cancel as well.
Keeping only the compact factor or one contraction diagram would
give a wrong nonzero result.

The statement is on the explicit slice s=1. It has not been
extended by sampling to an identity for all s. It does not map the
original Fourier cap eta_F=0 to either displayed r point: bounded
band ratios supply a principal character incidence, not that
source/cycle pushforward.

## 5. A rational primitive gives an exact derivative certificate

There is no logarithmic Hermite residual. Define

    G(r)= (2-t)r^3/9+(7+t)r^2/9+(-167+454t)r/216
       +[(34960t-16932)r+(7004t-23476)]/(81J^3)
       +[(5228t+3356)r+(8022t-8974)]/(81J^2)
       -[(154t+214)r+(55t+697)]/(27J).             (5.1)

Then EXACTLY

    dG/dr=z_1(r).                                (5.2)

The script computes all twenty actual atoms, performs the Wick
contractions, solves the finite Hermite equations and checks the
zero rational-field residual of (5.2). Thus (5.1) is a reproducible
derivative certificate for the fixed whole first-loop formula.
Its poles have order three at the two caustics, and it is regular
at both cap points. A formal change r->r+H G(r) can absorb this
vertical density correction on this slice if its SOURCE is
transported too. It is not automatically an endpoint-preserving
change of the marked source.

## 6. Relative endpoints retain a nonzero first-loop datum

An additive constant in G fixes one endpoint, but not both. The
two cap points give

    G(1-t)-G(-2)=(889-125t)/216 !=0.               (6.1)

The actual classical centralizer step is r->r+s. On s=1, the
interval from -2 to -1 instead gives

    G(-1)-G(-2)=(1076-991t)/432 !=0.               (6.2)

These are DIFFERENT marked geometric endpoint comparisons. The
two geometric boundary points are not asserted to be the original
finite head endpoints or the image of the Fourier cap. Their quantum
endpoint/half-density/ordered-band adapter remains necessary.

There is also a normalization distinction. z_1 above excludes
the original base-only line C_beta(H). If its first unit coefficient
is kappa, the full relative coefficient is z_1+kappa. All residues
in (4.1) remain zero, but (6.1) changes by kappa(3-t), and (6.2)
changes by kappa. Thus the two numbers are given in the specified
variable-amplitude frame, not after silently resetting C_beta.
Their combination

    [G(1-t)-G(-2)]/(3-t)-[G(-1)-G(-2)]
                                      =(295t-138)/112 !=0       (6.3)

is unchanged by ANY such base-only first-order unit. Absolute
rational exactness and zero cap residues therefore do not remove
all relative endpoint data even at this first loop.

A finite connected algebraic cover preserving these endpoint marks
does not remove this particular relative datum. If pi is such a
cover and dG_tilde=pi^*(z_1 dr), then
d(G_tilde-G composed with pi)=0. In characteristic zero the
difference is constant on that connected curve, possibly after
its specified constant-field extension. Its endpoint differences
are therefore the SAME nonzero differences in (6.1)--(6.2).
For a base-only unit kappa the invariant (6.3) also stays nonzero.
This is a restriction on an endpoint-preserving primitive gauge;
it does not prohibit solving a source-corrected comparison on a
cover and descending the FULL relative object.

The calculation proves neither a global cancellation nor a nonzero
selected cap period. The principal eta identification is not an
all-order source comparison, and higher loops may have different
poles. The result instead isolates a concrete finite-order target:
the actual cap/current comparison must transport the primitive's
endpoint values and the full base line, rather than retain only
the vanishing absolute residue.

Reproduction: [exact computation](../experiments/compute_figure_eight_first_loop_cap.py)
with `--fast-exact`; [characteristic-zero result](../experiments/figure_eight_first_loop_cap_exact_results.json);
[two-place modular check](../experiments/figure_eight_first_loop_cap_modular_results.json).
