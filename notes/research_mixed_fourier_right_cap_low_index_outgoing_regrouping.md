# Regrouping the low-index outgoing contour at its true boundaries

Research deduction, 7 November 2026. The low-index source admits
one exact outgoing contour on its full original supported interval,
at every retained physical index. It has no internal outgoing cuts.
The original root-Pochhammer interpolation is regular across both
true outgoing endpoints, because the other outgoing factor is kept
as a finite polynomial. The four exact contour groups retain the
whole zero mode, both aliases, and the two true boundary currents.

This removes the artificial outgoing cuts as separate source terms.
It does not estimate the resulting complete currents or import
the taller alias bounds proved for a different exact interpolation.
There is no whole right-cap asymptotic or new numerical evaluation.

## 1. One interpolation on the whole supported outgoing interval

For \(N\ge2\), use the exact split from the
[low-index source reduction](research_mixed_fourier_right_cap_low_index_source_reduction.md):
\[
 \begin{gathered}
 r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad
 p_j(Z)=(rZ;r)_j,\quad X=e^{-2\pi ia},\quad Y=e^{2\pi iy},\\
 M_N=\lceil N/2\rceil-1,\qquad
 A_{j,N}(a)=X^{-j}p_j(X)/P_j^3,\qquad
                         n_j=N-j-1.
 \end{gathered}
 \tag{1}
\]
The actual source is
\[
 V_N^<(y,X)=
 \sum_{j=0}^{M_N} A_{j,N}(a)
       \sum_{l=0}^{n_j}p_j(r^l)f_l(y).
 \tag{2}
\]
Here
\[
 f_l(y)=\frac{e^{-\pi i(N-1)y}}N\,
          Y^l\prod_{k=l+1}^{N-1}(1-Yr^k).
 \tag{3}
\]
In particular \(p_j(r^l)=P_{j+l}/P_l\) on this support.
Both the triangular termination and the exact factor \(1/N\)
in (3) are unchanged.

Let \(\mathcal P_N\) be the specified function from
[root-Pochhammer interpolation](research_root_pochhammer_interpolation.md),
equation (2), including its resonant term. Define
\[
 f_N(q;y)=\frac{e^{-\pi i(N-1)y}}N(1-Y^N)
       \frac{e^{2\pi iNyq}}{\mathcal P_N(q+1/N,Y)}.
 \tag{4}
\]
Unlike the factorial-suffix chart, this function requires no
restriction on \(\Re(q-y)\). Its exact holomorphic domain is
\[
                |Y|<1,\qquad |Ye^{-2\pi iq}|<1.
 \tag{5}
\]
For the original output, \(\Im y>0\), so every \(q\) with
\(\Im q<\Im y\) belongs to (5). The denominator is nonzero.
At each integer \(0\le l<N\), the original difference equation
gives \(f_N(l/N;y)=f_l(y)\), including \(l=0\) and \(N-1\).

For each physical \(j\), retain the entire finite polynomial and put
\[
             F_{j,N}(q;a,y)
                  =A_{j,N}(a)\,p_j(e^{-2\pi iq})\,f_N(q;y).
 \tag{6}
\]
It is holomorphic throughout (5), for every real part of \(q\).
This remains true at \(q=0\) and \(q=1-j/N\). No continuation
of an inverse sine factorial through those endpoints is involved.
If \(A_{j,N}\) vanishes, the entire function (6) vanishes;
no division by that value is used.

On any compact subset of (5), the original proved expansion is
\[
 f_N(q;y)=\frac1N
 \frac{e^{\pi iy}}{\sqrt{(1-Y)(1-Ye^{-2\pi iq})}}\,
             e^{N\ell_q(y)}(1+O(N^{-1})).
 \tag{7}
\]
The logarithms and square roots are those fixed by their unit-disk
series, and the exact lifted action is
\[
 \ell_q(y)=2\pi iy(q-\tfrac12)
 -\frac{\operatorname{Li}_2(Ye^{-2\pi iq})
                         -\operatorname{Li}_2(Y)}{2\pi i}.
 \tag{8}
\]
The same expansion is uniform on a compact neighborhood of the
full real outgoing interval used below. It describes only (4);
the polynomial \(p_j\) is still exact.

