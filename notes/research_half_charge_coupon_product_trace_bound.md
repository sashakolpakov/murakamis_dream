# Full traces of products of half-charge coupons

At level \(N\ge2\), fix finitely many original coupons
\[
 C_{\ell,N}(\zeta_1,\ldots,\zeta_{r_\ell})
 =\phi_N^{(x)}
 \left[R(x)^{n_\ell}e_{L_N}(x)
       \prod_{i=1}^{r_\ell}K_N(x,\zeta_i)\right],
 \qquad r_\ell\ge1,\quad n_\ell\in\mathbb Z,
 \tag{1}
\]
where \(L_N=N-1-\lfloor N/2\rfloor\). Their internal traced
variables are separate. All outside slots remain ordinary
polynomial variables until the identifications below.
The level, crossing, trace and Newton normalization are those
of [H] and [C]; in particular
\[
 P_N(z)=2T_N(z/2)+2,\quad
 \phi_N(f)=\eta N^2[z^{N-1}]\operatorname{rem}_{P_N}f,
 \quad \eta=(-1)^{N-1}.
 \tag{2}
\]

For \(r_\ell+|n_\ell|>1\), let \(M_\ell=M_{r_\ell,n_\ell}\)
be the complete half-charge action in [H, equation (5)].
For the exceptional pair \((r_\ell,n_\ell)=(1,0)\), put
\(M_\ell=0\). This assigns no saddle to that exception.

Let \(V\) be a fixed finite set and assign every outside slot
\((\ell,i)\) to a variable \(z_{\sigma(\ell,i)}\), where
\(\sigma(\ell,i)\in V\). Repetitions within one coupon and
between coupons are allowed. Count occurrences, not distinct
coupons:
\[
 q_v=\#\{(\ell,i):\sigma(\ell,i)=v\},\qquad
 T_N(\mathbf z)=
 \prod_\ell C_{\ell,N}
       (z_{\sigma(\ell,1)},\ldots,z_{\sigma(\ell,r_\ell)}).
 \tag{3}
\]
Vertices with \(q_v=0\) are permitted.

The distinct physical nodes are
\[
 c_a=2\cos((2a+1)\pi/N),\quad
 0\le a\le\lfloor(N-1)/2\rfloor,\quad
 \tau_a=\arccos(-c_a/2),\quad g_a=1-\cos\tau_a.
 \tag{4}
\]
Their multiplicity \(\mu_a\) in \(P_N\) is two, except for
the simple node \(c_{\lfloor N/2\rfloor}=-2\) at odd levels.
At that simple node \(\tau_a=g_a=0\). A physical full jet
uses derivative orders \(0\le\beta_v<\mu_{a_v}\).

## 1. The product estimate with repeated slots

There are constants \(c,C>0\) and \(A\), depending only on
the fixed coupons and slot assignment, such that for all
sufficiently large \(N\) and every
\(\alpha\in\{0,1\}^{V}\), at every physical node assignment,
\[
 \boxed{\quad
 |\partial^\alpha T_N(c_{\mathbf a})|
 \le CN^A
  \exp\left\{N\sum_\ell M_\ell
       -cN\sum_{v\in V}(q_v-\alpha_v)_+g_{a_v}\right\}.
 \quad}
 \tag{5}
\]
Here \(x_+=\max\{x,0\}\). The assertion concerns ordinary
derivatives of the polynomial (3). A subsequent original
trace uses only the orders required by the node multiplicities.

For each nonexceptional coupon, [H, equation (10a)] gives
\[
 |\partial^{\nu}C_{\ell,N}(c_{b_1},\ldots,c_{b_{r_\ell}})|
 \le C_\nu N^{A_\nu}
 \exp\left\{NM_\ell
       -c_\ell N\sum_{i:\nu_i=0}g_{b_i}\right\}.
 \tag{6}
\]
Only finitely many slot derivative patterns are needed here.

The exception satisfies the same bound with \(M_\ell=0\)
and any fixed \(c_\ell>0\). Indeed [H, equation (11)] is the
exact identity \(C_{1,0,N}=e_m\), \(m=\lfloor N/2\rfloor\).
This polynomial vanishes at every double physical node.
Its only remaining physical value, at the odd simple node
\(-2\), is one and has \(g_a=0\). Its fixed ordinary
derivatives on the physical interval have polynomial bounds
by [H, Section 6]. Thus the unhit-slot assertion in (6)
is exact zero away from the odd simple node; differentiated
slots have only the stated polynomial bound.

Choose one positive \(c\le c_\ell\) for all coupons.
The chain and product rules give a finite sum for
\(\partial^\alpha T_N\): for each \(v\) with \(\alpha_v=1\),
choose one of its \(q_v\) slot occurrences to differentiate.
Each choice contributes the product of the corresponding
slot derivatives of the separate coupons, evaluated after
identification. If \(q_v=0\) and \(\alpha_v=1\), the derivative
is zero.

In every nonzero term exactly \(\alpha_v\) of the \(q_v\)
occurrences are hit. Applying (6) leaves
\(q_v-\alpha_v\) unhit losses at \(v\). The number of
choices is bounded by the fixed product of the nonzero
incidences. Summing them proves (5). In particular,
differentiating a repeated variable does not remove the
loss from all of its occurrences at once.

## 2. A weighted norm of the ordinary exterior

