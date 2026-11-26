# Finite cores and Volterra carriers of the actual clock source

Private written proof, 18 November 2026.

At each fixed transverse order, the original highest-cut clock source
is a finite combination of derivatives and primitives of its exceptional
clock family. The proof counts the actual normal-order and trace
contractions. It retains scalar framing, the highest-cut projector,
and every clock; no logarithm of a trace is taken.

Primitives produce polynomial densities on a segment. They cannot in
general be replaced by endpoint derivatives. Nevertheless the negative
odd Laurent coefficients at the exceptional fold have a single point
carrier. These are distinct assertions. No convergence of the full
transverse series after continuation, finite-meridian character, or
physical scalar lower bound is inferred here.

## 1. Source, coordinates, and the assertion

Keep the actual source of [H], under the simple two-branch node
hypotheses used for its exceptional family (21). Explicitly,
\(\alpha\notin\{0,1\}\) is a simple Alexander root, and the
analytic actual scalar annihilator has classical symbol \(P\)
with an abelian factor and
\[
 P(\alpha,1)=P_L(\alpha,1)=0,\qquad
                 P_{LL}(\alpha,1)P_{YL}(\alpha,1)\ne0.
\]
These are the node hypotheses of this note, not a claim that every
Alexander root or every knot satisfies them. Put
\[
 z=Y-\alpha,\qquad h=z^2\varepsilon,\qquad m=\nu/z,
 \qquad
 \mathcal F(z,\varepsilon,\nu)
       =z\,\mathscr W_{\nu/z}(z^2\varepsilon,\alpha+z).
 \tag{1}
\]
The marks in \(m\) are the original index clocks, equivalently
their fixed linear specialization from stage clocks. All assertions
about (1) initially mean coefficientwise formal identities.
Write its \(\varepsilon\)-Borel transform as
\[
                  F(z,\eta,\nu)=\sum_{k\ge0}z^kF_k(\eta,\nu).
 \tag{2}
\]
The absence of negative \(z\)-powers will also follow below.
The exceptional family in [H, (21)] is
\[
 F_0(\eta,y)=\frac r{w}e^{yf},\qquad
 w^2=1-4\sigma\eta,\quad w(0)=1,\quad
 f=\frac{1-w}{2\sigma},\quad y=\mu\cdot\nu,
 \qquad r\sigma\ne0.
 \tag{3}
\]
When differentiating in \(y\), regard it first as an independent
scalar variable and only afterward substitute \(y=\mu\cdot\nu\).
This convention also applies if \(\mu=0\).

**Theorem.** For every \(k\ge0\), the actual coefficient \(F_k\) is
a finite sum of terms
\[
       c\,\nu^\gamma\,\mathcal J_{b,a}F_0(\eta,y)
                         \big|_{y=\mu\cdot\nu},
 \qquad
 \mathcal J_{b,a}=
 \begin{cases}
 I_\eta^{b-a}\partial_y^a,& b\ge a,\\
 \partial_\eta^{a-b}\partial_y^a,& b<a,
 \end{cases}
 \tag{4}
\]
with constants fixed by the original word and its Taylor coefficients.
Here \(I_\eta\) is the primitive from the canonical origin, and the
indices can be chosen to satisfy
\[
 0\le b\le2k,\qquad 0\le a\le3k,\qquad
 |\gamma|\le2k,\qquad a-b\le k.
 \tag{5}
\]
For \(k=0\), (4) is just (3).
The constants in this finite representation are not asserted to have
a uniform exponential bound in \(k\).

Each coefficient is therefore an actual analytic Borel germ in
\(\eta\) and an entire function of the clocks. It has continuation
on the square-root cover in (3). Its full clock carrier consists of
endpoint derivatives and polynomial-density segments from zero to
\(\Theta(\eta)=\mu f(\eta)\), as specified in Section 5.
At \(w=0\), its odd principal part has order at most \(2k+1\),
and every coefficient in that principal part is
\[
          e^{\nu\cdot\Theta_*}\,P(\nu),\qquad
                  \Theta_*=\frac{\mu}{2\sigma},
                  \qquad \deg P\le4k.
 \tag{6}
\]
The full segment has not been discarded in (6).

## 2. The joint logarithmic filtration and the actual cut

We first derive the mark refinement of [H]. Move all unmarked
classical substitutions to the right in the finite word. Their
matrices are invertible, and conjugation preserves differential
order and homogeneous degree zero. A stage mark specialized to
\(e^{hm}\) is the exponential of \(h\) times an Euler vector
field linear in \(m\). Give \(m\) polynomial degree one.
This generator has differential order plus mark degree two.
The crossing logarithms in [H] have order at most \(j+1\) at
order \(h^j\), and have no marks before this operation.

