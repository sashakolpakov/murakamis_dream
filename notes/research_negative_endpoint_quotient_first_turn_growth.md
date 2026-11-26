# Exact first-turn growth of a coherent negative-endpoint quotient

Private written proof, 16 November 2026.

The subtraction in the dual-contour formula does not generally remove
the growing negative-endpoint channel. Already for one original
microscopic kernel, its actual ordinary quotient has first-turn rate
\(4G/\pi\). This is a statement about the coherent quotient, including
its original full normals, rather than about either dual coupon
separately. It rules out transferring the zero first-turn budget to
all auxiliary spatial quotients. It is not a counterexample to a
filled-source or volume assertion.

## 1. Source and uniform statement

Use the original conventions
\[
 N\ge2,\quad D=N-1,\quad \eta=(-1)^D,\quad q=e^{\pi i/N},
 \quad c_j=2\cos((2j+1)\pi/N),\quad c_0=q+q^{-1},
\]
\[
 P_N(C)=2T_N(C/2)+2,\quad
 S_j=\prod_{h=1}^j2\sin(h\pi/N),\quad
 e_j(C)=S_j^{-2}\prod_{h<j}(c_h-C),
\]
\[
 K_N(w,C)=\sum_{j=0}^{D}e_j(w)e_j(C),\qquad
 Te_j=e_{D-j},\qquad
 \phi_N(e_i e_j)=\mathbf1_{i+j=D},\qquad J=TCT.
 \tag{1}
\]
Here \(C\) on the right denotes multiplication in
\(\mathcal A_N=\mathbb C[C]/(P_N)\). Norms are ordinary norms of
canonical representatives on \([-2,2]\). Put
\[
 G=\int_0^{\pi/4}\log\cot t\,dt,\qquad M_\infty=4G/\pi.
 \tag{2}
\]

Fix finite \(A,B\ge0\). For real parameters
\[
 |\alpha|\le A,\qquad |\beta|\le B,\qquad
 w_N=2\cosh(\alpha/N),\qquad a_N=-2+\beta/N^2,
 \tag{3}
\]
form the specified ordinary polynomial
\[
 Q_N(C)=\frac{K_N(w_N,C)-K_N(w_N,a_N)}{C-a_N},
 \qquad Y_N=TQ_N.
 \tag{4}
\]
The diagonal in (4) is interpreted polynomially; no inverse of a
physical nonunit is taken. In particular \(\deg Q_N\le D-1\).

**Theorem.** Uniformly on the real parameter rectangle (3),
\[
 \boxed{\quad
 \frac1N\log\|Y_N\|_{[-2,2]}\longrightarrow M_\infty.
 \quad}                                                    \tag{5}
\]
The same assertion holds with the full-normal norm
\[
 \|Y_N\|_{\mathrm{jet},N}
   =\|Y_N\|_{[-2,2]}+N^{-2}\|Y_N'\|_{[-2,2]}.
 \tag{6}
\]
The input \(Q_N\) has polynomial real norm uniformly in (3).
Thus (5) is actual exponential growth under the first original
turn of this source. Uniformity means that both the upper bound
and the lower bound hold for every parameter in (3), not only
for a chosen sequence.

## 2. Exact coherent equation and its positive value recurrence

The original dual coupon is the ordinary polynomial
\[
 \delta_w(C)=TK_N(w,C)
       =\frac{P_N(C)-P_N(w)}{\eta N^2(C-w)}.
 \tag{7}
\]
Applying \(T\) to the ordinary identity defining (4) gives in the
full original algebra
\[
 \boxed{\quad
 (J-a_N)Y_N=\delta_{w_N}-K_N(w_N,a_N)e_D.
 \quad}                                                    \tag{8}
\]
The reset term in (8) remains part of the source. Also
\[
 Y_N(c_0)=\phi_N(Q_N)=0,                                    \tag{9}
\]
because \(Q_N\) has degree at most \(D-1\). This initialization
does not use a value-only replacement for the quotient.

