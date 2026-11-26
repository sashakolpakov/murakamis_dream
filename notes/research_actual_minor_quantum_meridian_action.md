# The actual marked minor satisfies the quantum-meridian action equation

Private written proof, 18 November 2026.

The exact external row of the original highest-cut source determines
the meridian derivative of its reconstructed local action. The proof
uses actual continued Borel minors, not a stationary ansatz. It keeps
the original zero-framing scalar, all finite clock shifts, and every
primitive base. No finite-cutoff endpoint is discarded.

## 1. Actual source, action, and assertion

Use the simple-node source of [M], with \(Q=e^h\), \(Y=\alpha+z\),
\(\alpha\ne0,1\). Write its analytic endpoint phase as \(f(Y,x)\);
this abbreviates \(f(z,x)\) in [M], with the same soft coordinate
\(x\). Let
\[
 f_x(Y,x_g(Y))=0,\qquad
 \xi_g(Y)=f(Y,x_g(Y)),\qquad S_g(Y)=-\xi_g(Y).
 \tag{1}
\]
The principal phase and clock map are the actual analytic germs
constructed in [P] and reconstructed in [M].

The original marked Borel source has, on its continued local cover,
\[
 b_m(Y,\xi)=E_m(Y,\rho)+\rho^{-1/2}A_m(Y,\rho),
 \qquad \rho=\xi-\xi_g(Y),
 \tag{2}
\]
where the two coefficients are holomorphic and
\[
 \mathfrak a_m(Y):=A_m(Y,0)\ne0,\qquad
       \mathfrak a_m(Y)=\mathfrak a_0(Y)e^{m\cdot\Theta_g(Y)}.
 \tag{3}
\]
These are the actual leading minors of [M], with a common
square-root convention. They hold jointly on any prescribed compact
set of clock values after shrinking the disks.

