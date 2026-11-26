# A local forced system for an arbitrary original rational word

Research note, 3 November 2026.

Every fixed rational word has an exact local system with a fixed
number of channel fields on a triangular two-color grid. Its boundary
forcing is the original input, each turn is the original coefficient
reversal, and its output is the entire Newton coefficient vector.
The construction works with arbitrarily many fixed turns.

There is a reason to retain the second color: already one original
crossing has middle-cut rank \(\lfloor N/2\rfloor\). Therefore no
fixed-size causal streaming system can realize its action on an
arbitrary input vector. This does not rule out a fixed-size equation
for a restricted family of prepared word states. A generating-function
calculation below gives exact transport identities for that latter
problem, including the endpoint term lost by formal division by the
nilpotent variable.

## 1. The original word and its local channel equations

Fix \(N\ge2\), \(D=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), and
\(\kappa=q^{D^2/2}\). Let \(M\) and \(J\) be the original crossing
and turn matrices in the Newton basis. A word may be written
\[
 W=J^{\varepsilon_{\rm out}}M^{p_s}J M^{p_{s-1}}
                  \cdots J M^{p_1}J^{\varepsilon_{\rm in}},
 \quad p_r\ne0,\quad \varepsilon_{\rm in},\varepsilon_{\rm out}\in\{0,1\}.
 \tag{1}
\]
Adjacent powers can be combined and adjacent turns cancel by
\(J^2=I\), so this includes every word, apart from the identity
and a lone turn, which are immediate. The number of runs and
their signed powers are fixed; no bound on that number is assumed.

For one run \(p\), put \(\sigma=\operatorname{sgn}p\),
\(k=\lceil |p|/2\rceil\), \(q_\sigma=q^\sigma\), \(Q_\sigma=Q^\sigma\).
Let \(T_k\) denote path adjacency and define
\[
 \begin{split}
 C_k(r)&=(r+r^{-1})I_k-T_k-rE_{11},\\
 r_j&=q_\sigma Q_\sigma^j,\qquad
 H_{j,\ell}=C_k(r_j)-q_\sigma^{-1}Q_\sigma^{-\ell}E_{kk},\\
 D_j^{(p)}&=
 \begin{cases}
 (1-Q_\sigma^j)(1-Q_\sigma^{-j})I_k,&p\text{ even},\\
 \operatorname{diag}(1-Q_\sigma^{-j},
 (1-Q_\sigma^j)(1-Q_\sigma^{-j}),\ldots),&p\text{ odd}.
 \end{cases}
 \end{split}                                                     \tag{2}
\]
The odd diagonal has just its first entry if \(k=1\).
For \(0\le\ell\le D\), retain the original diagonal crossing unit
and the resonant vector
\[
 \mu_\ell=\kappa(-1)^\ell q^{\ell(\ell+1)},\qquad
 (v_\ell)_a=r_\ell^{\,k-a}\quad(1\le a\le k).
 \tag{3}
\]

Given an arbitrary input \(h=(h_0,\ldots,h_D)^T\), introduce one
\(k\)-component field \(u_{j,\ell}\) on \(0\le\ell\le j\le D\).
Its boundary forcing and local equations are
\[
 \boxed{\begin{aligned}
 u_{\ell,\ell}&=\mu_\ell^p v_\ell h_\ell,\\
 H_{j,\ell}u_{j,\ell}&=D_j^{(p)}u_{j-1,\ell},
                                  &&\ell<j\le D.
 \end{aligned}}                                                  \tag{4}
\]
No equation at the singular diagonal \(j=\ell\) replaces the
first line of (4). The input amplitude there is prescribed.
Use a scalar accumulator on each row:
\[
 a_{j,-1}=0,\qquad
 a_{j,\ell}=a_{j,\ell-1}+e_k^Tu_{j,\ell}\quad(0\le\ell\le j),
 \qquad g_j=a_{j,j}.
 \tag{5}
\]

**Theorem 1.** The local system (4)--(5) has a unique solution,
and its output is exactly \(g=M^p h\). Applying it to the runs
in (1), with
\[
 h^{(1)}=J^{\varepsilon_{\rm in}}h,\qquad
 h^{(r)}_\ell=g^{(r-1)}_{D-\ell}\quad(r>1),
 \tag{6}
\]
and final reversal \(J^{\varepsilon_{\rm out}}\), gives exactly
\(Wh\). It retains all Newton coefficients, both level parities,
all signs of the powers, and arbitrary free input coefficients.

