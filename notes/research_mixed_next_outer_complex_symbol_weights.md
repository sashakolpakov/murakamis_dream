# Fourier weights controlled by the Hermitian part of the full symbol

Private finite-source proof, 9 November 2026. A Fourier weight can be
tested against the real part of the complex-shifted principal symbol.
This avoids paying the absolute size of its skew-Hermitian change.
The elementary sufficient loss is quadratic in a small weight, through
\(\cosh(\ell\lambda)-1\), rather than linear. The reflection at the
zero Fourier mode is handled separately in the actual even space.

The conclusion is an inverse for a fixed low-frequency compression of
the original grouped operator. Its exact residual retains the original
input tail and all eleven boundary output modes. The resulting action
comparison has not been established. No numerical evaluation or change
to a frozen source is used.

## 1. Original operator and a proposed weight

Use the exact operator \(\mathcal C_N\), the full leading-shift
operator \(\mathcal P_N\), and the principal symbol of the
[full-shift inverse theorem](research_mixed_next_outer_full_shift_low_frequency_inverse.md).
Thus, with \(z(u)=-2\cos u\),
\[
\mathcal C_Ng=e_M^{-1}\mathcal B_N(e_MQ_{3,N}^{\rm rev}g),
\qquad Q_{3,N}^{\rm rev}(z)=\prod_{j=0}^{2}(z-c_{U-j}),
\]
where \(\mathcal B_N\) is the original ordered conjugated adjoint.
No factor order, endpoint zero, or Hermite normal is changed.
The full leading-shift operator has Fourier matrix
\[
(\mathcal P_N)_{n,k}=p_{n-k}(k/N),\qquad
p(u,t)=\sum_{\ell=-11}^{11}p_\ell(t)e^{i\ell u}.
\tag{1}
\]
Its explicit symbol is
\[
p(u,t)=(2-2\cos u)^3d(u,-e^{3iu+2\pi it}),
\tag{2}
\]
with \(d\) as in equations (4)--(5) of that source. All the
\(p_\ell\) are smooth functions of the real frequency parameter.
For real \(u,t\),
\[
p(u,t)\in\mathbb R,\qquad
p_{-\ell}(t)=\overline{p_\ell(t)},\qquad
p(-u,-t)=p(u,t).
\tag{3}
\]
For every fixed \(0<\alpha<1/2\),
\[
\mu_\alpha=\min_{u\in\mathbb R,\ |t|\le\alpha}p(u,t)>0.
\tag{4}
\]
In particular the actual endpoint values are
\(p(0,t)=4096\cos^6(\pi t)\) and \(p(\pi,t)=256\).

Fix such an \(\alpha\). Let \(\lambda:[0,\alpha]\to(0,\infty)\)
be Lipschitz, fixed independently of \(N\). Suppose it is constant,
equal to \(\eta>0\), on some fixed interval \([0,\beta]\), where
\(0<\beta<\alpha\). Put
\[
W(t)=\int_0^t\lambda(s)\,ds,\qquad
K_N=\lfloor\alpha N\rfloor,\qquad
(E_{W,N}f)_k=e^{NW(|k|/N)}f_k.
\tag{5}
\]
The matrix in (5) acts on \(|k|\le K_N\). When a bounded number
of further output modes are used below, extend \(\lambda\) constantly
past \(\alpha\). This extension does not change any test on the
compressed interval.

We impose two concrete conditions. The first controls the reflection
at zero frequency. Write \(\mu_0=\min_u p(u,0)>0\), and require
\[
\sum_{\ell=-11}^{11}|p_\ell(0)|
       \{\cosh(\ell\eta)-1\}<\frac{\mu_0}{4}.
\tag{6}
\]
The second uses the complete complex-shifted symbol:
\[
\Re p(u-i\lambda(t),t)\ge c>0
\qquad(u\in\mathbb R,\ 0\le t\le\alpha).
\tag{7}
\]
Both are finite-symbol conditions. They are satisfied by a sufficiently
small fixed constant weight, by (4) and continuity. The theorem does
not presume a larger weight satisfies them.

