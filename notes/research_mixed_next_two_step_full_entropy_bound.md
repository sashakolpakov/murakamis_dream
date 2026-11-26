# The full three-entry entropy bound for the next conditional source

Private source theorem, 9 November 2026. Retaining all three
crossing entries in the exact third Gram moment improves the
half-input estimate further. The resulting positive variational
profile has a unique maximum in the coupled Fourier envelope
at half input and zero frequency. Its half-input constant is
specified by an exact two-variable stationary system. A separate
cubic gives the sharp value of the preceding rowwise estimate.

These are bounds on the complete original source at both parities.
They retain its phases before applying the stated triangle
inequality. No stationary equation below is substituted for the
phase of the quantum source, and no numerical evaluation is used.

## 1. Exact finite source and all three crossing entries

Use the full feature identity of
[the half-input overlap theorem](research_mixed_next_two_step_half_input_overlap.md).
In its notation,
\[
|C^{(2)}_{0\beta,N}(r^b,W)|
 \le \|\mathsf M\mathsf M^*\mathsf M e_b\|_2\,
                         \|\mathsf D_\beta\mathbf f(W)\|_2,
 \qquad \beta=0,1 .                                               \tag{1}
\]
Here \(D=N-1\), \(q=e^{\pi i/N}\), \(r=q^{-2}\),
\(\kappa=q^{D^2/2}\), and
\[
S_j=\prod_{h=1}^j2\sin(\pi h/N),\qquad S_0=1.
\]
The exact original matrix has
\[
\mathsf M_{jk}=\kappa(-1)^j q^{j(k+1)}
                         \frac{S_j}{S_kS_{j-k}}\quad(k\le j),
\]
and is zero otherwise. Consequently, for every \(0\le i,b\le D\),
\[
\boxed{\quad
(\mathsf M\mathsf M^*\mathsf M e_b)_i
 =\kappa(-1)^i
   \sum_{j=b}^D\ \sum_{\ell=0}^{\min(i,j)}
 q^{\,i(\ell+1)+j(b-\ell)}
 \frac{S_iS_j^2}
 {S_b S_\ell^2S_{i-\ell}S_{j-\ell}S_{j-b}} .
\quad}                                                           \tag{2}
\]
Every summand has a positive magnitude, but the displayed phases
remain part of the exact vector. The two indices are not cut off
at a bulk window. In particular \(j=D\), \(\ell=0\), and all
support boundaries are retained.

Write
\[
J(x)=\int_0^x\log(2\sin\pi t)\,dt,\qquad c=-2J(1/6),
\]
\[
E(x,y)=J(x)-J(y)-J(x-y),\qquad
V(y)=-2J((1-y)/2)-J(y),\qquad
R(z)=J(z)-2J(z/2).
                                                                    \tag{3}
\]
These functions extend continuously to their closed intervals
and triangles. The uniform estimate
\(\log S_j=NJ(j/N)+O(\log N)\), including \(j=0,D\),
bounds the magnitude of a summand in (2) by
\[
CN^A\exp N\{E(x,y)+E(z,y)+E(z,a)\},
\quad x=i/N,\ y=\ell/N,\ z=j/N,\ a=b/N.
                                                                    \tag{4}
\]
There are at most \(N^2\) summands and \(N\) output entries.
Since
\[
\max_{y\le x\le1}E(x,y)=V(y),
\]
equations (2)--(4) prove the complete finite bound
\[
\|\mathsf M\mathsf M^*\mathsf M e_b\|_2
 \le CN^A e^{N F(b/N)},                                           \tag{5}
\]
where
\[
\boxed{\quad
P(z)=\max_{0\le y\le z}\{V(y)+E(z,y)\},\qquad
F(a)=\max_{a\le z\le1}\{P(z)+E(z,a)\}.
\quad}                                                           \tag{6}
\]
Thus \(F\) retains the full three-entry entropy. No separate
Hilbert--Schmidt cost \(c\) has been added. Continuity and
compactness in (6), together with the uniform factorial
estimate, make (5) uniform as \(b/N\) tends to one.

