# The retained three-crossing packet on a directed wire tube

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

This quantifies the neighborhood in the
[retained-vertex theorem](research_traced_three_vertex_endpoint.md),
Theorem 7. The tube is the same one as the actual
[complete-cap packet](research_homogeneous_wire_complete_cap.md),
Section 6. The estimates retain the original finite index complement,
both cotangent aliases and all contour sides. They do not identify
the entire wire cycle of an open chain with its local saddle.

## 1. The source theorem

Put
\[
 x_h=\frac16+\frac{i\log2}{2\pi},\qquad
 \mathcal D=\left\{x_h+(1-\tfrac45i)u+iv:
 0\le u\le\frac{13}{1000},\quad
 -\frac3{2000}\le v\le\frac1{1000}\right\}.
 \tag{1}
\]
Keep the original matrices, cardinal vector and corner deletion
\(\widetilde A=JM^3-M^TP_LJM P_LM\),
\(L=\lfloor N/50\rfloor\), from the retained-vertex theorem.
For \(X=e^{2\pi ix},Y=e^{2\pi iy}\), the exact source is
\[
 \widetilde V_N(x,y)=\kappa c_xc_y
 \sum_{\substack{i,j\ge0,\ i+j<N\\\max(i,j)>L}}
 \frac{X^iY^j(Q^{-1};Q^{-1})_{i+j}}
 {(X;Q^{-1})_{i+1}(Y;Q^{-1})_{j+1}},
 \quad c_x=N^{-1}e^{-\pi i(N-1)x}(1-X^N).
 \tag{2}
\]

**Theorem 1.** On a fixed open complex neighborhood of
\(\mathcal D\times\mathcal D\),
\[
 \widetilde V_N(x,y)=
 \kappa N^{-1/2}a(x,y)e^{N\Phi(x,y)}\{1+O(N^{-1})\}.
 \tag{3}
\]
The functions \(\Phi,a\) are holomorphic and \(a\) is nowhere zero.
The error is uniform with each fixed parameter derivative after
factoring the displayed packet. This holds at both parities, without
a congruence restriction on \(N\). The branches and amplitude are
those of the original retained-vertex theorem.

Thus the actual cap and retained vertex have an explicit common
parameter domain. Their local composition still requires its coupled
stationary point and wire contour. No full-chain coefficient follows
merely from (3).

## 2. Critical branch and compact inequalities

Use
\[
 \begin{split}
 F(s,t;X,Y)={}&\mathcal J(s+t)+\frac{i\pi}{2}\{s+t-(s+t)^2\}
            +s\log X+t\log Y-I_X(s)-I_Y(t),\\
 I_X(s)={}&\frac{\operatorname{Li}_2(Xe^{-2\pi is})
                       -\operatorname{Li}_2(X)}{2\pi i}.
 \end{split}
 \tag{4}
\]
The branches continue from the homogeneous point. Set
\[
 \begin{split}
 \alpha&=X^{-1}-1,\quad\beta=Y^{-1}-1,\quad
 \Delta=1-2(\alpha+\beta)+(\alpha-\beta)^2,\\
 U_c&=(1+\alpha-\beta-\sqrt\Delta)/2,\quad
 V_c=(1-\alpha+\beta-\sqrt\Delta)/2,\\
 s_c&=i\Log U_c/(2\pi),\quad t_c=i\Log V_c/(2\pi),
 \qquad F_c=F(s_c,t_c;X,Y).
 \end{split}
 \tag{5}
\]
The outward certificate described in Section 5 proves
\[
 \begin{gathered}
 \Im\Delta>0,\quad U_c,V_c\text{ in the lower-left quadrant},\\
 \Re X,\Im X,\Re Y,\Im Y>2/25,\quad |X|,|Y|<27/50,\\
 3/10<\Re s_c,\Re t_c<2/5,\quad
 |\Im s_c|,|\Im t_c|<3/200,\quad \Re F_c>-7/100.
 \end{gathered}
 \tag{6}
\]
The principal square root in (5) is therefore valid throughout the
parameter domain. The
[central-index branch lemma](research_three_vertex_central_index_chart.md)
proves the actual equations \(F_s=F_t=0\), including their logarithmic
lifts, and excludes the other algebraic branch from the original
triangle. Its curvature theorem gives
\[
 -\Re F''\succ(9/100)I
 \quad\text{on}\quad
 1/4\le\Re s,\Re t\le9/20,\quad
 |\Im s|,|\Im t|\le1/50.
 \tag{7}
\]
The wider box of that theorem contains a neighborhood of this box.

Let \(B=[1/4,9/20]\), \(h=1/50\),
\(\mathcal R=B+i[-h,h]\). The remaining certified inequalities are:

