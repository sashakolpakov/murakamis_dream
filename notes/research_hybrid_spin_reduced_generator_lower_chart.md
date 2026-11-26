# The complete reduced boundary generator in a hybrid spin chart

Private written proof, 19 November 2026. Author-final for independent review.

The actual product \(S_rD_{\rm red}\), rather than its Euler factor
alone, has a nonzero ordinary-binomial coherent kernel near the
resolved lower donor. Physical recipients may lie in any fixed compact
incidence complement; factorial recipients lie near their lower row.
The statement includes its true fixed-root meridian family, explicit
phase and unit amplitude, all recipient caps, and the canonical graph
of the product in its actual order.

This completes the local boundary factor introduced by a positive left
stabilization. It does not estimate the other physical crossings or
select a component of the original closed cycle. The complete directs
are H, the hybrid star proof, and G, the literal reduced generator and
its rational graph. They are pinned below.

## 1. Literal finite kernel and its donor-slot recurrence

Use \(N\ge2,\ d=N-1,\ h=N^{-1},\ c=2\pi i,\ Q=e^{ch}\),
\[
 x=-M e^{-ch/2},\qquad f_a=(Q;Q)_a,\qquad
 G_Fw_a=f_aw_a .
 \tag{1}
\]
The quantum root is fixed and \(M\ne0\) varies. G gives the exact
positive reduced generator \(\kappa(M)S_rD_{\rm red}\), where
\[
 S_r=\sum_{n=0}^d\frac{(x^{-1}L_1F_{\rm t})^n}{f_n},
 \qquad
 F_{\rm t}=\sum_{j=2}^rK_2^{-1}\cdots K_{j-1}^{-1}F_j,
 \tag{2}
\]
\[
 D_{\rm red}w_a=\lambda_aw_a,\qquad
 \lambda_a=(-1)^aQ^{a(a-1)/2}x^{-2a}
           =(-M^{-2})^aQ^{a(a+1)/2}.
 \tag{3}
\]
Thus
\[
 \lambda_0=1,\qquad
 \lambda_{a+1}/\lambda_a=\beta_hQ^a,\qquad
                         \beta_h=-QM^{-2}.
 \tag{4}
\]
The rightmost factor acts first.

Choose factorial gauges on the donor and a subset
\(H_0\subset\{2,\ldots,r\}\) of recipients, and physical gauges
elsewhere. Put
\[
 \mathcal G=G_{F,1}\prod_{i\in H_0}G_{F,i},\qquad
 \widetilde B=\mathcal G^{-1}S_rD_{\rm red}\mathcal G.
 \tag{5}
\]
The diagonal (3) commutes with \(\mathcal G\). The exact kernel is
\[
 \mathcal K_N(z,w)=
 \sum_{\alpha,\gamma\in\{0,\ldots,d\}^r}
 z^\alpha\widetilde B_{\alpha\gamma}
                     \prod_i\binom d{\gamma_i}w_i^{\gamma_i}.
 \tag{6}
\]
Every gauge in (5) is retained on the neighboring source tensors.
No separate asymptotic for its diagonal coupon is invoked.

Write \(t=w_1,\ v_i=z_iw_i,\ I_i=1+v_i\) for \(i\ge2\). Fix any
compact set of \(M,z_1,z_i,w_i\) satisfying
\[
 M\ne0,\qquad I_i\ne0,\qquad
                  |v_i|\le\rho<1/8\quad(i\in H_0).
 \tag{7}
\]
There is no size restriction on physical-recipient \(v_i\).
All neighborhoods and constants below are fixed independently of \(N\).

As in H, temporarily remove only the output caps on \(H_0\).
A physical recipient has the exact output action
\[
 F_j=z_j(1-QT_j),\qquad T_j:z_j\mapsto Qz_j;
 \tag{8}
\]
a gauged recipient has multiplication \(F_j=z_j\) in this auxiliary
model. Physical top arrows in (8) are exactly zero. An auxiliary
gauged output degree is at most \(2d\), because the donor can transfer
at most \(d\). The actual kernel is the final projection of these
gauged output degrees to at most \(d\); monotone raising proves this
without deleting any return path.