Set \(J_N=\lfloor(N-1)/2\rfloor\). For the forward physical
rows below the last folded row, the original operator is
\[
 (Jf)(c_j)=(c_0+A_j+B_j)f(c_j)
                       -A_jf(c_{j+1})-B_jf(c_{j-1}),
 \tag{10}
\]
where
\[
 A_j=\frac{s_{j+1}^4}{s_{2j+1}s_{2j+2}},\qquad
 B_j=\frac{s_j^4}{s_{2j}s_{2j+1}},\qquad
 s_x=2\sin(\pi x/N),\qquad B_0=0.
 \tag{11}
\]
Here \(A_j>0\), \(B_j\ge0\) for \(0\le j<J_N\).
The polynomial \(e_D\) vanishes at every distinct physical
value, including the odd simple node. Since
\(P_N(w_N)=4\cosh^2(\alpha/2)>0\), define
\[
 Z_j=-\frac{\eta N^2}{P_N(w_N)}Y_N(c_j).
 \tag{12}
\]
Equations (7)--(11) give exactly
\[
 A_jZ_{j+1}=(c_0-a_N+A_j+B_j)Z_j-B_jZ_{j-1}
                                  +\frac1{w_N-c_j}.
 \tag{13}
\]
For all sufficiently large \(N\), uniformly in (3),
\(c_0-a_N>0\) and \(w_N>c_0\). At \(j=0\), (9) gives
\[
 Z_0=0,\qquad Z_1=\frac1{A_0(w_N-c_0)}>0.
 \tag{14}
\]
Both factors in the denominator of (14) are bounded above and
below by positive constants times \(N^{-2}\), uniformly in
\(\alpha\). Thus \(Z_1\asymp_{A}N^4\).

Write \(\Delta Z_j=Z_j-Z_{j-1}\). For \(j\ge1\),
\[
 \Delta Z_{j+1}=q_j\Delta Z_j+d_jZ_j+f_j,
 \quad q_j=B_j/A_j\ge0,\quad
 d_j=(c_0-a_N)/A_j>0,\quad
 f_j=\frac1{A_j(w_N-c_j)}>0.
 \tag{15}
\]
Consequently every \(Z_j\) and \(\Delta Z_j\), \(j\ge1\), is
positive, and \(Z_j\ge Z_1\). The coherent reset cannot cancel
this physical value channel.

