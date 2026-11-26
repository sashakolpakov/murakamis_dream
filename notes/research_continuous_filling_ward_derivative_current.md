# Filling derivatives restore a value current in the original Ward identity

Private written proof, 15 November 2026.

The original integer full-twist Ward identity has a purely normal
endpoint source, which becomes a scalar after the prescribed turn.
Its canonical continuous-power extension has an additional value
source. That source vanishes at every integer power but has a nonzero
first derivative there. It is detected by the original closing.

This proves that the integer Ward deletion cannot be differentiated
as a closed scalar filling equation. It does not prove that the ideal
of all geometric asymptotic coefficients fails derivative stability
by some other, source-specific mechanism.

## 1. The prescribed continuous full-Hermite extension

Fix \(N\ge2\), \(d=N-1\), and
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad \rho=q-q^{-1},\quad
 \hbar=\frac{2\pi i}{N},\quad
 \kappa=q^{d^2/2},\quad
 \log\kappa=\frac{\pi i d^2}{2N}.
 \tag{1}
\]
All complex powers use these displayed logarithms. Let
\[
 P_N(z)=2\mathrm T_N(z/2)+2,\qquad
 \mathcal A_N=\mathbb C[z]/P_N(z),
 \tag{2}
\]
where \(\mathrm T_N\) is the first-kind Chebyshev polynomial.
The actual positive crossing is \(R=\kappa r_N(\Omega)\).
The [original Gaussian functional calculus](actual_coherent_filling_gaussian_chirp.md),
§1, specifies
\[
 K(z)=\operatorname{arccosh}(-z/2)^2
 \tag{3}
\]
on the branch holomorphic on \(\mathbb C\setminus[2,\infty)\),
including its removable value at \(z=-2\).
For arbitrary \(P\in\mathbb C\), define \(f_P\in\mathcal A_N\) to
be the full Hermite representative of
\[
 F_P(z)=\kappa^{-P}\exp\!\left(\frac{P K(z)}{\hbar}\right).
 \tag{4}
\]
This is entire in \(P\), coefficientwise at each fixed \(N\).
For integer \(P\) it is the actual normalized full twist:
\[
                         R^{2P}=\kappa^{2P}f_P(\Omega).
 \tag{5}
\]
The definition is the specified Gaussian lift of the original power,
not an assertion that a noninteger power is a physical tangle.

Let \(c_j=2\cos((2j+1)\pi/N)\).
The reflected node \(c_0=c_d\) is double at every level, including
\(N=2\). Denote by \(\Pi_0\) its full spectral idempotent: its value
is one and its first derivative is zero at \(c_0\), and all its other
physical values and required first derivatives are zero.
Let \(\Xi_0\) have value zero at every physical node, first derivative
one at \(c_0\), and first derivative zero at every other double node.
At an odd level the node \(-2\) is simple, so only its value is specified.
These data uniquely determine both elements of \(\mathcal A_N\).

Keep the spectral shift distinct from the genuine physical turn:
\[
 (\mathcal T f)(w+w^{-1})
  =f(Qw+Q^{-1}w^{-1})+f(Q^{-1}w+Qw^{-1}).
 \tag{6}
\]
Here \(f\) is its canonical polynomial of degree less than \(N\)
before shifting. The right side is a symmetric Laurent polynomial.
Its class in \(\mathcal A_N\) defines \(\mathcal T f\); this linear
operation is not asserted to preserve products of quotient classes.

Finally put
\[
 C_P(z)=2\cosh(2P\sqrt{K(z)}),\qquad e(P)=e^{2\pi iP}.
 \tag{7}
\]
The expression for \(C_P\) is single-valued: the even power series
for the hyperbolic cosine defines it directly as a function of \(K\).
Its values and normals, and products involving it, are taken in the
full algebra \(\mathcal A_N\).

## 2. Continuous Ward identity at every physical value and normal

**Theorem 1.** For every complex \(P\) and every \(N\ge2\),
\[
 \boxed{\quad
 E_P:=\mathcal T f_P-Q^P C_P f_P
   =(1-e(P))\Pi_0+
       \frac{P\{d+(N+1)e(P)\}}{\rho}\,\Xi_0 .
 \quad}                                                        \tag{8}
\]

