# First-cap critical points for powers three and four

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

This note locates the original first-cap stationary point uniformly for
real outgoing index \(z\in[1/5,9/20]\). It also identifies a concrete
outer-index wall that cannot be discarded by an absolute estimate.
Neither statement is a full cap finite-sum asymptotic.

## 1. Original phase and logarithmic equations

Use the original strip primitive \(J'(v)=\Log(2\sin\pi v)\) from
[the complete-boundary calculation](research_mixed_complete_boundary_sum.md).
For \(\epsilon=0,1\), set
\[
\begin{split}
 F_\epsilon(z;s,u)={}&-2J(1/2-u)-3J(u)-J(s-u)
 +J(s+z)-J(z)-\epsilon J(s)\\
 &+i\pi s(u-z)-\frac{i\epsilon\pi}{2}(s-s^2).
\end{split}\tag{1}
\]
This is the complete-end coefficient phase together with its first
original vertex factor. Its equations are
\[
\begin{split}
 F_s={}&-\Log(2\sin\pi(s-u))+\Log(2\sin\pi(s+z))
 -\epsilon\Log(2\sin\pi s)+i\pi(u-z)
 -i\epsilon\pi(1/2-s),\\
 F_u={}&2\Log\cos\pi u+\Log\sin\pi(s-u)
 -3\Log\sin\pi u+i\pi s.
\end{split}\tag{2}
\]
Every logarithm here has its original continuation from the positive
real sine strip. The zero lift, rather than just the exponentiated
polynomial equation, is part of the theorem below.

Put \(U=e^{2\pi iu}\), \(V=e^{-2\pi is}\), and
\(Z=e^{-2\pi iz}\). Eliminating the inner equation gives
\[
 V=\frac{(1+U)^2}{1-2U+5U^2},\qquad
 U(1-VZ)=(1-VU)(1-V)^\epsilon.                 \tag{3}
\]
Consequently the selected root satisfies, respectively,
\[
 (Z-6)U^3+(2Z+5)U^2+(Z-4)U+1=0,              \tag{4}
\]
\[
 (5Z-29)U^4+(8Z+36)U^3+(2Z-38)U^2+20U+Z-5=0. \tag{5}
\]
These eliminations are useful proposals. The proof does not identify
an original stationary point merely by selecting a polynomial root.

## 2. Uniform original critical branch

For fixed real \(z\in[1/5,9/20]\), let \(\mathcal C_{0,z}\) be
\[
 0<\Re u<1/2,\qquad 0<\Re(s-u)<1/2,\qquad
                         1/2<\Re(s+z)<1.     \tag{6}
\]
For type four intersect this domain with \(0<\Re s<1/2\),
obtaining \(\mathcal C_{1,z}\). These are convex complex domains;
there is no restriction on their imaginary coordinates.

**Theorem 1.** For each type and every real \(z\in[1/5,9/20]\),
(2) has a unique zero in \(\mathcal C_{\epsilon,z}\). It obeys
\[
 \frac{33}{100}<\Re s<\frac{47}{100},\quad
 -\frac9{100}<\Im s<\frac8{100},\qquad
 \frac{21}{100}<\Re u<\frac14,\quad
 \frac1{100}<\Im u<\frac1{10}.                 \tag{7}
\]
The branch is simple and holomorphic on a neighborhood of this entire
real outgoing interval. The inner variable is the original continued
complete-end root \(u_c(s)\).

*Proof.* The outward certificate subdivides the full closed outgoing
interval into exact rational intervals. On every interval it verifies
a two-complex-variable Newton self-map using (2) itself, with a rational
center and an outward enclosure of a fixed inverse preconditioner. If \(r\) is the
certified radius, \(Y\) the preconditioner, and \(J_F=F''\), the actual
test is
\[
 |(Y\nabla F(s_0,u_0))_i|
       +r\sum_j|(I-YJ_F)_{ij}|<r.             \tag{8}
\]
The residual includes the entire outgoing parameter interval. A separate
point-inverse test proves that \(Y\) is nonsingular. Every root polydisk
lies strictly in (6), satisfies (7), and uses the principal logarithms in
(2); hence no integer lift is omitted.

There is an analytic uniqueness argument on the whole stated chamber.
For horizontal differentials set
\[
\begin{split}
 a&=\pi\Re(2\tan\pi u+3\cot\pi u),\\
 b&=\pi\Re\cot\pi(s-u),\\
 c&=-\pi\Re\cot\pi(s+z)+\epsilon\pi\Re\cot\pi s.
\end{split}\tag{9}
\]
Every coefficient is positive in (6), with the additional type-four
condition when needed. The imaginary quadratic in (1) contributes
nothing to the real Hessian, so
\[
             -\Re d^2F=a\,du^2+b(ds-du)^2+c\,ds^2>0.     \tag{10}
\]
Integrating this strictly accretive negative Hessian on a segment proves
complex-gradient injectivity in the convex chamber. It also proves
nonsingularity at every point. The local certified branches therefore
agree on overlaps. The implicit function theorem and compactness supply
a holomorphic neighborhood of the entire real interval. Each recorded
root polydisk additionally has \(a>1,c>1\).

The first equation defining the inner endpoint root is exactly \(F_u=0\).
The checker also evaluates the positive-real square-root and continued
arctangent formula of the complete-boundary theorem throughout every
certified s-box. Its value lies in the same scalar sine chamber and its
original logarithmic residual has modulus less than \(\pi\). The exact
quadratic identity makes that residual an integer multiple of
\(2\pi i\), so it is zero. Scalar strict concavity then identifies this
formula with the inner coordinate of our original root, rather than
another root of (3). \(\square\)

For each fixed outgoing value, the horizontal chamber through this
critical point is a legal local contour in the original factorial
strips. On every compact convex subregion containing that point,
(10) gives a strict quadratic loss away from it and a nonzero local
Gaussian determinant. It does not bound the currents joining this
contour to the original full finite support.

## 3. Why the outer half-index wall cannot be dropped

**Proposition 2.** At type three and \(z=1/5\), let \((s_*,u_*)\)
be the original critical point from Theorem 1. Then
\[
 \Re F_0(1/5;1/2,u_c(1/2))
 -\Re F_0(1/5;s_*,u_*)>\frac{11}{1000}.        \tag{11}
\]
Here \(u_c(1/2)=\pi^{-1}\arctan((i+\sqrt3)/2)\), in the
original endpoint branch.

*Proof.* A separate narrow Newton polydisk verifies (2) at the exact
parameter \(z=1/5\). The checker then evaluates both sides using the
same strip primitive
\[
 J(v)=\frac{\operatorname{Li}_2(e^{-2\pi iv})-\pi^2/6}{2\pi i}
                         -\frac{i\pi}{2}(v-v^2).          \tag{12}
\]
The outward difference exceeds \(11/1000\). All arguments in this
comparison have real part strictly between zero and one. \(\square\)

Thus even after performing the complete-end coefficient sum, an
absolute removal of every outer index at or above \(1/2\) cannot
produce a gap below the selected first-cap rate. Along levels divisible
by ten the index pair \((Nz,Ns)=(N/5,N/2)\) is physical. The
[full interior-index boundary theorem](research_complete_boundary_full_index_interval.md)
places its nonzero endpoint coefficient at precisely the first rate in
(11); the other original factors there are regular and nonzero.
This is an obstruction to that particular absolute cutoff, not an
obstruction to the cap asymptotic.

For type three, the coherent chamber (6) extends across \(\Re s=1/2\):
there is no isolated \(\cot\pi s\) term in (9). A candidate global
contour may therefore retain this wall and deform through the larger
chamber. A full source proof still requires quantitative continuation
of the boundary coefficient along that deformation, all outer and
inner boundary currents, and every cotangent alias. The existence and
local concavity theorem does not supply these missing global estimates.

## 4. Reproduction

```sh
python3 experiments/check_mixed_first_cap_critical.py --precision 256
```

The record contains the complete rational outgoing cover, the original
logarithmic Newton inequalities, the two exact eliminations, and the
outward half-index comparison. It proves neither a global cap packet
nor a nonzero coefficient for an arbitrary mixed word.