Retain [E]'s integral matching-lattice forms and finite Laurent
polynomials
\[
 \begin{split}
 D(Y,X)&=\prod_+(1-Y^{-1}X^a)\prod_-(1-YX^{-b'}),\\
 N(Y,X)&=\prod_+(1-Y^{-1}X^{a-n})\prod_-(1-YX^{n-b'}),\\
 H&=\sum_-(a+b'-n)+\sum_+(-a-b'+n),\\
 \mathcal R(Y,X)&=X^{H/2}N(Y,X)/D(Y,X).
 \end{split}
 \tag{4}
\]
Each index in these products is its original integral lattice form;
\(H/2\) is integral. The signs and zero-framing convention are those
of [E], unchanged.

**Theorem.** On a sufficiently small meridian disk,
\[
 \boxed{\displaystyle
          \exp\!\bigl(Y S_g'(Y)\bigr)
                =\mathcal R\!\left(Y,e^{\Theta_g(Y)}\right).}
 \tag{5}
\]
Every exponential and derivative in (5) is an analytic germ fixed
by the original source. Both sides have value one at \(Y=\alpha\).
The quotient on the right is a local analytic unit.

This is an actual action/clock identity. It does not identify the
rational map with a preferred topological longitude, a hyperbolic
branch, or a physical root-of-unity contribution.

## 2. Shifting the actual source with a common endpoint phase

The endpoint reconstruction in [M] uses the formal amplitude
\[
 a(h,Y,x,m)=\sum_{j\ge0}h^j a_j(Y,x,m),\qquad
 \|a_j\|\le MC^j j!,\qquad
 a_0=e^{A_0(Y,x)+m\cdot\Theta(Y,x)}.
 \tag{6}
\]
The norm is on common buffered meridian and soft-variable disks
and a neighborhood of a prescribed clock compact. The nonzero
prefactor \(r(Y)\) is the original one in [M].

Fix \(s\in\mathbb Z\); negative \(s\) is allowed. Consider the actual
formal source \(\mathscr W_m(h,e^{sh}Y)\), keeping \(h,m\) fixed.
Its endpoint identity is rewritten with the SAME phase \(f(Y,x)\)
and amplitude
\[
 a^{(s)}(h,Y,x,m)=
 \frac{r(e^{sh}Y)}{r(Y)}
 \exp\!\left(-\frac{f(e^{sh}Y,x)-f(Y,x)}h\right)
                   a(h,e^{sh}Y,x,m).
 \tag{7}
\]
The coordinate \(x\) is kept fixed in this expression. Formula (7)
is a formal rewriting of the original moment identity; it does
not assume a convergent Laplace integral.

We check the analytic estimates needed to reconstruct it. On smaller
common meridian and \(x\) disks there is \(\epsilon>0\) such that
\(e^{sh}Y\) stays inside the original buffers for \(|h|<\epsilon\).
Cauchy's estimate on this \(h\)-disk gives
\[
 \left\|[h^\ell]a_n(e^{sh}Y,x,m)\right\|
                        \le MC^n n!\epsilon^{-\ell}.
 \tag{8}
\]
At total order \(j=n+\ell\), sum (8) and use \(n!\le j!\).
This preserves a bound \(M'C'^j j!\).
The prefactor ratio in (7) is holomorphic because \(r\) is a unit.
The phase quotient is also holomorphic at \(h=0\), with value
\[
                         s\,Y f_Y(Y,x).
 \tag{9}
\]
Its exponential therefore has geometrically bounded coefficients
on the same smaller disks. Multiplication by it and by the ratio
preserves the Gevrey estimate, by the same finite convolution.
Thus
\[
 a^{(s)}=\sum_{j\ge0}h^j a_j^{(s)},\qquad
 \|a_j^{(s)}\|\le M_s C_s^j j!,\qquad
 a_0^{(s)}=e^{-sYf_Y(Y,x)}a_0(Y,x,m).
 \tag{10}
\]
All these identities retain the original clocks and framing.

For \(Y\ne\alpha\), let \(x(Y,\xi)\) be the inverse of \(f(Y,x)\)
at \(x=\xi=0\). The exact coefficient and residue argument of
[M, Section 3], applied to the amplitude (10), gives the actual
convergent Borel germ of the shifted source:
\[
 \mathcal B_h[\mathscr W_m(h,e^{sh}Y)]
   =r(Y)\sum_{j\ge0}I_\xi^j
      \left[
       \frac{a_j^{(s)}(Y,x(Y,\xi),m)}
            {f_x(Y,x(Y,\xi))}
      \right].
 \tag{11}
\]
Every \(I_\xi\) starts at the original zero. The only ingredients
needed for that proof are the Gevrey bound, \(f(Y,0)=0\),
\(f_x(Y,0)=Y-\alpha\), and the finite residue expansion of the
phase; all are unchanged here. Thus (11) is the shifted original
source, not another analytic solution with the same candidate
action.

Use [M]'s inverse Morse coordinate
\[
                   f(Y,x(Y,v))=\xi_g(Y)+v^2,
 \quad v_0(Y)=v(Y,0),\quad v_0(Y)^2=-\xi_g(Y).
 \tag{12}
\]
For \(j\ge1\) the terms in (11) are exactly
\[
 \frac1{(j-1)!}\int_{v_0(Y)}^v
       (v^2-t^2)^{j-1}
       a_j^{(s)}(Y,x(Y,t),m)x_v(Y,t)\,dt .
 \tag{13}
\]
The same factorial cancellation as in [M] makes their sum
holomorphic in \(v\) on a fixed smaller Morse disk.
Consequently only \(j=0\) supplies its leading \(v^{-1}\) term.
Relative to the original source its coefficient is multiplied by
\(e^{-sY f_Y(Y,x_g)}\).

The envelope identity, using \(f_x(Y,x_g)=0\), gives
\[
       Y S_g'(Y)=-Yf_Y(Y,x_g(Y)).
 \tag{14}
\]
We have therefore proved the actual shifted-source minor rule
\[
 \boxed{\displaystyle
  \operatorname{leadminor}\!
       \left(\mathcal B_h[\mathscr W_m(h,e^{sh}Y)]\right)
                = e^{sY S_g'(Y)}\,\mathfrak a_m(Y).}
 \tag{15}
\]
The cover used in (11)--(15) is the same unshifted cover (12);
the quantum shift has been incorporated in its actual amplitude.
No analytic summation of an infinite meridian differential operator
was used.

## 3. Scalar quantum factors and retained histories

We also need the effect of a scalar \(c(h,Y)\), holomorphic near
\(h=0\). Multiplication by \(h^j\) on the original formal source
is the canonical primitive \(I_\xi^j\) on its Borel transform.
This statement includes its initial constants.

Write a local continued Borel source as \(b(Y,\xi)=B(Y,v)/v\),
where \(B\) is holomorphic on the Morse disk. For \(j\ge1\),
\[
 I_\xi^j b=
       \frac2{(j-1)!}\int_{v_0(Y)}^v
               (v^2-t^2)^{j-1}B(Y,t)\,dt .
 \tag{16}
\]
Thus every positive primitive is holomorphic in \(v\), including
its complete original-base contribution. On fixed smaller disks,
its norm is bounded by
\(C(2r^2)^{j-1}/(j-1)!\).
The coefficients of \(c(h,Y)\) have a geometric bound. Therefore
the convolution \(\sum c_j(Y)I_\xi^j b\) converges normally there,
and its leading minor is exactly
\[
                            c(0,Y)\operatorname{leadminor}(b).
 \tag{17}
\]
All returned histories contained in this local cover are still
the integrals from \(v_0(Y)\) in (16). Their holomorphy at the
fold is what excludes them from the \(v^{-1}\) coefficient.
They have not been removed from the source function.

In particular the original factor \(Q^{c/2}=e^{ch/2}\) in [E]
has leading multiplier one. It is not being replaced by one in
the exact equation; its other terms remain positive canonical
primitives.

## 4. Extracting the actual external row

The source equation proved in [E, (9)] is
\[
 D(Y,\mathsf E)\,\mathsf T\mathscr W_m
     =Q^{c/2}\mathsf E^{H/2}N(Y,\mathsf E)\mathscr W_m,
 \quad
 \mathsf T:Y\mapsto e^hY,\quad
 \mathsf E_i:m\mapsto m+e_i .
 \tag{18}
\]
It follows from the literal whole-lattice product identity and
the original grading completion. The external shift changes no
support face. The displayed left ordering matters: the \(Y\)
in \(D\) is not shifted by \(\mathsf T\).

All Laurent polynomials in (18) are finite. Given a clock compact,
enlarge it by their finitely many positive or negative clock
translations. Equations (2), (11) and (16) provide convergent
actual Borel germs for every term, and their continuation on one
common smaller Morse cover. Since (18) is the actual formal
identity, their initial germs agree. Analytic uniqueness continues
the equality along the same original lifts to that cover.

Take its \(v^{-1}\) coefficient. The actual clock character (3),
the shifted-source rule (15) with \(s=1\), and (17) give
\[
 e^{Y S_g'}D(Y,e^{\Theta_g})\,\mathfrak a_m
   =e^{(H/2)\cdot\Theta_g}N(Y,e^{\Theta_g})\,\mathfrak a_m .
 \tag{19}
\]
The factor \(\mathfrak a_m\) is nonzero, by [M].
Moreover \(\Theta_g(\alpha)=0\), so
\[
 D(\alpha,\mathbf1)=N(\alpha,\mathbf1)
   =(1-\alpha^{-1})^{\ell_+}(1-\alpha)^{\ell_-}\ne0.
 \tag{20}
\]
Both evaluations stay units after shrinking the disk. Cancelling
these actual nonzero factors proves (5).
Since \(S_g=O((Y-\alpha)^2)\), its left side has value one at
the node, consistent with \(\mathcal R(Y,\mathbf1)=1\).

For the normal-state gauge \((Y-1)\mathscr W_m\), use [E, (10)].
Its extra leading gauge factors are the same unit \(Y-1\) on
both sides. The conclusion (5) is unchanged. This observation
does not alter the reduced normalization used in the proof.

## 5. Scope and complete proof directs

The identity is forced by the actual finite source row and the
actual nonzero marked Borel minor. It is stronger than matching a
first derivative at the Alexander node or substituting a formal
stationary ansatz into a scalar operator.

No finite Laplace cutoff was required: the argument extracts a
local Laurent coefficient of continued Borel functions. All
original positive primitives remain in those functions, and no
statement about finite-cutoff endpoint cancellation or physical
cycle coefficients follows. Identifying a preferred longitude or
hyperbolic branch is a separate problem.

| Label | Complete proof direct | SHA256 |
|---|---|---|
| M | notes/research_actual_marked_fold_borel_reconstruction.md | e4024d94b614087078c9860572a80486731ebdae7632694ec4ac16c1a4d29cab |
| E | notes/research_actual_quantum_meridian_clock_connection.md | 883a4526e8db3e666f8f962b8eb5311700afbc7813b1b74b16be03bcdac3e865 |
| P | notes/research_actual_analytic_principal_phase.md | 9ae7b5df2dbd955ee6ac4580590d9f21d1b1750bcdd6c5085e7322251ab70bcb |

M supplies the actual endpoint reconstruction, common-disk amplitude
bounds and nonzero leading clock character. E supplies the exact
external row, its zero-framing normalization and finite Laurent
coefficients. P supplies the analytic phase and its calibrated
critical germ. The shifted amplitude estimate and the extraction
of the actual action equation are proved above.
Only written mathematics and source-text/hash operations were used.
Frozen proofs and public manuscripts are unchanged.