**Proof.** Retain the unwrapped node logarithms
\[
 x_j=\frac{(2j+1)\pi i}{N},\qquad 0\le j<N,
 \qquad
 G_P(x)=\kappa^{-P}
          \exp\!\left(\frac{P(x-\pi i)^2}{\hbar}\right).
 \tag{9}
\]
The branch (3) gives \(K(c_j)=(x_j-\pi i)^2\).
Thus \(g_P(x)=f_P(e^x+e^{-x})\) has exactly the value and
logarithmic first derivative of \(G_P\) at every double node:
\[
 g_P(x_j)=G_P(x_j),\qquad
 g'_P(x_j)=G'_P(x_j)
            =-P(d-2j)G_P(x_j).
 \tag{10}
\]
At the odd simple node \(x_j=\pi i\), the value agrees and both
logarithmic first derivatives are zero. This zero is the chain-rule
value there, not an additional Casimir-normal condition.

Direct translation of the Gaussian gives
\[
 G_P(x+\hbar)+G_P(x-\hbar)
   =Q^P\,2\cosh(2P(x-\pi i))G_P(x).
 \tag{11}
\]
For \(1\le j\le d-1\), both shifted nodes remain in the specified
window. Equations (10)--(11) therefore make the value of \(E_P\)
zero there, and make its Casimir derivative zero at every such
double node. The value at the odd simple node is covered by the
same comparison.

At \(x_0=\pi i/N\), the backward shift leaves the window.
The canonical Laurent polynomial \(g_P\) is \(2\pi i\)-periodic,
so its value and derivative at \(x_0-\hbar=-\pi i/N\) are those
at \(x_d\). The exact endpoint data are
\[
\begin{array}{c|cc}
 &\text{value}&\partial_x\text{ value}\\ \hline
 g_P(x_0-\hbar)&1&Pd\\
 G_P(x_0-\hbar)&e(P)&-P(N+1)e(P).
\end{array}                                                     \tag{12}
\]
Indeed \(G_P(x_d)=G_P(x_0)=1\), with the logarithm of \(\kappa\)
in (1), while
\[
 \frac{(x_0-\hbar-\pi i)^2-(x_0-\pi i)^2}{\hbar}=2\pi i .
 \tag{13}
\]
The forward shift at \(x_0\) is still inside the window.
Consequently the value defect is \(1-e(P)\), and its logarithmic
derivative defect is \(P\{d+(N+1)e(P)\}\).
Since \(d(e^x+e^{-x})/dx=\rho\) at \(x_0\), division by \(\rho\)
gives the Casimir derivative in (8).

Reflection \(x\mapsto2\pi i-x\) fixes the centered Gaussian and the
canonical polynomial. At \(x_d\) it reverses both the derivative
defect and \(d(e^x+e^{-x})/dx\). Thus the same Casimir derivative
is obtained at the paired endpoint, without duplicating a condition.
For \(N=2\) there are only these two representatives of one double
node, so this endpoint calculation is already the complete proof.
For all other levels the interior comparisons give all remaining
data. Full Hermite uniqueness proves (8). \(\square\)

For integer \(m\), \(e(m)=1\) and
\(C_m(z)=2\mathrm T_{2m}(z/2)\), with the usual equality for
negative integer indices. Equation (8) reduces to the existing
even-power identity \(E_m=(2mN/\rho)\Xi_0\).
More generally, at \(P=n/2\) with \(n\in\mathbb Z\),
\[
 e(P)=(-1)^n,\qquad
 C_P(z)=(-1)^n2\mathrm T_n(z/2).
 \tag{14}
\]
Thus (8) also recovers the value defect for odd crossing powers
in the [signed Ward theorem](research_signed_gaussian_ward_endpoint_packet.md).
No odd-level simple node or odd-power endpoint has been suppressed.

## 3. The filling derivative contains a new value coupon

All terms of (8) are entire in \(P\), so ordinary differentiation
is legitimate. At any integer \(m\),
\[
 \boxed{\quad
 \left.\partial_P E_P\right|_{P=m}
  =-2\pi i\,\Pi_0+
        \frac{2N+2\pi i\,m(N+1)}{\rho}\,\Xi_0 .
 \quad}                                                        \tag{15}
\]
The derivative of the integer-only right side
\((2PN/\rho)\Xi_0\) would miss both the value term and the last
normal term in (15).

