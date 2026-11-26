# Extending the real zero collar to an adjacent angle as small as one tenth

Research proof, 4 November 2026. The 256-bit certificate passes all
64 reference boundary products on 975 cells, 18 scalar comparisons,
two endpoint-source records and the original collar record. The
source estimates below are unchanged established inputs. The original
zero-collar artifacts remain unchanged.

## 1. Statement and original source

Use the literal finite kernel
\[
 C_{\epsilon,N}(X,Y)=\sum_{j=0}^{N-1}
       \frac{X^{-j}p_j(X)p_j(Y)}{P_j^{2+\epsilon}},\qquad
 p_j(X)=(r_NX;r_N)_j,\quad P_j=(r_N;r_N)_j,
 \quad r_N=e^{-2\pi i/N},                                   \tag{1}
\]
and the original degree-less-than-\(N\) Fourier polynomial
\(d_N(r_N^j)=P_j^{-1}\). Put \(L=1/1000\) and
\[
 \mathcal C_*=
 ([0,L]\times[1/10,1/2])\ \cup\
 ([1/10,1/2]\times[0,L]).                                   \tag{2}
\]
Both target heights are zero.

For \(\eta,\epsilon\in\{0,1\}\), let the independent reference
pair \(r=(a,b)\) range over
\[
 R_{3+\eta}\times R_{3+\epsilon},\qquad
 R_3=[.30,.39]+i[-.03,.02],\quad
 R_4=[.27,.33]+i[-.057,-.02].                                \tag{3}
\]
The normalized original allocated phase and its complex tangent are
\[
 \begin{split}
 g(z)&=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},\\
 \Phi(a,b)&=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias
            -(1+\eta/2)g(a)-(1+\epsilon/2)g(b),\\
 \Gamma_r(t)&=\Phi(r)+\Phi_a(r)(t_1-a)+\Phi_b(r)(t_2-b).
 \end{split}                                               \tag{4}
\]
Here \(s\) is the original zero-lift conditional root, holomorphic
on a neighborhood of the entire reference product by the established
[endpoint source theorem](research_mixed_all_endpoint_support.md).

**Theorem 1.** Uniformly over (2)--(3), at both integer parities,
\[
 \left(\sum_{j=0}^{N-1}
  \left|\frac{X^{-j}p_j(X)p_j(Y)}{P_j^{2+\epsilon}}\right|\right)
 |d_N(X)|^{\eta/2}|d_N(Y)|^{\epsilon/2}
 \le C N^A\exp N\{\Re\Gamma_r(t)-3/50\},                   \tag{5}
\]
where \(X=e^{-2\pi it_1}\), \(Y=e^{-2\pi it_2}\).
In particular, (5) bounds the original kernel modulus. All selected
frequency factors have unit modulus here, so every selection is
included. The low angle may equal zero or depend on the integer
level; the other angle includes both endpoints of its closed interval.

## 2. The unchanged zero-uniform source estimates

Write \(J(u)=\Re g(u)\), extended periodically, and set
\[
 \nu_L=-J(L)>0,\qquad \Delta_L=L\log2-J(L).
\]
Sections 2--4 of the
[original real zero-collar proof](research_mixed_real_zero_collar.md)
establish the following estimates for every original row, uniformly
through all product zeros:
\[
 \frac{|p_j(e^{-2\pi ix})|}{|P_j|}
        \le C N^A e^{N\Delta_L}
 \quad(0\le j<N,\ 0\le x\le L),\qquad
 \sup_{0\le x\le L}|d_N(e^{-2\pi ix})|
        \le C N^A e^{N\nu_L}.                              \tag{6}
\]
The first follows from
\(J(u+x)-J(u)-J(x)\le\Delta_L\) and the zero-uniform
truncated-log product estimate. The second uses the exact downward
forced recurrence
\[
 d_N(r_N^{-1}X)=(1-X)d_N(X)+
                         \frac{X}{N^2}\sum_{q=0}^{N-1}X^q,
\]
starting on a fixed compact interval near \(L\); its forcing is
retained. Neither estimate refers to the other target angle.

