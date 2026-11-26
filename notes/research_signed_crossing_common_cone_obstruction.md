# Signed crossings have no common positive packet cone

21 November 2026. Research note. Earlier final notes and public
manuscripts remain unchanged.

There is no single closed pointed real cone in the full physical
boundary algebra which contains the unit and is preserved by both
original signed crossings. This remains true after any invertible
change of boundary coordinates. More generally, such a common cone
cannot send all its original marked periods into one pointed scalar
sector.

The obstruction uses crossing powers whose lengths grow with the
quantum level. It is an exact statement about a proposed common positive
compiler for *all* signed words at each level. It is **not** a
counterexample to the asymptotics of a fixed filling or to the volume
conjecture. It does not exclude a cone or reflected pairing which
depends on the received word.

## 1. Full boundary algebra and original phases

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), and

\[
 \eta=(-1)^d,\qquad \kappa=q^{d^2/2},\qquad
 P_N(z)=2T_N(z/2)+2,\qquad H_N=\mathbb C[z]/(P_N).
 \tag{1}
\]

Here \(T_N\) is the Chebyshev polynomial of the first kind. The
algebra includes the first normal at every double root; its complex
dimension is \(N\). Put

\[
 c_j=2\cos\frac{(2j+1)\pi}{N},\qquad
 s_r=\prod_{a=1}^r2\sin\frac{\pi a}{N},\qquad s_0=1,
\]
\[
 b_r(z)=s_r^{-2}\prod_{j=0}^{r-1}(c_j-z),\qquad 0\le r\le d.
\]

The original crossing and its inverse, with their Cartan scalars
retained, are the actual full-Hermite elements

\[
 R=\kappa\sum_{r=0}^d(-q)^r b_r,
 \qquad R^{-1}=\kappa^{-1}\sum_{r=0}^d(-q)^{-r}b_r.
 \tag{2}
\]

The unit is \(1=b_0\). Multiplication by \(R\) or \(R^{-1}\)
is the original local crossing action. The prescribed marked
Frobenius functional is

\[
 \phi_N(f)=\eta N^2[z^d]\operatorname{rem}_{P_N}f.
 \tag{3}
\]

These operations and their normalizations are those of the
[Newton source theorem](actual_newton_turn_positive_gram.md).
No ordinary trace or different closing row is substituted.

## 2. A source-visible unipotent power

Define in the full algebra

\[
                         U_N=\eta R^{2N}-1.
 \tag{4}
\]

The established crossing jets and original derivative-sampling source
give

\[
 U_N^2=0,\qquad
 \phi_N(U_N)=\frac{i\eta N^2}{\sin(\pi/N)}\ne0.
 \tag{5}
\]

For completeness, the short calculation retains the normal which
makes both statements possible. Write

\[
 \tau_j=\frac{\pi(d-2j)}N,\qquad
 C_N=\exp\frac{\pi i d^2}{4N},\qquad 0\le j<N.
\]

At the physical nodes \(z=-2\cos\tau_j=c_j\), the original
crossing has the value and first angular jet

\[
 R(c_j)=C_N e^{iN\tau_j^2/(4\pi)},\qquad
 \frac{R_t}{R}(\tau_j)=\frac{iN\tau_j}{2\pi}.
 \tag{6}
\]

The notation in (6) specifies the physical jets only; it does not
select a continuation of the canonical polynomial between nodes.
Equivalently \(R(c_j)=\kappa(-1)^j q^{j(j+1)}\).
Consequently \(R(c_j)^{2N}=\eta\), so

\[
 U_N(c_j)=0,\qquad
 (U_N)_t(\tau_j)=\frac{iN^2\tau_j}{\pi}.
 \tag{7}
\]

The square has zero value and first normal at every double root,
and zero value at the odd simple root. Thus \(U_N^2=0\) in
\(H_N\). The original source formula is

\[
 \phi_N(f)=\eta\sum_{j=0}^{N-1}
 \left.\frac{d}{dt}\{\sin t\,f(-2\cos t)\}\right|_{t=\tau_j}.
 \tag{8}
\]

Using (7) in (8) yields

\[
 \phi_N(U_N)=i\eta N\sum_{j=0}^{N-1}(d-2j)
                         \sin\frac{(2j+1)\pi}{N}.
\]

The sum is \(N/\sin(\pi/N)\). Indeed, with
\(\theta=\pi/N\), the geometric sums give

\[
 \sum_{j=0}^{N-1}(d-2j)e^{i(2j+1)\theta}
                 =\frac{2Ne^{i\theta}}{1-e^{2i\theta}}
                 =\frac{iN}{\sin\theta}.
\]

