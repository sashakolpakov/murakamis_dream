# The conditional root at the closed cotangent boundary

Research proof, 4 November 2026. This extends the algebraic root and
curvature results to a half-period outer angle while its neighbor may
be complex. It is a statement about the original critical equation.
It does not extend a finite-sum asymptotic to this whole parameter set.

## 1. Closed outer domain and logarithms

Write \(P=p+i\alpha\), \(Q=q+i\beta\), and assume
\[
 p,q\ge0,\qquad |\alpha|,|\beta|<1/2.
 \tag{1}
\]
The original conditional polynomials are
\[
 F_0(S)=S^2+(P+Q)S-1+i(Q-P),\qquad
 F_1(S)=(S+i)(S+P)(S+Q)-2i(P-i)(Q+i).
 \tag{2}
\]
Let \(\mathcal S=\{\Re S>0,\ |\Im S|<1\}\).

**Theorem 1.** Each polynomial in (2) has exactly one root in
\(\mathcal S\), counting multiplicity. That root is simple and
has a holomorphic extension to a neighborhood of every parameter
pair in (1). On compact subsets the roots stay uniformly inside
\(\mathcal S\). The corresponding original logarithmic equation
has its zero lift.

Here the outer inverse cotangent at \(p=0\) is defined without a
discontinuous principal-log convention. Use the logarithm with argument
in \((0,2\pi)\), cut along the positive real axis, and put
\[
 a(P)=\frac1{2\pi i}\Log_{(0,2\pi)}\frac{P+i}{P-i}.
 \tag{3}
\]
For \(p>0\), the quotient is in the upper half-plane, so this is
the original branch. At \(p=0\), it is the negative real number
\((\alpha+1)/(\alpha-1)\), and (3) gives \(\Re a=1/2\).
It is holomorphic on a neighborhood of every such finite parameter.
Define \(b(Q)\) in the same way and use the original upper-half-plane
inverse for the inner selected root \(S_*\), obtaining \(s_*\).
Then
\[
 0<\Re s_*<1/2,
 \qquad 0<\Re a,\Re b\le1/2,
 \qquad 0<\Re(s_*+a),\Re(s_*+b)<1.
 \tag{4}
\]
Thus all critical factorial arguments stay in their original regular
strips, including when an outer cotangent has zero real part.

## 2. Boundary exclusion with nonnegative real cotangents

For the quadratic, on the upper and lower sides \(S=u\pm i\),
\(u>0\), one has
\[
 \Im F_0(u+i)=u(2+\alpha+\beta)+2q>0,
 \qquad
 \Im F_0(u-i)=u(-2+\alpha+\beta)-2p<0.
 \tag{5}
\]
On the full left side, including the two corners,
\[
 \Re F_0(iv)=-1-v^2+\alpha(1-v)-\beta(1+v)<-v^2\le0,
                      \qquad -1\le v\le1.                 \tag{6}
\]
The strict inequality follows from \(|\alpha|,|\beta|<1/2\);
it does not require \(p,q>0\).

For the cubic, the left-side calculation in the
[global cotangent theorem](research_mixed_global_cotangent_roots.md)
is
\[
 \Im F_1(iv)=(v-1)pq+
  2(\alpha-1)(\beta+1)-(v+1)(\alpha+v)(\beta+v).
 \tag{7}
\]
The first term is nonpositive for \(p,q\ge0\). The remaining
bilinear expression in \(\alpha,\beta\) is at most \(-1/8\)
on their closed half-square, by the four exact corner estimates in
that theorem. This excludes the whole left side even at \(p=0\)
or \(q=0\).

If \(F_1(u+i)=0\), solving for \(P\) gives
\[
 \Im P=-1-
 \frac{2\{4q+uq(u+q)+u(\beta+1)^2\}}
      {u\{(u+q)^2+(\beta+3)^2\}}<-1.                      \tag{8}
\]
The denominator is nonzero and the numerator in braces is strictly
positive, including when \(q=0\). Equation (8) contradicts (1).

On the lower side, a root would imply
\[
 \frac{P+u-i}{P-i}\,\frac{Q+u-i}{Q+i}=\frac{2i}{u}.
 \tag{9}
\]
The first factor equals \(1+u/(P-i)\); its real part is at least
one and its imaginary part is strictly positive. Its argument is
therefore in \((0,\pi/2)\), also at \(p=0\). The numerator of the
second factor has argument in \((-\pi/2,0)\), while its denominator
has argument in \((0,\pi/2]\). Its argument is in \((-\pi,0)\),
also at \(q=0\). Their product cannot have the argument \(\pi/2\)
of the right side of (9).

Join any parameter pair (1) to \(P=Q=1\) inside that convex closed
domain. The polynomials are monic and their coefficients are bounded
along the compact path, so no root escapes to infinity. The boundary
exclusions make the number of roots in \(\mathcal S\) constant.
The exact base counts of the global theorem give one root, counting
multiplicity. This proves uniqueness and simplicity, including at
the new outer boundary. Compactness gives uniform separation from
\(\partial\mathcal S\). The implicit function theorem gives the
local holomorphic extensions, which agree wherever their selected
roots are defined.

Exponentiation of the original logarithmic equation gives (2), with
nonzero denominators throughout (1) and \(\mathcal S\). Its value
is therefore in \(2\pi i\mathbb Z\). On the interior \(p,q>0\),
the original zero lift has already been proved. The regular branches
(3)--(4) extend that value continuously to either outer boundary,
so it remains zero. This completes the proof of Theorem 1.

## 3. The positive triangle forms also extend

Let \(S_*=u+iv\), \(u>0\), \(|v|<1\), and put
\[
 C=\Re\frac{PS_*-1}{S_*+P}.
\]
For \(V(s,a)=g(s+a)-g(s)-g(a)\), the negative real Hessian,
divided by \(\pi\), is
\[
 T=\begin{pmatrix}u-C&-C\\-C&p-C\end{pmatrix},\qquad
 \det T=\frac{(u+p)^2-(pv-u\alpha)^2}
                   {(u+p)^2+(v+\alpha)^2}>0.                \tag{10}
\]
Indeed \(|pv-u\alpha|\le p|v|+u|\alpha|<p+u\). Also
\(\det T=up-(u+p)C>0\), so \(C<up/(u+p)\) and both diagonal
entries are positive. In particular, at \(p=0\),
\[
 C=\frac{u(\alpha^2-1)}{u^2+(v+\alpha)^2}<0,
 \qquad
 \det T=\frac{u^2(1-\alpha^2)}{u^2+(v+\alpha)^2}>0.          \tag{11}
\]
Both incident triangle forms are therefore positive definite.
The extra own-index and allocated outer-factorial terms have
nonnegative real diagonal coefficients, since \(u>0\) and
\(p,q\ge0\). The exact complex Schur identity in the
[real support theorem](research_mixed_real_outer_support.md),
equation (9), then proves
\[
                         -\Re\phi_{\eta\epsilon}''>0        \tag{12}
\]
for the allocated critical phase on (1), uniformly on compact sets.
This is ambient curvature at fixed imaginary heights. It asserts
neither concavity after a varying-height substitution nor dominance
of the complete finite source on this larger domain.

The new endpoint permits the convex contour domains to meet
\(\Re a=1/2\) with the other cotangent still complex. A full
source theorem there needs its own contour-current estimates; the
real half-endpoint source theorem is not being silently enlarged.

## Reproduction

    python3 experiments/check_mixed_closed_cotangent_roots.py

The checker verifies the boundary algebra and closed-face triangle
identities exactly, and validates the original base-count and
zero-lift records. The monic homotopy and strict inequalities are
the analytic argument above.
