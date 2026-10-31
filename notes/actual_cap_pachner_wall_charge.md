# Actual cap residues at the Pachner norm wall

28 October 2026. The actual source and co-source give an explicit
residue functional at the simultaneous norm wall of
[the last-move calculation](oversized_alias_last_pachner_wall.md).
For a full holomorphic product it retains its original matrix corner.
For split meromorphic terms it retains a finite list of source jets,
with bounds uniform in the level. The cap is not a projector onto
geometric edge winding one.

The results below use exactly the source frames and residue constants
of [the cap-wall theorem](cap_wall_fermat_quad_residue_transport.md).
They do not replace an invariant or assign an arbitrary source to
the geometric triangulation. The original geometric exterior still
needs its typed comparison with these local matrix coordinates.

The [exact audit](../experiments/audit_actual_cap_pachner_wall_charge.py)
checks 148 direct finite-product identities in cyclotomic fields,
the generic first and second central jets, and the uniform-bound
constants. Its [saved results](../experiments/actual_cap_pachner_wall_charge_results.json)
separate central-meromorphic, fixed-cover-pole, and global-source scope.

For the original word, its Ward corner is used only after the full
intertwining contraction has been assembled. These residue formulas
do not authorize applying that Ward replacement separately to a
cyclic/sewing sector whose full original marked row is different.

## 1. Coincident residues reproduce the original corners

Fix $N\ge2$, $d=N-1$, $Q=e^{2\pi i/N}$ and put

$$
 \varepsilon=a^N,\quad
 \delta=(1-\varepsilon)^{1/N},\quad
 u_0=\delta,\quad u_d=Q\delta,
$$

with the branches equal to $1$ at $\varepsilon=0$. For
$s,t\in\{0,d\}$ use the original Fermat frames

$$
 P_n^{s}(a)=
 \frac{a^n}{\prod_{j=1}^{n}(1-u_sQ^j)},\qquad
 L_m^{t}(a)=
 a^{-m}\prod_{j=0}^{m-1}(1-u_tQ^j).
                                                            \tag{1}
$$

Their original residue constants are

$$
 \alpha_0=\beta_0=1,\qquad \alpha_d=1-Q,\qquad\beta_d=N.
$$

Write $\sigma_0=\tau_0=0$, $\sigma_d=1$, $\tau_d=d$, and
$D_{ts}=\sigma_s+\tau_t$. For any matrix $O(a)$ holomorphic at
zero,

$$
 \boxed{\quad
 \frac1{\alpha_s\beta_t}
 \operatorname{Res}_{a=0}
 a^{D_{ts}-1} L^t(a)O(a)P^s(a)\,da
       =\langle e_t,O(0)e_s\rangle.
 \quad}                                                     \tag{2}
$$

Indeed $P^d_d=(1-Q)a^{-1}+O(a^{N-1})$, while
$P^d_n=O(a^n)$ for $n<d$. Also
$L^d_d=Na^{-d}+O(a)$ and $L^d_m=O(a^{-m})$ for $m<d$.
At the zero corner $P^0_0=L^0_0=1$, whereas
$P^0_n=O(a^n)$ and $L^0_m=O(a^{N-m})$ for $m,n>0$.
Thus exactly $(m,n)=(t,s)$ has the maximal required pole;
every other term has at least one additional power of $a$.
Multiplication by a holomorphic $O(a)$ cannot create another
residue.

For $s=t=d$, (2) is specifically

$$
 \frac1{N(1-Q)}
 \operatorname{Res}a^{N-1}L^d(a)O(a)P^d(a)\,da
       =O_{dd}(0).                                         \tag{3}
$$

This equals the actual independent input/output cap residues.
It is an equality of residue functionals on the stated class,
not a pullback of two differential forms to their diagonal.
For individually singular factors the order of regularization
must therefore still be proved; it cannot be inferred by
substituting the same parameter into two residue formulas.

Taking $O=I$ in (3) gives exactly one. The marked wall has its
original unit augmentation.

## 2. Exact source jets for meromorphic split terms

Suppose now $O=O(\varepsilon)$ is meromorphic, with pole order
at most a fixed integer $p$:

$$
 O(\varepsilon)=\sum_{r=-p}^{\infty}O_r\varepsilon^r.
$$

Let $m(n)=n+t-s\bmod N$, valued in $0,\ldots,d$.
The residue functional in (2) is exactly

$$
 \mathcal R_{ts}(O)
  =\operatorname{CT}_{\varepsilon=0}
       \sum_{n=0}^{d}H^{ts}_n(\varepsilon)
                           O_{m(n),n}(\varepsilon).          \tag{4}
$$

All factors in this formula are retained. Direct telescoping in (1)
gives the following kernels:

| Input $s$ | Output $t$ | Kernel |
|---|---|---|
| $0$ | $0$ | $H_0=1$; for $n>0$, $H_n=(1-\delta)/(1-Q^n\delta)$ |
| $d$ | $d$ | $H_n=\varepsilon(1-Q\delta)/[N(1-Q)(1-Q^{n+1}\delta)]$ |
| $d$ | $0$ | $H_d=(1-Q\delta)/(1-Q)$; for $n<d$, $H_n=(1-\delta)(1-Q\delta)/[(1-Q)(1-Q^{n+1}\delta)]$ |
| $0$ | $d$ | $H_0=\varepsilon/[N(1-\delta)]$; for $n>0$, $H_n=\varepsilon/[N(1-Q^n\delta)]$ |

The quotients at $\varepsilon=0$ are their removable values.
Every kernel is holomorphic there and
$H^{ts}_n(0)=1$ exactly when $n=s$, and is zero otherwise.
If $H^{ts}_n=\sum_{r\ge0}H^{ts}_{r,n}\varepsilon^r$, then

$$
 \boxed{\quad
 \mathcal R_{ts}(O)=
 \sum_{r=0}^{p}\sum_{n=0}^{d}
 H^{ts}_{r,n}(O_{-r})_{m(n),n}.
 \quad}                                                     \tag{5}
$$

Thus a full regularized product uses only its original corner.
Its singular summands can also use $H_1,H_2,\ldots,H_p$.
Those terms disappear only when their corresponding pole
coefficients cancel in the complete product or source current.

For the marked $d\to d$ corner, write $K=H^{dd}$. At $n\ne d$,

$$
 K_{1,n}=\frac1{N(1-Q^{n+1})},\qquad
 K_{2,n}=\frac{Q-Q^{n+1}}
 {N^2(1-Q)(1-Q^{n+1})^2}.                              \tag{6}
$$

At $n=d$,

$$
 K_{0,d}=1,\quad
 K_{1,d}=\frac{Q}{N(1-Q)}-\frac{N-1}{2N},\quad
 K_{2,d}=-\frac{N^2-1}{12N^2}.                         \tag{7}
$$

The second-order coefficient includes the cubic expansion of
$\delta$ before the removable denominator is divided.

## 3. Uniform bounds: no exponential source-jet cost

Take $\rho=1/16$. On $|\varepsilon|\le\rho$,

$$
 |\delta-1|\le\frac{2|\varepsilon|}{N}.
$$

For a nontrivial root $Q^r$, put
$\ell=\operatorname{dist}(r,N\mathbb Z)\ge1$.
The elementary sine bound gives $|1-Q^r|\ge4\ell/N$, and hence

$$
 |1-Q^r\delta|\ge\frac{3\ell}{N},\qquad
 \left|\frac{1-Q\delta}{1-Q}\right|<2.                \tag{8}
$$

All nonexceptional entries of the table are therefore bounded
by $(4/3)|\varepsilon|/\ell$. The two removable quotients use

$$
 A(\varepsilon)=\frac{\varepsilon}{N(1-\delta)}
              =\frac{1+\delta+\cdots+\delta^{N-1}}N,
 \qquad |A|\le1+\rho.
$$

In particular

$$
 K_d=A+\frac{\varepsilon Q}{N(1-Q)},\qquad
 |K_d|\le1+\rho+\rho/4<2.
$$

The remaining wrap value $(1-Q\delta)/(1-Q)$ is also bounded
by two. Consequently, for **all four actual cap channels**,
all $N\ge2$, and all indices,

$$
 \sup_{|\varepsilon|\le1/16}|H^{ts}_n(\varepsilon)|\le2,
 \qquad
 |H^{ts}_{r,n}|\le2\cdot16^r.                         \tag{9}
$$

For example, in the original flat Euclidean matrix basis,

$$
 \boxed{\quad
 |\mathcal R_{ts}(O)|
 \le2N\sum_{r=0}^{p}16^r\|O_{-r}\|_{\mathrm{op}}.
 \quad}                                                     \tag{10}
$$

The factor $N$ can be replaced by a trace-norm bound on each
selected cyclic diagonal. Independent source variables tensor:
for a fixed word and fixed pole orders their combined extraction
has polynomial cost in $N$.

This is a bound relative to the actual Laurent coefficient norms.
It does not turn exponentially large input currents into small
ones without their exact cancellation. Nor is the norm asserted
unchanged under an exponentially conditioned fusion frame.

The [actual sewing theorem](cyclic_sewing_regularized_cut_cycle.md)
retains at most second-order poles per Euler variable. When such
an actual matrix term is expressed in the stated central local
coordinate, (5)--(10) give its exact cap correction and a bound
for the finite source-jet pushforward. They do not authorize
dropping the sewing poles or their finite-part prescription.

### Fixed pole order on the Fermat cover, without central descent

There is a complementary statement for an actual matrix that is
meromorphic in $a$ itself. Put

$$
 \widehat P_s=a^{\sigma_s}P^s/\alpha_s,\qquad
 \widehat L_t=a^{\tau_t}L^t/\beta_t,\qquad
 J_{ts}(a)=\widehat P_s(a)\widehat L_t(a).