## 2. Exact full-interval outgoing currents

Retain the actual outgoing reference height
\(h_0=\Im q_*\in[-.102,-.001]\), and choose
\[
 h_-=-1/5,\qquad h_+=\tfrac12\Im y>0.
 \tag{9}
\]
At every height in this rectangle,
\(|Ye^{-2\pi iq}|\le\sqrt{|Y|}<1\). Thus (6) is holomorphic
on a neighborhood of all the following rectangles, uniformly
over \(0\le j\le M_N\). Small output neighborhoods may instead
use a fixed \(h_+\) strictly below the smallest \(\Im y\)
in that neighborhood.

The two half-grid endpoints are
\[
 \alpha_N=-\frac1{2N},\qquad
 \beta_{j,N}=\frac{n_j+1/2}{N}
                   =1-\frac jN-\frac1{2N}.
 \tag{10}
\]
They enclose exactly \(l=0,\ldots,n_j\). In particular the
endpoints tend to the true boundaries \(q=0\) and \(s+q=1\),
where \(s=j/N\); they are not cuts at fixed intermediate \(q\).

Define
\[
 \begin{split}
 Z_{j,N}&=N\int_{\alpha_N}^{\beta_{j,N}}
                         F_{j,N}(q+ih_0)\,dq,\\
 L_{j,N}&=N\int_{\alpha_N}^{\beta_{j,N}}
       F_{j,N}(q+ih_-)
       \frac{e^{-2\pi iN(q+ih_-)}}{1-e^{-2\pi iN(q+ih_-)}}\,dq,\\
 U_{j,N}&=N\int_{\alpha_N}^{\beta_{j,N}}
       F_{j,N}(q+ih_+)
       \frac{e^{2\pi iN(q+ih_+)}}{1-e^{2\pi iN(q+ih_+)}}\,dq.
 \end{split}
 \tag{11}
\]
All factors in these definitions have their original normalization.
For the vertical group, put
\[
 \begin{split}
 w_{N,h_0}(v)&=\frac1{1+e^{2\pi Nv}}
                         -\boldsymbol1_{\{v<h_0\}},\\
 B_{j,N}&=iN\int_{h_-}^{h_+}w_{N,h_0}(v)
       \{F_{j,N}(\beta_{j,N}+iv)
                         -F_{j,N}(\alpha_N+iv)\}\,dv .
 \end{split}
 \tag{12}
\]
The value of the indicator at \(v=h_0\) is irrelevant.
Its signed subtraction is kept before taking a modulus.

**Theorem 1.** At every level of either parity,
\[
 \boxed{\qquad
 V_N^<=\sum_{j=0}^{M_N}
                     \bigl(Z_{j,N}+L_{j,N}+U_{j,N}+B_{j,N}\bigr).
 \qquad}
 \tag{13}
\]

*Proof.* Apply the exact one-index identity in
[vertical-current regrouping](research_exact_vertical_current_regrouping.md),
equations (4)--(5), to the holomorphic function (6), with the
half-grid endpoints (10) and heights (9). It gives
\[
       \sum_{l=0}^{n_j}F_{j,N}(l/N)
                  =Z_{j,N}+L_{j,N}+U_{j,N}+B_{j,N}.
 \]
The left side is exactly the \(j\)-th summand group in (2).
Sum this finite identity over the unchanged low-index range.
No outgoing physical row has been estimated or deleted.
The coefficient \(N\) of the zero mode, the two full alias
denominators, both signed vertical orientations and the original
cardinal \(1/N\) are all retained. \(\square\)

