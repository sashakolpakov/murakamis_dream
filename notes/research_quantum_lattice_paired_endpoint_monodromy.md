# Paired endpoint monodromy at the actual quantum lattice

Private written proof, 18 November 2026.

The global interval formula [G] gives an exact contour correction.
When an actual contour change pairs the two endpoint windings,
that correction vanishes at every integer quantum label. Both
endpoints are essential. A loop about only one endpoint generally
has a nonzero correction.

The statement concerns the literal scalar defect logarithms, before
normal products and the knot closing operation. It does not identify
an arbitrary cap deformation with a paired endpoint operation.

## 1. The actual interval and its two Borel conventions

Use the endpoint germ \(F=\log G_0\) of [G], with \(G_0\) meromorphic
on the plane and regular and nonzero at the endpoints \(0,s\).
The endpoint branches are fixed. They include the actual functions
\[
 F_0(t)=\log\frac{e^t-1}{t},\qquad
 F_\pm(Y,t)=\log\frac{1-Y^{\pm1}e^t}{1-Y^{\pm1}},
                      \qquad Y\ne0,1.
 \tag{1}
\]
The removable value of \(F_0\) at zero is retained.

For a fixed integer offset \(c\), let
\[
 V_c(h;s)=\sum_{a\ge1}h^{a-1}\frac{B_a(c)}{a!}
             \bigl(F^{(a-1)}(s)-F^{(a-1)}(0)\bigr).
 \tag{2}
\]
The scalar constant is
\(v_{0,c}=B_1(c)(F(s)-F(0))\).
Write \(\widehat V_c=\mathcal B_0V_c\), with
\(\mathcal B_0(h^j)=\xi^j/j!\), and put
\[
                     g_c(\xi;s)=\partial_\xi\widehat V_c(\xi;s).
 \tag{3}
\]
Thus \(g_c\) is the Borel transform of the positive quantum orders
with the convention
\(\mathcal B_1(h^j)=\xi^{j-1}/(j-1)!\), \(j\ge1\).
This derivative is single-valued meromorphic in \(\xi\), even
though \(\widehat V_c\) can have logarithmic monodromy.

Let \(\Sigma\) be the zeros and poles of \(G_0\), and write
\(m_\tau=\operatorname{ord}_\tau G_0\).
For \(n\ne0\), set
\[
 \omega_n=2\pi i n,\qquad
        q^s_{n,\tau}=\omega_n(\tau-s),\qquad
        q^0_{n,\tau}=\omega_n\tau .
 \tag{4}
\]
By [G], only finitely many of these candidate points occur in
any bounded \(\xi\)-set. At an upper-endpoint point the contribution
to \(\operatorname{Res}g_c\) is \(-m_\tau/\omega_n\); at a
lower-endpoint point it is \(m_\tau/\omega_n\). Collisions add
these contributions, with their signs. Every integer offset
adds only an entire Borel function and changes none of these
finite residues.

## 2. A finite endpoint-completed Laplace value

Fix \(h\ne0\), an endpoint \(R\) avoiding the poles, and a finite
piecewise smooth \(\xi\)-path \(\gamma:0\to R\) avoiding them.
Define
\[
 \mathscr V_c(h,s;\gamma)
      =v_{0,c}+\int_\gamma e^{-\xi/h}g_c(\xi;s)\,d\xi .
 \tag{5}
\]
No infinite-ray convergence is required.
This is the finite Laplace value with its endpoint companion:
\[
 \mathscr V_c
       =\frac1h\int_\gamma e^{-\xi/h}
                        \widehat V_c(\xi;s)\,d\xi
                         +e^{-R/h}\widehat V_c(R;s).
 \tag{6}
\]
The terminal value uses the actual branch continued along
\(\gamma\). To verify (6), integrate
\[
 d\bigl(e^{-\xi/h}\widehat V_c\bigr)
       =e^{-\xi/h}g_c\,d\xi
                     -h^{-1}e^{-\xi/h}\widehat V_c\,d\xi.
 \tag{7}
\]
The initial value is precisely \(v_{0,c}\). This proof is valid
on the continued path lift, including its loops.

In particular it would be incorrect to identify the integral in
(5) with the finite Laplace integral alone. The endpoint term in
(6) changes when a loop changes the logarithm at \(R\).

If \(\gamma_1,\gamma_0\) have the same endpoints, the residue
theorem applied to the single-valued meromorphic integrand in
(5) gives exactly
\[
 \mathscr V_c(\gamma_1)-\mathscr V_c(\gamma_0)
   =2\pi i\sum_q
       \operatorname{wind}_{\gamma_1-\gamma_0}(q)\,
           e^{-q/h}\operatorname{Res}_{\xi=q}g_c .
 \tag{8}
\]
Only finitely many points contribute. Thus (8) includes the
endpoint companion automatically and uses no discarded term
at infinity.

## 3. Paired contour changes and the exact character factor

