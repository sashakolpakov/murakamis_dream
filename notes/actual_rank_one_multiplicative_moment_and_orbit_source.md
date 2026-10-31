# The actual cyclic head has a rank-one moment relation and an orbit co-source

Research proof, 27 October 2026. The proposed multiplicative relation
is exact for the actual repaired head. Its natural moment covector
differs from the original Whittaker row. Retaining their finite orbit
path gives the original source and an explicit whole Ward homotopy.
Actual R coefficients transport the moment framing, but do not make
the orbit row an eigenrow. Thus the relation yields an exact source
sum rule rather than survival of the geometric line in the last sum.

This is a direct finite-matrix calculation. No classification or
published multiplicative-moment proof is used.

## 1. Exact framed multiplicative relation before root specialization

Use the actual matrices from
[the highest/Whittaker boundary construction](actual_highest_whittaker_boundary_and_moving_walls.md):

\[
 B=\operatorname{diag}(1,Q,\ldots,Q^{N-1}),\quad
 P=\sum_{j=0}^{N-2}E_{j+1,j}+E_{0,N-1},\quad P^N=I.
\]

Write Z=Q^N, delta=1-Z, v=e_0, w=e_0^t, e=vw=E_00, so wv=1.
Since W=eP=E_(0,N-1), the exact relation BP-QPB=delta W gives

\[
 \boxed{\quad
 BPB^{-1}P^{-1}=Q[I+(Z^{-1}-1)vw].\quad}                   \tag{1}
\]

For example W B inverse P inverse=Q^(-(N-1))e, proving every
coefficient and the sign in (1). With the actual framing vector
v and scaled covector what=(Z inverse minus one)w, it is the
framed equation Q inverse BPB inverse P inverse=I+v what. Its
determinant forces and satisfies 1+what v=Z inverse. The inverse
equation is equally exact:

\[
 PB P^{-1}B^{-1}=Q^{-1}[I+(Z-1)e].                         \tag{2}
\]

It is the rank of the Q-NORMALIZED commutator minus I that is at
most one. The factor Q cannot be dropped: at a primitive N-th root
Q is not one. Generically Z not one makes that rank exactly one.
At Z=1 it drops to zero, but the divided normal retains

\[
 \left[\frac{Q^{-1}BPB^{-1}P^{-1}-I}{1-Q^N}\right]_{Q_N}=e.
                                                                  \tag{3}
\]

The actual whole lift specifies w through what=(Z inverse minus
one)w. A bare root moment relation with what=0 does not reconstruct
that divided covector or the selected source.

## 2. Both actual endpoint walls use this same marked projector

Let kappa=M-M inverse, e_top=P inverse eP. The cyclic expressions
and actual finite generators factor WHOLE as

\[
 F_{cyc}=P(I-QB),\quad \mathcal E_{cyc}=P^{-1}(MB^{-1}-M^{-1}I),
\]
\[
 \boxed{\quad
 F=F_{cyc}(I-e_{top})=F_{cyc}-\delta eP,\qquad
 \mathcal E=\mathcal E_{cyc}(I-e)
                         =\mathcal E_{cyc}-\kappa P^{-1}e.
 \quad}                                                       \tag{4}
\]

The first equation deletes the last raising arrow and the second
deletes the first lowering arrow. Thus both actual walls have the
same rank-one framing transported to the appropriate end. The
multiplicative commutator itself only sees the Q-wall delta;
the independent meridian character kappa must also be retained.

In particular F^N=0 while F_cyc^N=delta(Q;Q)_(N-1)I, and the
original pair detects the divided wrap value N. At a primitive
root E_cyc^N=(-1)^(N-1)(M^N-M inverse N)I. These are the actual
central norms and endpoint factors, including the ones entering
the full modified-dimension ratio. Neither (1) nor its root rank
drop replaces these norms by numerical units or equates their
different normal directions.

## 3. The actual co-source is a required finite orbit path

The natural moment covector is w. The original output row is
ell=ones transpose. It is recovered exactly by the finite path

