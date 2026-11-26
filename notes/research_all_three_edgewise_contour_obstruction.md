# Why a full wire contour cannot be treated one edge at a time

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

The local adapted contour in the
[network phase theorem](research_unsummed_network_phase_coercivity.md)
exists at every regular positive geometric point. It does not follow
that the original full wire cycle can be moved there with a smaller
remainder. On long paths whose selected powers are all three, that
edgewise assertion fails at all but a bounded number of internal
edges. At the same time, the leading endpoint factors responsible
for its failure cancel exactly when adjacent edges are contracted.
This identifies a collective source calculation that cannot be
replaced by individual bare-kernel estimates.

No numerical search or new geometric existence assumption is used.
The argument strengthens the finite-path consequence of the proved
[power-three bare-kernel obstruction](research_bare_kernel_power_three_obstruction.md),
using its uniform energy bound.

## 1. The original paths and the endpoint-dominance region

Let \(\Gamma_m\) be the original path with \(m\) selected vertices,
all of power three, and a complete outside vertex at each end.
Its positive unit-charge solution exists by the
[integer corridor theorem](research_negative_corridor_variational_bounds.md),
after mirroring. Retain all original primitive curves and carriers.
Write its actual selected angles as \(t_{v,m}\).

The homogeneous reference point \(t_*=a-iH\) is fixed by
\[
 \cos t_*=-\frac14+\frac{3\sqrt3}{4}i,\qquad
 \frac\pi2<a<\frac{2\pi}3,\quad H>1.
 \tag{1}
\]
It satisfies the full original degree-two equation
\[
                3t_*+4i\operatorname{arsinh}(\sin(t_*/2))
                         =2\pi.
 \tag{2}
\]
The original edge geometry is positive at this point.

Put \(D=N-1\) and retain the full same-index kernel
\[
             K_N(z,w)=\sum_{j=0}^{D}e_j(z)e_j(w),
                 \qquad z(t)=-2\cos t.
 \tag{3}
\]
The bare-kernel theorem supplies a fixed product neighborhood of
\((t_*,t_*)\) on which
\[
 K_N(z(t),z(r))
       =e_D(z(t))e_D(z(r))(1+O(N^{-4})),
 \tag{4}
\]
uniformly at both parities, with every fixed derivative.
For a sufficiently small compact neighborhood \(U\) of this point,
there is a fixed \(\eta>0\) such that
\[
 -\Im t-\Im r\ge\Re\psi(t,r)+\eta
                         \quad((t,r)\in U).
 \tag{5}
\]
The strict inequality at the center is proved there by the absolute
volume identity, and hence persists after shrinking \(U\).
All constants in (4)--(5) are independent of \(m\).

## 2. The obstruction occurs on all but a bounded number of edges

For an edge, let \(X_e\in\mathbb R^4\) be its two square-coordinate
pairs
\((A_P,y_P,A_Q,y_Q)\). Let \(X_*\) be the fixed reference pair
at \((t_*,t_*)\), using the same orientation on every path edge.
The convex-energy argument in Section 4 of the bare-kernel note
proves
\[
             \sum_{e\in E(\Gamma_m)}
                      \|X_{e,m}-X_*\|^2\le C
 \tag{6}
\]
with \(C\) independent of \(m\). It includes the two attaching
edges. The reference violates only the complete outside values;
correcting those two ends costs bounded energy, which is why the
right side does not grow with the path.

**Proposition 1.** There is an integer \(B\), independent of \(m\),
such that all but at most \(B\) of the \(m-1\) internal edges have
their actual angle pair in \(U\).

**Proof.** The inverse square-coordinate map is smooth near the
fixed interior reference. Choose \(\varepsilon>0\) so that
\(\|X_e-X_*\|<\varepsilon\) implies that its two recovered angles
belong to \(U\). Every edge failing this implication contributes
at least \(\varepsilon^2\) to (6). Thus there are at most
\(\lfloor C/\varepsilon^2\rfloor\) such edges. The actual angle
pair outside \(U\) is among these. \(\square\)

Consequently the fraction of internal edges satisfying (4)--(5)
tends to one as \(m\) grows. This is a statement about the sequence
of actual finite positive fillings. For each fixed path, the quantum
limit below still takes \(N\) to infinity with \(m\) fixed.

## 3. A lower bound for the omitted part of any edgewise deformation