* For real indices in each of
\[
 \begin{split}
 E_0&=\{0\le s\le1/50,\ 1/50\le t,\ s+t\le99/100\},\\
 E_1&=\{1/50\le s\le1/4,\ 0\le t,\ s+t\le99/100\},\\
 E_2&=\{s=9/20,\ 0\le t\le54/100\},
 \end{split}
 \tag{8}
\]
one has \(\Re(F_c-F)>1/200\).
* On each product of two sides of \(\partial\mathcal R\), when
at least one side is vertical,
\[
                         \Re(F_c-F)>1/1000.
 \tag{9}
\]
* On the four horizontal-side products,
\[
                         \Re(F-F_c)<1/20.
 \tag{10}
\]

These statements hold independently for all \(x,y\in\mathcal D\).
They are full compact-domain bounds, not sampled inequalities.

## 3. The entire original real-index complement

For real indices write \(H=\Re F\). Its derivative is
\[
 H_s=\log\frac{2|X|\sin\pi(s+t)}{|1-Xe^{-2\pi is}|}.
 \tag{11}
\]
This is negative for \(s\ge9/20,t\ge0,s+t<1\).
Indeed, for \(9/20\le s\le9/10\), the rotated argument
\(\arg X-2\pi s\) belongs to \((-3\pi/2,-\pi/2)\), so
\[
 |1-Xe^{-2\pi is}|\ge\sqrt{1+|X|^2}>2|X|,
 \qquad |X|<27/50<1/\sqrt3.
 \tag{12}
\]
For \(s\ge9/10\), the numerator is at most
\(2(27/50)\pi/10<1-27/50\), while the denominator is at
least \(1-|X|\). Every high-index part below \(s+t=99/100\)
therefore reduces, at fixed \(t\), to \(E_2\).
Interchange the indices and parameters for the other high strip.
Together with \(E_0,E_1\), this covers the retained complement of
\(B^2\) below the top collar. The deleted corner matters: if
\(s\le1/50\), a retained partner has \(t>1/50\), as required in
\(E_0\).

For the top collar the following elementary bounds suffice:
\[
 \begin{gathered}
 |X|,|Y|\le\tfrac12e^{2\pi(119/10000)}<r=27/50,\quad
 \log r<-3/5,\\
 \operatorname{Li}_2(r)\le r+r^2/4+\frac{r^3}{9(1-r)}<2/3.
 \end{gathered}
 \tag{13}
\]
Consequently \(|I_X(s)|,|I_Y(t)|<2/(3\pi)<2/9\).
For \(\delta=1/100\), use \(2\sin\pi u\ge4u\) on
\([0,\delta]\), and \(\log25<10/3\). On \(s+t\ge99/100\)
this gives \(\mathcal J(s+t)\le-\mathcal J(\delta)<13/300\).
Therefore
\[
 H\le-\frac35\frac{99}{100}+\frac49+\frac{13}{300}
       <-\frac7{100}-\frac3{100}<\Re F_c-\frac3{100}.
 \tag{14}
\]
The original uniform sine-factorial entropy estimate, including its
finite endpoints, and the nonvanishing denominator products now put
the entire finite complement below
\(\operatorname{poly}(N)e^{N(\Re F_c-\delta_0)}\), for a fixed
\(\delta_0>0\). The \(O(N^{-1})\) locations of the actual corner
and half-grid cuts preserve these strict gaps. Near the top endpoint
the sine-factorial estimate already allows its logarithmic endpoint
error. No complex interpolation of that endpoint is used.

## 4. Exact cotangent contours and the coefficient

On \(\mathcal R^2\), the exact interpolation of (2) is equation (51)
of the retained-vertex theorem, using the exact sine factorial and
the [finite-root Pochhammer interpolation](research_root_pochhammer_interpolation.md).
It has the holomorphic symbol
\[
 \mathcal T_N(s,t)=N^{1/2}g(s,t;X,Y)e^{NF(s,t;X,Y)}
                      \{1+O(N^{-1})\},\qquad
 g=\frac{\sqrt{2\sin\pi(s+t)}e^{-i\pi(s+t)/2}}
 {\sqrt{(1-X)(1-Xe^{-2\pi is})(1-Y)(1-Ye^{-2\pi it})}}.
 \tag{15}
\]
All factors are nonzero on a fixed neighborhood of this box:
\(|X|e^{2\pi h}<1\) and \(1/2\le\Re(s+t)\le9/10\).
Thus the deformed analytic interpolation matches the original
finite summands exactly.

Choose the vertical sides at physical half-grid locations within
\(O(N^{-1})\) of the ends of \(B\). The double cotangent residue
formula then recovers exactly the central summands in (2).
On a vertical half-grid side the cotangent is bounded. Equation (9)
bounds every such current, including products with a horizontal side.
The maximum principle in the other index also bounds the side currents
created when that other contour moves inside \(\mathcal R\).
All strict margins survive the half-grid perturbations.

