# The real half-period endpoint of the conditional packet

Research proof, 4 November 2026. The original conditional packet extends
to real neighbors equal to \(1/2\), uniformly when both neighbors stay
away from zero. The proof checks the boundary root and contour geometry
directly. The earlier open-interval source theorems are unchanged.

## 1. The closed real cotangent quadrant

Put \(p=\cot\pi a\), \(q=\cot\pi b\). For
\(0<a,b\le1/2\), these numbers are real and nonnegative. The original
conditional critical equations are the polynomials
\[
 \begin{split}
 F_0(S)&=S^2+(p+q)S-1+i(q-p),\\
 F_1(S)&=(S+i)(S+p)(S+q)-2i(p-i)(q+i).
 \end{split}                                                   \tag{1}
\]
The selected root domain is still
\(\mathcal S=\{\Re S>0,\ |\Im S|<1\}\).

**Lemma 1.** For every \(p,q\ge0\), either polynomial in (1)
has exactly one root in \(\mathcal S\), counting multiplicity.
It is simple, is the original zero logarithmic lift, and has a
holomorphic implicit extension near each such parameter pair.

For the quadratic, at \(S=u\pm i\), \(u>0\),
\[
 \Im F_0(u+i)=2u+2q>0,\qquad
 \Im F_0(u-i)=-2u-2p<0.
 \tag{2}
\]
At \(S=iv\), \(-1\le v\le1\), its real part is
\(-1-v^2<0\), including the two corners. Thus the full boundary
is excluded even when one or both outer cotangents vanish.

For the cubic, the left boundary has
\[
 \Im F_1(iv)=(v-1)pq-v^2(v+1)-2\le-2.                       \tag{3}
\]
On the upper boundary \(S=u+i\), solving for \(p\) would give
\[
 \Im p=-1-
 \frac{2\{4q+uq(u+q)+u\}}{u\{(u+q)^2+9\}}<-1,             \tag{4}
\]
with a nonzero denominator, contradicting reality. On the lower
boundary \(S=u-i\), the equation would be
\[
 \frac{p+u-i}{p-i}\,\frac{q+u-i}{q+i}=\frac{2i}{u}.          \tag{5}
\]
The first factor is \(1+u/(p-i)\), with positive imaginary part
and real part at least one, including \(p=0\). Its argument is
strictly between zero and \(\pi/2\). The second factor has argument
strictly between \(-\pi\) and zero, also when \(q=0\).
Their product has an argument in \((-\pi,\pi/2)\), excluding the
right side. The left-boundary calculation already handles \(u=0\).

Join any \((p,q)\) to \((1,1)\) by a path in the closed nonnegative
quadrant. Both polynomials are monic and have bounded coefficients
on this compact path, so no root escapes to infinity. The boundary
exclusions and the exact base counts in the
[global cotangent theorem](research_mixed_global_cotangent_roots.md)
give a count of one throughout. Counting multiplicity proves simplicity.
This is a root-count argument at the boundary, not an assumption that
a simple interior root remains simple in its limit.

For the inverse cotangent of the root use
\[
                 s_*=(2\pi i)^{-1}\Log\frac{S_*+i}{S_*-i},
 \tag{6}
\]
whose ratio stays in the upper half-plane. For an outer cotangent
equal to zero, the inverse uses the local logarithm at \(-1\)
with value \(i\pi\), giving \(a=1/2\) or \(b=1/2\).
No principal-log holomorphy across its negative-axis cut is asserted.
All inner and shifted arguments satisfy
\(0<\Re s_*<1/2\) and \(0<\Re(s_*+a),\Re(s_*+b)<1\).
The original logarithmic equation is therefore regular at each
boundary pair and equals zero there by its already fixed interior
lift and continuity. The simple implicit extensions retain that
same lift on sufficiently small neighborhoods.

## 2. Strict phase inequalities at the half endpoint

Every compact set \(K\Subset(0,1/2]^2\) corresponds to a compact
subset of the closed cotangent quadrant. Lemma 1 and the no-boundary-
crossing argument imply uniform separation of the selected roots
from \(\partial\mathcal S\). In particular all local factorial
arguments stay in compact regular strips.

The triangle quadratic form remains positive when an outer cotangent
vanishes. If \(S=u+iv\), \(u>0\), and \(p=0\), then
\(\cot\pi(s+1/2)=-1/S\). The exact determinant is
\[
 \det(-\Re V''/\pi)=\frac{u^2}{u^2+v^2}>0,
 \qquad V(s,a)=g(s+a)-g(s)-g(a),                             \tag{7}
\]
and both diagonal entries are positive. For \(p>0\) the earlier
triangle determinant applies. The optional type-four own-index
term is nonnegative. Thus \(-\Re Q_{ss}>0\) at the selected root,
uniformly on compact sets, and the Gaussian coefficient does not
degenerate at \(a=1/2\) or \(b=1/2\).

The exact type-four upper-height exclusion in
[the real contour geometry](research_mixed_real_conditional_contour_geometry.md)
also holds for \(p,q\ge0\). On its proposed crossing circle,
the \(v\le-1/2\) constant term is strictly negative and the other
terms are nonpositive. For \(v>-1/2\), the quadratic in \(p\)
has negative leading coefficient and negative discriminant, including
at \(p=0\). Therefore
\[
                              e^{2\pi\Im s_*}<\sqrt2
                              \quad(\epsilon=1).             \tag{8}
\]
The same monic-polynomial homotopy supplies the strict side of this
circle, so equality has not been introduced by an endpoint limit.