Let \(E_N(\mathbf z;\boldsymbol\xi)\) be any joint ordinary
polynomial in the selected variables \(\mathbf z\).
It can have arbitrary \(N\)-dependent coefficients and degree.
The remaining ordinary variables \(\boldsymbol\xi\), if present,
are held free. Define, pointwise in those free variables,
\[
 \begin{split}
 \|E_N\|_{N,c,\mathbf q}
 =\max_{\substack{\mathbf a\\0\le\beta_v<\mu_{a_v}}}
 \bigg[
 |\partial^\beta E_N(c_{\mathbf a};\boldsymbol\xi)|\,
 \exp\left\{-cN\sum_{v\in V}
                   (q_v-1+\beta_v)_+g_{a_v}\right\}
 \bigg].
 \end{split}
 \tag{7}
\]
It is a norm of the selected physical full-jet class, not
of the unreduced exterior polynomial away from those nodes.
At an odd simple node the maximum includes only \(\beta_v=0\).
There is no added first normal there.

Fix signed integers \(p_v\), independently of \(N\), and keep
their original full-Hermite crossing powers. Then
\[
 \boxed{\quad
 \left|
 \phi_N^{\otimes V}
 \left[E_N(\mathbf z;\boldsymbol\xi)
       \prod_{v\in V}R(z_v)^{p_v}\,T_N(\mathbf z)\right]
 \right|
 \le C N^{A'}
       \exp\left\{N\sum_\ell M_\ell\right\}
       \|E_N\|_{N,c,\mathbf q}.
 \quad}
 \tag{8}
\]
The constants depend on the fixed coupons, incidences and
crossing powers, and not on the exterior \(E_N\). Thus (8)
also applies uniformly to a family of free parameters whenever
the displayed exterior norm is uniformly bounded there.

## 3. The original trace and its Leibniz terms

The literal trace (2) has the physical residue expression
\[
 \phi_N(f)=
 \eta\sum_{\mu_a=2}
       \{(4-c_a^2)f'(c_a)-c_af(c_a)\}
       +\mathbf1_{N\ {\rm odd}}f(-2).
 \tag{9}
\]
For completeness, the coefficient of \(z^{-1}\) in \(f/P_N\)
is the top coefficient in (2), so \(\phi_N\) is \(\eta N^2\)
times the sum of its finite residues. At a double root the
Chebyshev differential equation gives
\[
 P_N''(c_a)=\frac{2N^2}{4-c_a^2},\qquad
 \frac{P_N'''(c_a)}{P_N''(c_a)}
                      =\frac{3c_a}{4-c_a^2}.
 \]
These give the two terms in braces. At the odd simple node
\(P_N'(-2)=N^2\) and \(\eta=1\), giving exactly its value
term. All coefficients in (9) have modulus at most four.

The original signed crossing data in [C, equations (5),(21)]
satisfy, at every double node,
\[
 |R(c_a)^{p_v}|=1,\qquad
 \frac{(R^{p_v})'(c_a)}{R(c_a)^{p_v}}
 =\frac{i p_v(N-1-2a)}
        {4\sin((2a+1)\pi/N)} .
 \tag{10}
\]
Thus the values and trace-required derivatives have
polynomial bounds, uniformly in the physical node:
\(|(R^{p_v})'(c_a)|\le C_{p_v}N^2\).
Negative powers obey the same formula. Only the unit-modulus
value is used at the odd simple node.

Expand the tensor trace (9). Its derivative orders satisfy
\(0\le\alpha_v<\mu_{a_v}\). In each Leibniz term write
\[
 \alpha=\beta+\gamma+\delta,
 \]
where the derivatives hit \(E_N\), the crossing product,
and \(T_N\), respectively. Componentwise,
\(\delta_v\le1-\beta_v\). Consequently
\[
 (q_v-\delta_v)_+\ge(q_v-1+\beta_v)_+ .
 \tag{11}
\]
Apply (5) with \(\delta\), (10) with \(\gamma\), and (7)
with \(\beta\). The exponential exterior weight in (7)
is paid by the unhit-slot loss in (5), precisely by (11).
Each term is bounded by a polynomial times
\(e^{N\sum M_\ell}\|E_N\|_{N,c,\mathbf q}\).

There are at most \(N^{|V|}\) node-and-jet rows in the
tensor of (9), and at most \(3^{|V|}\) Leibniz choices
per row. Their trace coefficients are bounded, and (10)
costs at most a further \(C N^{2|V|}\). Summing proves
(8); for example \(A'=A+3|V|\) is sufficient after
enlarging the fixed constant.

The exponent in (7) is stronger than the uniform
\((q_v-1)_+\) value weight: when the exterior takes the
first normal, that derivative cannot also hit a coupon
slot, and all \(q_v\) slot losses remain. Formula (9)
is used in full throughout; neither first normals nor
odd simple-node values are projected away.

## 4. Scope

The slot identifications and all exterior products in this
argument are ordinary polynomial operations. Only the final
selected variables are subjected to the original traces.
The estimate therefore applies to their actual joint
contraction, including repeated slots and arbitrary joint
exteriors, rather than only to factorized outside sources.
All free variables remain ordinary.

The norm (7) of the particular exterior is not estimated
here. Nor is the sum of local half-charge actions identified
with a parent filled volume. The product and full trace are
not assigned a Gaussian coefficient, a positive pairing or
a scalar lower bound. In particular the degenerate
\((1,0)\) coupon is included by its exact polynomial and
physical support, not by a limiting saddle assertion.

## Direct sources

- H: [The original multi-leg half-charge coupon](research_multileg_half_charge_source_bound.md),
  SHA256 df85063947dc52c876d1cb810208e4da725517b7556661e3ddb21a3de7f0f8d2.
  The full original coupon, its mixed physical-slot bound,
  and the exact exceptional polynomial with its derivative bounds.
- C: [Exact source compilation with arbitrary crossing powers](research_arbitrary_power_source_compilation.md),
  SHA256 55e2de84870cfd20dac5922791dbc2bed54909439dfbf4663f17c70a1089445f.
  The ordinary exterior convention, original tensor contractions,
  and signed full-Hermite crossing values and first normals.