The vertical coefficient has precisely the bounds
\[
 |w_{N,h_0}(v)|\le
 \begin{cases}
 e^{2\pi Nv},&v<h_0,\\
 1,&h_0<v\le0,\\
 e^{-2\pi Nv},&v\ge0 .
 \end{cases}
 \tag{14}
\]
Thus the segment between \(h_0\) and zero has no positive
Fourier debit. In particular (13) does not pay its true-boundary
profiles merely by calling them vertical aliases.

## 3. Internal outgoing cuts cancel before a modulus is taken

Partition \([\alpha_N,\beta_{j,N}]\) at any finite collection
of intermediate half-grid points, including points tending to
\(11/50\) and \(9/20\). Use the same interpolation (6)
and the same three heights in each panel.
The zero modes and horizontal aliases concatenate exactly.
At each internal cut, the right vertical value of its left panel
and the left vertical value of its right panel occur with opposite
signs and the identical coefficient \(w_{N,h_0}\).
They cancel as analytic functions of the retained parameters.
The only surviving vertical values are those displayed in (12).

This proves cancellation also for the unpenalized parts of the
joining currents. If one first used different zero-mode heights
in adjacent panels, their intervening horizontal/vertical path
differences must first be joined by Cauchy's theorem; one may not
discard the corresponding connecting currents. Equation (13)
avoids that additional bookkeeping by choosing the common height
from the outset.

The older factorial-suffix interpolation
\(\widehat f_N\) is a different specified exact interpolation.
Its useful upper contour at height \(1/2\) lies outside (5).
Although its original leading phase and symbol agree with (4)
on a common negative-height domain, equality of their off-grid
values is not asserted. Therefore an upper panel using
\(\widehat f_N\) cannot be joined to a panel using \(f_N\)
by this cancellation argument. The whole construction (11)--(13)
uses (4), with the restricted upper height (9).

## 4. What the regrouping does and does not settle

The complete original cap is now exactly its already paid
coherent high-index group plus the four groups in (13).
Each group still includes the sum over all low retained indices.
No artificial outgoing-face profile is forced by this identity.
The main outgoing path is now the full supported interval, and
its only endpoint limits are the true \(q=0\) and \(q=1-s\)
boundaries.

On a compact subset of \(0<s,\ 0<q,\ s+q<1\), the factorial
recurrence and (7) recover the unchanged uneliminated phase
\[
 g(s+a)+g(s+q)-3g(s)-(1+\eta/2)g(a)-g(q)
                                      +2\pi ias+\ell_q(y)
 \tag{15}
\]
after the original incoming halfweight is allocated. There is
no new action constant, parity scalar, or stationary branch.
Near the true edges, however, (6) remains the definition:
compact-strip Gaussian or factorial symbols are not extended
there without their own proof.

The negative-height plateau estimate for the truncated conditional
factor, proved in the low-index reduction, applies on \(q_R\in P\).
It does not by itself control the full paths in (11), their true
boundary integrals, or the restricted-height upper alias.
Similarly the separate \(j\)-dependent right endpoints in (10)
cannot be replaced by one rectangular endpoint when deforming
the retained index; any such further deformation must retain the
sloping support edge and its exact connecting currents.

Thus (13) supplies an exact coherent alternative to the sufficient
four-face absolute criterion. A bound for its complete currents
still has to preserve their phases and the actual true-boundary
terms. The new identity alone supplies neither a calibrated
remainder estimate nor a whole-cap noncancellation theorem.

## 5. A common full-period contour with its exact monodromy

There is also a source-preserving way to obtain one fixed outgoing
rectangle before summing over the retained index. It uses the
vanishing of additional physical rows, rather than a deformation
of the moving boundary in (10). Define
\[
 C_N^<(X,Z)=\sum_{j=0}^{M_N}
                    \frac{X^{-j}p_j(X)p_j(Z)}{P_j^3},
 \qquad
 \mathcal F_N(q)=C_N^<(X,e^{-2\pi iq})f_N(q;y).
 \tag{16}
\]
For every \(0\le j<N\) and \(N-j\le l<N\),
\(p_j(r^l)=0\): the factor with index \(k=N-l\) in
\(\prod_{k=1}^j(1-r^{l+k})\) vanishes. For \(j=0\) that added
range is empty. Consequently the exact same low source satisfies
\[
 V_N^<=\sum_{l=0}^{N-1}\mathcal F_N(l/N).
 \tag{17}
\]
This identity retains the original \(f_l\), the incoming
coefficient, the cardinal \(1/N\), and both parity conventions.

