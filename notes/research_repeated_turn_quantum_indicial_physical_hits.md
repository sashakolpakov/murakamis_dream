# Exact quantum indicial phases and physical-row hits

Private written proof, 16 November 2026.

The raw ordered scalar equations have an exact quantum indicial
calculation at the old spectral infinity. Their finite \(q\)-shifts
matter: a transformed kernel and its terminal forcing have different
indicial phases. These shifts nevertheless do not exclude physical
rows. At primitive resonant phases the source-ordered candidates meet
infinitely many physical levels, at explicitly determined nearby rows.

This is a statement about indicial candidates of specified ordinary
difference expressions. It is not a proof that those candidates survive
the complete stacked source equations, divide their maximal minors, or
participate in the actual canonical source.

## 1. Original operators and the meaning of an indicial calculation

Use the ordinary full-step expressions for \(N\ge3\); all
infinite-residue assertions concern sufficiently large levels. Put
\[
 q=e^{\pi i/N},\quad c_0=q+q^{-1},\quad
 \eta=(-1)^{N-1},\quad \kappa=q^{(N-1)^2/2},\quad
 C=v+v^{-1},\quad Ef(v)=f(q^2v),\quad
 V_n=\kappa^nTR^{-n}T,\quad D_n=V_nCV_{-n}.
 \tag{1}
\]
The original full algebra is \(\mathcal A_N=\mathbb C[C]/(P_N)\),
where \(P_N(C)=2T_N(C/2)+2\). The full-step angular lift retains
values and first derivatives at every root of \((v^N+1)^2\).
No angular derivative is applied as a derivation of that quotient.

The ordinary rational difference expressions from the pinned interface
are
\[
 A(v)=-\frac{(qv-1)^4}{q(v^2-1)(q^2v^2-1)},\quad
 B(v)=A(v^{-1}),\quad r(v)=\frac8{C+c_0},
\]
\[
 J=r-AE-BE^{-1},\qquad
 D_1=r+q^{-1}A\,v^{-1}E+q^{-1}B\,vE^{-1}.
 \tag{2}
\]
All coefficients multiply on the left. The exact turn recurrence is
\[
 qD_{n+2}+q^{-1}D_n+D_{n+1}J=8I,\qquad D_0=C.
 \tag{3}
\]
It defines the same ordinary rational expressions for every signed
fixed \(n\). They descend to the full physical quotient; their ordinary
residuals are not set to zero away from physical rows.

In this note an indicial candidate with signed nonzero slope \(1/n\)
means the following substitution in a fixed finite difference expression:
\[
                    Ef/f\sim a\,v^{1/n},\qquad a\ne0 .
 \tag{4}
\]
For every integer \(\ell\), the consistently shifted quotient is then
\[
             E^\ell f/f\sim
              a^\ell q^{\ell(\ell-1)/n}v^{\ell/n}.
 \tag{5}
\]
This follows by finite multiplication for \(\ell>0\), by inversion
for \(\ell<0\), and holds trivially at zero. A branch for rational
powers of \(q\) is fixed near \(q=1\), and is specialized to
\(e^{\pi i/(nN)}\) at physical levels.

Equations (4)--(5) are a Newton-polygon balance, not an assertion
that a canonical physical polynomial has this asymptotic. In particular
an arbitrary formal branch need not obey the additional global physical
identity \(E^N=1\). It is legitimate to calculate its coefficient
equation first at generic \(q\) and then substitute physical \(q\).
All uses of “candidate” below have exactly this meaning.

## 2. Two exact coefficients at old infinity

Fix \(n\ne0\) and write \(m=|n|\). The shift range of \(D_n\) is contained in
\([-m,m]\), and its coefficient functions have at most a simple
pole at \(v=\infty\). These assertions follow inductively from
(2)--(3), also using (3) solved backward for negative \(n\).
Indeed \(J\) has coefficients bounded at infinity. Write
\[
 D_n=v\,\mathcal A_n(E)+\mathcal B_n(E)+O(v^{-1}),
 \tag{6}
\]
where the remainder is coefficientwise in this fixed shift range.
The exact two displayed Laurent polynomials are
\[
 \mathcal A_n(E)=(-1)^nq^{-2n}E^{-n},
 \tag{7}
\]
\[
 \mathcal B_n(E)=(-1)^nE^{-n}
       [q^{-2n}\mathcal R_n(q^2E)-\mathcal R_n(E)],
 \qquad
 \mathcal R_n(E)=
 -\frac{4(E-1)}{q-q^{-1}}\frac{1-(-E)^n}{1+E}.
 \tag{8}
\]
The quotient in (8) is a Laurent polynomial for every integer \(n\).
In particular
\[
 \begin{cases}
 \mathcal B_n\in\operatorname{span}\{E^{-1},\ldots,E^{-n}\},
       &n>0,\\
 \mathcal B_n\in\operatorname{span}\{E,\ldots,E^{|n|}\},
       &n<0.
 \end{cases}
 \tag{9}
\]