This proves (5), including \(U_N\ne0\). Equations (6)--(8)
are the original jet and source identities recorded in the
[twist-period insertion proof](research_twist_period_insertion_growth.md),
Sections 1--2. Its asymptotic estimates are not used here.

Crucially, the original crossing itself obeys

\[
 R^{4N}=(\eta(1+U_N))^2=1+2U_N,
 \qquad R^{4Nm}=1+2mU_N\quad(m\in\mathbb Z).
 \tag{9}
\]

Negative \(m\) are allowed because \((1+2U_N)^{-1}=1-2U_N\).
No phase has been removed in (9).

## 3. The common-cone obstruction

A **real cone** \(\mathcal C\) in \(H_N\), viewed as a real
vector space, is a nonempty set closed under addition and multiplication
by nonnegative real scalars. It is **closed** in the ordinary finite
dimensional topology. It is **pointed** if

\[
                         \mathcal C\cap(-\mathcal C)=\{0\}.
\]

A **pointed scalar sector** means a closed pointed real cone
\(\Sigma\subset\mathbb C\). A ray or a closed angular sector
of opening strictly less than \(\pi\) is an example.

**Theorem.** Suppose \(\mathcal C\subset H_N\) is a closed
real cone, \(1\in\mathcal C\), and

\[
               R\mathcal C\subset\mathcal C,
               \qquad R^{-1}\mathcal C\subset\mathcal C.
 \tag{10}
\]

Then \(U_N,-U_N\in\mathcal C\). In particular
\(\mathcal C\) is not pointed. Moreover
\(\phi_N(\mathcal C)\) is contained in no pointed scalar sector.

**Proof.** Repeated application of (10), followed by (9), puts
\(1+2mU_N\) in \(\mathcal C\) for every integer \(m\).
For positive \(m\), scale this element by \(1/(2m)\) and let
\(m\to\infty\). Closedness gives \(U_N\in\mathcal C\).
Using negative \(m\) and scaling by \(1/(2|m|)\) gives
\(-U_N\in\mathcal C\). Since \(U_N\ne0\), pointedness fails.
If all periods belonged to a pointed sector \(\Sigma\), it would
contain both \(\phi_N(U_N)\) and its negative. Equation (5)
contradicts pointedness of \(\Sigma\). \(\square\)

Thus no single invertible boundary-coordinate change makes the
original two signed crossing maps entrywise nonnegative real matrices
while giving the unit nonnegative real coordinates. The inverse image
of the nonnegative coordinate orthant would be a closed pointed cone
satisfying (10). This applies to any complex basis, or any real basis
of the underlying real packet space. A common invertible gauge does
not change the theorem: transport the cone, unit, operators and source
together by that gauge.

## 4. What this rules out, and what remains possible

The cone may depend on \(N\), and the invertible gauge may mix every
value and normal coordinate. The theorem still applies separately at
each level. Hence a universal positive-basis compiler for arbitrary
signed unit components cannot be obtained merely by finding a better
linear Fourier or Hermite basis.

The witnessing words \(R^{4Nm}\) have lengths depending on \(N\).
The theorem therefore supplies no asymptotic cancellation example
for one fixed short component, and no failure of a fixed-filling volume
identity. It does not exclude word-dependent cones, metrics at different
objects of a groupoid, or a positive pairing of a suitably reflected
whole network. A doubled density action \(X\mapsto RXR^*\) also
preserves its usual positive matrix cone; it is a different action
from the packet multiplication in (10), and its closing still has to
be the prescribed one.

The normalized residual Gram of the
[convex source theorem](research_convex_normalized_conway_source.md)
likewise does not assert (10). Its positive energy retains the signed
gate residuals, the original closing, and the normalization budget.
The present result is consistent with that construction. It closes a
common-cone positivity route; it gives no new lower bound for that
minimum or for the original knot source.

## Complete proof sources

Both complete matching texts were read. The cone argument is proved
above; the source inputs are the full crossing and the retained
unipotent jet, not asymptotic estimates.

| Source | SHA-256 |
|---|---|
| [Original Newton boundary operations](actual_newton_turn_positive_gram.md) | d8b21fa8db909120035e86e997a0e02cb84f8dce2dcf6fb244bb5c85c17e28a3 |
| [Original twist-period insertion](research_twist_period_insertion_growth.md) | 45a5183609ddea6b8d69915efc7c86798157f3c16cedb17a94b4adff61531308 |

Only written mathematics and text/hash operations were used. No
mathematical program, test, build, numerical calculation, git operation
or earlier-final edit was performed.