The output feature remains the complete one of the
[two-step Gram theorem](research_mixed_next_two_step_gram_fourier_bound.md).
For any fixed compact \(\mathcal K\subset\mathbb C\) and
\(\epsilon>0\),
\[
\|\mathsf D_\beta\mathbf f(W)\|_2
 \le C_\epsilon N^{A_\epsilon}e^{N[B_\beta(W)+\epsilon]},
\]
\[
B_\beta(W)=\max_{0\le s\le1}
 \left\{\int_0^s\log|1-We^{-2\pi iu}|\,du-(1+\beta)J(s)\right\}.
                                                                    \tag{7}
\]
This bound includes all output zeros and the top feature.
Combining (1), (5), and (7) gives
\[
\boxed{\quad
|C^{(2)}_{0\beta,N}(r^b,W)|
 \le C_\epsilon N^{A_\epsilon}
             e^{N[F(b/N)+B_\beta(W)+\epsilon]}.
\quad}                                                           \tag{8}
\]

## 2. The unique positive entropy maxima

The original entropy \(E\) is strictly concave in the open
triangle. Its Hessian is negative definite there, with
determinant \(\pi^2\), as in
[the one-crossing theorem, (4)](research_one_crossing_gaussian_window.md).
Also
\[
V'(y)=-\log(2\sin(\pi y/2)),\qquad
V''(y)=-\frac{\pi}{2}\cot(\pi y/2)<0\quad(0<y<1).
                                                                    \tag{9}
\]
For each \(0<z<1\), the maximizer \(y(z)\) in \(P(z)\)
is unique and lies in \((0,z)\). Indeed the \(y\)-derivative
of \(V(y)+E(z,y)\) tends to \(+\infty\) at zero and to
\(-\infty\) at \(z\), and the second derivative is negative.
The implicit function theorem gives a smooth maximizer.
The Schur complement of the negative definite Hessian shows
that \(P''(z)<0\) on \((0,1)\).