*Proof.* Directly from the channel determinant,
\[
 \det H_{j,\ell}
       =r_j^{-k}(1-Q_\sigma^{j-\ell}).
 \tag{7}
\]
It is nonzero whenever \(0<j-\ell<N\). Thus, after the diagonal
forcing has been set, every column has a unique forward solution.
The independently proved full-column formula in
[the resonant source theorem](research_resonant_crossing_run_source.md),
Theorem 1, says precisely that this solution obeys
\[
                e_k^Tu_{j,\ell}=(M^p)_{j\ell}h_\ell .
 \tag{8}
\]
Its phase is \(\mu_\ell^p\), not an unspecified kernel
normalization. For negative \(p\) the channel coefficients in
(2)--(3) are conjugated, but the arbitrary input \(h_\ell\) is
not conjugated. This is the actual complex-linear operator \(M^p\).
Equations (5) and (8) prove \(g=M^ph\). Equation (6) is exactly
the original turn \(J e_\ell=e_{D-\ell}\); induction over the
runs proves the statement for \(W\). \(\square\)

For each fixed run the system has only \(k+1\) channel fields.
There are \(N(N+1)/2\) grid positions per run, and only adjacent
output-color equations, tridiagonal channel equations, and adjacent
input-color accumulator equations. The original turns join the
boundary rows by the explicit reversal (6). This is a local
two-color system, not a one-color system with a hidden growing
number of channels.

The coefficients of \(H_{j,\ell}\), \(D_j^{(p)}\), \(v_\ell\),
and \(\mu_\ell^p\) are uniformly bounded at the physical colors
for each fixed run. Their inverses need not be: (7) can be small.
No inverse estimate or cancellation estimate follows from the
bounded local coefficients.

For \(h=e_0\), the last output coefficient is the original
closure \(\phi_N(F_W)\). Keeping the output coefficients instead
gives \(F_W(z)=\sum_j(Wh)_j e_j(z)\). Inputs may themselves have
polynomial free variables. The theorem then holds coefficientwise,
and therefore retains every first normal at a repeated root and
every mixed derivative of free boundary variables.

## 2. Why arbitrary inputs cannot use fixed causal memory

**Theorem 2.** The original one-crossing matrix \(M_N\) has a
middle-cut submatrix of rank \(\lfloor N/2\rfloor\). Consequently
any exact causal linear state-space realization of its action on
arbitrary inputs, in the original increasing color order, requires
at least \(\lfloor N/2\rfloor\) internal states.

*Proof.* Write \(F_j=(Q;Q)_j=\prod_{r=1}^j(1-Q^r)\), with
\(F_0=1\). The original matrix formula is equivalently
\[
       M_{kj}=\kappa(-q)^kq^{j^2}
                    {k\brack j}_Q,\qquad j\le k<N.
 \tag{9}
\]
Indeed \(S_j=i^jq^{-j(j+1)/2}F_j\); substitution in the original
sine-factorial formula gives (9).
For each \(j<N\),
\[
 {k\brack j}_Q
     =\frac{\prod_{h=0}^{j-1}(1-Q^{k-h})}{F_j}
     =p_j(Q^k),
 \qquad
 \operatorname{lc}(p_j)=
       \frac{(-1)^jQ^{-j(j-1)/2}}{F_j}\ne0.
 \tag{10}
\]
Thus the \(j\)-th column is a degree-\(j\) polynomial in \(Q^k\).
Let \(r=\lfloor N/2\rfloor\), take columns \(0,\ldots,r-1\),
and rows \(r,\ldots,2r-1\). Their determinant, after the
nonzero row and column factors in (9), is
\[
    \left(\prod_{j=0}^{r-1}\operatorname{lc}(p_j)\right)
       \prod_{0\le i<h<r}(Q^{r+h}-Q^{r+i})\ne0.
 \tag{11}
\]
All displayed powers of \(Q\) are distinct and all factorials
have index less than \(N\).

