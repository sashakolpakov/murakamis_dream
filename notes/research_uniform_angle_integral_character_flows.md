# Integral character flows for the actual uniform checkerboard angles

Private written proof, 19 November 2026.

The actual alternating checkerboard source fixes both its factorial
rows and its quadratic term. At uniform one-third angles, its strict
Legendre feasibility problem has an exact description by flows on
the oriented dual shadow graph. The divergence must be integral in
the original face lattice. Two currents belonging to the same
crossing also obey a coupled capacity inequality.

This gives a finite criterion for candidate integral characters, a
constructive sufficient cut test, and explicit sufficient and
impossible configurations. It does not assign a coefficient to any
character in a deformation of the original capped source cycle.
Neither feasibility nor a character satisfying the criterion is
identified with a geometric critical point.

The complete directs are C, the actual checkerboard source, and D,
its exact affine factorial function and Legendre theorem. All graph
convexity and capacity arguments used here are proved below.

## 1. The actual angle and character conventions

Use C's connected alternating closed-braid shadow with c>=1 crossing
occurrences. At crossing j its sign is sigma_j in {1,-1}; its two
over-port charges are u_j,z_j and its under-port charges are
A_j=u_{a(j)}, B_j=z_{b(j)}. The honest flow equations are
u_j+z_j=A_j+B_j. Every one of the 2c shadow edges has exactly one
over-port name u or z. Repeated incidences and parallel edges remain
distinct throughout.

Color the regions black and white, and fix one black face B_0.
The original integer face coordinates are f_F, F != B_0, with
f_{B_0}=0 and edge charge e=f_B+f_W. C proves that these are a
bijection with the honest integer flow lattice, before its finite
nonnegative caps. There are c+2 faces and hence c+1 coordinates.
For clarity, this is an integral statement: after putting
g_B=f_B and g_W=-f_W, charge e is the increment g_B-g_W on a
dual edge from white to black. The crossing equations give zero
sum around every dual quadrilateral. Integral path integration on
the dual sphere, with its repeated incidences retained, recovers
the unique integral g after the base value is fixed.

Set c_0=2 pi i and w=c_0 f/N. Let U,Z,A,B be the corresponding
linear charge forms in w. D's exact principal potential is
\[
 W_*(w)=\sum_j\{2\operatorname{Li}_2(e^{U_j})
        +2\operatorname{Li}_2(e^{Z_j})
        +\operatorname{Li}_2(e^{-U_j-Z_j})-5\operatorname{Li}_2(1)\}
                  +Q_*(w),                                      \tag{1}
\]
where the last marked logarithm is c_0-U_j-Z_j and
\[
 Q_* =\sum_j\left\{
 \tfrac34 U_j^2+\tfrac12 U_jZ_j+\tfrac34 Z_j^2
 +\tfrac{\sigma_j}{4}(Z_j-U_j)(B_j-A_j)
 -\tfrac{c_0(3+\sigma_j)}4(U_j+Z_j)\right\}.                \tag{2}
\]
The exact source still has D's shifted last factorial, pivot,
d=N-1 amplitude and scalar. They are not changed in this note.

Let \(\mathcal A\) denote the matrix of the five logarithmic rows
U,U,Z,Z,-U-Z per crossing, including the last row's offset 2 pi.
Write the quadratic and linear pieces of (2) as
\(\tfrac12w^{\mathsf T}\mathcal H w+i\kappa^{\mathsf T}w\).
For a character in the original integral dual lattice use
\[
 W_n=W_*+c_0 n^{\mathsf T}w,\qquad n\in\mathbb Z^{c+1}.
                                                               \tag{3}
\]
The target of the beta constraint is therefore
\(b_n(\theta)=-\mathcal H\theta-\kappa-2\pi n\).
No multiple, sublattice enlargement or reduction modulo N is made.

