# One angle-weighted path for the local geometric sources

21 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

The same explicit path works for the original trivalent tensor and
for the two-boundary crossing kernel: damp a leg of angle \(x\) by
\(r^x\). Every strict positive prism remains on the growing side of
its initialized action along this path. The crossing theorem already
establishes the corresponding statement for every strict tetrahedron.
Thus these two local building blocks can use one rule for their
radial parameters.

This is a local source theorem. It does not identify the parameters
on adjacent pieces, deform a whole Conway coefficient cycle, or
evaluate its final marked closing.

## 1. The full prism action and the path

Let
\[
 \mathcal P=\{(x_1,x_2,x_3):
 x_i>0,\quad x_i+x_j<1\ (i\ne j),\quad
 S:=x_1+x_2+x_3>1\}.
 \tag{1}
\]
In particular \(x_i<1\), \(1<S<3/2\), and at most one
\(x_i\) exceeds \(1/2\). Use the initialized action
\[
 \Psi(\mathbf t)=-\frac{\pi}{12}
 +\frac1{2\pi}\left[
 \sum_i\operatorname{Li}_2(-t_i)
 +\operatorname{Li}_2(-t_1t_2t_3)
 -\sum_{i<j}\operatorname{Li}_2(t_it_j)\right].
 \tag{2}
\]
The branches start from the power series on the unit polydisk.
For \(0<r\le1\), put
\[
                    t_i(r)=-r^{x_i}e^{-2\pi i x_i}.
 \tag{3}
\]
At \(r=1\), every dilogarithm argument in (2) avoids one,
by (1), so the indicated boundary values are regular.

**Theorem.** For every \(\mathbf x\in\mathcal P\),
\[
                  -\operatorname{Im}\Psi(\mathbf t(r))>0
                                      \qquad(0<r\le1).
 \tag{4}
\]
The positive height has a positive lower bound when
\(\mathbf x\) varies in a compact subset of \(\mathcal P\)
and \(r\in[r_0,1]\), for any fixed \(r_0>0\).

Here “growing” means precisely (4): the modulus of
\(e^{iN\Psi}\) is \(e^{-N\operatorname{Im}\Psi}>1\).
No assertion uniform down to \(r=0\) is included.

## 2. Two elementary properties of the radial Clausen function

Define
\[
 F_\rho(u)=-\operatorname{Im}
                    \operatorname{Li}_2(\rho e^{-2\pi iu}),
                         \qquad 0<\rho\le1.
 \tag{5}
\]
It is periodic in \(u\), has
\(F_\rho(1-u)=-F_\rho(u)\), and vanishes at \(0,1/2\).
For \(0<u<1/2\), differentiation gives
\[
 \begin{split}
 \partial_u^2F_\rho(u)
   &=-\frac{4\pi^2\rho\sin(2\pi u)}
                {1-2\rho\cos(2\pi u)+\rho^2}<0,\\
 \partial_{\log\rho}F_\rho(u)
   &=\arg(1-\rho e^{-2\pi iu})>0,\\
 \partial_{\log\rho}^2F_\rho(u)
   &=\frac{\rho\sin(2\pi u)}
                {1-2\rho\cos(2\pi u)+\rho^2}>0.
 \end{split}
 \tag{6}
\]
The branches are those in the disk; the conclusions at \(\rho=1\)
follow by continuity on the open angle interval. Thus \(F_\rho\)
is positive and strictly concave in the angle, increasing in the
radius, and convex in its logarithm. For fixed \(r\), it follows
that \(e\mapsto F_{r^e}(u)\) is convex for \(e>0\).

Substitution in (2) expresses the height to be proved positive as
\[
 H:=-2\pi\operatorname{Im}\Psi(\mathbf t(r))
 =\sum_iF_{r^{x_i}}(x_i)+F_{r^S}(S-1)
                     -\sum_{i<j}F_{r^{x_i+x_j}}(x_i+x_j).
 \tag{7}
\]
The exponent of the triple radius is \(S\), although its reflected
angle is \(S-1\). This distinction is retained throughout the proof.

## 3. Proof on the whole strict prism domain

If all \(x_i\le1/2\), each pair satisfies
\(x_i+x_j=S-x_k>1/2\). Every single term in (7) is nonnegative,
each subtracted pair term is positive after its minus sign, and
\(0<S-1<1/2\) makes the triple term positive. Hence \(H>0\).

Otherwise relabel the unique large angle as
\[
 a=x_1=1-\delta>1/2,\qquad b=x_2,\quad c=x_3,
 \qquad s=b+c,\quad u=s-\delta,\quad
 p=\delta-b,\quad q=\delta-c.
 \tag{8}
\]
The strict prism conditions give
\[
 0<u<b,c<\delta<1/2,\quad p,q>0,\quad
 b=u+q,\ c=u+p,\ \delta=u+p+q,\ s=2u+p+q.
 \tag{9}
\]
Reflection in (5) turns (7) into
\[
 \begin{split}
 H={}&F_{r^b}(b)+F_{r^c}(c)-F_{r^a}(\delta)
       +F_{r^{1+u}}(u)\\
    &+F_{r^{1-p}}(p)+F_{r^{1-q}}(q)-F_{r^s}(s).
 \end{split}
 \tag{10}
\]
If \(s\ge1/2\), its last term has the favorable sign.
Since \(a>b,c\), radius monotonicity and strict angle concavity
give
\[
 \begin{split}
 F_{r^b}(b)+F_{r^c}(c)-F_{r^a}(\delta)
 &\ge F_{r^a}(b)+F_{r^a}(c)-F_{r^a}(\delta)\\
 &>F_{r^a}(u)>0.
 \end{split}
 \tag{11}
\]
Here \(b+c=\delta+u\), and \((b,c)\) is strictly less
separated than \((u,\delta)\). All other positive terms
in (10) have angles in \((0,1/2)\), so this settles that case.