We specify a pairing condition on the actual contour change.
Write \(w(q)=\operatorname{wind}_{\gamma_1-\gamma_0}(q)\)
at each distinct candidate point. Require
\[
                 w(q^s_{n,\tau})=w(q^0_{n,\tau})
                         =:\nu_{n,\tau}
                    \quad\hbox{for every }n,\tau .
 \tag{9}
\]
Only finitely many \(\nu_{n,\tau}\) can then be nonzero, by
local finiteness of the labeled candidate set.
This condition uses one physical winding at a collision,
not an independently assigned winding for each label.
For example, if a point is an upper endpoint for one label
and a lower endpoint for another, both occurrences must use
that same \(w(q)\). Their other endpoints must carry it as well.
Independent labeled pairs cannot simply be added as physical
contours: doing that would introduce cross contributions at
collisions. Condition (9) is the precise compatibility to be
checked for a given contour deformation.

Substituting the two endpoint residues into (8) proves
\[
 \boxed{\quad
 \mathscr V_c(\gamma_1)-\mathscr V_c(\gamma_0)
   =\sum_{n,\tau}
        \frac{\nu_{n,\tau}m_\tau}{n}\,
             e^{-\omega_n\tau/h}
                    \bigl(1-e^{\omega_n s/h}\bigr).
 \quad}
 \tag{10}
\]
The signs are fixed: both loops in each pair have the same
winding; the opposite signs come from the two literal
endpoint residues. In particular they have not been chosen
after quantum specialization.

At the actual integer quantum labels,
\[
                             s=hL,\qquad L\in\mathbb Z,
 \tag{11}
\]
every factor \(1-e^{\omega_n s/h}=1-e^{2\pi i nL}\) vanishes.
Thus every paired finite contour change (9) preserves (5)
exactly. Its exponentiation preserves
\(\exp\mathscr V_c\) exactly as well. Negative integer labels,
all positive levels, and either parity require no alteration
of this character calculation.

All fixed integer offsets \(c\) obey the same theorem. Their
extra entire terms integrate to zero around the closed
contour, by [G] and the residue theorem.
The principal integral \(h^{-1}\int_0^sF\), kept separately
in the literal interval identity, is unchanged by a deformation
of the Borel path at fixed endpoint branches. Its prescribed
value can therefore be included on both sides of (10).

For example, if \(q^s_{n,\tau}\) carries just this one residue
contribution, a loop about that point alone has correction
\[
                     -\frac{m_\tau}{n}
                              e^{-\omega_n(\tau-s)/h}.
 \tag{12}
\]
It usually remains nonzero at (11). At a collision the correction
is instead the full residue sum (8).
Thus the integer-lattice cancellation does not justify deleting
individual endpoint currents or unpaired monodromies.
Nor is a nonzero compatible finite winding vector asserted
at every parameter value. Collisions can force additional
windings, and an infinite connected endpoint graph can forbid
any nonzero finite compatible vector. Formula (10) remains
an exact theorem for the actual compatible operations.

## 4. Source scope and parameter restrictions

The original factorial and color factors are finite signed
combinations of these intervals, with scaled endpoints given
by their integer occupation lengths. For fixed quantum labels
those endpoints have precisely the form (11). Applying (10)
to each retained interval therefore gives a general class of
contour changes preserving its scalar quantum-lattice value.
The signed sums preserve the same conclusion.

This observation keeps the full meridian parameters and the
normalization factors of the original entries. No color factor
or peripheral germ has been replaced by its numerical value.
The theorem is initially stated on regular endpoint charts.
It does not evaluate the original logarithm at a zero of its
argument. The finite correction formula can be continued as
a whole wherever defined, but its vanishing does not by
itself prove regularity of a separately singular quantum
factor or justify a \(0/0\) specialization.

Nor does (5) alone identify a finite-cutoff resummation with
the exact finite interval product. That identification needs
its finite difference equation or an exact remainder
comparison, with the endpoint companion in (6) retained.
The present result establishes the explicit monodromy
correction and a quantum-lattice invariance operation.

For a knot period, a further argument must show that a proposed
global cycle deformation induces the actual paired winding
condition (9), or compute its unpaired corrections. That
topological assertion is not supplied by scalar
exponentiation or by the nonvanishing of a local minor.
No physical-cycle lower bound follows from this note.

## 5. Complete proof direct

| Label | Complete written source | SHA256 |
|---|---|---|
| G | notes/research_literal_interval_global_borel_log.md | d0885ed0ae7f050ad72d8d128a1edb7bef4200f1b02f624612a8946bbef72a2e |

G supplies the actual literal interval identification, both
Borel conventions through differentiation, the global
meromorphic derivative and its finite residue sums, and the
entire integer-offset corrections. The endpoint-completed
finite transform, exact character factor, winding condition
and integer-lattice cancellation are proved above.

Only written mathematics, source-text reads and hash checks
were used. Frozen manuscripts and public documentation
are unchanged.