Fix the uniform angle point
\[
 \theta_{U_j}=\theta_{Z_j}=2\pi/3,\qquad
 \alpha_{j,L}=2\pi-\theta_{U_j}-\theta_{Z_j}=2\pi/3,
 \qquad a=\pi/3.                                           \tag{4}
\]
It is an honest face point: take all black angles zero and all
white angles 2 pi/3. Every five-row alpha angle is 2 pi/3, so each
beta coordinate must lie in (0,a).

At (4), Z-U and B-A both vanish. Thus the differential of the chirp
in (2) is zero. The other quadratic terms have coefficient 4 pi/3
on both U and Z, and the imaginary linear term has coefficient
-pi(3+sigma_j)/2. Consequently the unshifted target b is the
pullback of the following edge covector:
\[
 p^{\rm src}_{U_j}=p^{\rm src}_{Z_j}=
 \begin{cases}2a,&\sigma_j=1,\\-a,&\sigma_j=-1.\end{cases}   \tag{5}
\]
This calculation uses the actual source quadratic. Replacing it
by a preferred gluing quadratic would change the criterion.

## 2. The local strict hexagon

At a crossing the five beta coordinates have the image
\[
 p_U=\beta_{U,1}+\beta_{U,2}-\beta_L,\qquad
 p_Z=\beta_{Z,1}+\beta_{Z,2}-\beta_L.                        \tag{6}
\]
The image of the open cube (0,a)^5 is EXACTLY
\[
       -a<p_U,p_Z<2a,\qquad |p_U-p_Z|<2a.                  \tag{7}
\]
Necessity follows directly from (6). For sufficiency choose l in
the nonempty open interval
\[
 \max(0,-p_U,-p_Z)<l<\min(a,2a-p_U,2a-p_Z).                 \tag{8}
\]
The inequalities in (7) are precisely those asserting that every
entry in the left maximum is smaller than every entry in the right
minimum. Set beta_L=l and split each sum p_U+l and p_Z+l equally
between its two beta coordinates. These five numbers lie in (0,a)
and give (6). Thus the strict image and a preimage are both explicit.

For the two edges owned by crossing j define
\[
 q_e=\frac{\sigma_j}{2\pi}(p_e^{\rm src}-p_e).
                                                               \tag{9}
\]
Using (5), (7) becomes exactly
\[
             0<q_e<\tfrac12,\qquad
             |q_{u_j}-q_{z_j}|<\tfrac13\quad(1\le j\le c).
                                                               \tag{10}
\]
The pair inequality is part of the criterion; independent edge
capacities alone do not describe the five-factor source.

## 3. The original lattice is an integer divergence lattice

Let \(\mathcal D_\sigma\) have all the dual shadow vertices and
edges. Orient an edge from its white face to its black face, and
reverse that orientation if its owning overcrossing has negative
sign. Define HEAD-POSITIVE divergence by
\[
 (Dq)_v=\sum_{e:\,\operatorname{head}(e)=v}q_e
          -\sum_{e:\,\operatorname{tail}(e)=v}q_e.           \tag{11}
\]
In particular the sum of the divergences is zero. The underlying
graph is connected; it has 2c edges with their original multiplicity.

The strict beta equation for (3) is
\(\mathcal A^{\mathsf T}\beta=b-2\pi n\). By (6) it says
that the pullback of the edge covector p^{src}-p is 2 pi n.
Equation (9) and g_B=f_B, g_W=-f_W turn this into
\[
                         Dq=\nu.                          \tag{12}
\]
Here nu is precisely the following integral representative of n:
\[
 \nu_B=n_B\ (B\ne B_0),\qquad \nu_W=-n_W,
 \qquad \nu_{B_0}=-\sum_{F\ne B_0}\nu_F.                  \tag{13}
\]
Conversely every integral vector nu of sum zero gives exactly one
original n by (13). To check signs directly, an edge contributes
sigma_j q_e(dg_B-dg_W). This is q_e times its head increment minus
its tail increment for the orientation in (11). Summing gives
(Dq) dot dg. Deleting g_{B_0}=0 and undoing the white sign change
gives n dot df, with no factor of two or of three.

