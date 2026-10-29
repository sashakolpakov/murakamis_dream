# The cyclic Ward norm-root transfer carries the peripheral period

This gives an explicit group transfer, first-normal affine character,
and marked relative logarithmic period on the literal cyclic Ward
completion. It goes beyond equality of determinant characters.
The transfer is a quotient of a unit-group dilatation, not an
isomorphism between the \(N\)-dimensional unit group and the
one-dimensional geometric centralizer.

It constructs the full **peripheral** period
\(\Log(M^2)/(M-M^{-1})\). It does not construct the internal knot
Gaussian pushforward, identify a selected Bloch period, or prove
volume growth.

## 1. The actual finite algebra and its retained normal

Fix \(N\ge2\), \(Q\) primitive of order \(N\), and a characteristic-zero
coefficient field \(k\) containing \(Q\). Work near \(M=1\), with
\[
 R=k[[M-1]],\quad \kappa=M-M^{-1},\quad
 \kappa_N=M^N-M^{-N},\quad u_N=\kappa_N/\kappa,\quad
 \varepsilon_N=(-1)^{N+1}.
\]
The quotient \(u_N\) is a Laurent polynomial and a unit in \(R\),
with \(u_N(1)=N\). The actual cyclic Ward completion gives
\[
 A=R[e]/(e^N-\varepsilon_N\kappa_N),\qquad
 \sigma(e)=Qe.                                                \tag{1.1}
\]
The specified matrix realizes multiplication by \(e\), with its
single missing-edge completion retained. Write
\(\mathsf N=\operatorname{Norm}_{A/R}\) and \(\mathsf{Tr}=\operatorname{Tr}_{A/R}\).
The exact norm is
\[
 \mathsf N(1+te)=1+\kappa_Nt^N.                                \tag{1.2}
\]
These are the actual algebra and sign of
[the cyclic Ward norm calculation](cyclic_ward_norm_adapter.md).

The ideal \((e,\kappa)\) is topologically nilpotent, so logarithms
of units congruent to \(1\) modulo this ideal are well defined in
the completed order. No inverse of \(\kappa\) is taken in \(A\).

## 2. A divided-norm unit group and a genuine centralizer transfer

Consider the unit dilatation with coordinates
\[
 u=(1+\kappa a_0)+a_1e+\cdots+a_{N-1}e^{N-1}.                  \tag{2.1}
\]
Coefficients may lie in a complete \(R\)-algebra. Such \(u\) are
units, because their reduction is a principal nilpotent unit.
They are closed under multiplication and inversion. Moreover
\(\mathsf N(u)\equiv1\pmod\kappa\).

Retain the norm-root cover
\[
 \nu(u)^N=\mathsf N(u),
\]
and mark its identity sheet by \(\nu(u)\equiv1\pmod\kappa\).
Since \(N\) is invertible, Hensel recursion gives a unique such
root in the completed identity chart. The other \(\mu_N\) sheets
remain separate on the generic cover.

Define
\[
 \boxed{B(u)=\frac{\nu(u)-1}{\kappa}.}                         \tag{2.2}
\]
This is regular on the unit dilatation. Its fully algebraic
divided equation is
\[
 \frac{\mathsf N(u)-1}{\kappa}
  =\sum_{j=1}^{N}\binom Nj\kappa^{j-1}B(u)^j.                 \tag{2.3}
\]
At \(\kappa=0\) the derivative in \(B\) is \(N\), so (2.3)
also characterizes the completed identity-sheet map without
formally dividing a zero equation by zero.

Let the regular meridian centralizer be
\[
 J_M=\{C_M(b):1+\kappa b\ne0\},\quad
 C_M(b)=\begin{pmatrix}1+\kappa b&b\\0&1\end{pmatrix},
\quad b*b'=b+b'+\kappa bb'.
\]
Then
\[
 \boxed{\mathcal T_N:u\longmapsto C_M(B(u))}
                                                                    \tag{2.4}
\]
is an actual group homomorphism. Indeed uniqueness of the
marked root gives \(\nu(uv)=\nu(u)\nu(v)\), and (2.2) gives the
displayed centralizer law. It has the scalar section
\[
 C_M(b)\longmapsto (1+\kappa b)\,1_A.
\]
Its kernel is the marked norm-one unit group. Its generic
dimension is \(N-1\); no group isomorphism with \(J_M\) is claimed.