The exact last Newton polynomial is
\[
 e_D(z)=\frac{(-1)^D P_N(z)}{N^2(z-c_0)},\qquad
 P_N(z)=2T_N(z/2)+2,\quad c_0=2\cos(\pi/N).
 \tag{7}
\]
On the compact neighborhood \(U\), the growing exponential in
\(P_N(-2\cos t)=2+2(-1)^N\cos(Nt)\) is unique. The denominator
in (7) is bounded above and away from zero. Thus (4) gives a constant
\(c>0\), uniform on \(U\), such that
\[
 |K_N(z(t),z(r))|
       \ge cN^{-4}\exp\{N(-\Im t-\Im r)\}
 \tag{8}
\]
for all sufficiently large levels.

**Proposition 2.** Suppose an exact deformation of the full wire
source on an edge in \(U\) is written
\[
 K_N(z(t),z(r))=I^{\rm geom}_N(t,r)+R_N(t,r),
 \tag{9}
\]
and its retained geometric local integral obeys
\[
       |I^{\rm geom}_N(t,r)|
                 \le C_1N^A e^{N\Re\psi(t,r)}.
 \tag{10}
\]
Then, for all sufficiently large \(N\),
\[
 |R_N(t,r)|\ge\frac c2N^{-4}
                       e^{N(-\Im t-\Im r)}.
 \tag{11}
\]
In particular the remainder cannot have a rate below the geometric
edge action.

**Proof.** Equations (5), (8), and (10) make the geometric integral
at most half the full-kernel lower bound for large \(N\). Apply
the reverse triangle inequality to (9). \(\square\)

The proposition applies to any claimed local geometric wire packet
with only polynomial amplitude growth; it does not depend on how
that local chain was parametrized. In particular replacing the
horizontal direction by the adapted Morse coordinate does not
remove this full-fiber remainder.

Combining Propositions 1 and 2 rules out a proof for arbitrary
all-three paths that treats every original full wire independently
as its geometric local chain plus a smaller remainder.
It does not rule out a simultaneous contour deformation in the
wire and trace variables, or an exact regrouping before deformation.

## 4. The large endpoint factors cancel algebraically on adjacent edges

This obstruction does not supply a competing exponential rate for
the fully contracted path. The original algebra explains why.
In
\[
                         \mathcal A_N=\mathbb C[z]/(P_N(z)),
 \tag{12}
\]
the polynomial \(e_D\) vanishes at every physical root.
Those roots have multiplicity two, except for the simple odd-level
root. Therefore
\[
                             e_D^2=0\quad\hbox{in }\mathcal A_N.
 \tag{13}
\]
Indeed the square vanishes to at least the required multiplicity
at every root, so it is divisible by \(P_N\).

If two adjacent edges are both replaced by their endpoint factor
from (4), their common selected vertex receives \(e_D(z_v)^2\).
Multiplication by its crossing \(R(z_v)^3\), or by any other
original factor, leaves that product zero. Its full Hermite trace
is consequently zero, including the required first normals.
This is an identity before any asymptotic estimate.

For sufficiently long paths, the set of edges in Proposition 1
contains two adjacent edges: a matching of an \(m\)-vertex path
has at most \(\lfloor m/2\rfloor\) edges, whereas the number of
these edges is at least \(m-1-B\).
More strongly, in the exact expansion into high-index and remaining
edge factors, only matchings of high edges can survive. The full
statement and its retained first-normal contractions are proved in
the [radical-sector decomposition](research_radical_path_sector_gap.md).

Thus the pointwise dominant endpoint products on most edges do
not survive an unrestricted product followed by the original
traces. Pointwise relative errors in the individual bare kernels
cannot be passed through those traces without an operator or
coherent contraction estimate.

The remaining route is concrete: group the high sectors with their
original traces, retain the surviving matching components and their
boundary variables, and bound those actual components. The existing
matching decomposition is exact, but its geometric rate comparison
and whole-boundary bounds are not proved for arbitrary short
components. The local adapted contour addresses the complementary
geometric piece; it does not settle this missing collective bound.

## 5. The low-kernel cutoff current has the same recursive bound

Removing the radical does not make the individual remaining kernel
geometric. With
\[
 m=\lfloor N/2\rfloor,\qquad L=N-1-m,\qquad
 K_N^{\rm low}(z,w)=\sum_{j=0}^{L}e_j(z)e_j(w),
 \tag{14}
\]
Section 5 of the bare-kernel note proves the exact equation
\[
 (w-\mathscr L_N^{(z)})K_N^{\rm low}(z,w)
           =-s_{L+1}^2e_L(z)e_{L+1}(w),\qquad
                s_j=2\sin(j\pi/N).
 \tag{15}
\]
Here \(\mathscr L_N\) is the original angular difference operator,
acting on the ordinary polynomial in \(z=-2\cos t\).
Near the same homogeneous point, this forcing has a rate larger
than \(\Re\psi\). Therefore a uniform geometric bound for the
individual low kernel is already disproved, at both parities.