Suppose now \(s<1/2\). Set \(f(e)=F_{r^e}(\delta)\),
a convex function of \(e>0\). The positive terms in (10)
have the following angle weights and radius exponents:
\[
 \begin{array}{c|ccccc}
 \text{angle weight }w&b&c&u&p&q\\
 \text{radius exponent }e&b&c&1+u&1-p&1-q .
 \end{array}
 \tag{12}
\]
Every weight is strictly between zero and \(\delta\).
Strict angle concavity, including its comparison with the larger
angle \(s>\delta\), yields
\[
 H>\frac1\delta\left[
        \sum_{(w,e)\ {\rm in}\ (12)} w f(e)
                           -\delta f(a)-s f(s)\right].
 \tag{13}
\]
Indeed \(F_{r^e}(w)>(w/\delta)F_{r^e}(\delta)\) for
\(w<\delta\), while
\(F_{r^s}(s)<(s/\delta)F_{r^s}(\delta)\).

The bracket is nonnegative by a direct convexity comparison.
The first two exponents in (12) lie below \(s\); the other
three lie above \(a=1-\delta\). Since \(s<1/2<a\), they
all lie outside \([s,a]\). The secant line through
\((s,f(s))\) and \((a,f(a))\) lies below \(f\) outside
that interval. The positive weights and their first moments obey
\[
 \begin{split}
 \sum w&=\delta+s,\\
 \sum we
 &=b^2+c^2+u(1+u)+p(1-p)+q(1-q)
   =\delta(1-\delta)+s^2=\delta a+s^2.
 \end{split}
 \tag{14}
\]
For the second identity, both sides are
\(\delta+3u^2+2u(p+q)\), by (9).
Summing the secant-line inequalities with these weights
therefore gives
\[
                         \sum w f(e)\ge\delta f(a)+s f(s).
 \tag{15}
\]
Equations (13)--(15) prove \(H>0\).
This also covers \(r=1\): then \(f\) is constant, but
the strict angle inequality in (13) remains strict.
Continuity proves the compact uniformity in the theorem.

## 4. Consequences for the original local sources

Fix
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad
 \kappa=q^{d^2/2}.
\]
The full-prism transport theorem applies to (3), since its three
moduli remain in a fixed positive compact interval when
\(r\in[r_0,1]\). Uniformly on the compact families above,
\[
 \mathcal C_N(\mathbf t(r))
 =\kappa e^{i\pi/4-\pi i/(2N)}
     \prod_{i<j}(1-t_it_j)^{-1/2}
                    e^{iN\Psi(\mathbf t(r))}(1+O(N^{-1})).
 \tag{16}
\]
Thus the original source is nonzero at all sufficiently large levels,
uniformly along every such compact family of paths. This includes
both parities and level-dependent approaches to the unit norm walls;
it does not include a uniform origin layer.

The crossing endpoint theorem proves the same path rule for its
two angles \(b,c>0,\ b+c<1\):
\[
                 y(r)=-r^b e^{-2\pi ib},\qquad
                 z(r)=-r^c e^{-2\pi ic}.
 \tag{17}
\]
Its initialized action is
\[
 \Psi_0(y,z)=-\frac{\pi}{12}
       +\frac{\operatorname{Li}_2(-y)+\operatorname{Li}_2(-z)
                              -\operatorname{Li}_2(yz)}{2\pi}.
\]
The proved positive height on (17) gives the actual positive-crossing
kernel
\[
 \mathcal K_N^+(y,z)
 =\sqrt N\,\kappa e^{i\pi/4-\pi i/(4N)}
        (1-yz)^{-1/2}e^{iN\Psi_0(y,z)}(1+O(N^{-1}))
 \tag{18}
\]
on strict tetrahedron compacts and \(r\in[r_0,1]\).
Its inverse uses the exact reciprocal/conjugate chart and monomial
specified in that theorem, not a phase change in the same chart.

The local rule \(\log|t_i|=x_i\log r\) is linear in the
angles. Nothing above identifies its parameters on a shared
edge of a whole expression or turns it into a source-preserving
global contour. Complete boundary-vector transport, complementary
packet tails, attachment polarizations and the final marked
closing remain to be controlled. No knot-volume or finite-exception
theorem follows from (16)--(18) alone.

## Complete proof sources

Both entire matching proof texts were read:

| Source | SHA-256 |
|---|---|
| [Full initialized prism source transport](research_centered_tensor_full_prism_source_transport.md) | eb43e287eca5933b70de3b6362a81f92d46bb2e121f0eb5716793c107adaef10 |
| [Actual signed-crossing endpoint source](research_centered_signed_crossing_endpoint_source.md) | 40adef586a0c2c5c418caf5c8ea120391cf0ba308a7f7b2ad6649be044a77154 |

The second source already proves the two-leg angle-weighted path.
The additional result here is its extension to the whole strict
prism by the weighted secant comparison (12)--(15). No novelty
is claimed for the elementary concavity or convexity inequalities.

Only written mathematics and text/hash operations were used. No
mathematical program, numerical experiment, test, build, git operation
or earlier-final edit was performed.