$$

These are the regular original cap frames. The uniform cap-wall
estimate gives an absolute $C$ such that their Euclidean norms
are at most $C$ on $|a|\le1/(16N)$. Consequently the rank-one
kernel has trace norm at most $C^2$ there. If
$O(a)=\sum_{\ell=-p}^{\infty}A_\ell a^\ell$, then exactly

$$
 \mathcal R_{ts}(O)=
 \sum_{r=0}^{p}\operatorname{tr}(A_{-r}J_{ts,r}),
 \qquad
 \|J_{ts,r}\|_1\le C^2(16N)^r.                       \tag{10a}
$$

This follows from the original formula
$\operatorname{Res}\widehat L_tO\widehat P_s\,da/a$
and Cauchy's coefficient estimate in trace norm. Thus

$$
 |\mathcal R_{ts}(O)|
 \le C^2\sum_{r=0}^{p}(16N)^r\|A_{-r}\|_{\mathrm{op}}.
                                                            \tag{10b}
$$

For $0<r<N$ the actual endpoint jets are especially explicit.
Writing $F_r=(Q;Q)_r$ and $F_r^-=(Q^{-1};Q^{-1})_r$:

$$
\begin{array}{c|c|c}
 &r=0&0<r<N\\ \hline
 [a^r]\widehat P_0&e_0&e_r/F_r\\
 [a^r]\widehat P_d&e_d&e_{r-1}/F_r\\
 [a^r]\widehat L_0&e_0^t&e_{N-r}^t/F_r^-\\
 [a^r]\widehat L_d&e_d^t&e_{d-r}^t/F_r^-
\end{array}                                                   \tag{10c}
$$

The first central correction to $\delta$ has degree $N$, which
proves this table directly from (1). These are genuine source
and co-source derivatives, with all original normalizations.

A fixed pole order on the cover and a fixed pole order in the
central variable are different hypotheses: a central pole of
order $p$ has cover order $Np$. Estimate (10) is strong precisely
because it uses central descent and exact cyclic-diagonal
telescoping. Estimate (10b) applies without descent only when
the cover pole order is bounded. Neither is a uniform assertion
for arbitrary separated Puiseux factors with growing pole order.

## 4. Monodromy selects the physical cap charge

Under $a\mapsto Qa$, $\delta$ is fixed and

$$
 P^s(Qa)=ZP^s(a),\qquad
 L^t(Qa)=L^t(a)Z^{-1},\qquad Ze_n=Q^ne_n.
$$

The total residue weight is $Q^{D_{ts}}$.
Deck averaging keeps precisely matrix entries with

$$
 m-n\equiv t-s\pmod N.
$$

The zero jet of (4) further selects the actual corner $(t,s)$.
For $d\to0$ and $0\to d$ this is the WRAPPED entry of the
corresponding cyclic diagonal, with coefficient one. Thus actual
cap residues require, rather than delete, a retained cyclic
boundary charge.

In particular the compatible root monodromy $(Q,Q^{-1},Q)$ of
the last Pachner wall cannot by itself be read as a projector
onto geometric edge winding one. It gives a finite root/deck
charge. The geometric integer lift has not been identified
with the original integer-degree/carry data.

## 5. The literal primitive cap retains the generic local wall

There is also a direct local nonvanishing statement. Express the
primitive normalized pentagon in a common clock/shift basis

$$
 X=\mu Z,\quad Y=\eta S,\quad ZS=QSZ,
 \quad \mu(0)=Q,\quad \eta^N=x_0,
$$

and take the actual $d$ input and output cap corners in that
basis. At a generic exceptional direction,
$x_0\notin\{0,1\}$ and $y_0=1-x_0$. The regular two-atom side is

$$
 O_0=D(Y;b)\,D(bX;h),\quad b^N=y_0,\quad h^N=x_0.
$$

The second factor is diagonal with every entry nonzero.
Write the first as $\sum_{n=0}^{d}c_nS^n$.
Its exact cyclic difference equation gives

$$
 (Q^n-b)c_n=\eta Q^{n-1}c_{n-1},                     \tag{11}
$$

with indices cyclic. Since $\eta\ne0$ and
$b^N=1-x_0\ne1$, every coefficient is nonzero: one zero would
propagate around the entire cycle and make the invertible
matrix zero. Therefore

$$
 \boxed{\quad (O_0)_{dd}=c_0\,D(bX;h)_{dd}\ne0.\quad} \tag{12}
$$

Formula (3) says that the actual paired cap retains this local
wall. It is not killed by operator regularity, by a norm-root
zero, or by deck averaging.

This does **not** identify this primitive cap placement with
the exterior of the specific oversized $5_2$ face. The actual
crossing's atom order and commutator orientation must be matched;
an equation between central sums alone does not establish that
embedding. No global excessive-face coefficient is computed here.
The result is the explicit original-cap local charge and the
finite uniformly bounded extraction map that an eventual
typed exterior comparison must preserve.
