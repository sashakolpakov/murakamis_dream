# Exact radial compactification and sublevel transport of strict-Hall source cores

28 October 2026. For the ORIGINAL fixed-clock unit-factor source, every
strict-Hall core admits an explicit radial retraction which never increases
the modulus of its masterfunction. The retraction is piecewise monomial,
has uniformly bounded logarithmic differential, and puts every sublevel
cycle in a logarithmic box of radius O(log N). In addition, the complete
logarithmic metric gives a global horizontal-lift proof that ordinary
critical values are the ONLY nonzero finite bifurcation values of this
product masterfunction.

Consequently the original coefficient torus can actually be homotoped into
every sublevel above all its regular critical moduli. This is not yet the
polynomial-mass theorem: the horizontal flow in the bounded box need not
have a proved uniform complexity or Jacobian bound. The clocks are fixed
throughout. Their full coupled critical equations and the original volume
bound do not follow from this result.

## 1. The actual source and its strict cores

Let k>=2 and

    f(X)=gamma product_(e=1)^M(alpha_e X_(u_e)-beta_e X_(v_e))
                         / product_i X_i^(q_i),       (1)

where u_e!=v_e, |alpha_e|=|beta_e|=1, gamma!=0, q_i are integers,
and sum_i q_i=M. All original scalar, pivot and feedback factors which
have already been extracted remain in gamma or in the separate clock
weight. Loops are evaluated as their exact scalar monomials before (1).

For a nonempty proper anchor set I, let m_I count the factors internal to
I, C_I its crossing factors, and e_I=q(I)-m_I. Assume

    1<=e_I<=C_I-1 for EVERY such I.                 (2)

The source cut theorem gives exactly these strict inequalities in each
nontrivial residual SCC after tight cuts and forced factors are removed.
They imply C_I>=2 and M>=2. They concern endpoint support, not the
nonvanishing of the selected complex coefficient.

The function (1) is invariant under common complex scaling. We work on
the quotient torus T=(C*)^k/C*, using X_k=1 when a concrete coordinate
system is needed. Its original source is the positive generator

    I=(2*pi*i)^(-(k-1)) integral_(|X_1|=...=|X_(k-1)|=1)
                     f(X) dlog X_1 ... dlog X_(k-1).  (3)

The divisor f=0 is allowed in this coefficient cycle: the form in (3)
is holomorphic there. It is removed only when discussing horizontal
lifts over the nonzero base.

## 2. An exact OFF-critical cut derivative

Put rho_i=log|X_i|, r_i=|X_i|, and delta_i=S_i-2q_i, where S_i counts
the incident linear factors. At any point with f!=0,

    partial_(rho_i) log|f|
      =delta_i/2 + (1/2) sum_(e incident i)
                 (r_i^2-r_j^2)/|alpha_e X_i-beta_e X_j|^2.  (4)

The sign in the numerator always uses i as the first endpoint, irrespective
of the displayed orientation of the factor. This follows from

    Re[a/(a-b)]=(1+(|a|^2-|b|^2)/|a-b|^2)/2.

Suppose every radius in I is at least exp(g) times every radius outside I,
where g>0. Internal edge terms cancel after summing (4). Also

    (r_i^2-r_j^2)/|alpha_e X_i-beta_e X_j|^2
                      >=(r_i-r_j)/(r_i+r_j)>=tanh(g/2).

Since delta(I)=C_I-2e_I, the exact high-cut direction
V_I=sum_(i in I) X_i partial_(X_i) satisfies

    Re[(V_I f)/f]
      >=(C_I-2e_I+C_I tanh(g/2))/2.               (5)

In particular, for L=log M, (2) gives the uniform quantitative bound

    g>=L  ==>  Re[(V_I f)/f]>=1/(M+1).           (6)

Indeed tanh(L/2)=(M-1)/(M+1), so the right side of (5) is
C_I M/(M+1)-e_I >=1-C_I/(M+1)>=1/(M+1).
This is an identity and inequality away from the zero divisor, not an
evaluation of the critical equations alone.