Let \(\mathcal Z=x^{-1}F_{\rm t}^{\rm out}\), and let the artificial
donor binomial degree be \(0\le j\le d\). The auxiliary kernel is
\[
 K_j=\sum_{a=0}^j\binom ja(tz_1)^a\lambda_a
        H_a(\mathcal Z/z_1)\prod_{i=2}^rI_i^d,\qquad
 H_a(A)=\sum_{n=0}^a{a\brack n}_Q A^n .
 \tag{9}
\]
This is polynomial at \(z_1=0\). Formula (9) follows from the actual
factorial donor arrow \(f_a/f_{a-n}\), the \(f_n\) in (2), and the
literal input multiplier \(\lambda_a\), before any limit.

The Gaussian Pascal identity
\[
                         H_{a+1}(A)=H_a(QA)+AH_a(A)
\]
and ordinary binomial Pascal give the exact recurrence
\[
 \boxed{\quad
 K_{j+1}=K_j+\beta_h t z_1K_j(Q^2t,Q^{-1}z_1)
                   +\beta_h t\mathcal ZK_j(Qt,z_1),
 \qquad K_0=\prod_{i=2}^rI_i^d.
 \quad}
 \tag{10}
\]
Indeed \(Q^a\) in (4) multiplies the donor product by \(Q\);
in the first term the additional \(H_a(QA)\) requires precisely
the two shifts displayed in (10). All recipient arguments not
displayed remain unchanged.

## 2. Normalized evolution, phase and first correction

Divide only by the recipient background:
\[
                    G_j=K_j/\prod_{i=2}^rI_i^d.
 \tag{11}
\]
Thus \(G_j(0)=1\). The donor diagonal is not divided out or
replaced by an identity cap.

To state all coefficients explicitly, index \(\nu=(j,e)\), with
\(2\le j\le r,\ e=0\), and also \(e=1\) when \(j\notin H_0\).
Set
\[
 I_\nu=\{2,\ldots,j-1\}\cup
                       \bigl(\{j\}\text{ if }e=1\bigr),
 \qquad Y_\nu=c\sum_{i\in I_\nu}z_i\partial_{z_i},
 \tag{12}
\]
\[
 a_{\nu,h}=(-1)^eQ^ex^{-(j-1)}z_j
       \prod_{i\in I_\nu}
            \left(\frac{1+Qv_i}{1+v_i}\right)^{h^{-1}-1}.
 \tag{13}
\]
The ratio logarithms in (13) are zero at \(h=0\), so (13) has a
holomorphic germ there. This only expands the coefficients at the
physical sequence \(h=1/N\); it does not assert a non-root matrix
identity.

Let \(D=t\partial_t\), \(Y_*=c(2D-z_1\partial_{z_1})\) and
\(Y_\nu^*=cD+Y_\nu\). Then (10) becomes
\[
 G_{j+1}=G_j+\beta_h t
       \left[z_1e^{hY_*}G_j+
                    \sum_\nu a_{\nu,h}e^{hY_\nu^*}G_j\right].
 \tag{14}
\]
Every shift, including the double donor clock, carries \(t\).

For \(V_j=h\log G_j\), understood initially as a formal activity
series, (14) is
\[
 V_{j+1}=V_j+h\mathcal F_h(V_j),
 \tag{15}
\]
\[
 \mathcal F_h(V)=
 \log\left[1+\beta_h t
  \left\{z_1e^{(e^{hY_*}-1)V/h}
       +\sum_\nu a_{\nu,h}e^{(e^{hY_\nu^*}-1)V/h}\right\}\right].
 \tag{16}
\]
The multiplier of \([t^n]V_j\) in (15) is exactly one; every
remaining term uses lower activity degrees.

Put \(u_i=v_i/(1+v_i)\). Define
\[
 a_{\nu,0}=(-1)^e(-M)^{-(j-1)}z_j
                          e^{c\sum_{i\in I_\nu}u_i},
 \tag{17}
\]
\[
 b_\nu=ec+(j-1)c/2+
       \sum_{i\in I_\nu}\{-cu_i+c^2u_i(1-u_i)/2\}.
 \tag{18}
\]
Thus \(a_{\nu,h}=a_{\nu,0}(1+hb_\nu+O(h^2))\), while
\(\beta_h=\beta_0(1+ch+O(h^2))\), \(\beta_0=-M^{-2}\).
All these expansions, with fixed derivatives, are uniform on
buffered versions of (7).