For clarity, (7) has the exact expression
\[
\Re p(u-i\lambda,t)
 =\sum_{\ell=-11}^{11}p_\ell(t)\cosh(\ell\lambda)e^{i\ell u}.
\tag{8}
\]
Indeed complex conjugation of the shifted Fourier series, followed
by \(\ell\mapsto-\ell\), replaces \(e^{\ell\lambda}\) by
\(e^{-\ell\lambda}\). Thus a sufficient pointwise condition for
(7) is
\[
\sum_\ell |p_\ell(t)|\{\cosh(\ell\lambda(t))-1\}
       \le (1-\varepsilon)\min_u p(u,t),
\quad 0\le t\le\alpha,
\tag{9}
\]
for a fixed \(\varepsilon>0\). This implies (7) with
\(c=\varepsilon\mu_\alpha\). The sum in (9) is \(O(\lambda^2)\)
uniformly on the compact frequency interval as \(\lambda\to0\).
Condition (7) can also be used directly without the triangle bound
(9).

## 2. Coercivity of the weighted leading compression

Let \(\Pi_N\) project onto \(|k|\le K_N\), and put
\[
P_{I,N}=\Pi_N\mathcal P_N\Pi_N,
\qquad B_{I,N}=E_{W,N}P_{I,N}E_{W,N}^{-1}.
\tag{10}
\]
There is a fixed \(\gamma>0\) such that, for all sufficiently large
\(N\),
\[
\Re\langle f,B_{I,N}f\rangle\ge\gamma\|f\|_2^2.
\tag{11}
\]
This holds on the full compressed Fourier space, and hence on its
even subspace.

Here is a finite proof, including the reflection. Use the windows
\(\chi_j(k)=L^{-1/2}{\bf1}_{j\le k<j+L}\), with
\(L=\lfloor\sqrt N\rfloor\), and extend vectors by zero outside
the compressed interval. Their overlap is exactly
\(1-|n-k|/L\) for \(|n-k|\le11\). Every nonzero entry of
\(B_{I,N}\) has \(|n-k|\le11\), and its modulus is bounded by
a fixed constant: the weight ratio is at most
\(e^{11\max\lambda}\). Consequently replacing its quadratic
form by the sum of the windowed forms costs \(O(L^{-1})\|f\|_2^2\).

First consider a window whose nonzero indices have one sign. Choose
one of those indices \(k_j\), and write \(t_j=k_j/N\). For any
two indices in that window, the Lipschitz property gives
\[
N\{W(|n|/N)-W(|k|/N)\}
 =(n-k)\operatorname{sgn}(t_j)\lambda(|t_j|)+O(L/N),
\tag{12}
\]
where the error is uniform on the nonzero matrix diagonals.
The coefficients \(p_{n-k}(k/N)\) also differ from their values
at \(t_j\) by \(O(L/N)\). The frozen convolution therefore has
symbol
\[
p(u-i\operatorname{sgn}(t_j)\lambda(|t_j|),t_j).
\tag{13}
\]
Its real part is at least \(c\). For negative \(t_j\), this
follows from (3) and (7) by replacing \(u\) by \(-u\). Fourier
orthogonality proves a real quadratic-form lower bound \(c\) for
this frozen convolution. The error on the window is \(O(L/N)\).
If zero is one endpoint of such a window, use the sign of its
nonzero indices; if its supported vector has only the zero index,
choose the positive sign. The linear formula for \(W\) near zero
makes the same quadratic-form comparison valid.

It remains to consider a window containing indices of both signs.
All its indices have \(|k|\le L\), so for large \(N\) the
weight there is exactly \(e^{\eta|k|}\). Freeze the coefficients
at \(t=0\). The unweighted frozen convolution \(P^0\) is
Hermitian, with entries \(p_{n-k}(0)\), and is bounded below by
\(\mu_0 I\). The Hermitian part of its weighted matrix has entries
\[
p_{n-k}(0)\cosh\{\eta(|n|-|k|)\}.
\tag{14}
\]
The difference from \(P^0\) has row and column sums bounded by
the left side of (6), since
\(\big||n|-|k|\big|\le|n-k|\). Its real quadratic form is
therefore bounded below by \(3\mu_0/4\). The coefficient freezing
error is again \(O(L/N)\), including the bounded weight ratios.

Summing the windowed bounds proves
\[
\Re\langle f,B_{I,N}f\rangle
 \ge\left[\min\{c,3\mu_0/4\}
              -C\{L/N+L^{-1}\}\right]\|f\|_2^2.
\tag{15}
\]
One may take \(\gamma=\tfrac12\min\{c,3\mu_0/4\}\) after
increasing the level threshold. This proof retains the non-Hermitian
finite coefficient variation; it does not assume exact symmetry of
\(P_{I,N}\).

