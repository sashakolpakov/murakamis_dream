# A whole-interval upper rate for the original terminal Jordan pair

Private written proof, 16 November 2026.

Polynomial initialization at finitely many original physical rows,
crude propagation through short endpoint intervals, and the
compact-interior transfer theorem give a whole-real-interval
upper rate for every fixed signed terminal power. Both the
terminal eigenvector and its original normal companion are
included. This is an upper bound only, and does not control
ordinary branching products.

## 1. Statement and original normalization

Retain
\[
 q=e^{\pi i/N},\quad D=N-1,\quad \eta=(-1)^D,\quad
 \kappa=q^{D^2/2},\quad
 c_j=2\cos((2j+1)\pi/N),
\]
\[
 P_N(Z)=2T_N(Z/2)+2,\qquad
 \mathcal A_N=\mathbb C[Z]/(P_N).
\]
The operators \(T,R,C,J,V_n,D_n\), the kernel \(K_N\),
and the Frobenius functional \(\phi_N\) have their original
normalizations. In particular
\[
 Te_j=e_{D-j},\quad
 e_j(Z)=S_j^{-2}\prod_{r<j}(c_r-Z),\quad
 S_j=\prod_{r=1}^j2\sin(r\pi/N),\quad
 \phi_N(e_i e_j)=\mathbf1_{i+j=D},
\]
\[
 C f=Zf\pmod {P_N},\quad J=TCT,\quad
 V_n=\kappa^nTR^{-n}T,\quad D_n=V_nCV_{-n},
\]
\[
 Q_0(Z)=\partial_wK_N(c_0,Z),\qquad
 G_n=T(R^{-n}),\qquad H_n=T(R^{-n}Q_0).
 \tag{1}
\]
Every norm below is the norm of the ordinary canonical
polynomial on \([-2,2]\), denoted \(\|\cdot\|_{\mathbb R}\).

For fixed \(n\ne0\), let \(\tau_{\ell,n}(u)\),
\(1\le\ell\le |n|\), be the distinct physical shift roots
of the original terminal characteristic, each still of
algebraic multiplicity two. The physical coordinate is
\[
 u=j/N,\qquad x=2\cos(2\pi u),\qquad 0<u<1/2.
\]
Define
\[
 L_n(u)=\max_\ell\log|\tau_{\ell,n}(u)|,\qquad
 \mathcal I_n=\int_0^{1/2}L_n(u)\,du.                    \tag{2}
\]
The integral is improper. The modulus-order theorem proves
that it is finite and nonnegative. For \(|n|=1\), \(L_n=0\).
For \(|n|\ge2\), it equals the logarithm of one globally
labeled growing modulus \(\rho_{1,|n|}\). The definition
by the maximum is sufficient here. Put \(\mathcal I_0=0\).

**Theorem 1.** For every fixed integer \(n\),
\[
 \boxed{\quad
 \limsup_{N\to\infty}\frac1N
       \log\big(\|G_n\|_{\mathbb R}+\|H_n\|_{\mathbb R}\big)
                         \le \mathcal I_n .
 \quad}                                                   \tag{3}
\]
For fixed \(n\ne0\) and every sufficiently small fixed
\(\epsilon>0\), a quantitative form is
\[
 \begin{split}
 \|G_n\|_{\mathbb R}+\|H_n\|_{\mathbb R}
 \le{}& C_{n,\epsilon}N^{p_{n,\epsilon}}
   \exp\left\{
       N\int_\epsilon^{1/2-\epsilon}L_n(u)\,du
        +N C_n\epsilon\log(e/\epsilon)
        +C_{n,\epsilon}\sqrt N\right\}.
 \end{split}                                             \tag{4}
\]
Here \(C_n\) is independent of \(\epsilon\); the other
constants may depend on the fixed interior interval.
The two signs have the same integral, by the original
signed characteristic conjugation.

## 2. Polynomial data at every fixed initial row

