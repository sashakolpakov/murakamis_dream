# Local comparison of the original Conway boundary costs

22 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

For every fixed unfilled Conway expression, neighboring root rows of
its full positive covariance have polynomially comparable squared
norms. The estimate is uniform over the root index and all integer
levels. It includes the original two endpoint caps.

The proof uses the actual doubled synthesis tree, with all its label
constraints and positive Newton coefficients. An elementary finite
conformal-generation argument moves an integer configuration to a
nearby root fiber by changing every label only a bounded amount per
unit root change. Exact factorial ratios then compare the positive
partition sums. No entropy limit, spectral gap, or conditioning
assumption on the full covariance is needed.

The consequence concerns the cost of an original cap and its
finite-band observations. It does not bound the angle of the actual
filled packet with that cap, or the operator norm of an observable
on the whole quotient space.

## 1. The actual synthesis and the statement

Fix a finite expression \(E\) made from independent full leaves,
the actual Newton multiplication \(M\), and the genuine turn \(J\).
At level \(N\ge2\), put \(d=N-1\), and use the complete Newton
space \(H_N\), with its usual coefficient Hermitian norm.
The synthesis and covariance are
\[
 B_{\rm leaf}=I,\qquad B_{\mathscr R E}=JB_E,\qquad
 B_{EF}=M(B_E\otimes B_F),\qquad C_E=B_EB_E^* .
 \tag{1}
\]
Every leaf occurrence has its own \(N\)-dimensional input.
The matrix \(B_E\) depends on this unfilled expression and \(N\);
actual signed crossing powers may subsequently be supplied as leaf
vectors, with their phases and all Casimir normals retained.

All matrices in (1) are real, and the multiplication coefficients
are nonnegative. In the Newton basis \(e_0,\ldots,e_d\), put
\[
 s_h=2\sin(\pi h/N),\qquad
 S_a=\prod_{h=1}^a s_h,\quad S_0=1 .
 \tag{2}
\]
The nonzero product coefficients are
\[
 \mu_{ijk}
  =\frac{S_{i+j}S_k}
  {S_iS_jS_{k-i}S_{k-j}S_{i+j-k}},
 \quad
 0\le i,j,k\le d,\quad
 \max(i,j)\le k\le i+j\le d .
 \tag{3}
\]
Every displayed factorial index lies in \([0,d]\).
Products outside this support are zero in the full repeated-root
algebra, not only at distinct spectral nodes.
The turn has \(Je_i=e_{d-i}\).

Define the row costs
\[
              a_r(E,N)=(C_E)_{rr}=\|e_r^{\mathsf T}B_E\|^2,
                         \qquad0\le r\le d .
 \tag{4}
\]
They are positive: every \(B_E\) is surjective, by the unit
identity \(M(e_0\otimes f)=f\) and induction through (1).
The two original caps are precisely the rows \(r=0,d\).

**Theorem 1.** There is a constant \(A_E<\infty\), depending only
on the fixed expression, such that for every \(N\ge2\) and all
\(r,s\in\{0,\ldots,d\}\),
\[
 \boxed{\qquad
 N^{-A_E|r-s|}
       \le \frac{a_r(E,N)}{a_s(E,N)}
       \le N^{A_E|r-s|}.
 \qquad}
 \tag{5}
\]
In particular, for each fixed nonnegative integer \(k\), the
ratios \(a_k/a_0\) and \(a_{d-k}/a_d\) are polynomially bounded
above and below whenever the indicated indices exist. Their
logarithms divided by \(N\) tend to zero. The constant is not
claimed uniform over different expressions.

## 2. A finite integer-fiber lemma

We give the needed lattice argument completely.