For clarity, this derivative does differentiate the actual Gaussian
lift. In the full algebra,
\[
 \partial_P f_P
      =\left(\frac{K}{\hbar}-\log\kappa\right)f_P,\qquad
 \partial_PC_P=4\sqrt K\,\sinh(2P\sqrt K),
 \tag{16}
\]
and the differentiated left side is
\[
 \mathcal T(\partial_Pf_P)
 -Q^P\!\left[
    (\hbar C_P+\partial_PC_P)f_P+C_P\partial_Pf_P
       \right].
 \tag{17}
\]
The entire expression in (16) involving \(\sqrt K\) is again
single-valued by its even power series. Canonical reduction is
performed before applying \(\mathcal T\).
These are filling-power derivatives with \(N\) fixed, not
quantum-parameter, index, or main-meridian derivatives.

## 4. The original half twist, turn, and exterior

Let \(\mathscr R\) be the genuine physical turn. Keep a fixed
half-twist marking \(\epsilon\in\{-1,0,1\}\).
The original endpoint formulas give
\[
 \mathscr R(\Xi_0)=(-1)^N\rho^2 I,\qquad
 R^\epsilon\Xi_0=\kappa^\epsilon\Xi_0,\qquad
 R^\epsilon\Pi_0
   =\kappa^\epsilon
        \left(\Pi_0-\frac{\epsilon d}{2\rho}\Xi_0\right).
 \tag{18}
\]
For the last equality use
\(R'(c_0)/R(c_0)=-d/(2\rho)\) on the double channel;
its two-term local algebra makes this exact for negative powers too.
The first equality is the normalized original cup-cap identity,
not a scalar substitute for the spectral idempotent.

Applying (18) to (8) gives the source identity
\[
\boxed{\begin{split}
 \mathscr R(R^\epsilon E_P)
   =\kappa^\epsilon\bigg[
      &(1-e(P))\,\mathscr R(\Pi_0)\\
      &+(-1)^N\rho
       \left(P\{d+(N+1)e(P)\}
                 -\frac{\epsilon d}{2}(1-e(P))\right)I
                      \bigg].
\end{split}}                                                   \tag{19}
\]
At an integer \(m\) this is the existing scalar deletion
\[
          \mathscr R(R^\epsilon E_m)
                =2mN(-1)^N\rho\,\kappa^\epsilon I.
 \tag{20}
\]
Its true filling derivative is instead
\[
\boxed{\begin{split}
 \left.\partial_P\mathscr R(R^\epsilon E_P)\right|_{P=m}
   =\kappa^\epsilon\big[
       &-2\pi i\,\mathscr R(\Pi_0)\\
       &+(-1)^N\rho
           \{2N+2\pi i\,m(N+1)+\epsilon\pi i d\}I
                              \big].
\end{split}}                                                   \tag{21}
\]

Every equation is an equality of actual boundary coupons before
the exterior contraction. An arbitrary fixed exterior functional
\(\Lambda_N\), with its original marked closing, therefore gives
the two retained observations
\(\Lambda_N(\mathscr R\Pi_0)\) and \(\Lambda_N(I)\) in (19)--(21).
No physical turn has been moved through that exterior.

The actual filling convention is \(P=-p\), so the crossing power is
\(\epsilon-2p\). Its full crossing normalization multiplies the
displayed Ward coupon by \(\kappa^{2P}\), because of (5).
When differentiated at an integer, this factor contributes only
an additional scalar multiple of \(I\) from (20).
The coefficient of \(\mathscr R(\Pi_0)\) in (21) remains nonzero,
multiplied by the known unit \(\kappa^{2m}\).
Any further specified nonvanishing framing scalar has the same
property. The nonscalar current cannot be removed by omitting or
changing those scalar normalizations.

## 5. The original closing detects the omitted derivative

Let \(\phi_N\) be the original full Frobenius closing. In the
normalized Newton basis \(e_0,\ldots,e_d\),
\[
 \phi_N\!\left(\sum_j a_je_j\right)=a_d,\qquad
 \mathscr R(e_j)=e_{d-j}.
 \tag{22}
\]
Hence, for every \(N\ge2\),
\[
                 \phi_N(I)=0,\qquad
                 \phi_N(\mathscr R\Pi_0)=1.
 \tag{23}
\]
For the second identity, the coefficient of \(e_0\) in \(\Pi_0\)
is \(\Pi_0(c_0)=1\), since every other Newton basis polynomial
vanishes at \(c_0\). Reversal makes it the closing coefficient.
In particular \(\mathscr R\Pi_0\) is not a scalar multiple of \(I\).

Combining (19) and (23) yields the exact closed Ward source
\[
 \boxed{\qquad
 \phi_N\bigl(\mathscr R(R^\epsilon E_P)\bigr)
         =\kappa^\epsilon(1-e^{2\pi iP}).
 \qquad}                                                       \tag{24}
\]
It is zero at every integer \(P=m\), but its derivative there is
\(-2\pi i\kappa^\epsilon\ne0\).
This witness uses the actual original closing and works at every
level; it is not an arbitrary covector or a claim about one selected
knot example.

With the full factor and the actual filling variable it reads
\[
 \phi_N\bigl(\kappa^{-2p}
       \mathscr R(R^\epsilon E_{-p})\bigr)
     =\kappa^{\epsilon-2p}(1-e^{-2\pi ip}).
 \tag{25}
\]
At a nonzero integer \(p\), its \(p\)-derivative is
\(2\pi i\kappa^{\epsilon-2p}\).
In the reciprocal variable \(\delta=1/p\), its derivative is
\[
                  -2\pi i p^2\kappa^{\epsilon-2p}\ne0.
 \tag{26}
\]
Thus localizing away from the coordinate \(\delta=0\) does not
make the integer-source zero relation stable under this derivative.
In elementary algebraic terms, the alias relation
\(e^{-2\pi ip}-1=0\) is preserved by integer shifts of \(p\),
but not by \(\partial_p\). Equations (24)--(25) exhibit that relation
inside the prescribed finite source.

## 6. What this decides about the asymptotic coefficient ideal

The result concerns a specific proposed implication: differentiate
the scalar integer Ward deletion to obtain homogeneous relations
among the original filling coefficients. Equations (15), (21), and
(24) show exactly why that implication is false. The differentiated
source contains a value coupon and its actual exterior observation.
Retaining only the integer normal current loses a nonzero original
closing contribution.

It does not follow that the ideal generated by all geometric
asymptotic coefficients of an arbitrary fixed short partial filling
is not differential. Those coefficients live, when proved, in a
holomorphic reciprocal-slope chart after the specified action and
known factors have been extracted. The function
\(1-e^{-2\pi i/\delta}\) in (25) has an essential singularity at
\(\delta=0\); it is not a counterexample in that coefficient ring.
Rather, the exact source identity shows that integer evaluation
alone does not supply a derivative action on that ring.

A successful derivative-stability proof would have to identify the
geometric all-order images of both observations in (19), including
their original current and cycle data, and prove the required
relations without discarding either image. No such source comparison,
nonzero geometric participation, uniform slope/level remainder, or
new hyperbolic knot class is inferred here.

## Direct written sources

- [Original coherent filling Gaussian](actual_coherent_filling_gaussian_chirp.md):
  §1 supplies the actual full-Hermite functional calculus and its
  fixed logarithms; §8 supplies the integer even-power Ward identity
  and its literal cup-cap/turn normalization.
  SHA-256: d72f50bf1e9af5b15da89784c198a3cb5060b9ee9c3e6cc04b901049be516522.
- [Signed Gaussian Ward endpoint packet](research_signed_gaussian_ward_endpoint_packet.md):
  §§1--3 supply the full endpoint idempotent and normal element,
  odd-power endpoint data, and actual half-crossing turn formulas;
  §4 supplies the normalized Newton closing and turn conventions.
  SHA-256: 6bdced1b01917e41631386a24b337b60dfe5b04d35d70007cb56badc511a0191.

The continuous identity, derivative current, and closed-source
calculation are proved above from all physical values and first
normals. Only written reasoning and source-text reads were used.
No mathematical execution, numerical evidence, tests, compilation,
or frozen/public-source edits entered the proof.