The source of (2.4) must retain the first normal coordinate \(a_0\).
It is not merely the principal units of \(k[e]/e^N\).

## 3. The explicit first-normal affine class

For the special fiber of the dilatation, multiplication has
\[
 a_0''=a_0+a_0'
       +\varepsilon_N N\sum_{i+j=N}a_i a_j',                  \tag{3.1}
\]
while the nonconstant coefficients multiply by the ordinary
truncated rule modulo \(e^N\). Formula (3.1) is the constant
wrap term \(e^N=\varepsilon_N\kappa u_N\), divided by \(\kappa\).
It is a specified central affine cocycle.

Let
\[
 p(z)=1+\sum_{j=1}^{N-1}a_jz^j.
\]
The transfer (2.2) on this special fiber is the explicit additive
character
\[
 \boxed{B_0(u)=a_0+\varepsilon_N N[z^N]\log p(z).}              \tag{3.2}
\]
The coefficient is a finite polynomial: truncate the ordinary
logarithm at degree \(N\).

To prove (3.2), use
\[
 \log\mathsf N(u)=\mathsf{Tr}\log u,\quad
 \mathsf{Tr}(e^j)=0\ (N\nmid j),\quad
 \mathsf{Tr}(e^N)=N\varepsilon_N\kappa_N.
\]
To first order in \(\kappa\), only the central term
\(\kappa a_0\) and the degree-\(N\) logarithm coefficient can
contribute. Thus
\[
 \log\nu(u)=\kappa a_0+
       \varepsilon_N\kappa_N[z^N]\log p(z)+O(\kappa^2),
\]
which proves the formula since \(u_N(1)=N\).

For the literal missing-edge path
\[
 \alpha(t)=1+te
\]
it gives \(B_0(\alpha(t))=t^N\). This follows also from (1.2).
The normal term is indispensable: all the units \(1+\kappa c\)
reduce to \(1\) in \(k[e]/e^N\), but their transfer is the arbitrary
value \(c\). Consequently no map on the **bare nilpotent special
fiber** can recover (2.4). The first-normal extension removes this
precise ambiguity.

## 4. The marked path maps to the actual meridian

For \(\alpha(t)=1+te\), the transfer is
\[
 \boxed{B(t)=
   \frac{(1+\kappa_Nt^N)^{1/N}-1}{\kappa},}                    \tag{4.1}
\]
with the identity root retained. It satisfies
\[
 B(0)=0,\qquad B(t=M)=M.                                      \tag{4.2}
\]
Indeed \(1+\kappa_NM^N=M^{2N}\), whose marked root near \(M=1\)
is \(M^2\); then \((M^2-1)/\kappa=M\).
The endpoint \(C_M(M)\) is the original marked meridian in
projective normalization. Thus this is an explicit transport
of the relative path, not just its determinant value.

The endpoint lift \(t=M\) uses the retained meridian marking.
Other lifts \(t=\zeta M\), \(\zeta\in\mu_N\), have the same
norm-quotient endpoint but need not have the same norm-one
factorial gauge. They remain separate source lifts. The finite
norm character alone does not select an internal knot cycle.

The \(\mu_N\) marking matters. A root \(\zeta M^2\), \(\zeta\ne1\),
would give \(B=(\zeta M^2-1)/\kappa\), with a pole at completion.
Such a sheet is not the regular identity chart. It has not been
identified with the identity sheet or silently divided out.

There is also an exact power-map diagram. The geometric adapter is
\[
 p_N:J_M\longrightarrow J_{M^N},\qquad
 p_N(b)=\frac{(1+\kappa b)^N-1}{\kappa_N}.                      \tag{4.3}
\]
The whole \(u_N\) is a unit near completion. By construction,
\[
 \boxed{p_N(B(u))=\frac{\mathsf N(u)-1}{\kappa_N},\qquad
        p_N(B(t))=t^N.}                                      \tag{4.4}
\]
The right side is regular before special evaluation. For (4.4)
on a general unit, the norm-root cover is part of the input.

## 5. Exact invariant forms and the relative peripheral period