The phase is the unique analytic solution through \(0\le\tau\le1\)
of
\[
 V_\tau=\mathcal F(V)=\log Z(V),\qquad V(0)=0,
 \quad
 Z(V)=1+\beta_0t\left[
           z_1e^{Y_*V}+\sum_\nu a_{\nu,0}e^{Y_\nu^*V}\right].
 \tag{19}
\]
Its first correction is completely specified by
\[
 \mathcal F_1(V)=\frac{\beta_0t}{Z(V)}
 \left[z_1e^{Y_*V}(c+Y_*^2V/2)
 +\sum_\nu a_{\nu,0}e^{Y_\nu^*V}
                          (c+b_\nu+(Y_\nu^*)^2V/2)\right],
 \tag{20}
\]
\[
 A_\tau=d\mathcal F[V]A+\mathcal F_1(V)
                         -\tfrac12 V_{\tau\tau},\qquad A(0)=0.
 \tag{21}
\]
In particular the extra \(c\) in both terms of (20) is the literal
\(Q\) in (4). The \(b_\nu\) retain every Cartan half-step and
recipient \(N-1\).

## 3. Uniform analytic estimate and all finite tails

Here are the estimates needed to apply H's full finite-degree
argument to the changed recurrence; no composition of two
separately estimated kernels is used.

On a buffered coordinate polydisk, collapse absolute spatial Taylor
coefficients to a positive variable \(y\). Increase the constant
in \(\mathcal L=C(1+y)^2\partial_y\) so that it majorizes
\(Y_*\) and all \(Y_\nu^*\), including their donor coefficients.
The double donor clock only increases this fixed constant.
For the positive flow \(\phi_s\) of \(\mathcal L\),
\[
             (e^{h\mathcal L}-1)U/h
                         \preceq e^{h\mathcal L}\mathcal LU .
 \tag{22}
\]
A divided difference on activity coefficient \(k\) is bounded by
\(Ck+\mathcal L\) at padding \(\phi_{(k+1)h}\). Its occurrence
in (16) has output degree at least \(k+1\), because of the displayed
\(t\). Products and logarithms obey the same rule coefficientwise.
Thus the bound at output degree \(n\) uses only \(\phi_{nh}\).

The uniformly bounded coefficients (13) and \(\beta_h\), and the
exponentials and logarithm in (16), have a positive majorant
\[
             \frac{C(y)t}{1-C(y)(t+DU+\mathcal LU)}.
 \tag{23}
\]
H's characteristic proof for this explicit majorant applies
unchanged: its characteristics at \(t=0\) are stationary, its
momenta remain \(O(t)\) through time two on small disks, and
the initial-to-final projection is identity at zero activity.
Positive coefficient Euler-step comparison therefore gives, for
some \(\delta,R,C>0\),
\[
 |[t^n]V_j|\le CR^{-n},\qquad
           n\le L_N=\lfloor\delta N\rfloor,\quad j\le d.
 \tag{24}
\]
Choose \(\delta\) from the buffered incidence margin before
choosing the final donor disk. This controls accumulated recipient
rotations by \(n/N\); it does not require a full clock orbit to
avoid incidence. The same characteristic construction gives
the actual analytic solution of (19) and its linear transport
(21), with \(V(\tau,0)=A(\tau,0)=0\).

The exact complete polynomial has the independent bound
\[
                              |G_j|\le e^{C_0N}.          \tag{25}
\]
In (9), \(|{a\brack n}_Q|\le\binom an\), the original recipient
raising coefficients are at most two, and the auxiliary gauged
coefficients are one. Cartan phases have modulus one apart from
bounded powers of \(x^{\pm1}\). Each \(n\)-fold tail coefficient
is consequently at most \(C^n\). The new factor
\[
                         |\lambda_a|=|M|^{-2a}
\]
costs only \(e^{CN}\) on the fixed meridian compact. Input binomial
sums, evaluation of output degrees at most \(2d\), and the inverse
background in (11) have the same bound. This proves (25), retaining
the coherent normalization conditioning.

Let \(V_j^{[L_N]}\) be its low-degree logarithm. On a fixed small
activity circle, (24) bounds it by \(C|t|\). The exact \(G_j\)
and \(\exp(NV_j^{[L_N]})\) agree through degree \(L_N\).
On a smaller circle of relative radius \(\eta\), their difference
is at most
\[
                         C\eta^{L_N+1}e^{C_1N}.          \tag{26}
\]
Its comparison exponential is at least \(e^{-C_2N|t|}\).
Choose \(\eta\) after \(\delta,C_1,C_2\). This makes (26)
exponentially small relatively and pays all high activity degrees.

