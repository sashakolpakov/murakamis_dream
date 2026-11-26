# Convergent transport of the canonical minor along a regular branch

Private written proof, 18 November 2026.

The regular minor in [M] is the deck-odd part of the actual canonical
source at its specified Alexander node. This note continues that same
minor along a compact lifted path on the same isolated classical branch.
The proof retains every initial Taylor coefficient. One integration by
parts in the triangular transport equations gives a single-factorial
bound, which the Borel normalization converts into convergence.

Only the odd minor is continued by this argument. It does not continue
the full deck-even source, complementary cycles, or the original
fixed-cutoff endpoint current. The identification of the branch with a
hyperbolic representation and the original finite-color lower bound
remain separate.

## 1. Actual data and the transport assertion

Keep the logarithmic meridian, state gauge, and actual finite-shift
annihilator of [M]:
\[
 \mathcal P_h=\sum_{i\in\mathcal I}p_i(h,u)T^i,\qquad
 Tf(u)=f(u+h),\qquad
 P(u,L)=\sum_i p_i(0,u)L^i .
 \tag{1}
\]
The set \(\mathcal I\subset\mathbb Z\) is finite; \(i\) denotes an
integer shift, not the imaginary unit. Let \(\gamma\) be a compact
piecewise smooth lifted path beginning at a regular point of the
minor disk in [M]. Along this path assume that:

* the coefficients in (1) are holomorphic on neighborhoods of \(h=0\)
  and of the lifted path;
* the selected root \(\ell(u)\in\mathbb C^*\) continues along the path,
  with \(P(u,\ell(u))=0\) and
  \[
                   d_g(u)=\ell(u)P_L(u,\ell(u))\ne0;
  \tag{2}
  \]
* its logarithm and action are continued from the initial source,
  \[
                   S'(u)=\log\ell(u).
  \tag{3}
  \]

All statements below are on this lift. No action constant or logarithmic
branch is reset. The path does not pass through another discriminant or
coefficient pole. Its initial point can be any sufficiently small
nonzero point of the node chart; [M] already treats the node itself.

The initial actual odd source is
\[
 b_o(u,\xi)=\rho^{-1/2}A(u,\rho),\qquad
 \rho=\xi+S(u),\qquad
 A(u,\rho)=\sum_{n\ge0}a_n(u)\rho^n,
 \tag{4}
\]
where \(A\) is jointly holomorphic and \(a_0\ne0\).

**Theorem.** The germ \(A\) in (4) has joint analytic continuation along
\(\gamma\), with a positive transverse \(\rho\)-radius on a neighborhood
of the whole compact lifted path. On a finite chart cover of that path
there are constants \(C,D>0\) such that
\[
                         |a_n(u)|\le CD^n
                         \qquad(n\ge0).
 \tag{5}
\]
The leading coefficient never vanishes and is the continuation of
the original coefficient:
\[
 a_0(u)=a_0(u_c)
     \exp\left(-\int_{u_c}^{u}\frac{e_g(v)}{d_g(v)}\,dv\right),
 \tag{6}
\]
with the path and logarithms retained. Here
\[
 \begin{split}
 e_g(u)={}&P^{[1]}(u,\ell(u))\\
 &+\frac{S''(u)}2
      \{\ell(u)P_L(u,\ell(u))+\ell(u)^2P_{LL}(u,\ell(u))\},\\
 P^{[1]}(u,L)={}&\sum_i\partial_hp_i(0,u)L^i .
 \end{split}
 \tag{7}
\]
Every higher initial coefficient in (4), not just \(a_0\), is retained.
The theorem gives continuation on a path lift, not single-valuedness
after arbitrary loops in the meridian plane.

## 2. The exact triangular equations and their normalization

The action-coordinate coefficients are
\[
 p_i^S(h,u)=p_i(h,u)
       \exp\left(\frac{S(u+ih)-S(u)}h\right).
 \tag{8}
\]
They are holomorphic at \(h=0\) on every buffered regular chart.
Their differential expansion is
\[
 \sum_i p_i^S(h,u)e^{ih\partial_u}
       =\sum_{m\ge0}h^mL_m,\qquad
 L_0=0,\qquad L_1=d_g\partial_u+e_g.
 \tag{9}
\]
The differential order of \(L_m\) is at most \(m\).
All derivatives here hold \(\rho\) fixed.

