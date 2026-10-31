# An explicit half-degree Casimir polynomial for the original augmented pretzel base

**Subsequent analytic theorem.** This exact source now feeds the
[full coherent period asymptotic](actual_pretzel_coherent_circle_and_period_asymptotic.md),
which proves a nonzero leading coefficient and the actual augmented
link volume rate at arbitrary fixed odd width. The formulas below
retain their role as independently checked finite algebraic inputs.

29 October 2026. The COMPLETE mixed-circle base of every odd pretzel
has a single, explicit pair-Casimir polynomial. Its degree is at most
\(\lfloor(N-1)/2\rfloor\). Its coefficients in the physical continuant
basis are positive finite cosine/factorial products, with the actual
half-twist phase retained. This yields all nodal values AND first
normal jets, and an original one-variable coefficient source for every
odd number of boxes. No geometric saddle or noncancellation theorem
is inferred from this exact reduction.

## 1. Literal quarter-turn, not a partial transpose of a positive form

Use the original \(N,d,q,Q,x,\kappa,p,\ell,m,R,L_N\) of the
[pretzel source theorem](actual_odd_pretzel_augmented_transfer_source.md).
For any two-head box define its actual rigid quarter-turn by

\[
 (\mathscr R B)_{(u,b);(v,e)}
   =\sum_{r,t}\ell_{u,r}B_{(r,v);(b,t)}p_{t,e}
   =x^{u-e}B_{(d-u,v);(b,d-e)}.                      \tag{1}
\]

This is a linear tangle rotation using the original turns. It is not
a multiplicative map for vertical box composition and is not asserted
to preserve matrix positivity. The original crossing rotation/snakes
give \(\mathscr R(R^{-1})=R\), with full Cartan retained; also
\(\mathscr R(I)=p\ell\), rather than the identity matrix.

The charge transfer in the pretzel theorem makes this rotation source
exact. On degree \(T=d+h\), if \(S_h=\operatorname{diag}(x^a)\)
and \(P_h\) is physical reversal, then

\[
 (\mathscr R B)|_T=x^dP_hS_hM_B^{(h)}S_h^{-1}P_h.      \tag{2}
\]

Under this conjugation \(D_h\) becomes the clock \(Q^{-b}\) of
the second physical head. Its factor relative to the original pivot
\(g_b=x^{-d}Q^{-b}\) cancels every remaining phase in the pretzel
source. Precisely,

\[
 \boxed{\displaystyle
 \mathcal A_{s,N}(B_1,\ldots,B_s)
       =\Phi_2\bigl((\mathscr R B_1)\cdots(\mathscr R B_s)\bigr),
 \quad\Phi_2(X)=\frac1N\operatorname{Tr}_{V\otimes V}
                                      [(I\otimes g)X].} \tag{3}
\]

This is the same original marked source, not a new \(2N\) average.

## 2. Why the rotated box is a SINGLE full pair polynomial

An actual pair intertwiner rotates to another pair intertwiner by
the Hopf cup and cap equations. Work first at generic nearby \(q\),
with the ordinary finite highest module of dimension \(N\), its
genuine dual turns, and the literal mixed-circle polynomial. These
data specialize regularly to the displayed root source: all turn
factorials have indices below \(N\). Generic pair decomposition is
multiplicity-free, with \(N\) distinct Casimir nodes, so every rotated
box here is a unique polynomial in the generic pair Casimir of
degree less than \(N\).

These polynomial coefficients have NO root pole. Indeed the middle
degree block of the Casimir is tridiagonal, and all its adjacent
entries remain nonzero at the root. The map from its first \(N\)
polynomial coefficients to its first physical row is triangular with
these nonzero products on the diagonal. Its inverse is regular.
Consequently the polynomial identity specializes on the ENTIRE
physical pair, including high-degree blocks and all Jordan normals.
It is not only a statement about distinct root eigenvalues.

Apply this to \(B_*=R^{-1}L_N\), using the generic ordinary circle
with its standard pivot before specialization. At the root its
\((-1)^d\) pivot factor is exactly the original auxiliary pivot.
Thus \(\mathscr R B_*=z_N(\Omega)\) for one degree-\(<N\) polynomial.

## 3. Explicit positive coefficients and the half-degree truncation

Let \(A=\Omega|_{\deg d}\) in physical order \(|u,d-u\rangle\).
Write its diagonal as \(D_u\) and adjacent entry as
\(a_u=-(1-Q^{u+1})^2\). Define its canonical continuant polynomials