The normal-symbol product is
\[
 U\star V=\sum_\delta\frac1{\delta!}
                         (\partial_p^\delta U)(\partial_Z^\delta V).
 \tag{7}
\]
Its commutator loses at least one differential order, while mark
degrees add. The finite-product logarithm argument of [H, Section 3]
therefore applies with the combined degree. It gives the literal
word in the form
\[
 \mathscr W_m(h,Y)=x_0^c
    \operatorname{Tr}_{\mathrm{Sym}}
       \left[e^{D(h,Y,m)}\Gamma(B(Y))\right],
 \quad D=\sum_{j\ge1}h^jD_j,
 \quad B=L_\beta(x_0)T_0,
 \quad T_0=\operatorname{diag}(0,1,\ldots,1),
 \tag{8}
\]
with the rational grading completion understood. Before completion,
replace \(B\) by \(\tau B\) and take each finite grading sector.
For every normal monomial in \(D_j\), with mark degree \(a_v\)
and differential order \(d_v\),
\[
                         a_v\le j,\qquad a_v+d_v\le j+1.
 \tag{9}
\]
The first inequality holds because every mark factor begins with one
factor of \(h\). The coefficients are holomorphic in \(z\).
Every monomial has equal creation and differentiation degrees.

At order one the only terms with equality \(a_v+d_v=2\) are the
unmarked quadratic terms and the linear-clock Euler terms.
In particular no scalar quadratic-in-marks term occurs at that
order. The pivot and scalar framing remain in \(D_1\); their lower
differential orders are not replaced by quadratic ones.
The factor \(x_0^c\) in (8) remains outside the trace.
Neither \(T_0\) nor any trace has been inverted or logarithmized.

## 3. Exact highest-cut Wick contractions

Here is the trace identity needed for all insertions, including the
singular matrix \(B=L_\beta T_0\). In small formal grading, set
\[
 H(s,t)=\operatorname{Tr}\left(e^{s\cdot Z}
                              e^{t\cdot\partial}\Gamma(B)\right).
 \tag{10}
\]
Cyclicity coefficient by coefficient, followed by the elementary
translation commutator, gives
\[
                    H(s,t)=e^{t^TBs}H(Bs,t).
 \tag{11}
\]
Indeed \(\Gamma(B)e^{s\cdot Z}=e^{(Bs)\cdot Z}\Gamma(B)\).
Moreover \(H(0,t)=\operatorname{Tr}\Gamma(B)=\det(I-B)^{-1}\),
because every positive-order derivative has zero diagonal.
The last determinant identity follows for diagonal matrices by
geometric series, and hence for all matrices as a formal grading
identity, by polynomial identity on the dense diagonalizable locus.
Iterating (11) in the grading yields
\[
 H(s,t)=\det(I-B)^{-1}\exp(t^T\mathcal C s),
                     \qquad \mathcal C=B(I-B)^{-1}.
 \tag{12}
\]
No inverse of \(B\) or \(T_0\) occurs. Differentiating (12) proves
the labeled pairing rule for every normal degree-zero monomial.
All these rational identities may then be evaluated at grading one,
as required by the original completion in [H].

At the simple determinant zero, write
\[
 \mathcal C(z)=\frac{R_0}{z}+G(z),\qquad
 R_0=uv^T\ne0,\qquad \operatorname{rank}R_0=1,
 \qquad
 r(z):=\frac{z x_0^c}{\det(I-B)}\quad\hbox{holomorphic},
 \quad r(0)=r.
 \tag{13}
\]
Simplicity of the determinant zero implies corank one: otherwise
its adjugate, and hence its first determinant derivative, would
vanish. The adjugate formula then proves (13), since
\(B(I-B)^{-1}=(I-B)^{-1}-I\).
The actual classical source fixes \(r(0)\) to the residue in (3).

Call a pairing using \(R_0/z\) soft and one using \(G(z)\) regular.
All soft pairings of a fixed set of labeled legs give the same
product after evaluating creation and differentiation slots on
\(u,v\). If there are \(s\) such pairs left, their sum is exactly
\(s!\) times that product. This remains true if the eigenvalue one
is not algebraically simple: only the simple determinant zero and
rank-one residue were used.

## 4. The exact excess count and finite-core sum