**Exact coupled-flow criterion.** At (4), a specified original
character n has a strict beta fiber if and only if there is a real
flow q satisfying (10) and (12), with nu given by (13). Some
original integral character has a strict beta fiber if and only if
there is a flow satisfying (10) whose divergence is integral.

Every implication has already been proved: beta gives q by (9),
and a q satisfying (10) gives the original beta coordinates by
(5), (9), and (8). Equation (13) supplies exactly the original
character, rather than a character on a finite cover.

This is a finite coupled linear feasibility problem. There are only
finitely many possible integral divergences, since at each vertex
\[
 -\tfrac12\operatorname{outdeg}(v)<\nu_v
             <\tfrac12\operatorname{indeg}(v).             \tag{14}
\]
For each such nu of sum zero, (10),(12) are strict rational linear
equalities and inequalities. If feasible, they have a rational
solution: rational points in the affine rational solution space of
(12) are dense, and the inequalities are open. This describes a
finite exact test, without asserting that it always succeeds.

By D's Legendre theorem, a successful test gives the unique proper
radial minimum for this character at (4), an interior maximizing
beta fiber, and a nonzero Legendre graph Jacobian. A full critical
point also requires the remaining real critical equations. Nothing
in the divergence test supplies those equations or the coefficient
of the character in the original cycle.

## 4. A sufficient construction by strict cuts

The coupled problem has a useful smaller box subclass. Fix
\[
        \tfrac1{12}<\epsilon<\tfrac14,\qquad
        l=\epsilon,\qquad u=\tfrac12-\epsilon.              \tag{15}
\]
Any flow with l<q_e<u satisfies (10), since
u-l=1/2-2 epsilon<1/3.

For a vertex subset S, let in(S) be the edges entering S and
out(S) the edges leaving S. Write nu(S)=sum_{v in S}nu_v, and
count edges with multiplicity. For any prescribed real nu of sum
zero, there is a flow l<q<u with Dq=nu if and only if every nonempty
proper S satisfies
\[
 l|\operatorname{in}S|-u|\operatorname{out}S|
 <\nu(S)<
 u|\operatorname{in}S|-l|\operatorname{out}S|.                \tag{16}
\]
These signs follow from the head-positive convention: summing
(11) over S gives incoming flow minus outgoing flow. Necessity of
(16) follows immediately, with strictness since the graph is
connected and every proper cut has at least one edge.

Here is a proof of sufficiency including the strict boundary issue.
Let Z=D[l,u]^E, a compact zonotope in the sum-zero hyperplane.
Its support function, for a real vertex potential h, is
\[
 H_Z(h)=\sum_{e=(t\to s)}
                 [u(h_s-h_t)_++l(h_s-h_t)_-],              \tag{17}
\]
where v_-=min(v,0). Constants do not affect this expression or
nu dot h. Subtract min h and put S_t={v:h_v>t}. Integrating the
edge and vertex indicators gives the exact layer identity
\[
 H_Z(h)-\nu\cdot h
 =\int_{\min h}^{\max h}
       [u|\operatorname{in}S_t|-l|\operatorname{out}S_t|
                                      -\nu(S_t)]\,dt.      \tag{18}
\]
Every nonconstant h therefore has strictly positive support gap
under (16). In fact, if delta is the smallest of its finitely many
upper and lower cut gaps, the right side is at least
delta(max h-min h). On the space of potentials modulo constants
this bounds a positive multiple of any fixed norm. Thus nu lies
in the relative interior of Z, by the elementary supporting
hyperplane characterization of a compact convex set. Connectedness
ensures that D maps onto the sum-zero hyperplane: for example a
spanning tree transports an arbitrary sum-zero divergence, with
no capacity restriction at this rank check.

Finally an interior image point has a preimage in the OPEN box.
Indeed let q_0=(l+u)/2 on every edge, with image b_0. For small
t>0 the point (nu-t b_0)/(1-t) is still in Z. Choose any preimage
q_1 in the closed box. Then tq_0+(1-t)q_1 is an open-box preimage
of nu. This proves (16) without assuming a nonsingular graph
Laplacian or an integral flow theorem.