For the phase/transport comparison, \(W_j=V(jh)+hA(jh)\) has
residual \(O(h^3)\), with analytic activity factor \(t\), in (15).
The derivative of (16) on the bounded coefficient majorants has
the form \(B_1(t,y)De+B_2(t,y)\mathcal Le\), with \(B_i=O(t)\).
The positive linear characteristic flow and the same degree padding
bound the low-degree error by \(h^2CR^{-n}\). This is precisely
H's discrete stability argument, now with the explicitly changed
fields and coefficients (13),(16),(20). Combining it with (26)
and the analytic tails of \(V,A\) gives
\[
 G_d=e^{NV(1)}a(1+O(N^{-1})),\qquad
                       a=e^{A(1)-V_\tau(1)}\ne0.
 \tag{27}
\]
The last correction is the actual slot endpoint \(d/N=1-h\).
At \(t=0\), \(a=1\).

Finally restore every \(H_0\)-recipient output cap. Choose
\(R_m>1\) with \(R_m\rho<1\) and
\[
 g=\log R_m-\log\frac{1+R_m\rho}{1-\rho}>0.
 \tag{28}
\]
Apply (27) uniformly with \(z_i\mapsto\xi_i z_i\),
\(|\xi_i|=R_m\), for each subset of \(H_0\). The recipient
background ratio costs at most
\([(1+R_m\rho)/(1-\rho)]^{d|J|}\), and the normalized
phase ratio costs at most \(Ce^{CN|t|}\).
The Cauchy tail of output degree at least \(N\) on each
marked head gives \(R_m^{-N|J|}(1-R_m^{-1})^{-|J|}\).
Shrinking \(t\) after (28) pays every nonempty subset
exponentially relatively. Inclusion--exclusion therefore
restores the exact original kernel (6).

The result is
\[
 \boxed{\quad
 \mathcal K_N(z,w)=
       \prod_{i=2}^rI_i^d\,e^{NV(1,z,w,M)}
                     a(z,w,M)(1+O(N^{-1})).
 \quad}                                                  \tag{29}
\]
It is zero-free on a fixed small donor disk and the stated
recipient chart for all sufficiently large \(N\).
The normalized remainder
\(\mathcal K_N/[\prod I_i^d e^{NV(1)}a]-1\) is holomorphic
on a buffered chart. Cauchy bounds each fixed coherent and actual
fixed-\(q\) meridian derivative of this remainder by \(O(N^{-1})\).
No relative estimate is asserted after dividing by a derivative
of the leading term that may vanish.
The original reduced generator has kernel exactly
\(\kappa(M)\mathcal K_N\); every derivative of that specified
scalar and any separately assigned framing line remains.

## 4. Canonical graph in the actual order \(S\circ D_{\rm red}\)

The full phase is
\[
                  \mathfrak F=\sum_{i=2}^r\log I_i+V(1).
 \tag{30}
\]
Its amplitude with \(e^{N\mathfrak F}\) is
\(a/\prod_{i=2}^rI_i\), retaining the identity degrees \(N-1\).
Use the mixed spin dictionaries proved in H: input occupation
\(u_i=w_i\mathfrak F_{w_i}\), output occupation
\(u_i'=z_i\mathfrak F_{z_i}\), \(A_i=e^{cu_i}\),
\(A_i'=e^{cu_i'}\). On the factorial donor
\[
 f_1=\frac{\mathfrak F_t}{1-t\mathfrak F_t},\qquad
 f_1'=z_1.
 \tag{31}
\]
Recipients have their actual physical or factorial dictionaries,
including the ordinary-binomial \(1-u_i\) denominators.