**Lemma 2.** Fix an integer matrix \(\mathsf A\), and distinguish
one coordinate \(t\). There is \(G_{\mathsf A}<\infty\) with
the following property. Suppose
\[
       u,v\in\mathbb Z_{\ge0}^{D},\qquad
       \mathsf A u=\mathsf A v=b,\qquad u_t=r,\quad v_t=s .
 \tag{6}
\]
Then there is an integer \(u'\ge0\) such that
\[
       \mathsf A u'=b,\qquad u'_t=s,\qquad
       \|u'-u\|_\infty\le G_{\mathsf A}|r-s|.
 \tag{7}
\]
It can be chosen coordinatewise between \(u\) and \(v\).

**Proof.** Fix a closed orthant, allowing some coordinates to
be identically zero. Its intersection with \(\ker\mathsf A\)
is a pointed rational polyhedral cone. Intersecting it with
\(\sum_i|x_i|=1\) gives a compact rational polytope when the
cone is nonzero. Its finitely many rational vertices give
integer ray generators \(g_1,\ldots,g_m\) after clearing
denominators.

Every integer \(z\) in this cone can be written
\(z=\sum_\ell\alpha_\ell g_\ell\), \(\alpha_\ell\ge0\).
Subtract the integer sum
\(\sum_\ell\lfloor\alpha_\ell\rfloor g_\ell\).
The residual is an integer vector in the same cone and in the
bounded set
\(\{\sum_\ell\beta_\ell g_\ell:0\le\beta_\ell\le1\}\).
There are only finitely many such integer residuals.
Add them, except zero, to the generator list.
Thus every integer \(z\) in the cone is a nonnegative integer
sum of a fixed finite set of integer vectors in its orthant.
There are finitely many orthants, so their generator norms
have a common finite maximum \(G_{\mathsf A}\).

Apply this to \(z=v-u\). The decomposition is conformal:
every summand has the coordinate signs of \(z\). If \(s=r\),
take \(u'=u\). Otherwise retain just the summands with
nonzero \(t\)-coordinate, with their multiplicities.
All their \(t\)-coordinates have the sign of \(s-r\), and
are nonzero integers. Their total \(t\)-coordinate is
\(s-r\); hence there are at most \(|s-r|\) retained summands.
Let \(z'\) be their sum and set \(u'=u+z'\).
It is integer, remains in the same equality fiber, and has
the required \(t\)-coordinate. Conformality puts it
coordinatewise between \(u\) and \(v\), so \(u'\ge0\).
Its distance bound is (7). \(\square\)

The generator set need not be computed or used to evaluate the
original invariant. The lemma is a fixed-matrix lattice fact,
not an assumption about an optimizer or an asymptotic source.

## 3. The actual positive doubled-tree partition

Expand a matrix coefficient of \(B_E\) as a sum over the
integer wire labels of its expression. A leaf identifies its
input and output labels. A turn imposes \(i+j=d\).
A product imposes the four inequalities in (3), with its
weight \(\mu_{ijk}\).

To expand (4), take two copies of this tree and identify their
leaf input labels. Require their root labels to be equal,
but keep that common root label \(t\) as a coordinate rather
than fixing it yet. There is one label in \(\{0,\ldots,d\}\)
on every resulting wire. Squaring the real row sum gives
exactly
\[
             a_r(E,N)=
            \sum_{\substack{\xi\in\Omega_{E,N}\\t(\xi)=r}}
                          w_N(\xi),\qquad
             w_N(\xi)=\prod_{\text{both copies' products}}
                               \mu_{ijk}>0 .
 \tag{8}
\]
Repeated internal paths are separate configurations in (8).
There are no phases or cancellations in this covariance expansion.
The actual numerical leaf vectors have not been inserted.

All constraints are integer linear equalities or inequalities:
nonnegative labels, upper bounds \(d\), the product support (3),
the turns, the shared leaves, and equal root labels.
Introduce a nonnegative integer slack for each inequality.
This encodes the configurations uniquely as
\[
                    u\ge0,\qquad \mathsf A_Eu=b_d ,
 \tag{9}
\]
with a fixed integer matrix \(\mathsf A_E\).
Only the integer right side depends on \(d\).
The common root label \(t\) is one of the coordinates.
The number \(D_E\) of label and slack coordinates depends only
on the expression.

Each root fiber is nonempty, because its positive sum in (8)
equals the strictly positive number (4).
Consequently Lemma 2 applies to a source configuration at root
\(r\) and any witness at root \(s\).
For \(\delta=|r-s|\), it supplies a map, choosing one permitted
image for each source configuration,
\[
 \Psi_{r,s}:\Omega_{E,N}(r)\longrightarrow\Omega_{E,N}(s),
 \qquad
       \|\Psi_{r,s}(\xi)-\xi\|_\infty\le G_E\delta .
 \tag{10}
\]
All coordinates here include the slacks, so no support or endpoint
inequality has been weakened.
If \(\delta=0\), choose the identity map.
For \(\delta\ge1\), every target has at most
\[
                     (2G_E\delta+1)^{D_E}
 \tag{11}
\]
preimages: every such integer vector lies in that coordinate box.

## 4. Weight comparison and proof of Theorem 1

For every \(1\le h<N\),
\[
                  4/N\le s_h\le2 .
 \tag{12}
\]
This is the elementary sine chord bound and reflection.
Since \(N\ge2\), each \(s_h\) and its reciprocal are at most
\(N\). Therefore for all valid factorial indices \(a,b\),
\[
              N^{-|a-b|}\le S_a/S_b\le N^{|a-b|}.
 \tag{13}
\]
This includes a factorial index equal to zero.

Every factorial argument in (8) is one fixed integer linear
form in the labels. There are finitely many such arguments:
two numerator and five denominator factorials per product.
Equation (10) changes each argument by at most a fixed
constant times \(\delta\).
Applying (13) to every factor gives a constant \(A'_E\) such that
\[
 N^{-A'_E\delta}
       \le\frac{w_N(\xi)}{w_N(\Psi_{r,s}\xi)}
       \le N^{A'_E\delta}.
 \tag{14}
\]
No uniform Stirling formula or comparison with a continuum action
is used in this step.

Sum the upper inequality in (14) and use (11):
\[
 a_r(E,N)\le
        N^{A'_E\delta}(2G_E\delta+1)^{D_E}\,a_s(E,N).
 \tag{15}
\]
For an integer \(\delta\ge1\),
\[
 (2G_E\delta+1)^{D_E}
       \le(2G_E+1)^{D_E\delta}
       \le N^{A''_E\delta}
 \tag{16}
\]
with one fixed \(A''_E\), since \(N\ge2\).
Take \(A_E=A'_E+A''_E\).
Interchanging \(r,s\) proves both bounds in (5);
the case \(r=s\) is exact equality.
This completes the proof, including every integer parity and
every forced boundary face.

## 5. Finite-band observations at the original cap

The original quotient metric is \(G_E=C_E^{-1}\).
For a row \(\lambda\), its squared dual norm is
\[
                    \|\lambda\|_{G_E,*}^2=\lambda C_E\lambda^*.
 \tag{17}
\]
In particular \(\|e_r^{\mathsf T}\|_{G_E,*}=\sqrt{a_r}\).

**Corollary 3.** Suppose a specified matrix family \(H_N\) has
bandwidth at most a fixed \(b\), with entries bounded by
\(C_HN^p\), where \(p\ge0\). Then for every root row,
\[
 \boxed{\quad
 \|e_r^{\mathsf T}H_N\|_{G_E,*}
 \le (2b+1)C_H N^{p+A_Eb/2}
                     \|e_r^{\mathsf T}\|_{G_E,*}.
 \quad}
 \tag{18}
\]
Indeed positivity of \(C_E\) gives
\(|(C_E)_{ij}|\le\sqrt{a_i a_j}\).
If \(h=e_r^{\mathsf T}H_N\), then
\[
 hC_Eh^*\le
       \left(\sum_{|j-r|\le b}|h_j|\sqrt{a_j}\right)^2.
 \tag{19}
\]
Use (5) and the coefficient bound to prove (18).

This applies in particular to both original endpoint caps.
The actual Newton \(Z\), \(L=JZJ\), and their completed versions
have fixed bandwidth and bounded coefficients: writing
\(c_j=2\cos((2j+1)\pi/N)\), the next Newton factor gives
\[
 Ze_j=c_je_j-s_{j+1}^2e_{j+1},\qquad
 Le_j=c_je_j-s_j^2e_{j-1},
 \tag{19a}
\]
with the original absent end arrows. Here
\(s_{d-j}=s_{j+1}\) and \(c_{d-j}=c_j\) give the second identity.
Every other already-verified finite-band observable with polynomial
coefficients can be treated by the same estimate.
Thus these observations introduce at most polynomial additional
dual cost relative to the original cap in the actual unfilled
quotient metric.

Equation (18) is not a full operator-norm or Loewner inequality
for \(H_N\) in that metric. It is not a pointwise bound of
\(|e_r^{\mathsf T}H_Ny|\) by \(|e_r^{\mathsf T}y|\) for an
actual filled packet \(y\); the latter can vanish.
The source projection and original closing angle remain in the
exact scalar formula of the quotient-Gram theorem.
No lower bound for either is obtained here.

## 6. Positive diagonal leaf metrics

The same argument permits geometry-dependent positive leaf weights,
with an explicit regularity requirement.
For each leaf occurrence \(\ell\), let
\(D_{\ell,N}=\operatorname{diag}(w_{\ell,N}(0),\ldots,w_{\ell,N}(d))\)
have strictly positive entries. Suppose fixed constants \(b_\ell\)
satisfy
\[
 N^{-b_\ell}\le
       \frac{w_{\ell,N}(a+1)}{w_{\ell,N}(a)}
               \le N^{b_\ell},\qquad0\le a<d .
 \tag{20}
\]
Define the actual weighted covariance
\[
       C_E^{(w)}
          =B_E\left(\bigotimes_\ell D_{\ell,N}\right)B_E^* .
 \tag{21}
\]
**Corollary 4.** Theorem 1 and Corollary 3 hold for \(C_E^{(w)}\)
and its inverse, with constants also depending on the \(b_\ell\).

Indeed (8) gains the factor
\(\prod_\ell w_{\ell,N}(a_\ell)\), with one weight for each
shared leaf label, not two. The map (10) changes every such label
by at most \(G_E\delta\). Iterating (20) changes this additional
factor by at most \(N^{G_E(\sum_\ell b_\ell)\delta}\).
All support, positivity and multiplicity arguments are unchanged.
An overall positive scalar for a leaf need not be normalized.
For example \(w_{\ell,N}(a)=\exp[N h_\ell(a/N)]\) satisfies
(20) when the successive logarithmic increments obey that bound;
fixed functions \(h_\ell\) with bounded derivative do so.

This is an exact norm choice, not a change to the filled invariant:
replace \(B_E\) by
\(B_E(\bigotimes_\ell D_{\ell,N}^{1/2})\) and each actual
leaf vector \(f_\ell\) by \(D_{\ell,N}^{-1/2}f_\ell\).
Their full boundary output and both original closing scalars stay
identical. No conclusion is made for zero weights or arbitrary
nondiagonal leaf metrics.

In either version the fiber map may change the shared leaf labels,
consistently in its two replicas. It is legitimate for the positive
covariance, which sums over all those inputs. It is not a comparison
of scalar periods with fixed signed leaf coefficients: those
coefficients and their possible cancellations remain external.

## Complete proof sources and scope

Both complete matching proof sources were read:

| Source | SHA-256 |
|---|---|
| [Actual full boundary quotient Gram](research_conway_full_boundary_quotient_gram.md) | debe56dbad8151b90d44d0fccbf0dcf33dafb780370e01c8acdadbd2939dc077 |
| [Full positive Newton multiplication](actual_positive_newton_multiplication.md) | 543b5be6035ecec349ce8e78ee47085345ceefe4fc51e5f2005b802d999805bb |

They supply the original positive synthesis, surjectivity, exact
quotient metric and caps, and the full multiplication coefficients.
The fixed-matrix integer generation, fiber coupling, all-index
factorial comparison and finite-band cap estimate are proved above.
No novelty is claimed for finite conformal generation as a lattice
method. No ordinary-color quotient or physical Hermite direction
is discarded.
The standard Graver-basis framework is covered by
[Onn, *Nonlinear Discrete Optimization* (2010)](https://ems.press/books/zlam/84).
Only the publisher's primary description was checked for this
coverage statement; no theorem from the book is imported.
Lemma 2 is proved above.

The constants belong to a fixed unfilled expression; no uniform
bound over expression complexity or growing word length is asserted.
Actual short or long filling vectors remain arbitrary full inputs.
The theorem does not estimate their coherent projection or their
scalar closing angle, identify a boundary cost with hyperbolic
volume, or prove a new finite-exception volume theorem.

Only written mathematics, text/hash operations and that primary-record
lookup were used.
No mathematical program, numerical experiment, test, build, git
operation, or earlier-final edit was performed.
