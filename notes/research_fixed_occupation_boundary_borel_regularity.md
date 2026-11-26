# Fixed physical occupations remove a displaced Alexander pole

Private written proof, 18 November 2026.

Retain one intermediate physical occupation of the original highest-cut
source. If its determinant displacement at a simple Alexander zero is
nonzero, fixing that occupation to any nonnegative integer removes the
pole from every quantum-normal coefficient. The actual finite-sector
estimate gives a Borel disk through the node, with all clocks retained.
In particular these boundary sources have no local node monodromy.

## 1. The actual source and the chosen occupation

Keep [M]'s fixed one-component braid, its matching lattice
\(k\in\mathbb Z^d\), highest input/output cut zero, ordinary pivots,
and zero framing. Put
\[
 Q=e^h,\qquad x=Y^{1/2}e^{-h/2},\qquad
 c=b-1-\operatorname{wr}(\beta)\in2\mathbb Z .
 \tag{1}
\]
Choose one physical strand occupation \(a=a(k)\) at a specified
intermediate word stage. It is nonnegative on every supported path.
Insert the independent factor \(s^{a(k)}\), together with the complete
clock \(e^{h m\cdot k}\), \(m\in\mathbb C^d\).
Write the original graded source as
\[
 V(h,Y;s,\tau,m)
   =\sum_{\text{original supported }k}
       s^{a(k)}e^{h m\cdot k}\mathcal I(h,Y,\tau;k),
 \tag{2}
\]
where \(\mathcal I\) includes all the original cut, pivot, and framing
factors. Every total-index sector is finite. In particular each sector
is polynomial in \(s\), rather than Laurent in \(s\).

At \(h=0\), the occupation mark is the diagonal substitution
\[
 M_s=I+(s-1)e_i e_i^T
\]
at that very stage. With the word split there, define
\[
 \mathcal D(Y,s,\tau)
  =\det\!\left(I-\tau L_{\mathrm{left}}(Y)
                       M_s L_{\mathrm{right}}(Y)T_0\right),
 \qquad T_0=\operatorname{diag}(0,1,\ldots,1).
 \tag{3}
\]
The order in (3) is the original word order in [M].
No inverse of \(T_0\) or change of the closing functional is used.
Set \(D(Y,s)=\mathcal D(Y,s,1)\).
At \(s=1\),
\[
                         D(Y,1)=Y^{c/2}\Delta_K(Y).
 \tag{4}
\]
All quantities may first be read on a fixed square-root chart near
the meridian; the original staggered parity makes the source
independent of that choice.

Let \(\alpha\ne0,1\) be a simple zero of \(\Delta_K\), and assume
precisely the following condition on this occupation:
\[
 \mu_a:=-\frac{\partial_tD(\alpha,e^t)|_{t=0}}
                       {D_Y(\alpha,1)}\ne0 .
 \tag{5}
\]
Simplicity and (4) make the denominator nonzero. No assertion that
every physical occupation satisfies (5) is made.

For a fixed integer \(r\ge0\), let
\[
 U_{r,m}(h,Y)=\sum_{j\ge0}h^j U_{r,j,m}(Y)
 \tag{6}
\]
be the canonical grading-one completion of (2) restricted to
\(a(k)=r\). This definition first takes the \(h\)-coefficient in
each finite grading sector. The rational completion and its equality
with extraction of \([s^r]\) are proved below.

**Theorem.** On a meridian disk about \(\alpha\), every
\(U_{r,j,m}\) is holomorphic in \(Y\), is polynomial in \(m\) of total
degree at most \(j\), and satisfies
\[
 |U_{r,j,m}(Y)|
       \le C_r A^j j!e^{c_0\|m\|_1}.
 \tag{7}
\]
Here \(A,c_0\) and the disk are independent of \(j,m,r\);
one may take \(C_r=C\rho_s^{-r}\) for a fixed \(\rho_s>0\).
Consequently the actual Borel source
\[
 b_r(Y,\xi,m)=\sum_{j\ge0}U_{r,j,m}(Y)\frac{\xi^j}{j!}
 \tag{8}
\]
is jointly holomorphic through \(Y=\alpha\) on a fixed
\(\xi\)-disk, and is entire in all clocks.
For \(z=Y-\alpha\), the scaled family
\[
 F_r(z,\eta,\nu)=z\,b_r(\alpha+z,z^2\eta,\nu/z)
 \tag{9}
\]
extends holomorphically through \(z=0\), where it is zero, and obeys
\[
 |F_r(z,\eta,\nu)|
 \le \frac{C_r|z|}{1-A|z|^2|\eta|}
        \exp\!\left(C_1 A|z\eta|\,\|\nu\|_1\right),
 \qquad A|z|^2|\eta|<1.
 \tag{10}
\]
The same conclusions hold after any fixed finite composition of the
clock and meridian operations specified in Section 5.