Set
\[
 \beta_N=\alpha_N+1=1-\frac1{2N}.
 \tag{18}
\]
Let \(\mathcal Z_N,\mathcal L_N,\mathcal U_N\) be the three
integrals in (11), with \(F_{j,N}\) replaced by \(\mathcal F_N\)
and with endpoints \(\alpha_N,\beta_N\). Define
\[
 \mathcal B_N=iN\int_{h_-}^{h_+}w_{N,h_0}(v)
       \{\mathcal F_N(\beta_N+iv)
                      -\mathcal F_N(\alpha_N+iv)\}\,dv.
 \tag{19}
\]
All these functions use the same exact interpolation (4).
The domain (5) contains the full common rectangle and a
neighborhood of it. Applying the same residue identity to
(17) gives
\[
 \boxed{\quad
       V_N^<=\mathcal Z_N+\mathcal L_N+\mathcal U_N+\mathcal B_N .
       \quad}
 \tag{20}
\]
Thus (20) is an additional exact representation of the source
in (13), not an estimate for the moving-edge terms in that formula.

The common vertical group has an explicit one-sided form.
The original \(N\)-step Pochhammer recurrence gives
\[
 \frac{\mathcal P_N(q+1+1/N,Y)}
      {\mathcal P_N(q+1/N,Y)}
      =1-Y^Ne^{-2\pi iNq},
 \qquad
 f_N(q+1;y)=
       \frac{Y^N}{1-Y^Ne^{-2\pi iNq}}\,f_N(q;y).
 \tag{21}
\]
Indeed the product of its \(N\) successive factors is
\(\prod_{k=1}^N(1-Ye^{-2\pi iq}r^k)
 =1-Y^Ne^{-2\pi iNq}\), and the exponential numerator
of (4) gains exactly \(Y^N\). The polynomial
\(C_N^<(X,e^{-2\pi iq})\) is periodic in \(q\).
At the left half-grid edge,
\(e^{-2\pi iN(\alpha_N+iv)}=-e^{2\pi Nv}\).
Therefore (19) becomes the exact identity
\[
 \boxed{\quad
 \mathcal B_N=iN\int_{h_-}^{h_+}w_{N,h_0}(v)
   \left\{\frac{Y^N}{1+Y^Ne^{2\pi Nv}}-1\right\}
   C_N^<(X,e^{-2\pi i(\alpha_N+iv)})
   f_N(\alpha_N+iv;y)\,dv .
 \quad}
 \tag{22}
\]
The denominator is nonzero throughout the contour since
\(|Y|e^{2\pi h_+}<1\). Equations (21)--(22) do not
identify the cardinal interpolation as periodic, and the
braced factor is not omitted or replaced by a phase.

The fixed endpoint in (18) now permits the finite retained-index
sum to be combined before any contour estimate. It does not
make the off-grid extensions \(q\in(\beta_{j,N},\beta_N)\)
zero: their physical nodes vanish, while their complete
horizontal and boundary currents cancel only in the exact
residue identity. Bounds for (20) must therefore include
these added off-grid regions. In particular the main path
now crosses the original triangular edge for some retained
indices, and a factorial symbol valid only before that edge
cannot be used on its entire length.

Artificial outgoing cuts still cancel exactly, with the
common interpolation and heights. The remaining current
(22), the full horizontal paths, and the restricted-height
upper alias remain genuine analytic terms requiring bounds.
There is no claimed decay of (22) merely from its monodromy,
and (14) still leaves the interval \(h_0<v<0\) without a
Fourier debit. The corollary changes the exact organization
of the low source; it does not establish its calibrated
remainder or noncancellation.