Now suppose a causal realization has an internal state of
dimension \(d\). Feed it an arbitrary vector supported in input
colors \(0,\ldots,r-1\), and set every later input to zero.
Every later output factors linearly through the state just
after the cut at color \(r-1\). Hence the submatrix mapping those
inputs to output colors \(r,\ldots,2r-1\) has rank at most \(d\).
Equation (11) forces \(d\ge r\). The same assertion holds for
\(M^{-1}=\overline M\). \(\square\)

The claim concerns arbitrary free input vectors and a causal
one-pass realization in that color order. It does not rule out
a fixed-dimensional recurrence for a fixed prepared column, a
two-sided boundary problem, a multi-color system such as
(4)--(6), or source-specific holonomic elimination. In particular
it is consistent with the existing fixed-channel two-run theorem.
It does rule out summing the arbitrary input color in (4) while
silently assuming its \(Q_\sigma^{-\ell}\) dependence closes in
a fixed number of causal states.

## 3. Exact generating functions with their endpoint current

There is a complementary scalar representation useful for
source-specific elimination. Work on
\(\mathcal R_N=\mathbb C[t]/(t^N)\), identified with coefficient
vectors in the ordered basis \(1,t,\ldots,t^D\). Rescale original
Newton coefficients by the invertible diagonal \(F_j\):
\[
       H(t)=\sum_{j=0}^{D}\frac{h_j}{F_j}t^j .
 \tag{12}
\]
Define the nilpotent multiplication \(t\), the invertible
q-dilation \(T\), and the q-derivative \(\delta\) by
\[
 Tt^j=Q^jt^j,\qquad
 \delta t^j=(1-Q^j)t^{j-1},\qquad \delta1=0.
 \tag{13}
\]
They satisfy the exact finite relations
\[
 Tt=QtT,\qquad
 \delta t-Q t\delta=(1-Q)I,\qquad
 T=I-t\delta,\qquad t^N=\delta^N=0.
 \tag{14}
\]
There is no inverse of \(t\).

Let \(\mathcal E\) be multiplication by the polynomial
\[
 E_-(t)=\sum_{j=0}^{D}\frac{(-qt)^j}{F_j},
 \qquad
 \Gamma t^j=\nu_jt^j,\quad
 \nu_j=(-1)^jq^{j(j+1)}.
 \tag{15}
\]
Multiplication by \(E_-\) is a unit in \(\mathcal R_N\).
The original positive crossing and turn, in the rescaled basis,
are exactly
\[
 \boxed{\quad
       \widehat M=\kappa\mathcal E\Gamma,\qquad
       (\widehat JH)_j
          =\frac{N\nu_j}{F_j^2}\,H_{D-j}.
 \quad}                                                         \tag{16}
\]
Here \(H_j\) means the coefficient of \(t^j\). Formula (9)
proves the first identity by convolution. For the second, use
\[
                  F_{D-j}=\frac{N\nu_j}{F_j}.             \tag{17}
\]
Thus these are original operators, including their scalar
phases and both ends. Negative crossings are their literal
inverses.

The finite polynomial identity before truncation is
\[
 E_-(Qt)=(1+qt)E_-(t)-\frac{(-1)^N}{N}t^N.
 \tag{18}
\]
It gives the familiar dilation relation modulo \(t^N\). But
division of the discarded term by \(t\) restores an endpoint
current. Put \(\epsilon=(-1)^N\) and
\(R_\partial=t^D=e_De_0^T\). Then the exact operator identities are
\[
 \boxed{\begin{aligned}
 \delta\mathcal E
    &=(1+qt)\mathcal E\delta-q\mathcal E
                             +\frac{\epsilon}{N}R_\partial,\\
 \mathcal E\delta\mathcal E^{-1}
    &=(1+qt)^{-1}
             \left(\delta+qI-\frac{\epsilon}{N}R_\partial\right).
 \end{aligned}}                                                  \tag{19}
\]

To prove the first line, apply the finite q-Leibniz identity
\(\delta f(t)=f(Qt)\delta+(f(t)-f(Qt))/t\) to the polynomial
in (15). The quotient is a polynomial, not an operator inverse
of \(t\). Equation (18) makes that polynomial
\(-qE_-(t)+\epsilon t^D/N\).
For the second line, solve for \(\mathcal E\delta\mathcal E^{-1}\)
and use \(R_\partial\mathcal E^{-1}=R_\partial\), since the
constant coefficient of \(E_-^{-1}\) is one. This proves (19).
Its last term cannot be removed by working only with the
interior coefficient recurrence.