## 2. The retained determinant and a uniform unit disk

The matrix inside (3) is affine in \(s\), with rank-one variation.
Multilinearity of the determinant in its columns therefore shows that
its degree in \(s\) is at most one: a term using the variation in two
columns has two proportional columns and vanishes. Write
\[
                         D(Y,s)=A_0(Y)-s B_0(Y).
 \tag{11}
\]
This calculation remains valid although \(T_0\) is singular.
Equations (4)--(5) give
\[
 A_0(\alpha)=B_0(\alpha),\qquad
 \mu_a=\frac{B_0(\alpha)}{D_Y(\alpha,1)},\qquad
                      A_0(\alpha)=B_0(\alpha)\ne0.
 \tag{12}
\]
Choose a small closed meridian disk \(K\) about \(\alpha\), avoiding
zero and one, and \(0<\rho_s<1\), so that
\[
            |D(Y,s)|\ge d_0>0
       \quad(Y\in K,\ |s|\le\rho_s).
 \tag{13}
\]
All disks below may be slightly reduced to supply fixed buffers.
Thus the pole is absent on an entire occupation-mark disk, not merely
on its boundary circle.

At order zero this already gives the exact original value
\[
 U_{r,0,m}(Y)
   =[s^r]\frac{Y^{c/2}}{A_0(Y)-sB_0(Y)}
   =Y^{c/2}\frac{B_0(Y)^r}{A_0(Y)^{r+1}}.
 \tag{14}
\]
The formula retains the original framing unit; it is independent of
\(m\), as required by the complete clock at \(h=0\).

## 3. Actual normal coefficients and the uniform Gevrey estimate

The marked trace argument [M, Section 3], with the index-clock
filtration [D, Section 2], applies with this additional fixed mark.
For \(s\ne0\) one may move differential insertions through \(M_s\);
their order is unchanged. The highest-cut projector stays in (3).
Writing \(n=b-1\), it gives
\[
 [h^j]V
     =\frac{P_{j,m}(Y,s,\tau)}
                 {\mathcal D(Y,s,\tau)^{2j+1}},
 \qquad
           \deg_\tau P_{j,m}\le2jn,\quad \deg_m P_{j,m}\le j .
 \tag{15}
\]
For clarity, the degree-\(d\) clock part uses \(d\) Euler insertions
at residual quantum order \(j-d\). Its differential order is at most
\(2(j-d)+d=2j-d\). The determinant-trace numerator degree is at most
\((2j-d)n\); clearing to the denominator in (15) adds at most \(dn\).
This proves the stated grading bound with the mark retained.

There is no pole at \(s=0\) in the numerator of (15).
Indeed the original finite-sector coefficients are polynomial in
\(s\). Multiplication by the polynomial
\(\mathcal D^{2j+1}\) shows coefficientwise in \(\tau\) that all
negative \(s\)-powers in the temporary Laurent numerator cancel.
Since its \(\tau\)-degree is finite, this proves the assertion for
the entire numerator. The analogous temporary meridian denominators
cancel as in [M]. Thus (15) extends across \(s=0\).