## 3. The original operator is a small perturbation in this weight

The difference \(\mathcal R_N=\mathcal C_N-\mathcal P_N\) is
defined on even polynomials. Its full-shift source proves two facts:

1. For each fixed \(\rho>0\), its norm on the same even Hardy
   strip of height \(\rho\) is \(O(N^{-1})\).
2. On an even polynomial of degree \(k\), its output has degree
   at most \(k+11\).

These facts control the new variable weight without assuming an
unproved bound in a variable-width analytic domain. Use the orthonormal
cosine basis \(e_0=1\), \(e_k=\sqrt2\cos(ku)\) for \(k>0\),
and write \(R_{n,k}\) for the matrix of \(\mathcal R_N\) in this
basis. The same-strip Hardy estimate and its Fourier coefficient bound
give, for any fixed \(\rho>0\),
\[
|R_{n,k}|\le \frac{C_\rho}{N}e^{\rho(k-n)},
\qquad R_{n,k}=0\quad(n>k+11).
\tag{16}
\]
The harmless normalization factors of the cosine basis are absorbed
in \(C_\rho\).

Let \(\lambda_-=\min\lambda>0\), and choose
\(\rho=\lambda_-/2\). When \(n\le k\),
\[
N\{W(n/N)-W(k/N)\}\le-\lambda_-(k-n).
\]
Thus the weighted entry in (16) is at most
\(C_\rho N^{-1}e^{-\lambda_-(k-n)/2}\).
When \(k<n\le k+11\), its weighted modulus is at most
\(C_\rho N^{-1}e^{11\max\lambda}\).
Both row and column sums are \(O(N^{-1})\). Schur's bound proves
\[
\|E_{W,N}\Pi_N\mathcal R_N\Pi_NE_{W,N}^{-1}\|=O(N^{-1})
\tag{17}
\]
on the even subspace. The same argument controls all output rows
through \(K_N+11\), with the constant extension of the weight.
There are no other output rows for a compressed input.

The leading operator, the original operator, the projection, and the
weight all preserve the even subspace. Combining (11) and (17) gives
\[
\Re\langle f,E_{W,N}A_{I,N}^{\rm ev}E_{W,N}^{-1}f\rangle
 \ge\frac\gamma2\|f\|_2^2,
\qquad
\|(A_{I,N}^{\rm ev})^{-1}\|_{W\to W}\le\frac2\gamma,
\tag{18}
\]
where \(A_{I,N}^{\rm ev}=\Pi_N\mathcal C_N\) on even
polynomials of degree at most \(K_N\). This is a finite square
inverse. It makes no assertion about the full constrained operator.

## 4. The action profile in the exact boundary residual

Use the complete attached polynomial \(F_N^+(z,Z)\) from the
[action-weighted Green theorem](research_mixed_next_outgoing_action_weighted_green_ellipse.md).
Its original output parameter \(Z\) is restricted to the actual
region of that theorem. Write \(E_Z(t)=\mathcal E(1/2+t,Z)\)
for \(0\le t\le1/2\). That theorem proves that \(E_Z\) is
decreasing and that the cosine coefficients of the attached polynomial
satisfy
\[
|F_{k,N}^+(Z)|\le CN^A e^{NE_Z(k/N)},\qquad 0\le k\le U.
\tag{19}
\]
The exponent is the original anchored action; the last coefficient
is included.

Solve the unique compressed system
\[
g_N=(A_{I,N}^{\rm ev})^{-1}\Pi_NF_N^+,
\qquad r_N=F_N^+-\mathcal C_Ng_N.
\tag{20}
\]
Put
\[
A_W(\alpha,Z)=\max_{0\le t\le\alpha}\{E_Z(t)+W(t)\},
\qquad G_W(\alpha,Z)=A_W(\alpha,Z)-W(\alpha).
\tag{21}
\]
Equations (18)--(19) bound the weighted norm of \(g_N\) by
\(CN^A e^{NA_W}\). The leading matrix has only finitely many
diagonals, and (16)--(17) bound the full original output through
degree \(K_N+11\) in the same extended weight. Hence its boundary
coefficients, with \(K_N<k\le K_N+11\), are bounded by
\(CN^A e^{N(A_W-W(\alpha))}\). The fixed eleven-mode displacement
and the floor in \(K_N\) change only a bounded multiplier.