\[
 S_P=\sum_{r=0}^{N-1}P^r,\qquad
 \ell=w S_P,\qquad Q_0=v\ell=e S_P.                         \tag{5}
\]

Thus the exact highest-input period is ell C v=w S_P C v, not
just w C v on arbitrary current matrices. Both anchors equal
one on I, but their rows are not proportional for N greater than
one. Any simultaneous change of basis carries w,ell and S_P
together; it cannot erase their relative orbit path.

There is a source-preserving framed period identity, not just the
unpointed matrix relation. Write Delta_mom=BPB inverse P inverse
minus QI and lambda(C)=ell C v. Combining (1) and (5) gives

\[
 \Delta_{mom}S_P=Q(Z^{-1}-1)Q_0,
\]
\[
 \boxed{\quad
 \lambda(C_1\Delta_{mom}S_P C_2)
       =Q(Z^{-1}-1)\lambda(C_1)\lambda(C_2).
 \quad}                                                      \tag{5a}
\]

This holds for arbitrary actual whole matrices C_1,C_2 with their
coefficient lines consistently retained. It is the literal rank-one
cut/source factorization: Q_0=v ell. Dividing the already specified
whole equation by delta and evaluating at the root gives coefficient
Q_N on the right. Equivalently the selected divided moment insertion
is Q_N Q_0. Without S_P the right factor would have the different
moment row w. Thus (5a) is an actual whole loop/source identity with
its required orbit path, not permission to discard that path or to
assign a new value to the uninserted period.

The norm of S_P in the original flat unitary head metric is N,
and the norm of ell is sqrt N. No exponential source scale is
introduced by (5). Conversely these elementary source bounds
are not a bound on the actual R word or its period.

There is an exact WHOLE source-current comparison. Put
D_K C=K C K inverse minus C with K=xB inverse, and define

\[
 \beta_K(X)=\sum_{c=1}^{N-1}\frac{X_{c,0}}{Q^{-c}-1}.
\]

Every displayed denominator is a unit at a primitive N-th root.
Entrywise multiplication gives

\[
 \boxed{\quad
 \ell C v-wCv=\beta_K(D_K C).\quad}                        \tag{6}
\]

This is the K-only specialization of the established actual Ward
source homotopies. It holds before jets on arbitrary C, so all
derivatives of beta_K, K, C and the original peripheral line are
retained. At the physical root its exact flat-metric row norm is

\[
       \|\beta_K\|^2
        =\sum_{c=1}^{N-1}\frac1{4\sin^2(\pi c/N)}
        =\frac{N^2-1}{12}.                                \tag{7}
\]

For a direct proof of the last identity, apply two logarithmic
derivatives at one to (t^N-1)/(t-1), whose roots are the nontrivial
N-th roots. This gives sum Q^c/(1-Q^c)^2=-(N^2-1)/12; each
negative summand is the corresponding reciprocal squared sine.

## 4. Exact consequence for the actual one-index Fourier source

Use the whole Vandermonde change on the SECOND wire and put
A_j[c,a]=T^V_(c,j;a,j). Define

\[
 J^{Whit}_j=\ell A_j v,\qquad J^{mom}_j=w A_j v.
\]

Equation (6) gives the WHOLE coefficientwise relation

\[
             J^{Whit}_j-J^{mom}_j=\beta_K(D_K A_j).         \tag{8}
\]

At the original root, charge conservation and the ordinary scalar
closure prove

\[
 J^{mom}_j=P_N/N,\qquad
 J^{Whit}_j=P_N/N+\beta_K(D_K A_j),\qquad
 \sum_j\beta_K(D_K A_j)=0.                                \tag{9}
\]

Indeed setting c=a=0 forces the old second offset to zero;
Fourier transformation then contributes precisely 1/N and no j
dependence. The first formula is not an off-root scalarity claim.
The whole sum of (8) is beta_K(D_K C); it vanishes at the root
for the uninserted fully reclosed scalar C, while inserted currents
and normal derivatives retain their actual defects.