Here is a derivation retaining the full triangular phases. Put
\[
 p_j(C)=\prod_{a<j}(C-c_a),\quad
 c_a=q^{2a+1}+q^{-2a-1},\quad s_j=(q^j-q^{-j})/i.
\]
The monic Newton diagonal of \(V_n\) is
\(\lambda_n(j)=(-1)^{nj}q^{-nj(j+1)}\).
For \(j\ge1\) and \(U_+=V_1\), its next coefficient divided by this diagonal is
\(-q^js_j^3/s_1\). Taking any signed power of this upper triangular
matrix gives the finite geometric expression
\[
 \frac{[p_{j-1}]V_np_j}{\lambda_n(j)}
     =-\frac{q^js_j^3}{s_1}
                       \frac{1-(-q^{2j})^n}{1+q^{2j}}.
 \tag{10}
\]
The formula for negative powers follows from the same two-diagonal
multiplication law, or from its inverse; it is a Laurent identity.

Passing to ordinary monomials uses
\[
 [C^{j-1}]p_j=-\sum_{a<j}c_a,\qquad
 \sum_{a<j}c_a=\frac{q^{2j}-q^{-2j}}{q-q^{-1}}.
\]
With \(z=q^{2j}\), direct simplification gives
\[
       \frac{[C^{j-1}]V_n C^j}{\lambda_n(j)}
                                      =\mathcal R_n(z).
 \tag{11}
\]
For example the simplification in its numerator is
\[
 \frac{(z-1)^3}{z}-(z-z^{-1})(1+z)=-4(z-1).
\]
The identity \(D_nV_n=V_nC\) first gives the raising coefficient
\(\lambda_n(j+1)/\lambda_n(j)=(-1)^nq^{-2n(j+1)}\), proving (7).
Its next coefficient gives precisely (8).
Since \(C^j=v^j+O(v^{j-2})\), the next ordinary-monomial coefficient
is the constant-in-\(v\) coefficient in (6).

For \(n>0\), \(\mathcal R_n\) is a polynomial of degree at most \(n\);
its top terms cancel in the bracket in (8). This proves the first
part of (9). For \(n=-m<0\), \(\mathcal R_n\) has powers from
\(-m\) through zero; the lowest terms cancel in that bracket.
Multiplication by \(E^m\) proves the second part.
These calculations may be made for arbitrary fixed \(j\) at all
physical levels \(N>j+1\). Rational identities in \(q\) then follow
from the infinitely many such \(q\) accumulating at \(1\), after
clearing their fixed rational denominators. Thus no infinite
level-dependent triangular matrix is assumed. Since the fixed index
\(j\) is arbitrary, the Laurent polynomials in \(E\) agree at infinitely
many distinct \(E=q^{2j}\) over \(\mathbb C(q)\); this gives (7)--(8)
coefficientwise.

One more coefficient is needed. The coefficient of \(E^n\) in
\(D_n\), for either sign of \(n\), is
\[
                    (-1)^{|n|}v^{-1}+O(v^{-2}).
 \tag{12}
\]
For \(n>0\), this starts from \(q^{-1}A/v=-v^{-1}+O(v^{-2})\).
The highest forward shift in (3) multiplies the preceding one
by \(q^{-1}A\) at the shifted argument, whose limit is \(-1\).
For negative \(n\), (3) gives
\(D_{-1}=8q-q^2D_1-qCJ\). Its backward coefficient is \(qB/v\),
again \(-v^{-1}+O(v^{-2})\). Backward induction multiplies the
previous backward extreme by a shifted \(qB\), also tending to
\(-1\). This proves (12) with the original signed order.

## 3. The scalar indicial equation

Substitute (5) in \(D_n f\). The term (7) and the extreme (12)
are the only terms of order \(v^0f\). The constant-in-\(v\)
terms in (9) decay, because their shift sign is opposite to \(n\).
In the coefficientwise \(O(v^{-1})\) remainder, every other shift
decays since its order is strictly smaller than the \(E^n\) extreme;
the \(O(v^{-2})\) part decays even at that extreme.

Consequently the exact indicial equation for \(D_n-\lambda\) is
\[
 \boxed{\quad
 (-1)^n\bigl(q^{n-1}a^n+q^{1-n}a^{-n}\bigr)=\lambda.
 \quad}
 \tag{13}
\]
Both signs use the same formula. The backward shift in (5) is
essential for its powers of \(q\).