The contracted forcing is much smaller and has a useful general
bound. Let \(e=\{v,w\}\) join two selected vertices of an original
graph. Remove this one edge factor, retain \(z=z_v,w=z_w\) as
ordinary variables, omit their two crossings and traces, and perform
all other original contractions. Denote the resulting polynomial
by \(A_N(z,w)\). Other outside variables, if present, are retained
as parameters. Suppose its degree in \(z\) is at most \(dN\), where
\(d\) is fixed. One may take \(d=d_v-1\) for a same-index graph
of original vertex degree \(d_v\); no canonical reduction of the
ordinary boundary polynomial is needed. Put
\[
                 S_N=\sup_{z,w\in[-2,2]}|A_N(z,w)|.
 \tag{16}
\]
The two omitted crossing powers are the original fixed integers
\(n,p\). Contracting the right side of (15) gives exactly
\[
 J_{e,N}=-s_{L+1}^2\,
       \phi_z\phi_w\!\left[
        R(z)^n e_L(z)\,R(w)^p e_{L+1}(w)\,A_N(z,w)\right].
 \tag{17}
\]

**Proposition 3.** At both parities, for \(N\ge4\),
\[
 |J_{e,N}|
       \le4\left(2+2d^2+\frac{|n|}{2}\right)N^3S_N.
 \tag{18}
\]
The estimate is uniform in every retained parameter for which
(16) holds. In particular any angular loss already present in
that bound is preserved.

**Proof.** Lemma 6 of the bare-kernel note gives, for every original
canonical element \(F=\sum F_j e_j\),
\[
 |\phi(e_{L+1}F)|\le N\max_{P_N(c)=0}|F(c)|.
 \tag{19}
\]
The physical crossing values have \(|R(c)^p|=1\). Applying (19)
in \(w\) first gives a polynomial
\(B_N(z)=\phi_w[R(w)^pe_{L+1}(w)A_N(z,w)]\)
of degree at most \(dN\), with real-interval norm at most \(NS_N\).
Markov's inequality gives
\(\|B_N'\|_{[-2,2]}\le d^2N^3S_N/2\).

At odd levels the other functional is bounded by \(N\) times its
physical value norm, so its bound is at most \(N^2S_N\).
At even levels the exact middle-node formula gives
\[
 |\phi(e_LF)|\le2N^2\max_{P_N(c)=0}|F(c)|
                                      +4|F'(c_*)|,
 \qquad c_*=c_{m-1}.
 \]
Use it with \(F=R^nB_N\). Its original first normal is
\(|(R^n)'(c_*)|\le |n|N/8\). Therefore the last display is at most
\[
       \left(2+2d^2+\frac{|n|}{2}\right)N^3S_N.
 \]
We used \(N^2\le N^3\) for the crossing-normal term; all factors
are retained before that harmless polynomial enlargement.
Finally \(s_{L+1}^2\le4\), proving (18).
The normal and residue formulas concern the full original algebra,
so this argument retains the even middle first normal. \(\square\)

For a path, removing the edge separates its two sides:
\(A_N(z,w)=A_{L,N}(z)A_{R,N}(w)\), and \(d=1\).
If their actual whole-boundary bounds have rates \(\mu_L,\mu_R\),
then (18) has rate at most
\[
                              \mu_L+\mu_R.
 \tag{20}
\]
These are the same two open components and the same rate appearing
in the one-edge radical estimate. Thus the strict comparison
\(M_{\rm full}>\mu_L+\mu_R\), when proved, controls both the
radical term and this contracted midpoint forcing. No additional
exponential cost is introduced by the midpoint first normal.

Here the comparison with the original components presumes that
the other edge factors in \(A_N\) are their full original kernels.
If one instead starts with the sector where every edge has already
been truncated, (18) still holds for that specified polynomial,
but its norm is the norm of the corresponding truncated component.
It must first be related to the full component by the exact inverse
radical-matching expansion. A full-component bound cannot simply
be substituted for it; those additional matching currents remain
part of the calculation.

This proposition does not supply the smaller components' bounds,
prove that strict energy comparison for every short path, or
determine the homogeneous solution of the joint low-sector
difference equation. It isolates an actual recursive estimate that
can be used once those component bounds are available.