We next give the bound before evaluation at \(\tau=1\).
Choose a meridian circle surrounding \(K\), containing no Alexander
zero on the circle. The actual finite-sector estimate used in
[D, (11)--(13)] is uniform there. If the sector has total index \(T\),
then \(0\le a(k)\le T\), while
\(\|k\|_\infty\le K_\beta T\). On its actual Cauchy disk
\[
 |h|\le\rho/(T+1),\qquad 0<\rho\le1/4,
 \tag{16}
\]
the new weights satisfy
\[
 |s^{a(k)}|\le1,\qquad
 |e^{h m\cdot k}|\le e^{\rho K_\beta\|m\|_1}
                         \quad(|s|\le\rho_s).
 \tag{17}
\]
Hence the same absolute finite-path estimate applies: the added
occupation mark does not increase it. Each finite-sector coefficient
is holomorphic throughout the enclosed meridian disk, because the
literal entries have no meridian poles there. The maximum principle
therefore extends the circle bound through \(\alpha\), before summing
any infinite grading series.

Cauchy estimation in (16) and the same small-grading sum as in [D]
now give fixed \(C_2,A_2>0\), \(0<r_\tau\le1/2\), with
\[
 \sup_{\substack{Y\in K,\ |s|\le\rho_s\\|\tau|\le r_\tau}}
 |[h^j]V|
       \le C_2 A_2^j j!e^{\rho K_\beta\|m\|_1}.
 \tag{18}
\]
This is a sum of normal coefficients already defined by finite
sectors. No common generic-\(h\) disk for the infinite source is used.

Put
\[
 H=\max\left(1,\sup_{K,\ |s|\le\rho_s,\ |\tau|=r_\tau}
                                     |\mathcal D(Y,s,\tau)|\right).
 \tag{19}
\]
Multiply (18) by \(\mathcal D^{2j+1}\). Cauchy's estimate for the
polynomial in \(\tau\) in (15), followed by (13), yields
\[
 \sup_{K,\ |s|\le\rho_s}
 \left|\left.[h^j]V\right|_{\tau=1}\right|
 \le 2C_2\frac{H}{d_0}
  \left[A_2(H/d_0)^2r_\tau^{-2n}\right]^j
                    j!e^{\rho K_\beta\|m\|_1}.
 \tag{20}
\]
Only an exponential in \(j\) is lost in the grading completion.

Extraction of \([s^r]\) commutes with this canonical completion.
One can see this without exchanging an infinite generic trace:
\(\mathcal D\) is affine in \(s\), its value at \(s=0\) has
constant term one in \(\tau\), and the numerator of (15) has no
negative \(s\)-powers. Its fixed \(s^r\)-coefficient is consequently
a finite rational expression in \(\tau\), regular at \(\tau=1\)
by (13). It is the same expression obtained by first restricting
each finite sector to \(a=r\). Cauchy's \(s\)-coefficient estimate
in (20) proves (7), with \(C_r=C\rho_s^{-r}\).
Polynomial degree at most \(j\) in \(m\) is preserved by this
extraction.

## 4. The whole-clock Borel disk and zero node monodromy

Write
\[
 U_{r,j,m}(Y)=\sum_{|\gamma|\le j}u_{r,j,\gamma}(Y)m^\gamma .
 \tag{21}
\]
Optimized multivariate Cauchy estimates in (7), with radii
\(\gamma_i/c_0\) in nonzero coordinates, give
\[
 |u_{r,j,\gamma}(Y)|
       \le C_r A^j j!\,\frac{C_1^{|\gamma|}}{\gamma!}.
 \tag{22}
\]
Zero coordinates use limiting radii zero. If \(c_0=0\), all
nonconstant clock coefficients vanish and (22) is immediate.
There is no factorial depending on \(j\) beyond \(j!\).

Put \(t=A|\xi|<1\). Summing (22), retaining \(|\gamma|\le j\),
gives the stronger bound
\[
 |b_r(Y,\xi,m)|
   \le\frac{C_r}{1-t}
                     \exp(C_1t\|m\|_1).
 \tag{23}
\]
Indeed \(\sum_{j\ge d}t^j=t^d/(1-t)\), and the multinomial
formula sums the clock coefficients of total degree \(d\).
The normally convergent series proves joint holomorphy, including
\(Y=\alpha\), with a fixed \(\xi\)-radius for all clocks.