Nothing in this argument removes its first-normal equation.
Equation (8) is an equality modulo \(P_N\); its ordinary residual
has zero values and first derivatives at every double physical
node. Differentiating that residual before evaluation retains
all coefficient derivatives and the term
\(-K_N(w_N,a_N)e_D'\). The latter must not be deleted merely
because \(e_D\) has zero physical values. At the odd simple node
only its value is part of the original algebra. The value lower
bound already implies the norm obstruction, while (8) retains
the full source needed for later multiplication or tracing.

## 3. The full lower rate from positive compact transfer

Fix \(0<\epsilon<1/4\), and consider
\(\epsilon\le u=j/N\le1/2-\epsilon\). Put
\(X_j=(Z_j,\Delta Z_j)^t\). Equation (15) is
\[
 X_{j+1}=M_{N,j}X_j+f_j(1,1)^t,\qquad
 M_{N,j}=\begin{pmatrix}1+d_j&q_j\\d_j&q_j\end{pmatrix}.
 \tag{16}
\]
Uniformly on this interval and the parameters (3),
\[
 M_{N,j}=M(u)+O_\epsilon(N^{-1}),\qquad
 M(u)=\begin{pmatrix}1+4\cot^2(\pi u)&1\\
                                  4\cot^2(\pi u)&1\end{pmatrix}.
 \tag{17}
\]
Indeed \(A_j,B_j\to\tan^2(\pi u)\) there. The positive
matrix \(M(u)\) has determinant one and Perron root
\[
 \rho(u)=\bigl(\csc(\pi u)+\cot(\pi u)\bigr)^2
                         =\cot^2(\pi u/2)>1.
 \tag{18}
\]
Choose its positive left Perron row \(\ell(u)\), normalized by
\(\ell(u)(1,1)^t=1\). It is smooth, and both its entries are
bounded away from zero on the compact interval. With \(h=1/N\),
(17) therefore gives the componentwise inequality
\[
 \ell(u+h)M_{N,j}\ \ge\
                  \{\rho(u)-C_\epsilon h\}\ell(u).
 \tag{19}
\]
This follows by writing the left side as
\(\rho(u)\ell(u)+O_\epsilon(h)\) componentwise and using the
positive lower bound for the entries of \(\ell\).

The forcing in (16) is positive. Starting at
\(j_-=\lceil\epsilon N\rceil\), its Perron coordinate is at
least a positive constant times \(Z_1\). Iterating (19) to
\(j_+=\lfloor(1/2-\epsilon)N\rfloor\), and using
\(0<\Delta Z_j\le Z_j\), yields
\[
 \log Z_{j_+}\ge
 N\int_\epsilon^{1/2-\epsilon}\log\rho(u)\,du
                                         -O_\epsilon(\log N).
 \tag{20}
\]
The bound is uniform in (3). The Riemann-sum error and the sum
of the logarithmic errors in (19) are bounded on this fixed
compact interval; the polynomial initial normalization and (12)
cost only \(O(\log N)\).

Thus
\[
 \liminf_{N\to\infty}\ \inf_{(\alpha,\beta)\text{ in }(3)}
 \frac1N\log\|Y_N\|_{[-2,2]}
 \ge\int_\epsilon^{1/2-\epsilon}2\log\cot(\pi u/2)\,du.
 \tag{21}
\]
Let \(\epsilon\downarrow0\). The logarithmic singularity at
zero is integrable, and substitution \(t=\pi u/2\) gives
\[
 \int_0^{1/2}2\log\cot(\pi u/2)\,du=4G/\pi.
 \tag{22}
\]
No last-row equation, endpoint inverse, or selected lower
coefficient from a formal characteristic was used.

## 4. A matching first-turn ceiling

The following elementary ceiling also explains why the rate
in (22) is sharp. Write
\[
 A_{j,N}=e_j(-2),\qquad
 \Sigma_N=K_N(-2,-2)=\sum_{j=0}^{D}A_{j,N}^2.
 \tag{23}
\]
For \(0\le j\le J_N\),
\[
 A_{j,N}=\prod_{h=0}^{j-1}
       \frac{\cos^2((h+1/2)\pi/N)}{\sin^2((h+1)\pi/N)},
\]
\[
 \log A_{j,N}
    =2N\int_0^{j/N}\log\cot(\pi x)\,dx+O(\log N),
 \tag{24}
\]
uniformly in \(j\). For completeness, \(\log\sin(\pi x)\)
is monotone on \((0,1/2]\), and \(\log\cos(\pi x)\) is
monotone on \([0,1/2)\). Upper and lower rectangle comparisons
for their right and midpoint sums telescope to endpoint errors.
The grid points nearest either singular endpoint have distance
at least \(1/(2N)\); integrating their logarithmic singularities
and bounding the remaining endpoint values costs \(O(\log N)\).
This proves the uniform statement, including the last allowed
low index. The integral in (24) has its maximum at \(j/N=1/4\),
where its value is \(G/\pi\).

For \(j>J_N\), the archived radical Fourier bound gives
\(\|e_j\|_{[-2,2]}\le\sqrt{N-1}\). Equation (24), and the
term \(j=\lfloor N/4\rfloor\) for the reverse bound, prove
\[
                  \log\Sigma_N=M_\infty N+O(\log N).
 \tag{25}
\]
This covers both parities; the low product has no zero factor.

Here is a uniform bound for the ordinary kernel on the whole
real square. Its physical row
\(F_{j,N}(z)=K_N(c_j,z)\), \(0\le j\le J_N\), has roots
strictly greater than two and normalization \(F_{j,N}(c_0)=1\).
Consequently
\[
 \sup_{z\in[-2,2]}|F_{j,N}(z)|\le F_{j,N}(-2).
\]
Its terminating Newton expression has nonnegative terms at
\(-2\). For \(k\le j\), each factor \(c_h-c_j\) lies between
zero and \(c_h+2\), so \(0\le e_k(c_j)\le e_k(-2)\).
For \(k>j\), \(e_k(c_j)=0\). Hence
\[
 F_{j,N}(-2)\le\sum_{k=0}^j A_{k,N}^2\le\Sigma_N.
 \tag{26}
\]
The low kernel is the degree-\(J_N\) cosine interpolant of
these physical values; its norm costs at most \(N\) times
their largest modulus. Each high radical is bounded by
\(\sqrt{N-1}\) in either real variable. Thus
\[
 \sup_{z,C\in[-2,2]}|K_N(z,C)|
                       \le N\Sigma_N+N^2.
 \tag{27}
\]

For any canonical \(f\), the original reproducing identity and
full-normal trace bound give
\[
 |(Tf)(z)|=|\phi_N(K_N(z,C)f(C))|
 \le CN^3\|K_N(z,\cdot)\|_{[-2,2]}\|f\|_{[-2,2]}.
 \tag{28}
\]
The \(N^3\) version is the ordinary degree-\(2D\) Fourier and
full-Hermite folding bound from the dual-contour source; using
the coarser \(N^5\) canonical-product bound gives the same rate.
Combining (25)--(28) proves
\[
                 \|Tf\|_{[-2,2]}
                    \le N^{O(1)}e^{M_\infty N}\|f\|_{[-2,2]}.
 \tag{29}
\]
This ceiling is valid for arbitrary canonical inputs. It is
exponential, unlike the source-specific first-turn theorem for
original microscopic products.

That theorem's input estimates, or the endpoint-product source
directly, give a polynomial bound for \(K_N(w_N,\cdot)\).
Its derivative remains polynomial on
\([-2-B/N^2,2]\): expand in Chebyshev polynomials and use
their finite formulas on the Bernstein ellipse with parameter
\(e^{b_B/N}\). The coefficient sum, each fixed derivative,
and the enlargement cost only polynomial factors in \(N\).
The ordinary identity
\[
 Q_N(C)=\int_0^1
    \partial_C K_N(w_N,a_N+t(C-a_N))\,dt
 \tag{30}
\]
therefore proves a uniform polynomial norm for \(Q_N\).
Equations (29),(30) give the upper half of (5).
Finally Markov's inequality for degree at most \(D\) gives
\(N^{-2}\|Y_N'\|\le C\|Y_N\|\), proving (6).
In particular the full-normal upper budget has the same rate;
the lower bound came from actual values of that same source.

## 5. Coherent contour consequence and limitations

For the specified ordinary input \(P=K_N(w_N,\cdot)\), the
dual-contour source gives exactly, in the full algebra,
\[
 T\{\delta_zP-P(z)\delta_z\}
           =-\frac{P_N(z)}{\eta N^2}\,TQ_z.
 \tag{31}
\]
At physical \(z\) the scalar may vanish; it is not canceled
by inversion in the algebra. On the admissible microscopic
negative-endpoint parameter circles the normalized expression
in the contour formula has its ordinary removable meaning.
Its Cauchy integral at the real \(a_N\) in (3) is exactly
\(Y_N\), which has rate (5). Thus neither the coherent
subtraction nor its full contour integration gives a uniform
zero first-turn rate for these auxiliary quotients.

The original unquotiented \(TK_N(w_N,\cdot)=\delta_{w_N}\)
has bounded real norm. The enlargement by negative spatial
division therefore changes the actual source rate. A proposed
closure for arbitrary fixed microscopic products already
fails on its one-factor subclass. No claim is made that every
multifactor quotient has this same lower rate.

There is no conflict with fixed physical endpoint marks.
For \(w=c_b\) with \(b\) fixed, the original kernel and its
ordinary quotient have fixed degree, and the turn is polynomially
bounded. Those marks have \(P_N(w)=0\); the normalization (12)
and its positive forcing do not apply. They do not determine
the generic microscopic family by analytic continuation.

This result does not assign a rate to an arbitrary later shared
closing trace. Further original turns, spectators, and summation
can still cancel an exponentially large unclosed coupon. It
does not establish a nonzero geometric coefficient, a filling
threshold, or a failure of the volume goal.

## 6. Coverage and direct sources

A targeted search of the quotient, endpoint, and first-turn
notes found the individual negative dual-coupon lower bound,
but no bound for this coherent ordinary quotient. The new
input is the exact positive value recurrence (13), which
proves participation of the growing channel in the actual
source and supplies its full lower rate. The matching ceiling
uses the existing row and radical bounds with (24).

The following complete direct sources were read at unchanged
pins, with used implications and hashes checked:

* [Dual-contour quotient reduction](research_endpoint_quotient_dual_contour_reduction.md),
  SHA256 be10c62b6535ee9bb51b2895e4dae32514713c93d24cc659227ad15736139af1:
  ordinary reproducer, exact coherent quotient and contour identities,
  trace norm, both endpoint contours, and fixed-mark limitation.
* [Full endpoint products and physical-row bounds](research_endpoint_two_half_plane_relative_source.md),
  SHA256 985fa3331379c3877734f28773d314b667ee87fa63314a5ef4513a3fe128d194:
  root products, terminating physical rows, low cosine interpolation,
  high radical Fourier bound, and polynomial microscopic input norms.
* [Actual first-turn initialization](research_first_turn_endpoint_product_initialization.md),
  SHA256 7d0871a7dcde94c1cc73f98495b9521a61478729ddd52c51570ffa95f1901105:
  original physical operator and full-normal residual conventions,
  reproducing trace identities, and the distinct zero-rate input class.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test, build, or
compilation was run. Adopted notes and public manuscripts are unchanged.