Expand the operator exponential in (8), then use (7) to normal-order
each product, and finally use (12). Keep a term with vertices of
orders \(j_v\), mark degrees \(a_v\), and differential degrees
\(d_v\). Put
\[
 n=\sum j_v,\quad q=\#\{v\},\quad A=\sum a_v,\quad d=\sum d_v.
 \tag{14}
\]
Let \(c_n\) be the number of normal-order contractions and \(c_r\)
the number of regular trace pairings, counted with multiplicity.
The number of remaining soft pairs is \(s=d-c_n-c_r\).
Let \(v_z\ge0\) be the total Taylor order from the vertex
coefficients, regular propagators, and the prefactor \(r(z)\).
Under (1) the exact transverse order is
\[
 \begin{split}
 k&=2n-A-s+v_z\\
  &=\underbrace{\sum(j_v-1)}_{H}
    +\underbrace{\sum(j_v+1-a_v-d_v)}_{D}
    +c_n+c_r+v_z .
 \end{split}                                                    \tag{15}
\]
Every term on the last line is nonnegative. This proves that the
actual rescaled source has no negative transverse powers.

Mark a vertex exceptional if its order exceeds one, its inequality
in (9) is strict, it meets a normal or regular contraction, or its
coefficient has positive Taylor order. All other vertices are
precisely the untouched quadratic soft vertex or a linear soft clock.
Both endpoints of a regular pairing must be counted, even though
the pairing is taken only after the full product has been formed.
There are at most
\[
                 H+D+2c_n+2c_r+v_z\le2k
 \tag{16}
\]
exceptional vertices. Their total quantum order \(b\) obeys the
sharper bound
\[
          b\le2H+D+2c_n+2c_r+v_z=2k-D-v_z\le2k.
 \tag{17}
\]
Here an order \(j\ge2\) vertex costs \(j-1\ge j/2\), and every
other exceptional vertex has order one. Overcounting vertices
incident to several events only enlarges the bound.

Fix their ordered list, monomials, Taylor orders and all normal and
regular contraction edges. This is a finite collection of possible
cores at each \(k\), since all its orders and leg counts are bounded.
Let \(A_c\) be the total mark degree of a core and \(a\) its
remaining soft pairs. Untouched vertices contribute zero excess, so
\[
              k=2b-A_c-a+v_z,\qquad
              a-b\le k-A_c-D\le k,\qquad
              a\le3k,\quad A_c\le b\le2k.
 \tag{18}
\]

Let the ordered core have \(q_c\) vertices. Insert \(n_2\) untouched
quadratic vertices and \(n_1\) untouched clock vertices. Their
placements have multiplicity
\((n_2+n_1+q_c)!/(q_c!n_2!n_1!)\).
The exponential's factorial leaves \(1/(q_c!n_2!n_1!)\).
All constraints on the order of contraction endpoints are already
constraints on the finite ordered core. The untouched vertices meet
no such edge and commute as ordinary symbols. Summing their finitely
many monomial types gives an initially unspecified scalar weight
\(\bar\sigma\) and a linear clock weight \(\bar\mu\cdot\nu\).
They have the actual normalization in (3): the empty-core Wick sum
has coefficient \(r(2\bar\sigma+\bar\mu\cdot\nu)\) at
\(\eta^1\), whereas the known actual exceptional family has
\(r(2\sigma+\mu\cdot\nu)\). Since \(r\ne0\), comparison
of the constant and linear clock parts gives
\(\bar\sigma=\sigma\) and \(\bar\mu=\mu\).
The residual soft-pairing factor is exactly \((2n_2+n_1+a)!\).

Consequently one core contributes, up to a fixed coefficient and
its monomial \(\nu^\gamma\), the formal series
\[
 \varepsilon^b
 \sum_{n_2,n_1\ge0}
 \frac{(2n_2+n_1+a)!}{n_2!n_1!}
       \sigma^{n_2}y^{n_1}\varepsilon^{n_2+n_1}.
 \tag{19}
\]
This regrouping is coefficientwise finite at every quantum order.
It exchanges no analytic infinite trace and no logarithm.