Differentiating the exact donor coefficient in (9) gives
\[
 \boxed{\quad
 \partial_tK_d=(d-D)\{
       \beta_h z_1K_d(Q^2t,Q^{-1}z_1)
                +\beta_h\mathcal ZK_d(Qt,z_1)\}.
 \quad}                                                  \tag{32}
\]
The finite endpoint \(d-D\) is essential. Taking the principal
equation using (29), with all cap errors retained as above, gives
\[
 f_1=\beta_0\left[
       z_1\frac{A_1^2}{A_1'}+
                 \frac{A_1}{x_{\rm cl}}F_{\rm t}'\right],
 \qquad x_{\rm cl}=-M,\quad \beta_0=-M^{-2}.
 \tag{33}
\]
Here \(F_{\rm t}'\) is the original ordered recipient total,
using the physical \(f_j'\) on raw heads and \(f_j'=z_j\)
on factorial heads.

G's diagonal map and positive star map, in their actual order,
are
\[
 A_D=A_1,\quad p_D=-A_1p_1/x_{\rm cl}^2,\quad
 f_D=-x_{\rm cl}^2f_1/A_1,
 \tag{34}
\]
\[
 f_D=(A_D/A_1')f_1'+F_{\rm t}'/x_{\rm cl}.
 \tag{35}
\]
Substituting (34) in (35) proves exactly (33). The tail
\(F_{\rm t}\) is preserved by the star. No reversal of the
diagonal/star order has been made.

At \(t=0\),
\[
 \mathfrak F=\sum_{i=2}^r\log I_i,\qquad
 \mathfrak F_t=\beta_0(z_1+F_{\rm t}'/x_{\rm cl}).
 \tag{36}
\]
Equation (33) is an analytic implicit first-order evolution
in \(t\): occurrences of \(\mathfrak F_t\) on its other side
have a factor \(t\), so its implicit derivative is one at
the initial row. Its analytic solution with (36) is unique
by successive Taylor coefficients.

The rational product graph has a regular mixed projection there.
The diagonal changes the unit donor \(f\) by the nonzero factor
\(-x_{\rm cl}^2\); its resolved donor coordinate still satisfies
\(w_1=-p_1/c+O(p_1^2)\). Recipient coordinate derivatives are
the units of H. G's symplectic identity therefore supplies its
local generating function, normalized by (36), and (33)
identifies it with (30).

Equivalently, the mixed Hessian at the row is triangular,
with donor entry \(\beta_0\ne0\), recipient entries \(I_i^{-2}\),
and zero recipient-input/donor-output entries. It remains
nondegenerate on a smaller chart.

At completeness, use physical recipient spin coordinates
for \(p_i\ne0,A_i\ne1\), with any retained finite logarithm
\(u_i=\Log A_i/c\):
\[
 z_i=1/p_i,\qquad w_i=p_i u_i/(1-u_i),\qquad
                         I_i=(1-u_i)^{-1}\ne0.
 \tag{37}
\]
For resolved \(p_i=0,A_i=1,f_i\ne0\), its lower factorial
chart is \(z_i=f_i,w_i=0\). The donor is the lower resolved
row. Thus (29) covers all these local configurations of the
actual boundary product, with all chosen gauges retained.
Nonlower recipient logarithmic aliases are not reset to zero.

## 5. Scope of the completed boundary factor

The estimate concerns the full introduced factor
\(\kappa S_rD_{\rm red}\), with its literal common scalar,
its fixed-root meridian family, and the original finite
binomial columns. No separate pointwise cancellation of a
factorial or diagonal coupon was used.

The exact common-source convention still places inverse
interface gauges on neighboring factors and retains both
Cartan rows and the first meridian jet. This theorem does not
give a local kernel for arbitrary internal physical crossings.
Nor does a lower-row chart select its occurrence in the full
closed period, remove recipient aliases, or estimate a closing
pairing. Those remain separate source questions.

The zero donor action at the initial row is a local normalization.
Equality of rational canonical graphs does not identify the full
common-spin critical value with the geometric volume: that comparison
still includes the physical crossings, interface gauges, and measures.

## Complete proof-source pins

* H: notes/research_hybrid_spin_euler_star_lower_chart.md, 696 lines,
  SHA256 1575d7cee6c12c7d9c6ada57a7be61eecccf4b637cdc70ed7777fc7b9b620b93.
* G: notes/research_actual_reduced_braid_critical_scheme.md, 564 lines,
  SHA256 ddddcd9bf75f35afdf3e5de0c03323acee2c66e624db36142c2344ef729a977a.

Both complete matching direct reads are retained fresh unchanged
from the immediately preceding hybrid author/formal sequence.
The entire matching author-final was reread nontruncated, every used
implication checked, and both complete direct pins renewed.
Only written mathematics and text/hash operations were used.
Frozen and public files were unchanged.
