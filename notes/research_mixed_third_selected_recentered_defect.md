# Recentered enclosure of the third-selection difference of actions

Research deduction, 6 November 2026. This note gives a centered
mean-value enclosure of the original trial defect. It retains the
cancellations between the reference action and its two affine boundary
terms, even away from a stationary reference. It does not evaluate a
new cell or establish a new negative comparison. The existing provider,
evaluator, failed boundary attempt and saved audit remain unchanged.

The background is the [center comparison and signed compensation](research_mixed_third_selected_center_comparison.md)
and its [four-leg implementation proof](research_mixed_third_selected_implementation.md).
The earlier [centered reference evaluation](research_mixed_second_selected_centered_reference_evaluation.md)
centers rational root-image transport. Here the ordinary mean-value
principle is applied instead to the difference of actions, after a
reference box has already been certified. No root transport, inverse
certificate or reference derivative is required.

## 1. The original defect on a full reference box

Use the coordinate order \(r=(a,u,z,v,b)\), and put

\[
\begin{split}
 F(r)={}&g(a+u)+g(u+z)+g(z+v)+g(v+b)
       -3g(u)-(2+\beta)g(v)\\
 &-(1+\alpha/2)g(a)-3g(z)-(1+\beta/2)g(b)
       +2\pi i(au+zv).
\end{split}
\tag{1}
\]

All primitives and logarithms have their original branches. Let
\(B=\{a,b\}\), \(p_L=F_a\), and \(p_R=F_b\). Fix one original
profile label and one exact real trial \(x\) in that label's full target
box. Set

\[
 \Lambda=\operatorname{diag}(1,\lambda_u,0,\lambda_v,1),\quad
 h=(0,0,H,0,0),\quad H=1/100,\qquad
 w(r)=x+i\Lambda\Im r+ih.
\tag{2}
\]

Here an index has \(\lambda=1\) on its main contour and zero at
its original real cut. At a cut the corresponding entry of \(x\) is
fixed to that cut. Write \(\Phi\) for \(F\) with these constant
coordinate substitutions, plus
\((1-\nu)g(w_z)+2\pi i\nu w_z\). Its formal inactive rows vanish.
For arbitrary \(r\), not just a stationary reference, define

\[
 D_x(r)=\Re\left\{\Phi(w(r))-F(r)
             -\sum_{k\in B}F_k(r)(w_k(r)-r_k)\right\}.
\tag{3}
\]

The subscript denotes the fixed target trial. In particular the
boundary displacements
\(\Delta_a=w_a-a=x_a-\Re a\) and
\(\Delta_b=w_b-b=x_b-\Re b\) are real. The internal derivatives
\(F_u,F_z,F_v\) vanish at a true canonical reference but generally
do not vanish at the center of a Cartesian enclosure.

Let \(\mathcal R\) be a convex Cartesian reference rectangle. Assume
the original own and summed arguments in \(F(r)\) and \(\Phi(w(r))\)
remain in the open strip \(0<\Re t<1\) for every
\(r\in\mathcal R\). The certified coordinate boxes and original
target domains have this property. These checks concern the full box,
including its straight segments; membership of its center in the
canonical family is unnecessary.

## 2. Exact cancellation before taking interval bounds

Write \(r_j=X_j+iY_j\). Direct differentiation of (3) gives

\[
 \frac{\partial D_x}{\partial X_j}
 =\Re\left\{-\mathbf1_{j\notin B}F_j(r)
       -\sum_{k\in B}F_{kj}(r)\Delta_k\right\},
\tag{4}
\]
\[
 \frac{\partial D_x}{\partial Y_j}
 =-\Im\left\{\lambda_j\Phi_j(w(r))-F_j(r)
       -\sum_{k\in B}F_{kj}(r)\Delta_k\right\}.
\tag{5}
\]

Indeed \(w\) is independent of \(X_j\), while
\(\partial_{X_j}\Delta_k=-\mathbf1_{j=k}\). This cancels the
boundary derivative of \(-F\) in (4). For (5),
\(\partial_{Y_j}w_j=i\lambda_j\) and
\(\partial_{Y_j}F=iF_j\). Since both boundary coefficients are
one, \(\partial_{Y_j}\Delta_k=0\) for \(k\in B\). These facts
prove both identities on all of \(\mathcal R\), without using
stationarity at any intermediate point.

Put \(k(t)=g''(t)=\pi\cot(\pi t)-i\pi\). The only nonzero
entries in the two boundary Hessian rows are

\[
\begin{array}{ll}
 A=F_{aa}=k(a+u)-(1+\alpha/2)k(a),&
 L=F_{au}=k(a+u)+2\pi i,\\
 R=F_{bv}=k(v+b),&
 C=F_{bb}=k(v+b)-(1+\beta/2)k(b).
\end{array}
\tag{6}
\]