For the empty core, the Borel transform of (19) is (3).
An elementary verification is to use \(\eta=f-\sigma f^2\):
\[
 [\eta^{n+d}]\frac{f^d}{w}
  =\operatorname{Res}_{f=0}
       \frac{f^d\,df}{(f-\sigma f^2)^{n+d+1}}
  =\binom{2n+d}{n}\sigma^n.
 \tag{20}
\]
Expanding the exponential in (3) proves the required two-index
identity. The normalization of \(\sigma,\mu,r\) is therefore the
actual one in [H, (21)].
Applying \(\partial_y^a\) to the empty-core formal series supplies
\(\varepsilon^a\) and the factorial in (19). The remaining factor
is \(\varepsilon^{b-a}\). Under Borel transformation it becomes
exactly (4). If \(b<a\), no initial polynomial is lost:
\(\partial_y^aF_0\) begins at \(\eta^a\), so the indicated
\(a-b\) derivatives are the exact coefficient shift.
This proves (4)--(5) for the original highest-cut source.

## 5. Exact segment densities and bounded Cauchy complexity

For \(m\ge1\), repeated integration gives
\[
 I_\eta^m\partial_y^aF_0
  =\frac r{(m-1)!}\int_0^{f(\eta)}
            (\eta-\theta+\sigma\theta^2)^{m-1}
                      \theta^a e^{y\theta}\,d\theta.
 \tag{21}
\]
Indeed \(d\eta/w=d\theta\) under \(\theta=f(\eta)\).
The image of the canonical primitive path has been retained in
this change of variables. Its integrand is entire in \(\theta\),
so it can equally be the straight segment with these endpoints.
The polynomial factor satisfies
\[
 \eta-\theta+\sigma\theta^2
              =(f-\theta)\{1-\sigma(f+\theta)\}.
 \tag{22}
\]
For a core with \(m=b-a>0\), its degree is
\(2m-2+a=2b-a-2\le4k-2\).
Terms with \(b\le a\) are finite derivatives of the evaluation
carrier at \(\theta=f\). Their \(\eta\)-derivative order is at
most \(k\). Thus (21) is a genuine connector in the full answer,
not shorthand for two point evaluations.

These statements also give a finite-complexity Cauchy representation.
For a polynomial density \(P\), its canonical outer Cauchy transform is
\[
 \int_0^f\frac{P(\theta)}{\zeta-\theta}\,d\theta
 =-P(\zeta)\log(1-f/\zeta)
       -\int_0^f\frac{P(\zeta)-P(\theta)}{\zeta-\theta}\,d\theta.
 \tag{23}
\]
The second term is polynomial in \(\zeta\); the specified logarithm
vanishes at infinity. Endpoint derivatives give poles at \(f\).
This represents the whole functional, including its connecting banks.

When \(\mu\ne0\), choose a fixed vector \(v\) with
\(\mu\cdot v=1\), and write \(\nu=yv+\omega\),
\(\mu\cdot\omega=0\). The prefactor \(\nu^\gamma\)
in (4) is then a polynomial in \(y,\omega\) of total degree
at most \(2k\). Multiplication by \(y^e\) is the functional
\(\mathcal L(g)\mapsto\mathcal L(g^{(e)})\); on its Cauchy
transform it is exactly \((-\partial_\zeta)^e\).
This identity retains the actual endpoint terms of integration by
parts, rather than removing them.

There is a joint polynomial-log representation, not merely one
with arbitrary sheet-dependent coefficients. Namely the canonical
outer Cauchy density of \(F_k\), coefficientwise in \(\omega\),
has the form
\[
 \boxed{\displaystyle
 G_k(w,\zeta,\omega)=
 \frac{P_k(w,\zeta,\omega)+
       Q_k(w,\zeta,\omega)\log(1-f(w)/\zeta)}
      {w^{2k+1}\zeta^{2k}(\zeta-f(w))^{3k+1}}.}
 \tag{24}
\]
Here \(P_k,Q_k\) are polynomials, of total degree at most
\(13k+2\) in \((w,\zeta)\), and degree at most \(2k\)
in the transverse clocks \(\omega\). Constants depend on the
fixed source but not on \((w,\zeta)\). The logarithm in (24)
is initially its series at large \(\zeta\), then continues on
its retained sheet. On an outer circle containing the segment,
\((2\pi i)^{-1}\int e^{y\zeta}G_k\,d\zeta\) is precisely
the original \(F_k\).

For completeness, the degree and pole budget follows directly from
the blocks in (4). If \(l=a-b\ge0\), the block before clock
multiplication has density
\[
 \left(-\frac{2\sigma}{w}\partial_w\right)^l
                  \frac{r f(w)^a}{w(\zeta-f(w))}.
\]
It has denominator \(w^{2l+1}(\zeta-f)^{l+1}\) and polynomial
numerator of total degree at most \(a+l\): each derivative,
after putting terms over this denominator, raises numerator degree
by at most one. Applying \((-\partial_\zeta)^e\),
\(e\le2k\), raises the second denominator exponent to
\(l+e+1\) and does not raise this numerator-degree bound.
Since \(l\le k\), passage to the common denominator in (24)
gives degree at most \(7k+a-2l-e\le10k\).