## 3. Explicit simultaneous gap clipping

Order the logarithmic radii rho_(s1)<=...<=rho_(sk), and let
g_j=rho_(s(j+1))-rho_(sj). Replace each g_j by min(g_j,L), preserving
all arguments. Reconstruct the radii from these new adjacent gaps and
then divide all coordinates by their kth coordinate to restore X_k=1.
Call the resulting map C:T->T. The reconstruction is independent of
the choices among equal radii, so C is continuous across order walls.

A semialgebraic homotopy is obtained by interpolating the RADIUS RATIOS,
not by using arbitrary real powers. For R_j=exp(g_j), set

    R_j(s)=(1-s)R_j+s min(R_j,M), 0<=s<=1.        (7)

Reconstruct as above to obtain C_s, with C_0=identity and C_1=C.
Every changing gap stays at least L. Its derivative is nonpositive,
and changing gap j is exactly translation in the high-cut direction
I_j={s(j+1),...,sk}, modulo common scaling. Therefore (6) implies

    d/ds log|f(C_s X)|<=0,
    |f(C_s X)|<=|f(X)|.                          (8)

At a zero of f, a zero factor has equal endpoint radii and equal phased
arguments. Its endpoints remain at equal radii throughout (7), so that
factor stays zero. Thus (8) extends across f=0 by continuity.
Conversely no new zero factor is created: an originally positive radius
gap remains positive because L>0, and arguments never change. The same
homotopy therefore preserves the arrangement complement as well.

Every output gap is at most L. Hence

    max_i log|C(X)_i|-min_i log|C(X)_i|
                               <=(k-1)log M.     (9)

The map fixes this clipped region pointwise. It is thus a genuine strong
deformation retraction of EVERY sublevel {|f|<=R} onto its intersection
with the compact projective box (9). In the X_k=1 gauge, all log radii
then have absolute value at most (k-1)log M.

The endpoint map C is piecewise monomial in the positive radii. The
pieces are indexed only by the k! orders and 2^(k-1) clipped-gap choices.
On each piece, its logarithmic radial differential has integer entries
bounded by 2; the argument map is the identity. Thus, in the standard
Euclidean metric on (rho_1,...,rho_(k-1),theta_1,...,theta_(k-1)), its
Lipschitz constant is at most 4k. The same bound holds throughout (7):
the derivative of log R_j(s) with respect to log R_j lies in [0,1].

In particular, clipping increases Euclidean logarithmic (k-1)-mass by
at most (4k)^(k-1). This statement uses the full real logarithmic metric;
it does NOT claim such a comparison with only the absolute holomorphic
wedge |dlog X_1 wedge ... wedge dlog X_(k-1)|, which can vanish on a real
tangent plane before a nonholomorphic map is applied.

Using auxiliary positive r_i with r_i^2=X_i conjugate(X_i), the maps C
and C_s have semialgebraic graphs of degree bounded solely in k on each
piece (the coefficient M is retained). Images of chains whose algebraic
support degrees and multiplicities are polynomial in N therefore still
have polynomial support complexity after clipping. No such complexity
claim for the INTERIOR horizontal flow is inferred here.

## 4. Complete horizontal lifts: no hidden finite escape

Give T its complete flat logarithmic metric. Let J be a compact subset
of C* disjoint from all regular critical values of f. Write

    l_i=(X_i partial_(X_i) f)/f.

Their sum is zero by homogeneity, so they define the logarithmic
cotangent vector on the quotient. Outside the box (9), there is an
adjacent gap greater than L. Equation (6) implies

    ||dlog f|| >=c_k/(M+1).                       (10)

Here one may take c_k=1/(2sqrt(k)), a conservative quotient-coordinate
constant. Inside the box, the set f^(-1)(J) is compact. A factor cannot
approach zero there while f stays in J: the denominator is bounded
away from zero, all other factors are bounded, and J stays away from
zero. There is also no ordinary critical point there by the choice of
J. Thus ||dlog f|| has a positive minimum on this compact set.