The actual odd source equation in [M, Section 3] is
\[
 L_1b_o+\sum_{j\ge1}I_o^jL_{j+1}b_o=0,
 \tag{10}
\]
where \(I_o\) is the unique odd primitive on the square-root cover.
The retained primitive-history terms are deck even and hence absent
from (10); they have not been set to zero in the full source.
For the regular minor,
\[
 I_o^j\rho^{n-j-1/2}
       =\frac{\rho^{n-1/2}}{(n-j+\tfrac12)_j}.
 \tag{11}
\]
Thus the exact coefficient equations are
\[
 L_1a_n+
   \sum_{j=1}^n\frac{L_{j+1}a_{n-j}}
                       {(n-j+\tfrac12)_j}=0 .
 \tag{12}
\]
Only finitely many terms occur for each \(n\).

Put
\[
             v_n=(\tfrac12)_n a_n,\qquad f_n=v_n/a_0.
 \tag{13}
\]
Then \(f_0=1\), and (12) becomes
\[
 f_n'=\sum_{j=1}^n\sum_{l=0}^{j+1}
                         q_{jl}(u)f_{n-j}^{(l)}.
 \tag{14}
\]
The sign of the forcing has been included in \(q_{jl}\).
Equation (6) follows from (12) at \(n=0\).

We record the analytic coefficient bound for (14). On a buffered disk
where \(d_g\) and \(a_0\) are nonzero, the finite-shift coefficients
\[
 \widehat p_i(h,u)=
 \frac{p_i^S(h,u)a_0(u+ih)}{d_g(u)a_0(u)}
 \tag{15}
\]
are jointly holomorphic. The order-\(h\) differential coefficient of
their operator is exactly \(\partial_u\). Therefore
\[
 q_{jl}(u)=-
   \sum_i[h^{j+1-l}]\widehat p_i(h,u)\frac{i^l}{l!}.
 \tag{16}
\]
Cauchy estimates in \(h\), followed by one Cauchy estimate on a larger
\(u\)-disk, give constants \(M,C\) with
\[
        |q_{jl}(u)|+|q_{jl}'(u)|
                      \le \frac{MC^j}{l!},
      \qquad j\ge1,\quad0\le l\le j+1.
 \tag{17}
\]
This uses the literal finite set of shifts and holomorphic source
coefficients. It invokes no formal factorization or hypothetical
homogeneous mode.

## 3. A local analytic estimate

Choose a disk \(D_R=\{|u-u_c|<R\}\), with \(R\le1\), whose larger
buffer supports (17). Suppose the initial germ has
\[
                       |a_n(u_c)|\le M_0C_0^n .
 \tag{18}
\]
Because \((1/2)_n\le n!\), its normalized data satisfy
\[
                       |f_n(u_c)|\le M_1C_1^n n! .
 \tag{19}
\]
The constants include the fixed nonzero value \(a_0(u_c)\).

For a holomorphic function on \(D_R\), define
\[
 d(u)=R-|u-u_c|,\qquad
 \|f\|_p=\sup_{D_R}|f(u)|d(u)^p,\qquad p\ge0 .
 \tag{20}
\]
The elementary Nagumo estimate is
\[
        \|f^{(r)}\|_{p+r}
          \le e^r\frac{(p+r)!}{p!}\|f\|_p.
 \tag{21}
\]
For the first derivative, use a Cauchy circle with radius
\(d/(p+1)\) when \(p\ge1\), and \(d/2\) when \(p=0\).
The factor \((1+1/p)^p\le e\) proves the first-derivative bound.
Iteration proves (21).

Solve (14) recursively by integration from the center \(u_c\).
For \(l\ge1\), integrate its forcing once by parts:
\[
 \begin{split}
 \int_{u_c}^{u}q_{jl}(v)f_{n-j}^{(l)}(v)\,dv
   ={}&q_{jl}(u)f_{n-j}^{(l-1)}(u)
       -q_{jl}(u_c)f_{n-j}^{(l-1)}(u_c)\\
     &-\int_{u_c}^{u}q_{jl}'(v)
                            f_{n-j}^{(l-1)}(v)\,dv .
 \end{split}
 \tag{22}
\]
The term \(l=0\) is left as its ordinary integral. This single
integration by parts is the gain: every derivative on the right of
(22) has order at most \(j\), rather than \(j+1\).
The center boundary term is retained.

Write \(p=n-j\), \(F_p=\|f_p\|_p\), and \(r=l-1\le j\).
By (21),
\[
 \|f_p^{(r)}\|_n
       \le R^{j-r}e^r\frac{(p+r)!}{p!}F_p
       \le e^j\frac{n!}{p!}F_p .
 \tag{23}
\]
The constant function \(f_p^{(r)}(u_c)\) satisfies the same bound:
its pointwise estimate from (21) has a factor \(R^{-p-r}\),
whereas its norm of index \(n\) adds \(R^n\).