Let \(\alpha\) be the low target type indicator and \(\beta\) the
other target type indicator. The complete height-zero, slope-zero
endpoint source constants are
\[
 \begin{array}{c|rrrr}
 (\epsilon,\beta)&(0,0)&(0,1)&(1,0)&(1,1)\\\hline
 B_{\epsilon\beta}&.325066&.386681&.460764&.515591.
 \end{array}                                               \tag{7}
\]
They bound the entire row and other-angle supremum
\[
 \sup_{0\le u,y\le1}
 \{J(y+u)-J(y)-(1+\epsilon)J(u)
                      +\tfrac\beta2\max(-J(y),0)\}.
                                                               \tag{8}
\]
Thus lowering the other target endpoint from .22 to .1 does not change
these constants. The existing absolute Fourier estimate applies on
the compact interval \([.1,.5]\), retaining its forcing branch at
.5. Allocate a fixed exponent tolerance at most \(10^{-5}\) to this
other halfweight. Formulae (6)--(8) then give the same raw exponent
as in the original collar:
\[
 B_{\epsilon\beta}+\Delta_L+\frac\alpha2\nu_L+10^{-5}.
                                                               \tag{9}
\]
The finite row sum adds only a polynomial factor. The real chirp in
(1) has modulus one in both orientations.

## 3. The new reference comparison

Let \(c=0\) when the low coordinate is first and \(c=1\) when it
is second. Thus
\((\alpha,\beta)=(\eta,\epsilon)\) for \(c=0\), and
\((\alpha,\beta)=(\epsilon,\eta)\) for \(c=1\).
Use the following rational source ceilings \(S\) and plane floors
\(P=S+61/1000\):
\[
 \begin{array}{cc|cc|cc}
 \eta&\epsilon&S_{\eta\epsilon0}&P_{\eta\epsilon0}
                         &S_{\eta\epsilon1}&P_{\eta\epsilon1}\\\hline
 0&0&.332&.393&.332&.393\\
 0&1&.523&.584&.471&.532\\
 1&0&.335&.396&.394&.455\\
 1&1&.526&.587&.526&.587
 \end{array}                                               \tag{10}
\]
The original endpoint-source records and outward scalar checks verify
that (9) is strictly below the relevant \(S\). The new geometric
certificate verifies
\[
                 \Re\Gamma_r(t)>P_{\eta\epsilon c}
                                                               \tag{11}
\]
on the full reference product and corresponding target rectangle.
Since \(P-S=.061>.06\), these two strict inequalities prove (5).

Here is the complete reduction used for (11). For a fixed reference,
\(\Re\Gamma_r(t)\) is affine in both real target coordinates.
It suffices to test the four target corners
\((x,y)\in\{0,L\}\times\{.1,.5\}\), in each orientation.
For a fixed target, \(\Gamma_r(t)\) is holomorphic in both
reference variables. The branch exists on the full closed product
before successive harmonic minimum principles are applied.
Therefore it suffices to test every product of two rectangle sides.
There are four ordered type pairs and sixteen side products per pair,
giving 64 domains; no reference corner sampling replaces this cover.

On each two-parameter boundary cell the certificate encloses the
original root by an affine logarithmic Newton self-map. It evaluates
the tangent at the center and uses its exact reference derivative
\[
 d_r\Gamma_r(t)=
       \sum_{j,k}\Phi_{jk}(r)(t_j-r_j)\,dr_k                 \tag{12}
\]
for an outward full-cell mean-value bound. Both orientations and all
eight target corners are tested on every cell. Exact prefix-free
binary covers of mass one exhaust each side product. The checker
also requires the exact set of all 64 distinct typed products and
validates the original source, collar and dependency bindings before
and after the run.

## 4. Scope and reproduction

This is a zero-uniform raw upper bound on real targets. It neither
supplies a nonzero coefficient at zero nor estimates nonzero target
heights. It can be combined with separate compact real-target estimates
by overlapping their domains. No whole-period, arbitrary mixed-core,
or knot volume conclusion follows from this local comparison alone.

```sh
python3 experiments/certify_mixed_real_zero_collar_extension.py --precision 256
```