The low coefficients of \(r_N\) vanish exactly. Above
\(K_N+11\), its coefficients are those of \(F_N^+\), whose
rate is at most \(E_Z(\alpha)+O(N^{-1})\) by monotonicity and
local smoothness. This rate is at most \(G_W\), since the term
\(t=\alpha\) is included in (21). The same bound controls the
input coefficients in the eleven boundary modes, so both terms of
their residual are included. Summing the remaining polynomially many
coefficients gives
\[
\|r_N\|_{\mathbb R}\le CN^A e^{NG_W(\alpha,Z)}.
\tag{22}
\]
The eleven boundary coefficients in this argument are the actual
output coefficients of the solved system. They have not been replaced
by the tail coefficients of its input.

The original even-level forcing can be bounded without paying the
larger weighted input norm. Choose a second, sufficiently small fixed
constant weight \(\rho_0\le1/8\) satisfying the full-shift source's
constant-weight inverse condition. The same compressed system (20)
has only one solution. Its bound in this second weight, together with
the outgoing ellipse theorem, therefore gives
\[
\|g_N\|_{\rho_0,\mathrm F}\le CN^A e^{NE_Z(0)}.
\tag{23}
\]
This is a bound on that same polynomial, not a replacement test.

Let \(h_N=Q_{3,N}^{\rm rev}g_N\). The exact full Hermite identity
is unchanged:
\[
\mathcal L_N(F_N^+)=\mathfrak f_N\ell_N(h_N)+\mathcal L_N(r_N),
\quad
\mathfrak f_N=\begin{cases}4\kappa_N^3/N^2,&N\text{ even},\\
0,&N\text{ odd}.
\end{cases}
\tag{24}
\]
Here \(\mathcal L_N(F)=\phi_N[R_N^3e_MQ_N^{\rm full}F]\)
and \(\ell_N(h)=\phi_N[R_N^3e_Mh]\). The original complete
inner-source bound and (22)--(23) imply, for every fixed \(\tau>0\),
\[
|\mathcal L_N(F_N^+)|\le C_\tau N^{A_\tau}
 \left\{e^{NE_Z(0)}+
        e^{N(\mathfrak M_3+G_W(\alpha,Z)+\tau)}\right\}.
\tag{25}
\]
The first term vanishes at odd levels; its additional polynomial
factor \(N^{-1}\) can be retained. Every original normal and endpoint
condition remains in (24).

## 5. What would close the comparison

For the actual references, an admissible weight satisfying (6)--(7)
would close the remaining correction if it also gave uniform strict
inequalities
\[
E_{Z_*}(0)<\Lambda,
\qquad \mathfrak M_3+G_W(\alpha,Z_*)<\Lambda.
\tag{26}
\]
The original transfer scalar, geometric term, and previously bounded
errors are precisely those in the action-weighted Green theorem.
The theorem here does not certify (26). In particular the term
\(t=0\) in (21) imposes the necessary requirement, for this bound,
\[
W(\alpha)>\mathfrak M_3+E_{Z_*}(0)-\Lambda.
\tag{27}
\]
The vanishing endpoint rate \(E_Z(1/2)=0\) does not by itself
establish this accumulated-weight inequality. At \(\alpha=1/2\)
the central principal value degenerates; no inverse at that endpoint
is asserted.

The improvement proved here is the complex-symbol test (7), its
quadratic sufficient loss (9), and the exact action-profile attachment
(25). The required quantitative comparison and the extension to
arbitrary short partial fillings remain open.

## Frozen source bindings

- Full leading-shift compression and same-strip finite comparison:
  7b11e96c482d3c435e3fac0d9a488d0025aae31e2ec9d806949858031381b84c.
- Exact grouped operator and full Hermite pairing:
  cb47c9d87949e276615443150b2da2260fec5bb09d3780039b90b322cd14eeb8.
- Ordinary divisibility and exact degree increase:
  c5cb10096ed4c6aafefdc957958ddaf392ad17c81cab5e7e99dbbe026fc1aed3.
- Complete outgoing coefficient profile and original attachment:
  e39abb76185b6969901b6ee4c95a4f947bdda5f74d8ff57062ed4b6591a0c029.