For the low horizontal arc, the sine inequality used in that note
remains strict at \(a=1/2\):
\(\sin^2\pi(x+1/2)=\cos^2\pi x>\sin^2\pi x\) for
\(x<1/4\). Its actual low-arc endpoint is always strictly below
\(1/4\) at a finite height. The cone interval remains strictly
concave by (7). Hence the original root is the unique nondegenerate
maximum on the whole left half-period, with strict endpoint gaps.

The high-half mirror inequality also stays strict. The circular
second-difference bound from
[the full-period theorem](research_mixed_negative_height_full_period.md)
extends to \(c=1/2\) by its integrated formula:
\[
 D_{1/2,R}(x)\ge
       \frac{2R\sin(2\pi x)}{\pi(1+R)^2}>0
                 \quad(0<x<1/2,\ 0<R\le1).                 \tag{9}
\]
The upper-half comparison adds the same nonnegative linear term as
in the [all-real packet](research_mixed_all_real_conditional_packet.md).
Thus both selected-height signs have a unique global full-period
maximum, including the continuous height-zero case.

At the left vertical boundary the lower-height derivative is strictly
negative because its chirp contributes \(-2\pi a<0\), even if
both numerator arguments have zero argument at \(a=b=1/2\).
For positive height use
\[
 0\le\arg(1-R e^{-2\pi ic})\le\pi-2\pi c
          \quad(R>1,\ 0<c\le1/2).
 \tag{10}
\]
Equality at \(c=1/2\) is allowed. The resulting boundary derivative
is at least \(\epsilon\pi+2\pi b>0\). Thus both selected end
joins have their strict phase gaps exactly as before.

Finally, if \(a,b\ge\delta>0\), the exact alias reflection has
\[
 |a-b+\epsilon(x-1/2)|
       \le(1/2-\delta)+\epsilon/2\le1-\delta
                        \quad(0\le x\le1).                 \tag{11}
\]
There is a uniform strict alias reserve, including when an outer
coordinate is exactly one half.

## 3. The original complete source and coefficient

**Theorem 2.** For every compact \(K\Subset(0,1/2]^2\), the fixed
canonical source
\[
 \mathcal L_{\epsilon,N}(a,b)=P_N(Na)P_N(Nb)
 \sum_{j=0}^{N-1}\frac{e^{2\pi iaj}
       (r^{Na+1};r)_j(r^{Nb+1};r)_j}{(r;r)_j^{2+\epsilon}}
 \tag{12}
\]
has the uniform asymptotic
\[
 \mathcal L_{\epsilon,N}(a,b)=N^{(1-\epsilon)/2}
 \frac{\sqrt{2\pi}\,A_\epsilon(s_*;a,b)}
      {\sqrt{-Q_{\epsilon,ss}(s_*;a,b)}}
 e^{NQ_\epsilon(s_*;a,b)}\{1+O_K(N^{-1})\}.                 \tag{13}
\]
The original phase, sine-root amplitude \(A_\epsilon\), accretive
Gaussian branch and carrier are exactly those of the all-real packet.
Its coefficient remains nonzero and uniformly bounded away from zero.

To verify the finite-source passage, take the same exact midpoint
rectangle with real sides \(-1/(2N)\) and \(1-1/(2N)\).
The denominator interpolation stays in its original nonzero strip.
The two numerator arguments have real parts greater than \(-1\),
so they remain holomorphic, including their original zeros beyond
one period. The left numerator scaled real arguments near \(a,b\)
remain strictly inside \((0,1)\), even at \(a=b=1/2\).
The exact midpoint moduli, right-side multiplier inequality and both
Schwarz reflections therefore apply uniformly. The lower/upper
wall-crossing asymptotics apply on the exterior selected-side lines.

Sections 1--2 give every strict phase input required in that residue
proof: full-period horizontal maximum, both end-join gaps, local
nondegeneracy and the uniform alias reserve (11). Repeating its
constant-mode extraction gives \(+N\), with both vertical pieces
retained. The selected-side exterior lines and the central indentation
handle either height sign and height zero. The local Gaussian lies
strictly inside all three regular factorial strips; its sine factors
are nonzero. Thus its unchanged factor is
\(N\cdot N^{-\epsilon/2}\cdot N^{-1/2}=N^{(1-\epsilon)/2}\).
All other original currents have a uniform exponential gap. This
proves (13) directly with the closed-endpoint constants, rather than
extrapolating an unquantified asymptotic by continuity.

The canonical assertion holds at every integer level, including odd
levels when \(Na=N/2\) is not an integer. Its identification with an
original physical conditional is made only when \(Na,Nb\) are integers.
For example an exactly half-period physical neighbor occurs at even
levels; odd physical rows approaching one half are also covered
uniformly. No parity-dependent support is silently inserted into (12).

This result supplies the half endpoint required for coupled real
contours. It is not uniform as a neighbor tends to zero, does not
assert a source packet on an unquantified complex taper, and does
not evaluate the remaining coherent outer sum.

Reproduction:

    python3 experiments/check_mixed_half_endpoint_conditional_packet.py

The [focused exact checker](../experiments/check_mixed_half_endpoint_conditional_packet.py)
verifies seventeen closed-quadrant boundary, triangle, height and
normalization identities, 54 literal even/odd row-support cases at
levels 2 through 10, and thirty original physical half-endpoint source
comparisons. It validates all inherited proof, script and record
bindings. Uniformity of the contour and its asymptotic coefficient
is proved above, rather than inferred from these finite checks.