Substitute \(\xi=z^2\eta,\ m=\nu/z\) in (23) and multiply by
\(z\). This is exactly (10). The extension across \(z=0\) also
follows termwise: a monomial of clock degree \(d\le j\) has the
factor \(z^{2j-d+1}\), whose exponent is at least \(j+1\).
On every fixed bounded \(\eta\)-domain, shrinking \(z\) makes the
series normally convergent for all clocks on compact sets.
Thus no loop in such a domain produces local node monodromy.
Equivalently, the unscaled family (8) is single-valued on the
whole fixed product disk through \((Y,\xi)=(\alpha,0)\).

Canonical primitives also have no hidden local history contribution.
On a smaller \(\xi\)-disk, \(I_\xi^a b_r\), based at the original
zero, is holomorphic on the same product disk, with the usual
\(R_\xi^a/a!\) bound on each compact clock set. Its continuation
around a loop contained in that disk has no added constant.

## 5. Explicit finite-shift closure

This regularity is stable under the following actual finite adapters:
fixed clock translations \(m\mapsto m+p\), meridian shifts
\(Y\mapsto e^{t h}Y\), multiplication by
\(e^{h(\lambda+v\cdot m)}\), and scalar factors holomorphic in
\((h,Y)\) near \((0,\alpha)\). Integers \(p,t,v,\lambda\) include
the clock, \(Q\)-monomial, and meridian operations of the original
finite source equations. Fixed complex values satisfy the same
analytic bounds. Operators retain their original order.

Here is a coefficient proof, so no summability assertion is needed.
On a smaller meridian disk choose a fixed log-meridian buffer
\(|u-u_0|<d_u\), where \(u=\Log Y\). For \(E=\partial_u\),
\[
 |E^\ell U_{r,n,m+p}|
 \le \ell!d_u^{-\ell}C'_r A^n n!e^{c_0\|m\|_1}.
 \tag{24}
\]
The coefficient of \(h^j\) after the meridian shift is the finite sum
\(\sum_{n+\ell=j}t^\ell E^\ell U_{r,n,m+p}/\ell!\).
Equation (24) bounds it by \(C'_r A'^j j!e^{c_0\|m\|_1}\).
Its clock degree is still at most \(j\).

Multiplying by \(e^{h(\lambda+v\cdot m)}\) convolves this coefficient
with \((\lambda+v\cdot m)^d/d!\). Taking \(A'\ge1\), the finite
sum is bounded by
\[
 C'_r A'^j j!
          e^{|\lambda|+(c_0+\|v\|_\infty)\|m\|_1},
 \tag{25}
\]
and its clock degree remains at most \(j\).
Analytic scalar factors have geometrically bounded Taylor
coefficients on fixed buffers; their convolution changes only
the constants. Finite sums and finite compositions therefore have
the same coefficient properties (7), (21)--(22), on a fixed smaller
disk, and hence the same conclusions (8)--(10).

All these identities first hold on the original finite sectors and
their canonical formal completion. Their convergent Borel series
are therefore the actual adapted sources. This includes the
finite reindexing exponent \(e^{-h m\cdot v}\), but it does not
declare an arbitrary internal boundary a fixed occupation, divide a
clock factor, or reset a continued primitive.

## 6. Scope and complete proof directs

The result applies to a specified physical occupation satisfying
(5), and every fixed nonnegative value of that occupation. It keeps
the literal highest cut and every clock. It does not cover
\(\mu_a=0\), nor a transfer facet or a simultaneous family of
constraints without a separate determinant argument.
No character property of the remaining source, moving marked minor,
geometric-component identification, or physical scalar lower bound
is inferred.

| Label | Complete proof direct | SHA256 |
|---|---|---|
| M | notes/research_marked_verma_full_certificate_transport.md | a2d94711bb80e69139e25b4932f0878440934c0586ddd0535dc24fcfd61987b4 |
| D | notes/research_full_clock_initial_borel_family.md | d498ddfad641c85bba0257d22dcad53679ccd2cfb7e0c16f6cc790444f9e9b77 |

M supplies the literal marked highest-cut trace and rational normal
completion. D supplies its clock-degree filtration and finite-sector
Gevrey argument. The rank-one occupation determinant, uniform unit
disk, regular coefficient extraction, Borel bound and finite-shift
closure are proved above.
Only written mathematics, source-text reads and hash checks were used.
Frozen proofs and public manuscripts are unchanged.