For a piecewise C^1 base path w(t) in J, the standard logarithmic
Hermitian dual gives the explicit horizontal vector field

    dZ/dt=(w'(t)/w(t)) conjugate(l(Z))/||l(Z)||^2,  (11)

in any orthonormal logarithmic quotient coordinates. Its defining
identity is dlog f/dt=w'/w. Its norm is bounded on f^(-1)(J), by (10)
outside and the compact positive minimum inside. Local uniqueness and
completeness of the logarithmic metric therefore extend its flow for
the whole finite path time. Indeed a bounded-speed finite-time path is
Cauchy at a hypothetical endpoint; its limit remains in T, and f stays
in J, so the ordinary local ODE existence theorem extends it.

The same argument applies to every initial point, with smooth dependence
on it and on the base path. Lifting a short base contraction and its
reverse gives a local smooth trivialization over J. No finite nonzero
bifurcation values occur outside the ordinary critical-value set. The
outside bound (10) is uniform in N; the compact INSIDE minimum is only
proved positive at each fixed N and has no polynomial lower bound here.

## 5. An actual homologous sublevel cycle for the original source

There are finitely many regular critical VALUES. The critical locus is
algebraic with finitely many irreducible components, and f is constant
on each connected component of its regular critical locus. Put

    Mcrit=max_regular_critical |f|,

using zero if that set is empty. Fix R>Mcrit. Over |w|>=R the horizontal
lift (11) is complete on every finite closed radial base interval.
Choose a smooth radial base homotopy which fixes |w|<=R and moves each
point with |w|>R toward modulus R (or toward R+epsilon, followed by a
limit). Lifting it wherever |f|>R and using identity elsewhere yields
a deformation of T into {|f|<=R+epsilon}; the cutoff can be chosen so
that it is the identity at the joining level. Only the compact range
of |f| on the original coefficient torus is needed for its transported
cycle, so there is no assertion of a uniform infinite-time lift.

This produces a cycle Gamma_(R,epsilon) homologous in T to the ORIGINAL
torus (3), with |f|<=R+epsilon. Compose it with the explicit clipping
map C to put it in (9), preserving that sublevel and its homology class.
The holomorphic coefficient form is closed on all of T, so its integral
over the resulting cycle is exactly I, including its original scalar.

This is a global existence theorem for the required sublevel homotopy,
not a selection theorem for any individual critical point. It improves
the earlier sufficient macrodeficit condition e_Z>B: strict Hall support
alone gives the needed complete logarithmic lift for these PRODUCT
masterfunctions. It does not assert that every critical stratum of an
arbitrary compactification is regular; a topological horizontal lift on
T is the exact conclusion needed here.

## 6. The quantitative step which this proof does NOT supply

The endpoint clipping has fixed-dimensional semialgebraic complexity
and bounded logarithmic mass distortion. The preceding interior
horizontal flow need not be semialgebraic, and no uniform bound for its
Jacobian or for the multiplicities of a replacement algebraic chain
has been proved. Thus it is not yet valid to combine cycle existence
with the earlier polynomial logarithmic-mass lemma and announce

    |I|<=poly(N) Mcrit.

Effective triangulation of the sublevel SET alone would not prove that
bound either: one must control a representative of the particular
original integral homology class, including its coefficients. The
present proof isolates that remaining mass/complexity issue inside an
explicit compact logarithmic box, rather than leaving radius escape
or asymptotic bifurcation as additional hypotheses.

For the knot problem, every claim above still fixes the integer clocks.
Their exact feedback, factorial weights and original finite source must
remain when constructing the full phase cycle. Neither full critical
Hurwitz support nor a general-knot exponential upper bound follows by
taking absolute values over these fixed-clock cores.

[Audit](../experiments/audit_actual_anchor_sublevel_radial_transport.py):
actual source residual cores, exact off-critical cut derivatives,
strict-Hall bounds, modulus-monotone simultaneous gap clipping, and
horizontal right-inverse identities. The audit supplements the uniform
proof; it does not estimate the unresolved interior flow mass.