For \(\lambda=2\), all candidates are
\[
                  a=-q^{-1+1/n}\omega,\qquad \omega^{|n|}=1,
 \tag{14}
\]
with a double indicial root. For \(\lambda=c_0=q+q^{-1}\), they are
\[
       a=-q^{-1+2e/n}\omega,\qquad
              e\in\{0,1\},\quad\omega^{|n|}=1.
 \tag{15}
\]
This is the factorization \(b+b^{-1}=q+q^{-1}\), with
\(b=(-1)^nq^{n-1}a^n\).
The two branches in (15) are distinct for sufficiently large
physical levels and fixed \(n\), although their classical limits
coalesce. This is not a diagonalization of the original normal
channel. For instance the actual \(H_n\) still satisfies
\((D_n-c_0)H_n=G_n\), rather than a homogeneous scalar equation.

## 4. The ordered single-kernel source changes the phase

For an arbitrary ordinary endpoint parameter \(w\), the original
full quotient identity is
\[
 (w-J)V_nK_N(w,\cdot)
      =\frac{\eta\kappa^nP_N(w)}{N^2}G_n,\qquad
                  (D_n-c_0)G_n=0.
 \tag{16}
\]
Thus its ordered homogeneous consequence is
\[
              (D_n-c_0)(w-J)V_nK_N(w,\cdot)=0.
 \tag{17}
\]
The forcing (16) is retained; (17) does not replace it or its
endpoint/normal constraints. Both equations are full-quotient identities:
their ordinary residuals have the original polynomial factor \(P_N\),
and hence both values and first angular derivatives vanish at every
double physical row. This does not create an off-grid homogeneous
equation for the canonical source.

On a candidate (4), \(Jf\) has an extra nonzero leading factor
proportional to \(v^{1/|n|}\). This follows from
\(J=qE+q^{-1}E^{-1}+O(v^{-1})\): use \(E\) for \(n>0\), and
\(E^{-1}\) for \(n<0\). The \(O(v^{-1})\) coefficients cannot
cancel that leading term. The fixed scalar \(w\) is lower order.
Hence, for \(g=(w-J)f\),
\[
                Eg/g\sim q^{2/|n|}a\,v^{1/n}.
\]
The active indicial candidates of the ordered equation (17) are
therefore
\[
 a=-q^{-1+2e/n-2/|n|}\omega,\qquad
                e\in\{0,1\},\quad\omega^{|n|}=1.
 \tag{18}
\]
Solutions from the separate factor \(w-J\), and all original
source constraints, remain. In particular (18) does not assert
that the actual canonical kernel has any selected candidate.

For endpoint products with more than one factor before \(V_n\),
the exact mixed forcing remains. Equation (17) cannot be substituted
for their full module. None of its nonunit clearings or source
channels is removed by this calculation.

## 5. Products and the inverse outer turn

Take \(r\ge1\) active signed powers \(n_i\ne0\), and suppose
\[
 \gamma=\sum_i1/n_i=\epsilon\in\{1,-1\},\qquad
                    \tau=-\epsilon,\quad
 L=\operatorname{lcm}_i|n_i|.
 \tag{19}
\]
The actual outer state map \(U_\tau\) uses the inverse pullback:
the new multiplication coordinate is \(D_\epsilon\) in the old
variables, because \(U_\tau D_{-\tau}=CU_\tau\).
Products of candidates multiply their shift ratios exactly, so
their total ratio is \(a v^\epsilon\).

From (13) at \(n=\epsilon\), the finite new spectral coordinate is
\[
 C_{\rm new}=-(q^{1-\epsilon}a+q^{\epsilon-1}a^{-1}).
\]
Thus its two angular lifts are
\[
                   v_{\rm new}=-q^{1-\epsilon}a
                          \quad\hbox{and its reciprocal}.
 \tag{20}
\]
This is the indicial consequence of the ordered inverse pullback,
not a change of sign convention for the outer operator.

For the pure scalar candidates (14), equation (20) gives
\[
 v_{\rm new}=(-1)^{r+1}q^{1-r}\prod_i\omega_i.
 \tag{21}
\]
For the actual single-kernel ordered candidates (18), it gives
\[
 v_{\rm new}=\zeta q^\beta,\qquad
 \zeta=(-1)^{r+1}\prod_i\omega_i,\qquad
 \beta=1-r-\epsilon+
                   2\sum_i\frac{e_i}{n_i}
                    -2\sum_i\frac1{|n_i|}.
 \tag{22}
\]
The reciprocal lift remains part of both formulas.