The construction is quantitative. With E the total edge count,
choose
\[
 0<\eta<\min\{(u-l)/2,\delta/(2E)\}.                      \tag{19}
\]
Changing the box to [l+eta,u-eta] reduces each cut gap by at most
E eta. The same proof supplies a q in that smaller open box.
In particular both the individual capacity margin and the local
pair margin are positive and explicitly controlled.

For an INTEGRAL nu of sum zero, (16) is therefore a sufficient
construction of a candidate original character via (13). It is
necessary and sufficient for this chosen box subclass only, not
for the full coupled domain (10). Enumerating the finitely many
integral nu allowed by the vertex bounds and checking the finitely
many cuts is a concrete sufficient test; it does not replace the
original source by a different character lattice.

## 5. Explicit sufficient and impossible configurations

Let
\(\Delta_v=\operatorname{indeg}(v)-\operatorname{outdeg}(v)\).
If there is an integer p>=3 dividing every Delta_v, then
\[
                 q_e=1/p,\qquad \nu_v=\Delta_v/p            \tag{20}
\]
is a strict solution of the EXACT coupled criterion. Its two
currents at every crossing agree, and 0<1/p<1/2. Its slack
in each of the three kinds of inequality in (10) is at least
min(1/p,1/2-1/p,1/3)>0. Formula (13) gives the actual integral
character. This construction uses (10) directly; it does not
require 1/p to belong to any of the narrower boxes (15).

This is a conditional statement about the actual oriented graph.
For example, if all signs are equal, every dual vertex is a pure
source or sink, and the divisibility condition reduces to division
of its degree by p. No claim is made here that a particular braid
family satisfies that condition or that its candidate character
has nonzero cycle coefficient.

There is also a useful obstruction to arbitrary winding repairs.
If a vertex is a pure source or a pure sink of degree one or two,
then (10) makes the magnitude of its divergence lie strictly
between zero and degree/2, hence strictly between zero and one.
It cannot be integral. Thus NO original integral character has
a strict uniform-angle fiber in this case. In particular a bigon
whose two edges are both directed in or both directed out cannot
be repaired by assigning an integer winding elsewhere.

This conclusion is restricted to the uniform point (4). Nonuniform
angles change the capacities. It also shows why adding same-sign
twist bigons, without checking their actual role orientation, is
not a sufficient general construction of a strict uniform fiber.
The number of crossings alone supplies no replacement for the
coupled criterion or its cut test.

## 6. Source and scope

The character lattice in (3),(13) is the original integer face
lattice of C's honest charge coordinates, with its single face
gauge. The actual scalar still uses C's original averaged physical
cut and D's complete capped factorial function. This theorem does
not change that physical cut. If a fixed physical occupation cut
is imposed, it restricts an affine coordinate and changes the
dual character problem; the present criterion must then be
restricted and projected explicitly, not copied unchanged.

A feasible integer character is only a candidate for a retained
Fourier or cotangent sector. Its actual occurrence, its relative
cycle coefficient, the real critical equations, and geometric
peripheral matching remain separate questions. No positivity or
noncancellation of the original finite sum follows from (10) or
(16). The constructive content is the exact passage from the
actual five-factor source to its coupled integral-divergence test,
with sufficient capacities on the unchanged character lattice.

## Complete directs

* C: notes/research_alternating_charged_checkerboard_polarization.md,
  435 lines, SHA256
  c7102909f30c008e45a8e7040a225f1de4164187709c5548ff316d49954f1098.
* D: notes/research_affine_legendre_actual_checkerboard_function.md,
  504 lines, SHA256
  d5b138e3537fe6c4eafe161e74c8be0cf7d861abfa0b2a8b6a3b0c7e13d46569.

Both complete directs were freshly read in this author sequence;
the ending of D was recovered in a separate covering read after
the combined display was truncated. Every used implication is
accounted for above. All work is written mathematics; frozen and
public files remain unchanged.