If \(m=b-a\ge1\), (21)--(23) give polynomial plus polynomial
times logarithm, with both total degrees in \((w,\zeta)\)
at most \(D=2m-2+a\le4k-2\). Indeed
\(\eta=(1-w^2)/(4\sigma)\) and \(f(w)\) is affine;
integrating the polynomial quotient in (23) does not increase this
degree. After \(e\) derivatives in \(\zeta\), a denominator
\(\zeta^e(\zeta-f)^e\) suffices and the two numerator degrees
are at most \(D+e\). To see the induction, differentiate a
cleared expression once: multiplication by
\(\zeta(\zeta-f)\), the derivative of its denominator, and
\(\partial_\zeta\log(1-f/\zeta)=f/[\zeta(\zeta-f)]\)
raise its cleared numerator degree by at most one.
Passage to (24) gives degree at most \(D+7k+2-e\le11k\).
Thus the stated conservative bound \(13k+2\) covers all blocks
and their finite sums, including \(k=0\).

Formula (24) is holomorphic at \(w=1\) whenever \(\zeta\ne0\)
on the initial logarithm sheet; the two endpoints then coincide.
Returned logarithm sheets, and their connecting banks, remain part
of the displayed continuation. No division by \(f(w)\) was used.
If \(\mu=0\), (4) still holds with the auxiliary variable \(y\)
set to zero afterward; the clock dependence is a polynomial of
degree at most \(2k\). No nonzero clock direction is assumed
in the source theorem. We prove joint membership and linear
complexity in (24), not a product-contour bound uniform in \(k\),
and not convergence of the continued transverse series.

## 6. The negative odd Laurent carrier

Put \(\theta_*=1/(2\sigma)\), and denote by
\(f_+=(1-w)/(2\sigma)\), \(f_-=(1+w)/(2\sigma)\)
the two endpoint values on the actual square-root cover.
The deck difference of (21) is exactly
\[
 \frac r{(m-1)!}\int_{f_-}^{f_+}
       (\eta-\theta+\sigma\theta^2)^{m-1}
                        \theta^a e^{y\theta}\,d\theta.
 \tag{25}
\]
The common zero endpoint cancels here, not in (21).
With \(\theta=\theta_*+wt/(2\sigma)\), its limits are \(1\) to
\(-1\), and its polynomial factor is
\[
                  \eta-\theta+\sigma\theta^2
                          =\frac{w^2(t^2-1)}{4\sigma}.
 \tag{26}
\]
Thus (25) is \(w^{2m-1}e^{y\theta_*}\) times a function analytic
in \(w\), with polynomial-in-\(y\) Taylor coefficients. In
particular positive primitives contribute no negative odd powers.

For the remaining terms, \(\partial_y^aF_0=r f^a e^{yf}/w\),
and \(\partial_\eta=-(2\sigma/w)\partial_w\).
At most \(k\) such derivatives occur. Their Laurent order is at
most \(2k+1\), and every negative Laurent coefficient is
\(e^{y\theta_*}\) times a polynomial in \(y\) of degree at most
\(2k\). Multiplying the core clock polynomial of degree at most
\(2k\), and taking the odd deck projection, proves (6).

This is a statement at each fixed transverse order. It neither
identifies a resummed moving point carrier nor permits replacing the
full function by its principal part. The polynomial segment and all
regular terms in (21) remain part of the original source.

## 7. Complete proof source and scope

| Label | Complete proof direct | SHA256 |
|---|---|---|
| H | notes/research_actual_source_natural_log_filtration.md | 98c371fe71a210e9d886e30d60a487a3fe46599f1814c1b69229d829a1eb6f88 |

H supplies the literal signed crossing filtration, its finite-product
adapter, stage marks, original pivot/framing and highest-cut trace,
and the normalized exceptional family. The joint mark refinement,
Wick identity, exact excess count, finite-core factorials, Volterra
representation, Cauchy complexity and polar-carrier distinction are
proved above. No convergence of an operator logarithm or of the full
continued transverse series is assumed or concluded.

Only written mathematics and source-text reads were used. No
mathematical programs, tests or builds were run; frozen notes and
public manuscripts are unchanged.