We first prove the actual source initialization rather than
assuming small initial data for an abstract recurrence.
For a fixed nonnegative integer \(j\), put
\[
 F_j(w)=K_N(c_j,w),\qquad
 Q_j(w)=\partial_ZK_N(Z,w)|_{Z=c_j}.                      \tag{5}
\]

**Lemma 2.** For every fixed integer \(M\), there are constants
\(C_M,p_M\) such that, for all sufficiently large \(N\),
\[
 \max_{0\le j\le M}
       \big(\|F_j\|_{\mathbb R}+\|Q_j\|_{\mathbb R}\big)
                                             \le C_MN^{p_M}.
 \tag{6}
\]
Consequently, for every fixed \(n,M\), all the actual values
and first spectral normals of \(G_n,H_n\) at these rows
are polynomially bounded.

*Proof.* The original kernel gives \(F_0=1\), while the
full normal source gives
\[
                         \|Q_0\|_{\mathbb R}\le N^4/4.    \tag{7}
\]
We record a simple bound on the endpoint forcing as well.
The elementary sine product is \(S_D=N\), obtained by
evaluating \((z^N-1)/(z-1)\) at \(z=1\).
Thus
\[
 e_D(Z)=\frac{\eta P_N(Z)}{N^2(Z-c_0)},\qquad
                         \|e_D\|_{\mathbb R}\le1.         \tag{8}
\]
For the inequality use \(P_N(c_0)=0\) and
\(\|P_N'\|_{\mathbb R}\le N^2\), the latter following from
\(P_N'=N U_{N-1}(Z/2)\) and
\(\|U_{N-1}\|_{[-1,1]}\le N\).
Ordinary Markov inequalities give polynomial bounds for
each fixed derivative of \(e_D\).

Write \(c(r)=2\cos((2r+1)\pi/N)\), and retain the exact
ordinary kernel equation in its first variable,
\[
 (w-\widetilde J_Z)K_N(Z,w)
                      =\frac{\eta P_N(w)}{N^2}e_D(Z),     \tag{9}
\]
\[
 (\widetilde J f)(c(r))
  =(c_0+A(r)+B(r))f(c(r))
      -A(r)f(c(r+1))-B(r)f(c(r-1)),
\]
\[
 A(r)=\frac{s_{r+1}^4}{s_{2r+1}s_{2r+2}},\qquad
 B(r)=\frac{s_r^4}{s_{2r}s_{2r+1}},\qquad
 s_r=2\sin(r\pi/N).
 \tag{10}
\]
The removable first-row values are \(B(0)=B'(0)=0\).
For each fixed \(0\le j\le M\), \(A(j)^{-1}\), all the
other coefficients needed here, and their first index
derivatives have polynomial bounds in \(N\).
This follows directly from their finite sine quotients:
all their nonzero small-index sines have size comparable
to \(N^{-1}\). The removable \(B\) is simplified first.

The physical values \(e_D(c_j)\) vanish. Solving (9)
at row \(j\) therefore propagates \(F_{j+1}\) from
\(F_j,F_{j-1}\) with polynomial coefficients on the
real \(w\) interval. At \(j=0\) the previous value is
absent. Starting with \(F_0=1\), finitely many such
steps prove the value assertion in (6).

Differentiate the ordinary index equation (9) before
evaluating at the physical row. The unknown normal is
\[
                         Y_j(w)=c'(j)Q_j(w).
 \tag{11}
\]
It obeys the same homogeneous second-order row equation,
with forcing from coefficient derivatives and the
derivative of the literal right side of (9).
This forcing is polynomially bounded in real \(w\):
\(\|P_N\|_{\mathbb R}\le4\), (8) controls \(e_D'\),
and all already obtained \(F_j\) and coefficients are
polynomial. The first row again has no previous unknown,
because \(B(0)=B'(0)=0\).
Its initial datum is \(c'(0)Q_0\), controlled by (7).
Finitely many steps give polynomial \(Y_j\); division by
\(|c'(j)|\), whose inverse is polynomial at each fixed row,
proves (6). For large \(N\) all these fixed rows are double
physical nodes, so no ramified last-node normal is involved.

Here are the exact initial trace formulas:
\[
 \begin{split}
 G_n(c_j)&=\phi_N(R^{-n}F_j),&
 G_n'(c_j)&=\phi_N(R^{-n}Q_j),\\
 H_n(c_j)&=\phi_N(R^{-n}Q_0F_j),&
 H_n'(c_j)&=\phi_N(R^{-n}Q_0Q_j).
 \end{split}                                             \tag{12}
\]
They follow from
\((Tf)(Z)=\phi_N(f\,K_N(Z,\cdot))\), with all products and
product-rule normals inside the original trace.

For any fixed integer \(n\), the original physical jets of
\(R^{-n}\) have values of modulus one and angular first
derivative bounded by \(|n|N/2\).
This follows from the original signed crossing jets and
the product rule in the full algebra.
Equations (6)--(7), Markov's inequality, and the product
rule therefore bound the complete physical data of each
product in (12) by a polynomial in \(N\).
The stable full-Hermite Fourier reconstruction gives a
polynomial real norm for its canonical representative.
This operation is on the traced variable; no quotient is
imposed on a free exterior variable.

For clarity, the trace itself also has polynomial norm.
For a canonical polynomial \(p\),
\[
 \phi_N(p)=\eta N^2[Z^D]p,\qquad
                         |\phi_N(p)|\le N^2\|p\|_{\mathbb R}.
 \tag{13}
\]
The equality follows from \(\phi_N(e_j)=\mathbf1_{j=D}\)
and the leading coefficient \(\eta/N^2\) in (8).
For the inequality, the top Chebyshev coefficient has
modulus at most \(2\|p\|_{\mathbb R}\), and
\(T_D(Z/2)\) has leading coefficient \(1/2\).
Applying (13) to the canonical products in (12)
completes the proof. \(\square\)

## 3. Coarse propagation through both endpoint strips

Fix \(n=\sigma m\ne0\), \(m=|n|\), and put
\[
                   J_N=\lfloor(N-1)/2\rfloor.
 \tag{14}
\]
Use the exact \(8m\)-dimensional value/normal system of
the bulk-transfer theorem, with coordinate
\(c_N(u)=2\cos(2\pi u+\pi/N)\).
Its state is
\[
 \mathbb X_j=(X_j^G,Y_j^G,X_j^H,Y_j^H)^{\mathsf T},
\]
\[
 X_j^F=(F(c_{j-m}),\ldots,F(c_{j+m-1}))^{\mathsf T},
\quad
 Y_j^F=(c_N'((j-m)/N)F'(c_{j-m}),\ldots,
            c_N'((j+m-1)/N)F'(c_{j+m-1}))^{\mathsf T}.
 \tag{15}
\]
There is no collision between the row kernel notation
\(F_j\) in (5) and the placeholder \(F=G_n,H_n\) in (15).
The exact equation is
\[
 \mathbb X_{j+1}=\mathbb A_N(j/N)\mathbb X_j,\qquad
 \mathbb A_N=
 \begin{pmatrix}
 \mathsf A_N&0&0&0\\
 \mathsf A_N'&\mathsf A_N&0&0\\
 \mathsf B_N&0&\mathsf A_N&0\\
 \mathsf B_N'&\mathsf B_N&\mathsf A_N'&\mathsf A_N
 \end{pmatrix}.
 \tag{16}
\]
Primes are scaled-coordinate derivatives.
Here \(\mathsf A_N\) is the order-\(2m\) physical companion
matrix for \(D_n-c_0\); \(\mathsf B_N\) contains the literal
forcing of \(H_n\) by \(G_n\).
Their exact definitions, including the forcing column,
are (15)--(18) of the bulk-transfer source.

**Lemma 3.** For all sufficiently large \(N\) and all integers
\[
                         m\le j\le J_N-m,                \tag{17}
\]
put
\[
             d_j=\min\{j-m+1,\ J_N-m-j+1\}\ge1.
 \tag{18}
\]
There are constants \(C_n,B_n\), independent of \(j,N\),
such that
\[
                    \|\mathbb A_N(j/N)\|
                              \le C_n(N/d_j)^{B_n}.       \tag{19}
\]
The equation (16), including its angular-normal rows,
remains exact through the last row \(j=J_N-m\).
That last step generates the value at \(J_N\).

*Proof.* The ordinary operator expansion in the bulk source
constructs \(D_n\) by finitely many products of the
physical \(J\) row and spectral multiplication. In a
coefficient of its \(2m\)-order row, every occurrence of
\(A(r),B(r)\) has
\[
                          j-m+1\le r\le j+m-1.           \tag{20}
\]
This follows inductively from the right-ordered recurrence
for \(D_n\): a term of order \(k\) shifts the final \(J\)
row by at most \(k\), where \(k\le m-1\).
Thus \(r\ge d_j\) and \(J_N-r\ge d_j\).
In particular \(1\le r\le J_N-1\); no singular next row
is used.

Every sine in a denominator in (10) is bounded below
in modulus by \(c\,d_j/N\), uniformly in (17).
For example,
\(N-(2r+2)\ge2d_j\) at even \(N\), and
\(N-(2r+2)\ge2d_j-1\ge d_j\) at odd \(N\).
The other denominator arguments have at least the same
endpoint distance up to an absolute factor.
Also
\(\sin((r+1)\pi/N)\ge c\,d_j/N\).
Consequently \(A(r),B(r)\), their scaled-coordinate
derivatives, and \(A(r)^{-1}\) are bounded by fixed
powers of \(N/d_j\). Explicitly one can use
\[
 |A(r)|+|B(r)|\le C(N/d_j)^2,\qquad
                         |A(r)^{-1}|\le C(N/d_j)^4.
 \tag{21}
\]
Differentiating any sine factor in the coordinate \(u=r/N\)
costs only an absolute constant in its numerator, and
one extra inverse sine if it occurs in a denominator.
Thus the same type of bound holds for all fixed
coefficient derivatives needed in (16).

The exact forward extreme coefficient is
\[
 b_{n,m,N}(j/N)
       =q^{-\sigma(2j+m+1)}
                      \prod_{\ell=0}^{m-1}A(j+\ell).
 \tag{22}
\]
Its inverse is bounded by \(C_n(N/d_j)^{4m}\).
All other row coefficients are fixed finite sums of the
products just bounded. Dividing by (22), and differentiating
this quotient once, proves (19) for the companion and all
four blocks in (16). The power \(B_n\) need not be optimized.
No factor \(N^{B_n}\) independent of \(d_j\) is introduced.

The original ordinary residual is a \(P_N\) multiple,
and \(P_N(c_N(u))=4\sin^2(\pi Nu)\).
Its value and first \(u\) derivative therefore vanish
at all physical rows used here. This proves the same
exact nodal-normal equation even at the last output.
At odd \(N\), that output is the simple node \(c_{J_N}=-2\);
its angular derivative is zero. Its value is retained,
and no spectral normal at that simple node is asserted.
At even \(N\), the last output is the last double node.
All coefficient rows remain at most \(J_N-1\) by (20).
\(\square\)

Take \(0<\epsilon<1/16\), and define
\[
       \ell_N=\lceil\epsilon N\rceil,\qquad
       r_N=J_N-\lceil\epsilon N\rceil.
 \tag{23}
\]
For sufficiently large \(N\), \(\ell_N\ge m\) and
\(r_N\le J_N-m\).
The initial state \(\mathbb X_m\) consists only of the
fixed rows \(0,\ldots,2m-1\), and is polynomial by Lemma 2.
On the left strip \(m\le j<\ell_N\), the first distance
in (18) is the smaller one.
On the right strip \(r_N\le j\le J_N-m\), the second
one is the smaller one.
Products of (19) on either strip are consequently bounded by
\[
 C_n^K\prod_{r=1}^K(N/r)^{B_n}
       \le \exp\{C_n K\log(eN/K)\},                      \tag{24}
\]
where \(K\le\epsilon N+O_n(1)\).
Use \(K!\ge(K/e)^K\).
Increasing constants to include the fixed discrepancy,
the bound is
\[
 \exp\{N C_n\epsilon\log(e/\epsilon)+O_n(\log N)\}.        \tag{25}
\]
Constants in (25) are independent of \(\epsilon\).
The same estimate bounds every partial endpoint product,
after taking the coarse factors in (19) to be at least one.

## 4. Joining the estimates and recovering the ordinary polynomial

For fixed \(\epsilon\), all rows from \(\ell_N\) through
\(r_N\) lie in a compact physical interior interval.
The full coupled bulk theorem gives, for every intermediate
state, a polynomial factor times
\[
 \exp\left\{
     N\int_{\ell_N/N}^{r_N/N}L_n(u)\,du
                           +C_{n,\epsilon}\sqrt N\right\}.
 \tag{26}
\]
Here it is legitimate to use the integral over the entire
bulk interval when bounding any prefix: \(L_n\ge0\).
The original \(H_n\) forcing and both first normals are
inside this transfer estimate, not estimated separately.
Moving either endpoint of the integral by \(O(N^{-1})\)
changes its exponent by \(O_{n,\epsilon}(1)\).

Combine the polynomial initial state, (25) on both sides,
and (26). This bounds every value and every scaled angular
normal of \(G_n,H_n\) at all distinct physical nodes by
the right side of (4), with possibly different constants
and polynomial power.
There is no missing final row: the last matrix is
\(\mathbb A_N((J_N-m)/N)\), whose output state reaches
the node \(J_N\).

The stable full-Hermite reconstruction gives for every
canonical polynomial \(p\)
\[
 \|p\|_{\mathbb R}
 \le (2N-1)\max_{\rm physical}|p|
       +2\max_{\rm angular}|\partial_t p(-2\cos t)|.
 \tag{27}
\]
With \(t=\pi-2\pi u-\pi/N\), the angular derivative equals
\(-1/(2\pi)\) times the scaled derivative in (15).
The paired physical lifts have the required opposite
angular derivatives; the odd simple node has derivative
zero. Thus all data in (27) have just been bounded.
This proves (4) for the ordinary real norm, including the
full normal information of the original source.
If desired, division by
\(|c_N'(j/N)|\ge8\pi/N\) at a double physical node, or
ordinary Markov after (27), costs only a polynomial.

For fixed \(\epsilon\), divide the logarithm of (4) by
\(N\) and take the upper limit. Then let \(\epsilon\)
decrease to zero. The term
\(\epsilon\log(e/\epsilon)\) tends to zero, and the
characteristic integral converges by the modulus-order
theorem. This proves (3) for \(n\ne0\).
The order of the limits matters: no uniform bulk estimate
on a shrinking interval was assumed.

For \(n=0\), \(D_0=C\) and
\((C-c_0)G_0=0\), \((C-c_0)H_0=G_0\).
At every other double physical node both values and first
normals vanish, and at the odd simple node both values
vanish. The only remaining physical jets are the fixed
endpoint jets controlled by (12), with \(n=0,j=0\).
Equation (27) therefore gives a polynomial bound also
in this case, proving (3) with \(\mathcal I_0=0\).

## 5. Both original anchors with a polynomially bounded spectator

**Corollary 4.** Fix an integer \(n\), and let \(p_N\) be any
sequence of canonical polynomials with
\(\|p_N\|_{\mathbb R}\le C N^a\), for fixed \(C,a\).
Retain the actual coherent anchors
\[
 \mathcal A_{0,N}=\kappa^n\phi_N(G_n p_N),\qquad
 \mathcal A_{1,N}=\kappa^n\phi_N(H_n p_N).
 \tag{28}
\]
Then
\[
 \boxed{\quad
 \limsup_{N\to\infty}\frac1N
       \log(1+|\mathcal A_{0,N}|+|\mathcal A_{1,N}|)
                              \le\mathcal I_n .
 \quad}                                                   \tag{29}
\]
In particular this supplies an upper budget for both
branching anchors whenever the surviving coupon has
the stated polynomial ordinary real norm.

*Proof.* For any two canonical polynomials \(F,p\),
the physical values of their product are bounded by
\(\|F\|_{\mathbb R}\|p\|_{\mathbb R}\).
Markov's inequality and the full product rule bound its
angular first derivatives by
\(C N^2\|F\|_{\mathbb R}\|p\|_{\mathbb R}\).
Applying (27) to the canonical representative of this
product therefore gives, with a deliberately coarse power,
\[
 \|\operatorname{can}(Fp)\|_{\mathbb R}
              \le C N^3\|F\|_{\mathbb R}\|p\|_{\mathbb R}.
 \tag{30}
\]
The first-normal terms are part of this estimate; values
alone would not justify the canonical multiplication.
Now (13), \(|\kappa^n|=1\), and (30) give the exact
trace upper estimate
\[
 |\mathcal A_{0,N}|+|\mathcal A_{1,N}|
 \le C N^5\|p_N\|_{\mathbb R}
                  (\|G_n\|_{\mathbb R}+\|H_n\|_{\mathbb R}).
 \tag{31}
\]
Use Theorem 1 and \(\mathcal I_n\ge0\) to obtain (29).
No signs or normal channels in the original traces were
replaced; only their absolute size is bounded here.
\(\square\)

This corollary assumes the ordinary polynomial norm of
the actual spectator. It does not prove such a bound for
an arbitrary turned product, and does not estimate the
mixed forcing after a turn. The second anchor uses
\(H_n=T(R^{-n}Q_0)\) exactly; it is not obtained by
substituting \(V_nQ_0\). No lower bound is asserted.

## 6. Scope and direct sources

This theorem closes the physical endpoint initialization
and whole-interval upper propagation for the specified
terminal pair \(G_n,H_n\). It does not show that a
maximal-modulus characteristic has nonzero coefficient
in either polynomial. No lower bound or equality of
rates follows. It does not compare \(\mathcal I_n\) with
a filled geometric action, control an ordinary product
after branching, or identify a relative-cycle coefficient.
All original crossing phases and normal traces were
retained in (12) and the exact system (16).

The three complete direct sources were read at their
unchanged pins, and their used implications and hashes checked:

* [Exact terminal bulk transfer](research_terminal_twist_bulk_transfer_bound.md),
  SHA256 fca96865315f21dc9961be89061cc6c3a292b2b563e7ded756e86c3438ef5bde:
  signed extreme coefficients, canonical residual, exact
  value/normal system, and integrated maximum-root bound.
* [Global terminal modulus ordering](research_terminal_twist_global_modulus_order.md),
  SHA256 79f26184f1ea0a4d45bb9961397175fc1fa6bad332482edd681a85156a6eae3a:
  nonnegative maximum logarithmic modulus, both signs,
  and integrability at both physical endpoints.
* [Original full endpoint and normal propagation](research_full_endpoint_unit_turn_polynomial_bound.md),
  SHA256 329ee59c992c359c42775f564f540ffeee7f142bf51b5132913bf4cf2a859d35:
  original kernel equation, removable first row, \(Q_0\)
  real-norm bound, crossing full jets, and stable
  full-Hermite reconstruction including the odd simple node.

The fixed-row initialization, endpoint-strip estimates,
and limiting assembly are proved above. Only written
mathematics, source text and hashes were used. No mathematical
program, numerical experiment, test, or build was run.
Frozen notes and public manuscripts are unchanged.
