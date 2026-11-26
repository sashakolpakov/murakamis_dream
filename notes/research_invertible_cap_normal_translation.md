# An invertible normal translation before the original cap closing

Private written proof, 17 November 2026. The exact cap adjoint admits
a finite invertible extension when its full two-variable attachment
is retained. Both directions have uniform coefficient-norm bounds
on the \(N^{-1}\) protected scale. The extension agrees with the
original source only after its prescribed cap closing; no inverse
of the fused-value projection or scalar lower bound is claimed.

## 1. The exact transverse module

Use [A] and [J], with
\[
 N\ge3,\quad d=N-1,\quad q=e^{\pi i/N},\quad
 \sigma=\pm1,\quad \tau=q^{2\sigma},\quad
 a=-q^\sigma,\quad \lambda=q^{\sigma d^2/2}.
 \tag{1}
\]
Retain the prescribed lift of \(\lambda\). The adjacent crossing is
\(H_\sigma(X,Z,c,y)\), with protected outer and middle variables
\(X,Z\), and ordinary target variables \(c,y\).
All other parameters and \(X,Z\) belong to the coefficient ring
\(\mathcal B\); Jackson derivatives act only in \(c,y\).

The actual cap source factors through the free rank-\(N^2\) module
\[
 \mathcal E_N=\mathcal B[c,y]/(c^N,y^N),\qquad
 \{c^iy^j:0\le i,j<N\}.
 \tag{2}
\]
Indeed the crossing is a polynomial with nonnegative powers, so
\([c^dy^d]H_\sigma F\) annihilates the ideal \((c^N,y^N)\).
This holds even when \(F\) depends on \(X,Z\).
The quotient preserves this specified coefficient functional; it
does not preserve pointwise values of the attachment on an ordinary
complex face chart.

Put
\[
 D_y=D_{\tau^{-1},y},\qquad D_c=D_{\tau,c}.
\]
At this fixed root, \(D_{\theta,w}(w^Nf)=w^ND_{\theta,w}f\)
for \(\theta=\tau,\tau^{-1}\). The derivatives therefore descend
to (2), commute, and satisfy
\[
 D_y^N=D_c^N=0.
 \tag{3}
\]
These are literal finite-module identities. The representative
quotient is not taken before a genuine-\(q\) derivative, and no
such derivative is asserted here.

The prescribed remaining row is
\[
 \ell_a(F)=[t^d]F(at,t),\qquad
 \ell_a(c^iy^j)=a^i\mathbf1_{i+j=d}.
 \tag{4}
\]
It is well-defined on (2), since either discarded \(N\)-th power
maps into \((t^N)\).

## 2. A rectangular extension with the same original closing

For a nilpotent \(U^N=0\), define
\[
 e_\theta(U)=\sum_{k=0}^d\frac{U^k}{[k]_\theta!},
 \qquad [k]_\theta!=\prod_{r=1}^k\frac{1-\theta^r}{1-\theta}.
 \tag{5}
\]
All denominators in (5) are units. Define the rectangular operator
\[
 \mathscr T_\sigma(X,Z)
  =e_\tau(-\tau^{-1}XD_y)\,
       e_{\tau^{-1}}(-\tau ZD_c).
 \tag{6}
\]
Its two factors commute. It sums independently over \(0\le k,l<N\).
It is therefore different from the triangular operator
\(\mathscr A_\sigma\) of [A], whose sum has \(k+l\le d\).

Nevertheless, for every entire polynomial attachment,
\[
 \boxed{\quad
 [c^dy^d]H_\sigma(X,Z,c,y)F
       =\lambda\,\ell_a(\mathscr T_\sigma(X,Z)[F]).
 \quad} \tag{7}
\]
To prove the additional terms vanish, put
\(B(c,y)=H_\sigma(0,0,c,y)\), of total degree \(d\).
The unchanged-target adjoint in [A] gives
\[
 [c^dy^d]B\,D_y^kD_c^lF
 =(-\tau)^k(-\tau^{-1})^l
   [c^dy^d](D_{\tau,y}^{\,k}D_{\tau^{-1},c}^{\,l}B)F=0
       \quad(k+l>d).
 \tag{8}
\]
The cap identity \([c^dy^d]BG=\lambda\ell_a(G)\) now shows that
\(\ell_a(\mathscr T_\sigma-\mathscr A_\sigma)=0\).
Together with [A, (5)] this proves (7). The extra terms need not
vanish as operators on \(\mathcal E_N\); they vanish after this
specific original row. No change of the cap, mark, or scalar is made.

## 3. Exact inverse retaining every transverse coefficient

The finite dual exponential
\[
 E_\theta(U)=\sum_{k=0}^d
       \frac{\theta^{k(k-1)/2}U^k}{[k]_\theta!}
 \tag{9}
\]
satisfies \(e_\theta(U)E_\theta(-U)=I\) when \(U^N=0\).
For degrees \(1\le m<N\), its product coefficient is
\[
 \frac1{[m]_\theta!}
    \sum_{k=0}^m(-1)^k\theta^{k(k-1)/2}{m\brack k}_\theta
 =\frac{\prod_{j=0}^{m-1}(1-\theta^j)}{[m]_\theta!}=0.
\]
Higher powers vanish by nilpotence; the constant coefficient is one.
Thus (6) is a \(\mathcal B\)-linear automorphism of (2), with inverse
\[
 \mathscr T_\sigma^{-1}
 =\sum_{k,l=0}^d
  \frac{\tau^{k(k-3)/2+l(3-l)/2}X^kZ^l}
       {[k]_\tau![l]_{\tau^{-1}}!}\,D_y^kD_c^l.
 \tag{10}
\]
Its coefficients differ from those of (6) only by unit phases.
Both maps are triangular in total ordinary degree with diagonal one.
Formula (10) is the inverse of \(\mathscr T_\sigma\), not an
asserted inverse formula for the different triangular
\(\mathscr A_\sigma\).