\[
 f_0(z)=1,\quad f_1(z)=(z-D_0)/a_0,
\]
\[
 f_{u+1}(z)=\frac{(z-D_u)f_u(z)-a_{u-1}f_{u-1}(z)}{a_u}.
                                                               \tag{4}
\]

Tridiagonality gives \(e_0^Tf_u(A)=e_u^T\). Thus the first physical
row determines the polynomial by this specified basis.

Put \(M=\lfloor d/2\rfloor\) and

\[
 C_L=\prod_{r=0}^{L-1}2\cos\frac{\pi(2r+1-L)}{2N},
 \qquad C_0=1,
\]
\[
 b_v=\frac{s_{d-v}^2 C_{d-2v}}{s_{d-2v}}>0,
                 \qquad 0\leq v\leq M.               \tag{5}
\]

At exactly these lengths the cosine product simplifies further:

\[
 C_{d-2v}=\frac{F_{d-v}}{F_v}=\frac{N}{s_v^2},\qquad
 \boxed{\quad b_v=\frac{N^2s_{2v}}{s_v^4},\quad
           b_vx^v=N^2\frac{F_{2v}}{F_v^4}.\quad}      \tag{5a}
\]

Indeed \(-q^{1-(d-2v)}=Q^{v+1}\), so the product is precisely the
interval \((Q^{v+1};Q)_{d-2v}\). Root factorial complementation
gives the real positive value displayed. All integer lengths are
below \(N\); this retains the exact root phases, rather than taking
absolute values inside an unknown sum.

Then the COMPLETE original base polynomial is

\[
 \boxed{\displaystyle
 z_N(z)=\kappa^{-1}\sum_{v=0}^{M}b_v f_v(z).}           \tag{6}
\]

Proof of its first row. Equation (1), restricted to the middle degree,
gives
\((\mathscr R B_*)_{0,v}=x^{v-d}(B_*)_{(d,v);(d,v)}\).
In the high block of physical degree \(d+v\), the original \(R^{-1}\)
has only its first column in its last row, with coefficient
\(\kappa^{-1}x^{d-v}\). Therefore the two phases cancel exactly and

\[
 (\mathscr R B_*)_{0,v}
   =\kappa^{-1}(H_N|_{d-v})_{0,0}.                    \tag{7}
\]

The [positive reflected-circle theorem](actual_complete_circle_reflection_positive.md)
proves that this corner vanishes if \(2v>d\), and otherwise equals

\[
 s_{d-v}^2\sum_{a=0}^{d-2v}\frac1{s_as_{d-2v-a}}.
\]

The finite sum FACTORIZES. At any \(0\leq L<N\), the finite
q-binomial theorem and
\(F_a=(-i)^a q^{a(a+1)/2}s_a\) give

\[
 \sum_{a=0}^L\frac1{s_as_{L-a}}
   =\frac{(-q^{1-L};Q)_L}{s_L}=rac{C_L}{s_L}.        \tag{8}
\]

In the middle expression the product is real and positive: its
individual phases sum to zero, and all its cosine factors are
positive. This proves (5)--(7), including the exact truncation.

In particular the top coefficient of \(z_N\) is nonzero. For odd
\(N=2m+1\), it has the especially simple exact value

\[
 [z^m]z_N(z)=\kappa^{-1}q^{-m(m+1)},                  \tag{9}
\]

of modulus one. No absent leading channel is being supplied by a
normalization choice. At even \(N=2m\), its degree is \(m-1\) and
the top coefficient has modulus \(8/s_1\), also polynomial and nonzero.

## 4. All nodal values and normal jets without a large crossing matrix

For every original node \(c_j=q^{2j+1}+q^{-2j-1}\), define

\[
 \lambda_j=\kappa^{-1}\sum_{v=0}^M b_v f_v(c_j),\qquad
 \xi_j=\kappa^{-1}\sum_{v=0}^M b_v f'_v(c_j).           \tag{10}
\]

These give the FULL node values and first derivatives of the actual
rotated base box. Paired nodes have exactly the same data. At the
possible odd simple node only the value is required. Differentiate
(4) to compute every derivative with no divided zero:

\[
 f'_{u+1}=
 \frac{f_u+(z-D_u)f'_u-a_{u-1}f'_{u-1}}{a_u},
 \quad f'_0=0,\quad f'_1=1/a_0.                      \tag{11}
\]