The invariant centralizer form at fixed \(M\) is
\[
 \omega_M=\frac{db}{1+\kappa b}.
\]
Pullback along (4.1) gives the exact identity
\[
 \boxed{\mathcal T_N^*\omega_M
   =\frac1{N\kappa}\,d_t\log\mathsf N(1+te)
   =\frac{u_Nt^{N-1}}{1+\kappa_Nt^N}\,dt.}                    \tag{5.1}
\]
This is regular at \(\kappa=0\), where it is \(Nt^{N-1}dt\).
On the special fiber the transfer is \(b=t^N\), with its
ramified \(\mu_N\) cover retained; one does not replace its
differential by \(dt\).

Use the marked relative path \(t=0\) to \(t=M\), with logarithm
zero at the identity. Formal integration in \(R\), or continuation
on the same marked logarithmic chart, gives
\[
 \boxed{\int_0^M\mathcal T_N^*\omega_M
   =\frac{\Log(M^{2N})}{N\kappa}
   =\frac{\Log(M^2)}{\kappa}=L(M).}                            \tag{5.2}
\]
Thus the cyclic Ward block carries the full required peripheral
relative period, not merely its complete value or determinant.

For the raw target \(J_{M^N}\), the invariant form pulls back as
\[
 \frac{N t^{N-1}}{1+\kappa_Nt^N}\,dt.
\]
Its marked period is \(L(M^N)\). Comparing with (5.1) yields
\[
 \boxed{p_N^*\omega_{M^N}=\frac N{u_N}\omega_M,\qquad
 L(M^N)=\frac N{u_N(M)}L(M).}                                 \tag{5.3}
\]
The whole peripheral factor is retained before evaluating the
common zero. In particular \(L(1)=1\).
The phase \(\eta_N=i^{N+3}\) of the actual modified dimension
\(d_N=\eta_N/u_N\) remains its separately marked line; the
norm-root \(\mu_N\) sheet and this phase are different data.

The scalar logarithmic connection is also explicit. Its horizontal
period \(Z=\kappa L\) has
\[
 dZ=2\,d\log M,\qquad Z(1)=0,
\]
or, in the divided frame,
\[
 dL=-L\,d\log\kappa+\frac{2\,d\log M}{\kappa}.                 \tag{5.4}
\]
The selected regular solution is
\(L=1-\kappa^2/24+O(\kappa^4)\).
This is the peripheral logarithmic period; it is not the knot
Bloch regulator or its undetermined constant.

## 6. The actual factorial affine source normalizes to this torsor

The literal finite polynomial is
\[
 F(t,e)=\sum_{j=0}^{N-1}\frac{(-te)^j}{(Q;Q)_j}.
\]
Its exact affine equation from the actual missing-edge completion is
\[
 \sigma F-(1+te)F=-\frac{\kappa_Nt^N}{N}.                      \tag{6.1}
\]
The norm-root \(\nu=(1+\kappa_Nt^N)^{1/N}\) produces the norm-one
transport coefficient
\[
 a(t,e)=\frac{1+te}{\nu}.
\]
It has \(\mathsf N(a)=1\). This normalization is forced for a
homogeneous Hilbert--90 gauge: the unnormalized \(1+te\) has norm
\(1+\kappa_Nt^N\), so it cannot be a cyclic coboundary generically.

There is an explicit unique norm-one gauge lifting the actual
nilpotent \(F\). Define
\[
 H(t,e)=\sum_{j=0}^{N-1}
       \frac{t^j e^j}{\prod_{r=1}^j(\nu Q^r-1)},\qquad
 g=\mathsf N(H)^{-1/N}H,                                     \tag{6.2}
\]
with the scalar root marked by value one at \(\kappa=0\).
Every denominator in (6.2) is a unit on that chart.
Coefficient comparison gives
\[
 \nu\sigma H=(1+te)H.
\]
For the constant coefficient use
\[
 \prod_{r=0}^{N-1}(\nu Q^r-1)
       =\varepsilon_N\kappa_N t^N;
\]
the other coefficients follow from their displayed recursion.
Consequently
\[
 \boxed{\sigma g=a g,\qquad
        \mathsf N(g)=1,\qquad g|_{\kappa=0}=F|_{\kappa=0}.}     \tag{6.3}
\]