Use the radial segment \(v=u_c+t(u-u_c)\) for the integrals.
It satisfies \(d(v)\ge d(u)\), and its length is at most \(R\).
Consequently the integral term in (22) satisfies the same bound as
(23), multiplied by \(R\|q_{jl}'\|_\infty\).
The \(l=0\) integral is bounded by
\(R^{j+1}\|q_{j0}\|_\infty F_p\), which is also covered by the
right side of (23) with its coefficient constant.

Using (17), summing the at most \(j+2\) derivative terms, and absorbing
their geometric factors into constants gives
\[
 F_n\le R^n|f_n(u_c)|
       +M_2\sum_{j=1}^nD_2^j
                       \frac{n!}{(n-j)!}F_{n-j}.
 \tag{24}
\]
This estimate also proves inductively that the displayed norms are
finite; boundedness at the boundary of \(D_R\) was not assumed.

Let \(\beta_n=F_n/n!\). Equations (19) and (24) imply
\[
 \beta_n\le M_1C_1^n+
                  M_2\sum_{j=1}^nD_2^j\beta_{n-j}.
 \tag{25}
\]
This geometric convolution has a geometric majorant. For example,
choose \(D_3\) larger than \(2C_1\) and \((2M_2+1)D_2\), and then
choose \(C_3\) large enough for \(n=0\) and the initial term.
Induction in (25), using
\(\sum_{j\ge1}(D_2/D_3)^j=D_2/(D_3-D_2)\), gives
\[
                           F_n\le C_3D_3^n n! .
 \tag{26}
\]

On \(|u-u_c|\le R/2\), divide by \((1/2)_n\) in (13).
The elementary bound \(n!/(1/2)_n\le2^n\) yields
\[
                   |a_n(u)|
                      \le C_4(4D_3/R)^n .
 \tag{27}
\]
Hence the series for \(A\) converges normally, for example on
\[
             |u-u_c|<R/2,\qquad |\rho|<R/(8D_3).
 \tag{28}
\]
It is jointly holomorphic there. Cauchy estimates on smaller disks
also justify all fixed derivatives and the coefficient equations.
No second factorial has been lost.

## 4. Matching and continuation along the compact path

The recursion (12) is triangular. Once \(a_0\) and all values
\(a_n(u_c)\) are fixed, the ordinary first-order equations determine
every \(a_n\) uniquely. Starting in the actual minor disk of [M],
the construction of Section 3 therefore equals that actual germ on
its overlap. It is analytic continuation, rather than a new solution
selected only by its leading WKB coefficient.

Cover the compact lifted path by finitely many buffered disks where
(1)--(3) and (17) hold, and subdivide the path so each successive
piece lies in the inner half of its chart. At a new center, the
previous jointly holomorphic minor supplies an exponential bound
of the form (18). Apply Section 3 again with those exact values.
On the overlap, uniqueness of (12), followed by normal convergence,
identifies the two full germs \(A\).

There are only finitely many steps. Each supplies a positive
transverse radius; their minimum after further finite shrinking
is positive. Taking maxima of the finitely many coefficient constants
gives (5). Formula (6) proves nonvanishing of \(a_0\) along the lift.
This proves the theorem.

All branch and action data are continued along the specified path.
If its projection has loops, the proof does not identify different
lifts without their actual continuation. Higher integration constants
are never replaced by zero or inferred from the leading amplitude.

## 5. The phase branch and leading connection are source intrinsic

There is a useful consequence for any other analytic finite-shift
operator \(\mathcal Q_h\) that annihilates the same canonical formal
source on the common initial source/node chart. Keep its original state
gauge, and continue its coefficient functions along the same lift.
They must be regular on the portions under consideration; any
meromorphic coefficient poles are excluded from those portions.
An arbitrary operator germ specified only at an unrelated endpoint
is not included. Write \(Q(u,L)\)
and \(Q^{[1]}(u,L)\) for its classical and first normal symbols.

Repeat the explicit graph-coordinate/history adapter of [M, Section 3]
with these coefficients, without initially assuming that its
order-zero term vanishes. Its exact undifferentiated odd equation is
\[
 Q(u,\ell(u))b_o+\sum_{j\ge1}I_o^jK_jb_o=0 .
 \tag{29}
\]
Here \(K_j\) are the differential coefficients of its conjugated
finite-shift expansion. Normal convergence follows from the same
finite-shift Cauchy and primitive-factorial estimates. The history
corrections are still deck even; this is an identity for the actual
source, not a separate solution of \(\mathcal Q_h\).

The coefficient of \(\rho^{-1/2}\) in (29) is
\(Q(u,\ell(u))a_0(u)\). Every positive primitive of the regular
odd minor has strictly higher \(\rho\)-exponent. Since \(a_0\ne0\),
\[
                              Q(u,\ell(u))=0.
 \tag{30}
\]
Differentiating (29) once in \(\rho\), and extracting the same
coefficient, now gives
\[
                  d_Qa_0'+e_Qa_0=0,
 \tag{31}
\]
where
\[
 \begin{split}
 d_Q&=\ell Q_L(u,\ell),\\
 e_Q&=Q^{[1]}(u,\ell)
       +\frac{S''}2\{\ell Q_L(u,\ell)+\ell^2Q_{LL}(u,\ell)\}.
 \end{split}
 \tag{32}
\]
The identities first hold on the actual initial minor chart.
Coefficientwise analytic continuation, or the normally convergent
equation (29), preserves them along every part of the lift where
the coefficients of \(\mathcal Q_h\) are regular.

Consequently
\[
       -e_Q/d_Q=a_0'/a_0=-e_g/d_g
                      \quad\hbox{where }d_Q\ne0.
 \tag{33}
\]
At a point with \(d_Q=0\), equation (31) instead forces \(e_Q=0\).
Thus both the local branch and its leading rank-one connection are
determined by the actual source in its fixed gauge. The connection
one-form is
\[
                         \Omega=-\frac{e_g}{d_g}\,du,
                    \qquad da_0=\Omega a_0.
 \tag{34}
\]
This does not claim that the full minor is determined by \(a_0\);
all higher initial data in Section 4 remain necessary.

If the original quantum coefficients are rational in \(q\) and
\(Y=\alpha e^u\), so that their first normal coefficients are rational in
\(Y\), then \(\Omega\) is a meromorphic differential on the selected
algebraic curve. Indeed \(\ell\) is algebraic, and
\(S''=\ell'/\ell\) is algebraic wherever the root is simple.
The action itself retains its logarithmic lift.
No algebraicity of the horizontal section \(a_0\), triviality of its
holonomy, or identification with the geometric representation branch
is asserted.

## 6. The continued local Gaussian period and its scope

On any one compact portion of the resulting lifted tube, choose a
small fixed \(\rho\)-endpoint \(\rho_0\ne0\) inside its minor disk.
The actual continued odd minor has the local period
\[
 \mathfrak D_{\rho_0}(h,u)=
       \frac2h e^{S(u)/h}
       \int_{-\sqrt{\rho_0}}^{\sqrt{\rho_0}}
                         e^{-t^2/h}A(u,t^2)\,dt .
 \tag{35}
\]
The orientation and sheet are transported from [M]. Its integrand
is holomorphic throughout the small \(t\)-disk.
The finite Gaussian estimate proved in [M] applies uniformly on
closed sectors facing \(\rho_0\), and gives
\[
 \mathfrak D_{\rho_0}(h,u)=
     2\sqrt\pi\,h^{-1/2}a_0(u)e^{S(u)/h}
                                      \{1+O(|h|)\}.
 \tag{36}
\]
Its leading coefficient is nonzero. Every fixed higher coefficient
is \((1/2)_n a_n(u)\).

In the original Borel coordinate, however, the endpoint in (35) is
\(\xi=\rho_0-S(u)\). It moves with the meridian. Equation (35) is
therefore not automatically the original cutoff with a fixed
\(\xi=R\), nor the original finite-color scalar. Replacing one by
the other requires its actual endpoint current. No control of that
current, of the deck-even source, or of other action cycles is
claimed here.

## 7. Complete proof source

| Label | Complete proof direct | SHA256 |
|---|---|---|
| M | notes/research_canonical_borel_regular_square_root_minor.md | 23b1e6cfc5dcb303af37d7470ab262225c1ced3ede9772f183ab813eff94e42a |

M supplies the actual initial regular minor, its normalization, the
exact action-coordinate odd equation with retained histories, and the
finite local Gaussian estimate. All coefficient bounds, the
integration-by-parts/Nagumo majorant, matching, compact-path
continuation, and source-intrinsic connection are proved here.
In particular Section 5 rederives (30) from the regular actual minor;
it does not use the universal-annihilator conclusion of another note
as an unlisted proof premise.

This result applies along the stated lifted regular arcs. It neither
crosses endpoint discriminants nor supplies a geometric identification
for every short filling. It does not claim a global continuation of the
full original source or a physical lower bound.
Only written mathematics was used; no mathematical programs, tests,
builds, frozen-note edits, or public-manuscript changes were made.