For a formula entirely in finite q-factorials, use the actual q-Hahn
value formula in the
[complete physical packet](actual_complete_casimir_hermite_packet.md),
Section5, at \(T=d\): each \(f_v(c_j)\) is its displayed finite sum
of three Gaussian binomials and an explicit quadratic \(Q\) phase.
Equation (10) with (5) is therefore a finite factorial/quadratic-phase
formula, not an unspecified eigenvector or a spectral fit. Equations
(4),(11) retain all normal data even at even and composite levels.

There is a shorter polynomial factorial formula. Define

\[
 P_r(z)=\prod_{a=0}^{r-1}(1-qQ^a z+Q^{2a+1}),\qquad P_0=1.
\]

Direct substitution in the explicit recurrence (4), coefficient by
coefficient in this product basis, gives

\[
 f_v(z)=x^v\sum_{r=0}^v
       \frac{(Q^{-v};Q)_rQ^r}{F_r^3}P_r(z),
\]
\[
 \boxed{\displaystyle
 \frac{\kappa z_N(z)}{N^2}=
  \sum_{v=0}^M\frac{F_{2v}}{F_v^4}
     \sum_{r=0}^v\frac{(Q^{-v};Q)_rQ^r}{F_r^3}P_r(z).} \tag{11a}
\]

This is an OWN finite polynomial identity: its proof uses the
coefficient recurrence (4), the root relation \(x=-q^{-1}\), and
\(P_{r+1}=P_r(1-qQ^r z+Q^{2r+1})\). It does not assume a named
orthogonal-polynomial transformation or an asymptotic formula.
More explicitly, with
\(C_{v,r}=x^v(Q^{-v};Q)_rQ^r/F_r^3\) and zero coefficients outside
\(0\leq r\leq v\), the coefficient identity to check is

\[
 a_vC_{v+1,r}=(c_r-D_v)C_{v,r}
       -q^{-1}Q^{1-r}C_{v,r-1}-a_{v-1}C_{v-1,r}.
\]

It follows by inserting the finite products and clearing their
nonzero factorial denominators; the initial coefficients are those
of \(f_0,f_1\). This also specifies all boundary terms of the check.
Writing \(z=w+w^{-1}\) factors \(P_r=(qw;Q)_r(q/w;Q)_r\), so all
node values for \(0\leq j\leq M\) have the explicit quadratic sum

\[
 \frac{\kappa\lambda_j}{N^2}
  =\sum_{v=0}^M\sum_{r=0}^{\min(v,j)}
    \frac{Q^{r(r-v-j)}F_{2v}F_{j+r}}
         {F_v^3F_{v-r}F_{j-r}F_r^3}.                 \tag{11b}
\]

The NORMAL source must not truncate the same way. For every double
node let \(w_j=q^{2j+1}\), and

\[
 A_{v,r}=\frac{F_{2v}(Q^{-v};Q)_rQ^r}{F_v^4F_r^3},
\quad B_{j,r}=(Q^{j+1};Q)_r(Q^{-j};Q)_r.
\]

For \(r\leq j\) put

\[
 D_{j,r}=\sum_{a=0}^{r-1}
   \left[\frac{Q^{a-j}}{1-Q^{a-j}}
              -\frac{Q^{a+j+1}}{1-Q^{a+j+1}}\right].
\]

Every denominator in this expression is nonzero. Differentiating
the full polynomial BEFORE specializing gives the exact normal

\[
 \frac{\kappa\xi_j}{N^2}
 =\frac1{w_j-w_j^{-1}}\sum_{v=0}^M
 \left[\sum_{r=0}^{\min(v,j)}A_{v,r}B_{j,r}D_{j,r}
 +\sum_{r=j+1}^v A_{v,r}(-1)^jQ^{-j(j+1)/2}
                              F_{j+r}F_{r-j-1}\right]. \tag{11c}
\]

The second sum is essential. For \(r>j\), the value of
\((q/w;Q)_r\) vanishes at \(w_j\), but its logarithmic derivative
does not: removing its unique zero gives exactly
\((-1)^jQ^{-j(j+1)/2}F_jF_{r-j-1}\). Thus (11c) keeps the
first-normal source terms which are invisible in the terminating
node-value sum (11b). At the odd simple node \(w=-1\), no first
normal is required; the safe polynomial derivative (11) remains
available if desired. The audit checks (11a)--(11c) against the
original full physical Hermite blocks.

## 5. The unchanged one-variable source and what it does not prove

The actual pair source has the exact expression