For example the original first-crossing state has
\(H=\kappa E_-\), and hence the literal forced equation
\[
        (\delta+qI)H=\frac{\kappa\epsilon}{N}t^D,
                     \qquad H(0)=\kappa .
 \tag{20}
\]
The operator \(\delta+qI\) is invertible, so its endpoint-forced
solution is unique. The last coefficient equation, not a
homogeneous periodic extension, fixes its normalization.

## 4. What the scalar transport preserves

Conjugation by the original rescaled crossing gives
\[
 \begin{split}
 \widehat M T\widehat M^{-1}&=(1+qt)^{-1}T,\\
 \widehat M t\widehat M^{-1}&=-Q t(1+qt)^{-1}T,\\
 \Gamma\delta\Gamma^{-1}&=-\delta T^{-1}.
 \end{split}                                                     \tag{21}
\]
The first line follows from (18) in the truncated ring, and
the second from \(\Gamma t\Gamma^{-1}=-QtT\). Every inverse
\((1+qt)^{-1}\) is a genuine unit on \(\mathcal R_N\).
Together with (19), these give exact conjugation of any supplied
finite operator expression in \(t,T,\delta\), retaining its
endpoint term. In particular an annihilating or forced equation
can be transported under this crossing without changing the
underlying original state.

The turn has the exact identities
\[
 \widehat J T\widehat J=Q^{-1}T^{-1},\qquad
 \widehat J t\widehat J=-\delta T^{-1}(I-T).
 \tag{22}
\]
For completeness its action on \(\delta\) is
\[
 \boxed{\quad
 \widehat J\delta\widehat J
       =t\,(I-QT+P_D)^{-1},\qquad P_D=e_De_D^T.
 \quad}                                                         \tag{23}
\]
In the right side's diagonal inverse, the entries before the
last are \(1-Q^{j+1}\ne0\), while the last is one. Multiplication
by \(t\) kills that last input. Thus (23) has lower entry
\((1-Q^i)^{-1}\) in row \(i\ge1\), exactly the ratio from (16).
Dropping \(P_D\) would introduce a nonexistent inverse.
Equations (22)--(23) follow directly from
\[
 \frac{N\nu_i/F_i^2}{N\nu_{i-1}/F_{i-1}^2}
                    =-\frac{Q^i}{(1-Q^i)^2}.
 \tag{24}
\]

These identities are a source-specific starting point for
holonomic elimination. They do not prove that every transformed
endpoint projector remains local after further turns and
crossings, or that the final unpolarized source is fixed by a
homogeneous annihilator alone. Conjugating a rank-one endpoint
operator also transports its marked column and row. Those data
must remain; replacing them by zero or an arbitrary normalization
changes the original source.

The two-color construction (4)--(6) is already complete and
unconditional for arbitrary words. A bounded one-clock forced
system for every prepared word, with all these marked currents
controlled, is a further claim not established here. Neither
construction proves a geometric asymptotic or a general
finite-exception theorem.

## 5. Reproduction

The [original-matrix diagnostic](../experiments/check_rational_word_local_source_system.py)
propagates every free input column through the local forced
system, including words with four internal turns and both
optional outside turns. It compares the resulting whole matrices
with the literal products of the original crossing and turn
matrices. It also checks the q-exponential endpoint current,
the pinned turn derivative, and the explicit Vandermonde minor.
Its [saved record](../repro/results/research-rational-word-local-source-system.json)
contains 72 word cases and 3,072 coefficient entries at
\(N=2,\ldots,10\), together with nine levels of finite operator
checks. At 110 decimal digits the largest relative residual was
\(2.8808593383904\cdot10^{-109}\).

To reproduce:

    python experiments/check_rational_word_local_source_system.py \
      --precision 110 \
      --output repro/results/research-rational-word-local-source-system.json

This checks source normalization and implementation. The exact
arbitrary-word and cut-rank assertions are proved above, and no
large-level asymptotic is inferred from the diagnostic.
