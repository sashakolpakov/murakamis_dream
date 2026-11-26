# Exact contraction of the regular incoming rows

Research deduction, 7 November 2026. Moving the incoming coordinate
from \(a=1/2\) into \(a>1/2\) contracts each original numerator
row that remains below its first sine zero. The statement is an
exact finite-product inequality, before taking any asymptotic limit.
Its phase is an explicit Fourier modulation and its modulus is a
positive diagonal contraction.

The result supplies upper estimates on retained rows. It gives no
lower bound for a signed sum, and rows which pass the numerator
wall must be estimated separately.

## 1. The original finite products

For an integer \(N\ge2\), set
\[
 r=e^{-2\pi i/N},\qquad X_a=e^{-2\pi ia},\qquad
 p_j(X)=\prod_{k=1}^{j}(1-r^kX),\qquad p_0(X)=1.
 \tag{1}
\]
Fix \(a_1\in(1/2,1)\) and a nonempty index set
\[
 \mathcal J\subset\{j\in\mathbb Z_{\ge0}:j<N(1-a_1)\}.
 \tag{2}
\]
The same indices are retained for every \(a\in[1/2,a_1]\).
In particular \(j<N/2\), so \(p_j(-1)\ne0\).

For a fixed integer \(m\), define the exact row multiplier
\[
 D_{m,j}(a)=
  \frac{X_a^{-mj}p_j(X_a)}
       {X_{1/2}^{-mj}p_j(X_{1/2})}.
 \tag{3}
\]
The cases \(m=0,1\) are respectively the incoming factors of
the original cap and conditional sum.

**Theorem 1.** On the fixed retained index set (2),
\[
 \begin{split}
 D_{m,j}(a)
  &=e^{i\pi(2m-1)j(a-1/2)}R_j(a),\\
 R_j(a)
  &=\prod_{k=1}^{j}
       \frac{\sin\pi(a+k/N)}{\cos(\pi k/N)}>0,\\
 R_j(a)
  &\le
  \exp\left\{-\frac{\pi^2j(j+1)}{2N}(a-1/2)\right\}.
 \end{split}
 \tag{4}
\]
The convention for \(j=0\) is \(R_0=1\).

*Proof.* Every sine in (4) is positive by (2). The identity
\[
 1-e^{-2\pi iz}=2i\,e^{-\pi iz}\sin\pi z
 \tag{5}
\]
gives the first two lines exactly, including the phase contributed
by \(X_a^{-mj}\). For \(j\ge1\),
\[
 \frac{d}{da}\log R_j(a)
   =\pi\sum_{k=1}^{j}\cot\pi(a+k/N).
 \tag{6}
\]
Cotangent decreases on \((0,\pi)\). As \(a\ge1/2\),
\[
 \cot\pi(a+k/N)
  \le-\tan(\pi k/N)\le-\frac{\pi k}{N}.
 \tag{7}
\]
The last inequality follows from \(\tan s\ge s\) on
\([0,\pi/2)\). Since \(R_j(1/2)=1\), integrating (6)--(7)
and summing \(1+\cdots+j=j(j+1)/2\) proves the last line
of (4). \(\square\)

If one allows an endpoint \(a\) with \(a+j/N=1\), the upper
bound still holds by continuity: its left side is zero.
After that point the positive-product argument no longer
applies to the row. No estimate here removes those later rows
from the original finite sum.

## 2. A weighted norm estimate and its precise limitation

Give \(\mathbb C^{\mathcal J}\) any diagonal positive inner product
\[
 \|z\|_w^2=\sum_{j\in\mathcal J}w_j|z_j|^2,\qquad w_j>0.
 \tag{8}
\]
The weights may depend on \(N\) and on other fixed parameters,
but are kept the same at the two incoming coordinates.
Let \(D_m(a)\) be the diagonal operator with entries (3).
Its phase factor in (4) is unitary for (8). If
\(j_{\min}=\min\mathcal J\), Theorem 1 therefore gives
\[
 \|D_m(a)z\|_w
 \le
 \exp\left\{-\frac{\pi^2j_{\min}(j_{\min}+1)}{2N}
                        (a-1/2)\right\}\|z\|_w .
 \tag{9}
\]
For a retained window \(j\ge dN\), with \(d>0\), this implies
\[
                 \|D_m(a)z\|_w
 \le e^{-N\pi^2d^2(a-1/2)/2}\|z\|_w .
 \tag{10}
\]
The same estimates hold for the weighted sum of absolute
values, directly from the componentwise inequality.