\[
 \Phi_2(f(\Omega))=
 (-1)^d\sum_{j<d-j}
       [(4-c_j^2)f'(c_j)-c_jf(c_j)]
       +\mathbf1_{N\ \mathrm{odd}}f(-2).              \tag{12}
\]

This follows directly from the generic ordinary pair decomposition
and original pivotal partial trace, not from an imported polynomial
invariant. At generic angle \(\theta\) the coefficient is the ratio
\(\sum_j\sin(n_j\theta)f(2\cos n_j\theta)/\sin(N\theta)\),
where \(n_j=2N-1-2j\). At \(\theta=\pi/N\) numerator and denominator
vanish. Differentiate: a paired pair has \(n_j+n_{d-j}=2N\), giving
the summand in (12). The unpaired \(n_j=N\) gives \(f(-2)\).
The original root pivot differs from the ordinary \(K\) pivot by
\((-1)^d\), exactly the displayed sign. The actual partial trace is
regular, so this computes its value rather than a new derivative source.

Equivalently, reduce \(f\) modulo the FULL
\(\mathcal P_N(z)=2T_N(z/2)+2\), retaining its double roots. Then

\[
 \Phi_2(f(\Omega))=(-1)^dN^2[z^d](f\bmod\mathcal P_N). \tag{13}
\]

For a direct verification, put \(w_k=q^{2k+1}\). The right side of
(12) is
\(-(-1)^d\sum_k(w\partial_w)[(w-w^{-1})f(w+w^{-1})]/2\).
For degree below \(d\), root Fourier orthogonality annihilates it;
at degree \(d\), the coefficients at \(w^{\pm N}\) give
\((-1)^dN^2\). This proves (13).

Consequently the COMPLETE raw augmented pretzel base at every odd
number of boxes is

\[
 \boxed{\displaystyle
 \mathcal A_{s,N}(N,\ldots,N)
 =(-1)^d\sum_{j<d-j}
   [(4-c_j^2)s\xi_j\lambda_j^{s-1}-c_j\lambda_j^s]
       +\mathbf1_{N\ \mathrm{odd}}\lambda_{d/2}^s
 =(-1)^dN^2[z^d](z_N(z)^s\bmod\mathcal P_N).}          \tag{14}
\]

The literal original marked cut, all half-twist phases and all normal
channels remain. For \(N=2\) the polynomial has degree zero and the
base is exactly zero. For \(N=3\), (6) is
\(z_3(z)=q^2z-1-5i\sqrt3\); (14) at \(s=3\) recovers exactly
\(-189+81i\sqrt3\).

There is also an exact original one-variable residue and its finite
integer windings. For any \(R>1\), parametrizing the enclosing
\(z\)-ellipse by \(z=w+w^{-1}\) gives

\[
 \mathcal A_{s,N}
 =\frac{(-1)^dN^2}{2\pi i}\int_{|w|=R}
 z_N(w+w^{-1})^s
       \frac{w^N(1-w^{-2})}{(1+w^N)^2}\,dw.            \tag{15}
\]

Indeed the coefficient in (13) is the enclosing residue of
\(z_N(z)^s/\mathcal P_N(z)\), and
\(\mathcal P_N(w+w^{-1})=w^{-N}(1+w^N)^2\). Expanding on
the ACTUAL outer circle yields the finite coefficient identity

\[
 \boxed{\displaystyle
 \mathcal A_{s,N}=(-1)^dN^2
 \sum_{m=1}^{\lfloor(sM+1)/N\rfloor}(-1)^{m-1}m
 \left([w^{mN-1}]-[w^{mN+1}]\right)
                         z_N(w+w^{-1})^s.}            \tag{16}
\]

Coefficients outside the Laurent degree range are zero. The \(m\)
weight is exactly the double-pole/normal source from (12); it must
not be dropped. For \(s=3\) only \(m=1\) can occur. This gives a
fixed finite set of true winding channels at each fixed \(s\), not
an identification of independent logarithmic aliases. No separation
of the unit-circle poles or omission of the \(w=0\) Laurent behavior
is used: (15) is an exact parametrization of the original enclosing
residue, and (16) is its convergent outer Laurent expansion.

The source in (14) is oscillatory. Positive \(b_v\) do not make the
\(f_v(c_j)\) real positive, and taking separate absolute values of
the nodal terms need not give the sharp antiprism volume. A selected
asymptotic evaluation retaining these phases and integer Fourier
marks is still required. No nonzero geometric coefficient, open
cusp-color corridor or simultaneous long-filling survival is claimed
by this exact finite reduction.