Consequently (4) is the real part of

\[
 (-A\Delta_a,\ -F_u-L\Delta_a,\ -F_z,
                    -F_v-R\Delta_b,\ -C\Delta_b),
\tag{7}
\]

and (5) is minus the imaginary part of

\[
\begin{split}
 (&\Phi_a-F_a-A\Delta_a,
 \lambda_u\Phi_u-F_u-L\Delta_a,
 -F_z,\\
 &\lambda_v\Phi_v-F_v-R\Delta_b,
 \Phi_b-F_b-C\Delta_b).
\end{split}
\tag{8}
\]

In particular, both derivatives in the selected reference coordinate
are just components of \(-F_z\) or \(F_z\); no separately large
selected-coordinate primitive remains. For the same trial and index
labels, (4)--(8) are independent of the Fourier flag: the two Fourier
terms depend only on the fixed target \(x_z+iH\). This does not
identify the two defect values.

## 3. The centered enclosure and the full target bound

Let \(r^0\) be the exact Cartesian midpoint of \(\mathcal R\),
and let \(\rho_j^X,\rho_j^Y\) be its exact real and imaginary
halfwidths. Suppose interval evaluation of (4)--(5) on the full box
gives real intervals \(I_j^X,I_j^Y\). The fundamental theorem of
calculus along \(r^0+t(r-r^0)\) proves

\[
 D_x(\mathcal R)\subseteq D_x(r^0)
       +\sum_j I_j^X[-\rho_j^X,\rho_j^X]
       +\sum_j I_j^Y[-\rho_j^Y,\rho_j^Y].
\tag{9}
\]

All terms are outward enclosures; \(D_x(r^0)\) is evaluated from
the literal (3), including its nonzero off-stationary marginals.
Equivalently, an upper bound is

\[
 U_D=D_x(r^0)^+
       +\sum_j\rho_j^X\sup|I_j^X|
       +\sum_j\rho_j^Y\sup|I_j^Y|.
\tag{10}
\]

One may intersect (9) with the old direct interval for the same
defect. No logarithm, primitive or coordinate may be recentered
independently in a way that changes (3).

For the original target box \(\prod_j[l_j,r_j]\), retain an
outward enclosure \(G_j=[G_j^-,G_j^+]\) of the real target
derivative of (3) at \(x\), uniformly over \(\mathcal R\).
The existing labeled horizontal concavity then gives

\[
 \max_{\text{original targets}}D
 \le U_D+\sum_j\max\{G_j^-(l_j-x_j),\ G_j^+(r_j-x_j)\}.
\tag{11}
\]

Here \(x_j\in[l_j,r_j]\), so the lower gradient endpoint is
paired with the nonpositive displacement. A fixed cut contributes
zero. The old exact trial and old saved gradient support enclosures
may be retained unchanged; only the trial-defect enclosure is replaced.
With the same current reference and certified anchor, the sufficient
compensated bound remains exactly

\[
 U_D+\text{support correction}-C_0^-.
\tag{12}
\]

The midpoint \(r^0\) is not a substitute anchor and is not asserted
to solve a critical equation. The lower endpoint \(C_0^-\) cannot
be discarded or replaced by zero.

## 4. Elementary bounds for the derivative enclosure

Equations (7)--(8) need only original logarithms and cotangents on
the full reference and target boxes. In particular, they avoid
interval subtraction of several dilogarithm values over a wide box.
All needed derivative bounds also have explicit elementary versions.

For every argument whose real part remains in
\([\eta,1-\eta]\), \(0<\eta\le1/2\),

\[
 |k(t)|\le\pi\left(1+\frac1{2\eta}\right),\qquad
 |g'''(t)|\le\frac{\pi^2}{4\eta^2}.
\tag{13}
\]

Indeed \(|\sin\pi t|^2=\sin^2(\pi\Re t)+\sinh^2(\pi\Im t)\),
\(\sin\pi\eta\ge2\eta\), and
\(|\cot\pi t|\le\max\{1,|\cot(\pi\Re t)|\}\).
These bounds do not require an imaginary-height estimate. A common,
deliberately coarse choice for every own and pair argument on the
reference-to-target segments is \(\eta=1/20\): the largest real
pair sum is \(.5+.45=.95\), and all lower endpoints exceed
\(.05\). Thus \(|k|\le11\pi\) and
\(|g'''|\le100\pi^2\) suffice universally. Individual argument
strips give much smaller constants by the same proof.