For a linear observation \(L(z)=\sum_j b_jz_j\),
weighted Cauchy--Schwarz consequently gives
\[
 |L(D_m(a)z)|
 \le e^{-N\pi^2d^2(a-1/2)/2}
       \left(\sum_jw_j|z_j|^2\right)^{1/2}
       \left(\sum_j\frac{|b_j|^2}{w_j}\right)^{1/2}.
 \tag{11}
\]
There is no comparison with \(|L(z)|\) in (11). The latter
can vanish by cancellation even when both norms are large.
Likewise positivity of \(R_j\) does not make \(L(D_mz)\)
positive: both the initial vector and the observation can
have complex entries, and the modulation in (4) remains.

## 3. Application to the two literal source factors

The complete cap and conditional factors are
\[
 \begin{split}
 U_{0,N}(w,X_a)
   &=\sum_{j=0}^{N-1} H_N(w,r^{-j})\frac{p_j(X_a)}{P_j},\\
 C_{1,N}(X_a,Y)
   &=\sum_{j=0}^{N-1}
          \frac{X_a^{-j}p_j(X_a)p_j(Y)}{P_j^3},
       \qquad P_j=(r;r)_j.
 \end{split}
 \tag{12}
\]
These are the exact original sources of the
[complete half-cap theorem](research_mixed_half_face_complete_cap_packet.md)
and the
[complete conditional continuation](research_mixed_real_arc_complete_conditional_packet.md).

For the part of the first sum on \(\mathcal J\), take the initial
vector
\[
 z_j=H_N(w,r^{-j})p_j(-1)/P_j
 \tag{13}
\]
and apply \(D_0(a)\). For the second sum, take
\[
 z_j=X_{1/2}^{-j}p_j(-1)p_j(Y)/P_j^3
 \tag{14}
\]
and apply \(D_1(a)\). All other factors are unchanged.
Thus (9)--(11) transport actual finite row estimates from the
half-face boundary to the incoming interior, uniformly in any
other parameters for which the initial norms are bounded.
No approximation of \(H_N\), no truncation of its internal
Newton polynomial, and no normalization of a nonzero row is
used.

For example, an established bound
\[
 \sum_{j\in\mathcal J}|z_j|
                    \le C N^B e^{NM}
 \tag{15}
\]
would give, on \(\mathcal J\subset\{j\ge dN\}\),
\[
 \left|\sum_{j\in\mathcal J}D_{m,j}(a)z_j\right|
       \le C N^B
           e^{N\{M-\pi^2d^2(a-1/2)/2\}}.
 \tag{16}
\]
The hypothesis in (15) is an absolute row bound. A bound only
on the signed sum \(\sum_jz_j\) cannot be used in its place.
The asymptotic normalization and any other boundary variables
are those of the supplied initial bound.

The continuous phase counterpart of (6) is also immediate.
For \(0<e<1-a\), put \(I_a(e)=J(a+e)-J(a)\). Then
\[
 \frac{\partial I_a(e)}{\partial a}
    =\log\frac{\sin\pi(a+e)}{\sin\pi a}
    \le\log\cos\pi e
    \le-\frac{\pi^2e^2}{2}.
 \tag{17}
\]
For the first inequality, expand
\(\sin\pi(a+e)/\sin\pi a
 =\cos\pi e+\cot\pi a\,\sin\pi e\);
the second follows by integrating
\((\log\cos s)'=-\tan s\le-s\).
The exact discrete estimate (4) therefore has precisely the
same quadratic loss in the scaled row coordinate.

The retained index condition (2) is essential. To use (16)
for the full cap or conditional factor, one must also bound
the low indices and every original index outside this fixed
window, including rows beyond the incoming numerator wall.
Those separate estimates are not consequences of the
diagonal contraction. This note alone supplies neither a
whole-source lower bound nor a new knot-volume identity.