The product of the root groups \(\mu_{|n_i|}\) surjects onto
\(\mu_L\): the integers \(L/|n_i|\) have gcd one.
Furthermore \(L(r-1)\) is even. Indeed the integral vector
\(a_i=L/n_i\) is null for
\(\operatorname{diag}(n_i)-\epsilon\mathbf1\mathbf1^{\mathsf T}\);
reducing its quadratic value modulo two gives
\(\sum_i(n_i-\epsilon)a_i=L(r-1)\equiv0\pmod2\).
If \(L\) is odd, this forces \(r\) odd. If \(L\) is even,
\(-1\in\mu_L\). Therefore the phase set of \(\zeta\) in both
(21) and (22) is exactly \(\mu_L\), for each choice of the \(e_i\).

## 6. Nearby rows and exact infinite-residue hits

Write a phase as \(\zeta=e^{2\pi ik/L}\), and suppose \(L\beta\)
is an integer. The lift \(\zeta q^\beta\) is a physical angular
node exactly when an integer \(j\) satisfies
\[
 2j+1=2Nk/L+\beta\pmod{2N}.
\]
Equivalently,
\[
                  2Nk\equiv L(1-\beta)\pmod{2L}.
 \tag{23}
\]
Thus some infinite residue class of physical levels has such a hit
if and only if
\[
                  2\gcd(k,L)\ \hbox{divides}\ L(1-\beta).
 \tag{24}
\]
The equivalence is the elementary solvability criterion for a
linear integer congruence, obtained by dividing by the gcd and
using Bezout's identity.

For \(0<k/L<1/2\), these are actual distinct bulk rows for all
large levels in the resulting residue class. Their index is
\(Nk/L+(\beta-1)/2\), modulo the full period; hence they remain
a bounded number of rows from \(\lfloor Nk/L\rfloor\).
A coefficient window must include such fixed translations when
testing them. Comparing \(\beta\) only with the center exponent
\(\delta\in(-1,1]\) is invalid: neighboring rows have exponent
\(\delta+2s\).

For the ordered source candidates (22),
\[
 L(1-\beta)=L(r+\epsilon)
           -2\sum_i e_iL/n_i+2\sum_i L/|n_i|
 \tag{25}
\]
is even. Here \(L(r+\epsilon)\) is even by \(L(r-1)\) even
and \(\epsilon+1\) even. Consequently every primitive phase,
\(\gcd(k,L)=1\), satisfies (24), for every choice of the \(e_i\).
If \(L\ge3\), choosing \(k=1\) gives an interior phase and infinitely
many physical bulk hits. The reciprocal lift gives the equivalent
reflected physical nodes; it is not an omitted branch.

This contrasts with the special pure-recovery formula (21),
where the test is \(2\gcd(k,L)\mid Lr\). It can fail, for example
at every primitive phase when \(L\) and \(r\) are odd.
That distinction is a reason to retain the ordered terminal source,
not permission to replace a whole module by either scalar model.

## 7. What still has to be shown

The quantum shift does not by itself prove avoidance of the physical
grid. Equations (22)--(25) give a general indicial family for which
it instead changes the hit's residue class and finite row offset.

Conversely a hit of one of these candidates does not imply rank loss
of the complete finite-window system. The exact forcing in (16),
its normal rows, recovery equations, all finite old-color clearing
components, and the actual supplied packets remain. A raw indicial
factor may be redundant or removed by those simultaneous constraints.
No nonunit is canceled here. At special endpoint parameters
\(P_N(w)=0\), even the displayed forcing changes, so a candidate
cannot be assigned an actual source coefficient by this argument.

The maximal-minor question is therefore still the one for the exact
stacked rows. The formulas above supply candidate quantum locations
against which to test those rows; they neither establish a common
physical binomial divisor nor exclude one. No conditioning, global
source-rate, or geometric-cycle conclusion is asserted.

## 8. Direct sources

Complete direct texts were read at these unchanged pins, with used
implications checked:

* [Exact finite-band turn and branching operators](research_unit_turn_finite_band_branching_operator.md),
  SHA256 31d9f574c7dc3aaac07e4eb50c131b3328be46b3c2a2ef46f9dae7f0c4ddb9cb:
  triangular phases, signed recurrence, ordered kernel forcing,
  and actual terminal normal companion.
* [Full-step repeated-turn interface](research_full_step_repeated_turn_tensor_interface.md),
  SHA256 ef851eab40c8b2c44388a41d324e2fa41d4400f0f2118fe587405911e00e3398:
  ordinary rational expressions, source-safe quotient descent,
  and inverse outer transport.
* [Physical-window conditioning](research_resonant_physical_window_conditioning.md),
  SHA256 f1af212ec05ffdb79cc9b99ce03961622740d58622213e648918000e81e5fa07:
  exact rational trajectories, fixed translated windows,
  first-normal packet data and supplied-boundary scope.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test or build was run.
Adopted notes and public manuscripts are unchanged.