On a horizontal side at height \(\pm h\), the nonconstant part of
\(\cot(\pi Ns)\) is \(O(e^{-2\pi Nh})\). Thus every product
containing at least one nonconstant part is strictly smaller, by (10):
\[
                         2\pi h-1/20>7/100.
 \tag{16}
\]
The four constant products combine with precisely coefficient \(N^2\)
and the original positive residue orientation. By (9) their integrals
may all move to the horizontal plane through \((s_c,t_c)\), whose
heights lie inside \([-h,h]^2\). Strict concavity (7) gives the
unique maximum and uniform tails there. Analytic Gaussian integration
then yields
\[
 \sum_{\text{retained indices}}\mathcal T_N(i/N,j/N)
 =\frac{2\pi N^{3/2}g(s_c,t_c;X,Y)}
              {\sqrt{\det(-F''(s_c,t_c))}}
                 e^{NF_c}\{1+O(N^{-1})\}.
 \tag{17}
\]
This exact half-grid calculation applies at every level. The first
Gaussian correction is odd, so the relative error is \(O(N^{-1})\);
holomorphic centered Gaussian coordinates make the estimate uniform
in the parameters.

After multiplication by \(\kappa c_xc_y\), (3) has
\[
 \Phi=F_c-\tfrac12(\log X+\log Y),\qquad
 a=\frac{2\pi\sqrt{XY}\,g(s_c,t_c;X,Y)}
                 {\sqrt{\det(-F''(s_c,t_c))}}.
 \tag{18}
\]
Accretivity makes the determinant nonzero. The square roots continue
from the normalized homogeneous value, unambiguously on this simply
connected parameter domain. The factors \((1-X^N)(1-Y^N)\) differ
uniformly from one exponentially. Every bound used above is strict on
a compact set, so it persists on an open neighborhood of
\(\mathcal D^2\). Cauchy's estimate on a smaller such neighborhood
gives the fixed holomorphic derivative bounds. \(\square\)

## 5. Outward verification and independent replay

The [author checker](../experiments/certify_three_vertex_directed_packet.py)
and [artifact](../repro/results/research-three-vertex-directed-packet.json)
certify 321 domains. One four-dimensional parameter domain checks
the branch and critical enclosures in (6).
For the other assertions \(\Re(F_c-F)\), or \(\Re F_c\), is harmonic
separately in each wire variable. The minimum principle reduces
each parallelogram to its four boundary segments. All 16 ordered
pairs of wire segments are included. There are 16 action-floor
domains, 48 exterior domains (8), and 256 products of index-boundary
segments and wire faces. Exchanging indices and parameters supplies
the symmetric real-index complements without requiring \(x=y\).

The real-index maps are exactly
\(s=s_-+(s_+-s_-)p\) and
\(t=t_-+(99/100-s-t_-)q\), \(0\le p,q\le1\).
For the high boundary, \(s_-=s_+=9/20\), justified by (11)--(12).
Contour faces use affine maps onto the four sides of \(\mathcal R\).

Every accepted cell uses outward Arb arithmetic on its entire closed
rational rectangle. The action is evaluated at its exact center and
the mean-value error is bounded with interval gradients. The wire
derivative is
\[
 \partial_x(F_c-F)=2\pi i(s_c-s)
       +\log(1-XU_c)-\log(1-Xe^{-2\pi is}),
 \tag{19}
\]
and \(F_s=\log X+\log(1-UV)-\log(1-XU)\), with the corresponding
\(y,t\) equations. For the floor the wire derivative is
\(2\pi i s_c+\log(1-XU_c)-\log(1-X)\).
These incorporate the stationary dependence of the critical point.

The [independent replayer](../experiments/replay_three_vertex_directed_packet.py)
imports no author code. It reconstructs every rational rectangle from
its binary path, verifies the complete multiplicity-one partition
of each specified domain, and rechecks every bound at higher
precision. It independently evaluates the action as
\[
 F=\frac{\operatorname{Li}_2(e^{-2\pi i(s+t)})-\pi^2/6
 -\operatorname{Li}_2(Xe^{-2\pi is})+\operatorname{Li}_2(X)
 -\operatorname{Li}_2(Ye^{-2\pi it})+\operatorname{Li}_2(Y)}{2\pi i}
       +s\log X+t\log Y.
 \tag{20}
\]
This is the primitive of the same original logarithmic derivative
from the real origin and agrees with (4) by continuation on these
strips. The [replay record](../repro/results/research-three-vertex-directed-packet-replay.json)
also verifies the ten scalar inequalities for the top collar,
high-index reduction and alias margin. Exact accepted rectangles,
precision and source hashes are retained.

Reproduce with:

```sh
python3 experiments/certify_three_vertex_directed_packet.py --precision 160
python3 experiments/replay_three_vertex_directed_packet.py --precision 192
```

The theorem controls this exact retained vertex on (1). The already
proved corner deletion has a separate global after-trace error bound.
Neither statement discards the remaining full wire complement when
composing with actual caps.