For uniqueness, two gauges have \(\sigma\)-invariant ratio,
which is scalar because \(1,e,\ldots,e^{N-1}\) are eigenvectors
with distinct eigenvalues \(1,Q,\ldots,Q^{N-1}\).
Its norm is its \(N\)-th power. The identity marking forces that
ratio to be one. No disconnected constant phase is reset.

The first-normal affine class is explicit:
\[
 \left.\frac{\sigma F-(1+te)F}{\kappa}\right|_{\kappa=0}
       =-t^N=-B_0(1+te).                                    \tag{6.4}
\]
Thus the additive character of the unit dilatation is precisely
the negative of the divided actual source at this order.

One can also write the entire first-normal correction without an
existence assertion. Let \(\epsilon=\kappa_N\), and use
\(g=F+\epsilon h+O(\epsilon^2)\) in the free basis. Put
\(F_0=F\bmod\epsilon\). Then
\[
 (\sigma-1)(h/F_0)
  =-\frac{t^N}{N}\left(1-(\sigma F_0)^{-1}\right).              \tag{6.5}
\]
The right side has zero constant coefficient in \(k[e]/e^N\).
Its nonconstant coefficient of \(e^j\) is divided by \(Q^j-1\)
to obtain \(h/F_0\). Its constant is fixed by the norm-one mark:
\[
 [e^0](h/F_0)
    =-\varepsilon_N[z^N]\log
        \left(\sum_{j=0}^{N-1}\frac{(-tz)^j}{(Q;Q)_j}\right).  \tag{6.6}
\]
Formula (6.6) follows from (3.2), since the central normal
coefficient is \(N[e^0]h\) when \(\epsilon=u_N\kappa\).
It retains the actual affine source, including the mixed algebra
normal term \(e^N=\varepsilon_N\epsilon\).

The relative \(t\)-connection of this norm-one gauge satisfies
\[
 (\sigma-1)d_t\log g
 =d_t\log(1+te)-d_t\log\nu
 =\left(\frac{e}{1+te}
     -\frac{\kappa_Nt^{N-1}}{1+\kappa_Nt^N}\right)dt.           \tag{6.7}
\]
Its trace is zero. The removed scalar component is exactly the
norm-root connection used in (5.1).

## 7. An exact limitation for the full external connection

On \(A[\kappa^{-1}]\), the multiplicative Kummer connection is
\[
 \nabla e=\frac eN\,d\log(\varepsilon_N\kappa_N).
\]
It is compatible with \(e^N=\varepsilon_N\kappa_N\), but is
logarithmic at the nilpotent special fiber. There is no regular
\(M\)-derivation of the order \(A\) extending \(d/dM\).
Indeed such a derivation would give
\[
 Ne^{N-1}D(e)=(\varepsilon_N\kappa_N)'.
\]
Reducing at \(M=1\), the left side belongs to the nilpotent ideal
\((e^{N-1})\) in \(k[e]/e^N\); the right side is the nonzero
constant \(2N\varepsilon_N\). This is impossible.

This no-go concerns a derivation compatible with multiplication;
it does not rule out arbitrary regular connections on the
underlying free module. The norm-root quotient has the regular
connection
\[
 d\log\nu=\frac1N d\log(1+\kappa_Nt^N),
\]
and its divided relative form (5.1) extends. Thus the quotient
and its first-normal source can carry the peripheral period even
though a regular multiplicative full-block connection cannot.

## 8. Scope for the knot problem

The rank-one missing edge, its factorial affine source, the norm-root
torsor, the first-normal additive character, and the complete
peripheral period now occur in one explicit transport diagram.
Neither a group isomorphism nor a bare special-fiber identification
was assumed.

The relative path is the lift of the already specified meridian
section. The norm-root quotient forgets a norm-one kernel of
dimension \(N-1\); its peripheral period does not determine the
kernel period or the knot state which couples to it.

This is not yet a map from the actual knot's internal finite
contraction to its geometric Gaussian block. In particular it
does not identify its selected global source with the marked
Bloch regulator or prove that the geometric contribution survives.
Those assertions remain outside the norm-root peripheral theorem.

[Exact audit](../experiments/audit_cyclic_ward_norm_root_period.py).
It passes 198 exact checks: 126 generic/first-normal factorial-gauge
checks at \(N=2,\ldots,10\), 16 first-normal cocycle checks, and
56 peripheral form, period, and connection checks. No numerical
asymptotic fitting is used.