Equation (9) is a genuine constraint on the final finite j source.
It also explains a limitation: replacing the Whittaker orbit by
the natural moment row loses ALL nonconstant Fourier geometry.
The geometric formal block may occur in this Ward sector, whose
sum is controlled only after closure. A nonzero local block or a
rank-one moment relation does not prove its selected survival.

## 5. Actual R transports the framing but not the orbit row trivially

For any actual invertible crossing R, conjugating ALL B_i,P_i,e_i
and their vector/covector maps preserves (1)-(4) algebraically.
This is a strict identity of the actual finite matrix algebra;
it is not a claim that individual generators remain fixed.
For two highest inputs the literal actual coefficients give

\[
 R(v\otimes v)=r_{00}(v\otimes v),\qquad
 (w\otimes w)R=r_{00}(w\otimes w).
\]

The full scalar r_00, including its half-Cartan mark, is retained.
Thus the highest moment framing is compatible up to this actual
scalar. For two copies of the original boundary object, its tensor
orbit row has the exact residual

\[
 (\ell\otimes\ell)R-r_{00}(\ell\otimes\ell)
       =(w\otimes w)[S_P\otimes S_P,R].                    \tag{10}
\]

It is generally nonzero. At N=2, q=i, eta_half=exp(pi i/4), the
literal positive crossing matrix displayed in
[the actual boundary-moment audit](actual_negative_band_boundary_moment_and_ward_atom.md)
has r_00=eta_half. The input (0,1) component of (10) is
eta_half inverse minus eta_half=-sqrt(2)i, not zero. Multiplying
the crossing by its retained scalar normalization multiplies
both sides; it does not remove this defect. Actual word, cap and
prefix transport must carry the orbit path and this residual.
This is a local boundary-object covariance test. A full original
braid still has its pivotal caps on the other strands; their
source is not replaced by ell tensor ell. The actual fully sourced
one-index identity is (8)-(9), with those original caps retained.

Even the naive tensor product of the moment pairs is not another
rank-one pair: for B_tot=B_1B_2,P_tot=P_1P_2 its normalized
commutator is (I+a e_1)(I+a e_2), a=Z inverse minus one. For
generic Z not plus or minus one its defect has rank 2N-1, preserved
by every simultaneous crossing conjugation. The true Hopf/coprod
and source fusion therefore cannot be replaced by that naive
product if a rank-one target is desired.

## 6. Exact audit and scope

[The independent script](../experiments/audit_rank_one_moment_orbit_source.py)
and [its output](../experiments/rank_one_moment_orbit_source_results.json)
check the whole framed relation, endpoint projectors, root divided
class, orbit path, current homotopy, actual Fourier sum rule and
literal R residual, including a characteristic-zero example.

The usable whole object is the framed pair B,P,v,w WITH its
original orbit co-source S_P, both actual endpoint deletions and
the meridian characters. This is more precise than a bare root
commutator relation. It supplies exact source-current identities;
it does not identify a global geometric cycle, make the final
source horizontal by itself, or prove a volume limit.

## 7. Existing terminology and the root specialization

The defining rank-one multiplicative-commutator relation occurs in
[Chalykh--Fairon, Section 3, page 10](https://arxiv.org/pdf/1704.05814).
Their invertible-coordinate presentation has
rank(XZX inverse Z inverse minus q_0 I)=1. Our actual generic
pair has X=B, Z=P and q_0=Q. At Q^N=1 its rank drops to zero,
so the root belongs to the rank-at-most-one closure, with the
divided marking (3) retained. Their Proposition 3.3 assumes q_0
is not a root of unity. Their subsequent regular coordinate chart
also excludes x_i=q_0 x_j, which the actual clock spectrum
violates. No smoothness or coordinate theorem there is applied
to this resonant root/source section; only the defining coverage
is used.

The additional [aligned source-frame theorem](flat_cyclic_source_frame_and_scalar_period.md)
proves the whole matrix-algebra classification directly, including
its necessary alignment and flat-saturation hypotheses. The
[actual Fourier cancellation theorem](actual_fourier_source_cancellation.md)
then constructs a nonzero geometric Ward block whose selected
cyclic sum vanishes. These distinguish frame rigidity from the
remaining selected-period problem.