Both \(V(y)\le c\) and \(E(z,y)\le c\) have their unique
maxima at \(y=1/3\) and \((z,y)=(2/3,1/3)\), respectively.
Therefore
\[
P(2/3)=2c,\qquad P'(2/3)=0,\qquad P'(z)<0\quad(2/3<z<1).
                                                                    \tag{10}
\]
Continuity also gives \(P(0)=0\) and \(P(1)=c\).
For \(2/3<z<1\), evaluating the \(y\)-derivative at
\(y=1/3\) and \(y=z/2\) proves
\[
                         \frac13<y(z)<\frac z2 .                  \tag{11}
\]
At the first point the derivative equals
\(\log[\sin\pi(z-1/3)/\sin(\pi/3)]>0\);
at the second it is \(V'(z/2)<0\).

Now fix \(1/2\le a<1\). The function in the second maximum
of (6) is strictly concave in \(z\in(a,1)\). Its derivative
is positive near \(a\) and negative near one. It has a unique
maximizer \(z(a)\), with
\[
              \max\{a,2/3\}<z(a)<(1+a)/2 .                        \tag{12}
\]
For \(a<2/3\), its derivative at \(2/3\) is positive because
\(E(z,a)\) is still increasing there. For \(a\ge2/3\) its
left endpoint is already at least \(2/3\). At
\(z=(1+a)/2\), the \(E\)-derivative is zero while \(P'<0\).
This proves (12). The singular derivative at \(z=a\)
when \(a=2/3\) is interpreted by its positive one-sided limit.

Stationary differentiation in (6) now gives
\[
F'(a)=\log\frac{\sin\pi(z(a)-a)}{\sin\pi a}
 <\log\frac{\sin(\pi(1-a)/2)}{\sin\pi a}=V'(a)<0 .
                                                                    \tag{13}
\]
The strict inequality follows from (12), since
\(0<z(a)-a<(1-a)/2\le1/4\), where sine is increasing.
Integrating (13), and then using continuity at one, yields
\[
\boxed{\quad
F(a)-F(1/2)\le V(a)-V(1/2),\qquad1/2\le a\le1,
\quad}                                                           \tag{14}
\]
strictly when \(a>1/2\). The endpoint value \(F(1)=c\)
comes directly from (6); no singular derivative is substituted
there.

At \(a=1/2\), put \(z_\star=z(1/2)\),
\(y_\star=y(z_\star)\). Then
\[
\frac23<z_\star<\frac34,\qquad
\frac13<y_\star<\frac{z_\star}{2}.
\]
The two exact stationary equations are
\[
\boxed{\begin{split}
\sin\pi(z_\star-y_\star)
 &=2\sin(\pi y_\star/2)\sin(\pi y_\star),\\
\sin^2(\pi z_\star)
 &=-\cos(\pi z_\star)\sin\pi(z_\star-y_\star).
\end{split}}                                                     \tag{15}
\]
They uniquely specify the positive entropy maximum in this
rectangle, by the strict concavity just proved. All factors
in (15) have their indicated positive real signs. In particular
\[
F(1/2)=V(y_\star)+E(z_\star,y_\star)+E(z_\star,1/2).
                                                                    \tag{16}
\]
These are entropy maximizers, not roots chosen for the
original complex stationary phase.

## 3. The sharp preceding rowwise constant

For comparison, the unrelaxed rowwise proof of the half-input
overlap theorem has constant
\[
c+S(1/2),\qquad
S(1/2)=\max_{1/2\le z\le1}\{R(z)+E(z,1/2)\}.                      \tag{17}
\]
Its strictly concave maximand has a unique critical point
\(\widehat z\in(2/3,3/4)\), satisfying
\[
2\cos(\pi\widehat z/2)\sin(\pi\widehat z)
                                      =-\cos(\pi\widehat z).
                                                                    \tag{18}
\]
Put \(x=(1-\widehat z)/2\) and \(v=\sin^2(\pi x)\).
Then \(1/8<x<1/6\), and (18), with its positive signs, is
\[
4v\sqrt{1-v}=1-2v.
\]
Squaring gives the cubic
\[
16v^3-12v^2-4v+1=0.                                               \tag{19}
\]
There is exactly one root in \((0,1/4)\): the polynomial
has negative derivative there, positive value at zero,
and negative value at \(1/4\).
More sharply, its values at \(1/6,1/5\) are respectively
\(2/27\) and \(-19/125\), so
\[
                            \frac16<v<\frac15 .                   \tag{20}
\]
In this interval both sides of the unsquared equation are
positive, so (19) introduces no sign ambiguity.
Equivalently \(w=4v-1\) satisfies \(w^3-7w-2=0\)
on the corresponding interval.

Reflection and sine duplication for \(J\) give the explicit value
\[
S(1/2)=-J(2x)-2J(x)-J(1/2-2x).                                   \tag{21}
\]
No numerical root or integral value is used in this description.

The full bound is strictly better than this sharp rowwise one.
For \(0<z<1\), one has
\[
P(z)\le c+R(z),
\]
and equality requires simultaneously \(y=1/3\), the unique
maximum of \(V\), and \(y=z/2\), the unique maximum of
\(E(z,y)\). It therefore occurs only at \(z=2/3\) in that
open interval.
Since \(z_\star>2/3\), (16)--(17) imply
\[
F(1/2)<c+S(1/2)
 \le2c+V(1/2)-\frac{\pi}{720}.                                    \tag{22}
\]
The final inequality is the proved quadratic overlap estimate;
the first is a further strict improvement without numerical
optimization.

There is also a simple lower benchmark for this positive
majorant. The admissible point \(y=1/3,z=2/3\) has value
\[
2c+E(2/3,1/2)=2c+\frac{5c}{6}=\frac{17c}{6}.
\]
The derivative in \(z\) is positive there, so
\[
                              F(1/2)>\frac{17c}{6}.               \tag{23}
\]
This is a lower bound for the triangle majorant, not for the
signed matrix element or the conditional polynomial.

## 4. Exact maximum of the attached Fourier envelope

Retain the complete transition entropy \(\mathcal H\), the
selected observation rate \(\Gamma\), and the exact source
identities of the two-step Gram theorem. Its endpoint inequality,
together with (14), gives
\[
\begin{split}
F(1/2+x)+\mathcal H(x,t)+\Gamma(1/2-t)
 &\le F(1/2)-V(1/2)\\
 &\quad+V(1/2+x)+\mathcal H(x,t)+\Gamma(1/2-t)\\
 &\le F(1/2)+\Gamma(1/2),
 \qquad 0\le t\le x\le1/2 .
\end{split}                                                       \tag{24}
\]
Equality holds exactly at \(x=t=0\). Thus the maximum of the
full positive three-entry/Fourier envelope is
\[
                         F(1/2)+B_\beta(W)+\Gamma(1/2).            \tag{25}
\]

Put \(M=\lceil N/2\rceil\), \(U=D-M\).
The unchanged exact observation is
\[
(\mathsf T_{0\beta}\mathcal R_N^+)(w,W)
 =\frac1{\kappa^2N}\sum_{k=0}^U\mathcal O_{N,k}(w)
 (-1)^{M+k}\sum_{d=k}^Uq^{M+d}\beta_{d,k,N}
                                  C^{(2)}_{0\beta,N}(r^{M+d},W).
                                                                    \tag{26}
\]
All complete kernels, both Fourier sectors, full Hermite normals,
the odd simple node and the last physical row remain in (26).
Apply (8), the endpoint-uniform transition weights, and the
all-real-color observation bound to this identity. At odd levels
\((M+d)/N\) exceeds \(1/2+d/N\) by \(1/(2N)\);
by (13) this only improves the upper bound. The at most
\(N^2\) terms and the original scalar \(\kappa^{-2}/N\)
give, for any compact \(\mathcal K\subset\mathbb C\) and
\(\epsilon>0\),
\[
\boxed{\quad
\sup_{w\in[-2,2]}
|(\mathsf T_{0\beta}\mathcal R_N^+)(w,W)|
 \le C_\epsilon N^{A_\epsilon}
 e^{N[F(1/2)+B_\beta(W)+\Gamma(1/2)+\epsilon]},
 \quad W\in\mathcal K,\quad\beta=0,1 .
\quad}                                                           \tag{27}
\]
The same bound holds for the sum of the absolute complete
Fourier-mode contributions.

This is the exact maximum of the particular full-entry
triangle profile (4), not a claim that this profile is sharp
for the signed source. In particular (23) is not a failure
of the actual attachment. For the actual next reference the
remaining comparison for this bound is with the original
four-block conditional action in
[the local-source theorem](research_mixed_next_four_block_local_source_and_gram_comparison.md).
No sign of that correlated difference is established by
(15), (19), or (27). The propagated left remainder and the
next contour complement remain separate full-source obligations.

## Frozen source versions

- Exact third-moment source and the quadratic overlap bound:
  3f38dc436b48e0cef7d9217d0dce99940c84317b934d286b592d5a9940686c19.
- Complete output profile, Fourier source and endpoint comparison:
  be5dc00fde7c062f7b6ad0e7b8859b2e9dd5d564f16bce0aea75de9dba12cb6e.
- Original crossing coefficients, strict entropy Hessian and
  uniform factorial endpoints:
  d5d8611da7158539ee73af5413ab2f59da50afe5d3d43dcf2631f4c28f373683.
- Actual four-block local source and conditional action:
  c62f1cca0fbfe5bfe619824ca3fc3ce70af50176b623b82004848bf59a24f8ca.