This is a linear module automorphism, not a multiplicative
automorphism of the attachment algebra. A product attachment is
transformed as a whole. Its neighboring factors and all external
\(X,Z\) derivatives remain as prescribed by [A].

## 4. Two-sided bounds on the actual coefficient module

Fix positive radii \(r_c,r_y\). On each complex parameter fiber use
\[
 \|F\|_{r_c,r_y}
   =\sum_{i,j=0}^d |f_{ij}|r_c^ir_y^j
 \quad\text{for }F=\sum f_{ij}c^iy^j.
 \tag{11}
\]
The induced operator norms satisfy
\[
\begin{split}
 \|\mathscr T_\sigma^{\pm1}\|
   &\le B_N:=(1+|X|/r_y)^d(1+|Z|/r_c)^d,\\
 \|\mathscr T_\sigma^{\pm1}-I\|&\le B_N-1,\\
 B_N^{-1}\|F\|&\le\|\mathscr T_\sigma F\|\le B_N\|F\|.
\end{split} \tag{12}
\]
Indeed on \(y^j\), the absolute coefficient of the \(k\)-th
lowering term in either direction is
\[
 \left|\frac{[j]_{\tau^{-1}}!}
 {[k]_\tau![j-k]_{\tau^{-1}}!}\right||X|^k
 =\left|{j\brack k}_{\tau^{-1}}\right||X|^k
 \le\binom jk|X|^k.
 \tag{13}
\]
The Gaussian binomial has nonnegative integer polynomial
coefficients and value \(\binom jk\) at one, as proved in [J].
The \(c\)-factor has the same bound. Summing each weighted column
proves the first line of (12); omitting its identity entry proves
the second. Applying the inverse bound proves the third.
Every allowable lowering coefficient is nonzero when \(X,Z\ne0\):
all its factorial indices are less than \(N\). This fact does not
prevent cancellations after applying the original row.

Put \(\alpha_N=|X|/r_y+|Z|/r_c\). Since \(B_N\le e^{d\alpha_N}\),
both directions are uniformly bounded if \(\alpha_N\le C/N\),
and polynomially bounded if \(\alpha_N\le C\log N/N\).
If \(\alpha_N\le C/N^2\), both are \(I+O(N^{-1})\).
These are estimates on all transverse coefficients, not just
their merged values.

For holomorphic parameters, impose the stated scaled bound on a
fixed open buffer around the parameter compact. The same operator
estimates then hold for fixed parameter derivatives by Cauchy's
formula; in the \(N^{-2}\) regime these derivatives of
\(\mathscr T_\sigma^{\pm1}-I\) are \(O(N^{-1})\).
This concerns scaled parameter families \(X_N,Z_N\), not uniformly
bounded derivatives with respect to unscaled \(X,Z\).

There is no level-uniform polynomial bound on every fixed-size
protected domain in this norm. For \(8\mid N\), take \(X=1,Z=0\),
input \(y^{N/2}\), and lowering degree \(k=N/4\), with unit radii.
The corresponding entry in either direction has magnitude
\[
 \left|{N/2\brack N/4}_\tau\right|
  =\prod_{j=1}^{N/4}
       \frac{\sin(\pi(N/4+j)/N)}{\sin(\pi j/N)}
  \ge
   \left(\frac{\sin(\pi/4)}{\sin(\pi/8)}\right)^{N/8}.
 \tag{14}
\]
Use the displayed ratio on \(j\le N/8\), and the bound one on
the remaining factors. This written coefficient calculation
delimits the scale in (12); it is not a knot example.

## 5. The original scalar obligation remains

The exact source has been written as the unchanged row
\(\lambda\ell_a\) applied to an invertibly transported attachment.
The row is still a rank-one functional. For example
\(\mathscr T_\sigma1=1\) but \(\ell_a(1)=0\), since \(d>0\).
More generally \(\mathscr T_\sigma^{-1}\ker\ell_a\) is a nontrivial
subspace at every parameter value. Neither invertibility nor (12)
gives a lower bound for the prescribed scalar on an actual source.

The result supplies exact, controlled local normal transport at
the stated boundary scales. Applying it to a neighboring product
does not establish a nonzero geometric co-source, allow a
fixed-size complex contour displacement, or preserve a geometric
packet through arbitrary turns. All original coefficient targets,
normal data, and exterior source factors remain in (7).

## Complete direct sources

Both complete texts and their used implications were read.
No programs, numerical evaluations, or frozen/public edits were used.

| Label | Source | SHA-256 |
|---|---|---|
| A | [Exact all-jet cap attachment transform](research_protected_cap_all_jet_attachment_transform.md) | e45d2bef26c57011537a144c7e156eedf60f0bc05e3d7714edb45413ca9284b9 |
| J | [Original crossing Jackson boundary jets](research_crossing_jackson_boundary_jets.md) | 231d70047a49834c3df1f3cd722a704ec841c704a5213e5cf1d45caabc236bb7 |