The internal residuals in (7)--(8) can be enclosed without assigning
them the value zero. If \(H_{jk}\ge\sup_{\mathcal R}|F_{jk}|\)
and \(s_k\ge\sup_{\mathcal R}|r_k-r_k^0|\), then

\[
 |F_j(r)|\le N_j:=|F_j(r^0)|+\sum_kH_{jk}s_k,
                   \qquad j=u,z,v.
\tag{14}
\]

The midpoint residual is an original logarithmic value. This is a
first-order bound on the full box, whether or not the midpoint is
close to a canonical point.

There is a second useful cancellation for the imaginary derivatives.
Put \(\Delta_j=w_j-r_j\), and choose
\(t_j\ge\sup_{\mathcal R}|\Delta_j|\). For each own or pair
argument \(q\), choose \(M_q\ge\sup|g'''|\) on its entire
reference-to-target segment. Taylor's integral remainder gives

\[
 |g'(q+d)-g'(q)-k(q)d|\le M_q|d|^2/2.
\tag{15}
\]

Let \(c_a=1+\alpha/2\), \(c_b=1+\beta/2\),
\(U=k(a+u)+k(u+z)-3k(u)\), and
\(V=k(z+v)+k(v+b)-(2+\beta)k(v)\).
Absolute values of these coefficients below mean upper bounds on
the full reference box. The four bounds

\[
\begin{split}
 T_a={}&|L|t_u+\tfrac12M_{a+u}(t_a+t_u)^2
                         +\tfrac12c_aM_a t_a^2,\\
 T_u={}&|U|t_u+|k(u+z)|t_z
      +\tfrac12M_{a+u}(t_a+t_u)^2
      +\tfrac12M_{u+z}(t_u+t_z)^2+\tfrac32M_u t_u^2,\\
 T_v={}&|k(z+v)+2\pi i|t_z+|V|t_v
      +\tfrac12M_{z+v}(t_z+t_v)^2
      +\tfrac12M_{v+b}(t_v+t_b)^2
      +\tfrac12(2+\beta)M_v t_v^2,\\
 T_b={}&|R|t_v+\tfrac12M_{v+b}(t_v+t_b)^2
                         +\tfrac12c_bM_b t_b^2
\end{split}
\tag{16}
\]

bound respectively the four nonselected brackets in (8) when their
index is active. For \(a,b\) this applies to every label, with the
actual cut displacement in \(t_u,t_v\). To check (16), expand each
original \(g'\) at its reference argument using (15). The linear
boundary terms \(A\Delta_a,L\Delta_a,R\Delta_b,C\Delta_b\)
cancel exactly. The two chirps leave \(2\pi i\Delta_u\) in the
\(a\) row and \(2\pi i\Delta_z\) in the \(v\) row, already
included in \(L\) and \(k(z+v)+2\pi i\). There is no chirp
remainder. No Fourier term enters these four rows.

A fully explicit choice of absolute derivative bounds in (10) is
therefore

\[
\begin{array}{c|c|c}
 j&\sup|\partial_{X_j}D_x|&\sup|\partial_{Y_j}D_x|\\ \hline
 a&|A|t_a&T_a\\
 u&N_u+|L|t_a&\lambda_uT_u+(1-\lambda_u)(N_u+|L|t_a)\\
 z&N_z&N_z\\
 v&N_v+|R|t_b&\lambda_vT_v+(1-\lambda_v)(N_v+|R|t_b)\\
 b&|C|t_b&T_b.
\end{array}
\tag{17}
\]

Taking the smaller of (17) and direct interval bounds from (7)--(8)
is valid. Each is an independent bound for the same derivative.
The local constants, actual trial displacements and midpoint residuals
should be kept together; replacing them all by the universal strip
constants can lose the useful gain.

## 5. What this proves about the next bounded test

The cancellation and enclosure (9)--(17) are uniform on each certified
full reference rectangle and apply to every existing label. They
justify a saved-reference-only diagnostic using the stored exact
trials, the same support corrections and the same \(C_0\) interval.
It needs no new source input, optimizer, reference proposal or
subdivision. The center is only an evaluation point for (3).

Universal elementary constants prove finiteness and convergence of
the enclosure error as all reference-coordinate widths tend to zero.
They do not prove that the present unresolved cell passes (12).
In particular, small external parameter widths alone do not bound
all five reference-coordinate halfwidths or the error in (10).
The decisive uncomputed quantities are the centered trial values and
the full-box derivatives, preferably the local versions of
(7)--(8) or (14)--(17). A positive resulting upper bound would remain
inconclusive, not a counterexample or a geometric exclusion.

No new inequality has been evaluated in this note, and no completed
product-boundary coverage or finite-source suppression is claimed.
