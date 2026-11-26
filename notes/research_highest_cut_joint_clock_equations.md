# Exact joint clock equations with the highest cut retained

Private written proof, 18 November 2026.

The generic highest-cut source has zero-extended pointwise ratio
equations whose boundary factors can be specified explicitly. Fourier
marking transports internal shifts and multiplication characters
together. The resulting equations act on the genuine initial full-clock
family of [D], before scalar elimination. The highest vacuum and its
forced crossing columns remain part of this source.

No assertion is made that every boundary factor is a unit on a desired
classical branch. Nor is a convergent local division of this joint
system, or continuation of its marked Borel minor, proved here.

## 1. The generic source and its fixed support

Use the actual generic signed crossings [F, (2)] on the untruncated
nonnegative-index basis, with \(Q=q^2\), and the original highest-cut
word, pivots and zero framing. Write
\[
 \mathcal I(Q,x,\tau;k)
  =x^c\tau^{T(k)}Q^{-T(k)}
                  \prod_{\text{crossings}}R^\pm(\text{its labels}),
 \qquad c=b-1-\operatorname{wr}(\beta)\in2\mathbb Z.
 \tag{1}
\]
Here \(k\in\mathbb Z^s\) are [M]'s fixed integral coordinates for all
strand matching equations and the two cut indices zero. Every label
and transfer is an integral linear form in \(k\). Formula (1) is
defined on its actual support
\[
 \mathcal P=\{k\in\mathbb Z^s:\ell_\lambda(k)\ge0
                                   \text{ for every }\lambda\},
 \tag{2}
\]
and is zero elsewhere. The forms in (2) include the nonnegative
indices and the transfer bounds \(0\le n\le a\) or \(0\le n\le b'\)
of [F]. Identically zero redundant forms may be omitted.

The support is a fixed rational polyhedral cone, independent of \(Q,x\)
and the ordinary color. Every fiber of the total index \(T\) is finite:
each intermediate index is at most \(T\). All identities below are
therefore meaningful as formal grading series, coefficient by
coefficient in \(\tau\). A finite translation may introduce finitely
many negative grading powers; it introduces no infinite coefficient.

The generating source is exactly
\[
 V(Q,x;\tau,m)
       =\sum_{k\in\mathbb Z^s}Q^{m\cdot k}\mathcal I(Q,x,\tau;k),
 \qquad Q^{m\cdot k}=e^{h\,m\cdot k},\quad h=\log Q.
 \tag{3}
\]
At the natural meridian \(Y=Qx^2\), its coefficientwise grading-one
completion is the canonical \(\mathscr W_m(h,Y)\) of [D].
There is no cyclic reinterpretation of the indices.

## 2. Generic ratios and explicit boundary factors

Let \(S^v f(k)=f(k+v)\), with \(v\in\mathbb Z^s\), and let
\(\mathsf T^j\) send \(x\) to \(q^j x\), equivalently \(Y\) to
\(Q^jY\). The proper finite products in [F] give, on the common
support, a rational ratio
\[
 \frac{\mathcal I(Q,q^j x,\tau;k+v)}
      {\mathcal I(Q,x,\tau;k)}
    =\frac{A_{j,v}(Q,Y,\tau,X)}
            {B_{j,v}(Q,Y,\tau,X)},\qquad X_i=Q^{k_i}.
 \tag{4}
\]
After clearing denominators, \(A_{j,v},B_{j,v}\) may be taken Laurent
polynomial in the displayed variables, with fixed rational
coefficient denominators if desired. Their order is fixed before
acting on the source.

Here is why these are proper rational functions. Translating \(k\)
changes each factorial length and each color-product endpoint by a
fixed integer. Adjacent products cancel to finitely many factors
\(1-Q^rX^a\) or \(1-x^{\pm2}Q^rX^a\). A meridian shift changes the
color-product starts by an integral number of their \(Q\)-steps.
The difference of the quadratic \(Q\)-exponents is linear in \(k\).
The total \(x\)-exponent of each closed highest-cut summand is even:
the local sign under \(x\mapsto-x\) telescopes by [F]'s staggered
parity conjugation, and \(c\) is even. Thus the extra factor from
\(x\mapsto q^jx\) is an integral power of the \(X_i\) and \(Q\).
This proves (4) in the natural \(Y\) coordinate without a new
framing phase. Negative \(j\) and negative components of \(v\) use
the same finite product cancellation.

On any common supported pair, intervening factorial indices are
strictly positive; their generic denominators are nonzero. The
color denominators are nonzero for generic \(x\). The cleared ratio
identity is consequently valid there, including supported endpoints.
If the common support is empty, any rational choice in (4) may be
used for the boundary-killed relation below.

For each support form put \(a_\lambda=\ell_\lambda(v)\). For
\(a_\lambda\ne0\), define the finite integer interval
\[
 J_\lambda(v)=
 \{\min(0,-a_\lambda),\ldots,\max(0,-a_\lambda)-1\}.
 \tag{5}
\]
Write \(X^{\ell_\lambda}=\prod_iX_i^{\ell_\lambda(e_i)}\), and retain
the entire boundary factor
\[
 \Theta_v(Q,X)=
  \prod_{\lambda:\,a_\lambda\ne0}
       \prod_{r\in J_\lambda(v)}
                  (1-Q^{-r}X^{\ell_\lambda}).
 \tag{6}
\]
The empty product is one. Each included \(\ell_\lambda\) is nonzero,
so (6) is a nonzero Laurent polynomial in the independent characters.

The following pointwise relation is exact on the whole integer lattice:
\[
 \Theta_v(Q,X)
   \bigl(B_{j,v}(Q,Y,\tau,X)\mathsf T^jS^v
                      -A_{j,v}(Q,Y,\tau,X)\bigr)\mathcal I=0.
 \tag{7}
\]
If both entries are supported, this is the cleared ratio identity.
If neither is supported, both terms are zero. If exactly one is
supported, some form crosses its support boundary. When
\(a_\lambda>0\), its old value lies in
\(\{-a_\lambda,\ldots,-1\}\); when \(a_\lambda<0\), its old value
lies in \(\{0,\ldots,-a_\lambda-1\}\). In either case it belongs
to (5), making the corresponding factor of (6) zero. This proves
(7) with every boundary layer retained.

No factor of (6) has been canceled. The equation remains meaningful
at special meridians after the whole rational identity is cleared.

## 3. Exact Fourier action and canonical completion

Let \(\mathsf E_i f(m)=f(m+e_i)\), and let
\(M_i f(m)=e^{-hm_i}f(m)\). Finite reindexing in each grading
coefficient gives
\[
 S_i\longmapsto M_i,\qquad
 X_i\longmapsto\mathsf E_i,\qquad
 M_i\mathsf E_j=Q^{\delta_{ij}}\mathsf E_jM_i.
 \tag{8}
\]
This is the same ordering as \(S_iX_j=Q^{\delta_{ij}}X_jS_i\).
For example \(\mathsf E_iM_i f(m)=Q^{-m_i-1}f(m+e_i)\),
whereas \(M_i\mathsf E_i f(m)=Q^{-m_i}f(m+e_i)\).

The grading is already inside \(\mathcal I\). Reindexing
\(\sum_kQ^{m\cdot k}\mathcal I(k+v)\) therefore gives
\(Q^{-m\cdot v}V\), with no omitted grading factor. The ratio
coefficients in (4) already contain the literal grading change
\(\tau^{T(v)}\).

Replacing \(X\) by the commuting translations \(\mathsf E\) in
the displayed left ordering, (7) becomes
\[
 \Theta_v(Q,\mathsf E)
  \left[
   B_{j,v}(Q,Y,\tau,\mathsf E)\mathsf T^jM^v
                   -A_{j,v}(Q,Y,\tau,\mathsf E)
  \right]V=0.
 \tag{9}
\]
In particular \(B_{j,v}(Q,Y,\tau,\mathsf E)\) must not be moved
through \(M^v\) without its \(Q\)-commutation factors.

Equation (9) holds coefficientwise in the graded generic source.
After expanding at \(h=0\), each term is rational in \(\tau,Y\)
by [M] and [F], with polynomial dependence on \(m\) at each order.
Its rational identity may therefore be evaluated at \(\tau=1\)
for generic \(Y\), and continued meromorphically coefficientwise.
This proves (9) for the original canonical \(\mathscr W_m\), with
\(\tau=1\). It is not a choice of a new solution of that system.
The initial Gevrey and Borel estimates in [D] apply to this whole
clock source.

## 4. Rescaled coordinates and the external shift

At the simple node of [D], put \(z=Y-\alpha\) and define the formal
rescaled source
\[
 F(z,\epsilon,\nu)
       =z\,\mathscr W_{\nu/z}(z^2\epsilon,\alpha+z).
 \tag{10}
\]
Its \(\epsilon\)-Borel germ is the genuinely convergent family
constructed in [D]. The exact internal actions are
\[
 \mathsf E_i:\nu\mapsto\nu+ze_i,\qquad
 M_i:\ F\mapsto e^{-z\epsilon\nu_i}F.
 \tag{11}
\]
For an external meridian shift set
\[
 z_j=e^{jz^2\epsilon}(\alpha+z)-\alpha.
 \tag{12}
\]
The old \(h\) and \(m\) are held fixed by \(\mathsf T^j\).
Consequently its conjugated action on (10) is exactly
\[
 \frac{z}{z_j}\,
 F\!\left(z_j,\epsilon\Bigl(\frac z{z_j}\Bigr)^2,
                         \nu\,\frac{z_j}{z}\right).
 \tag{13}
\]
This is a formal identity for \(z\ne0\), with its coefficientwise
scaled interpretation. In particular the external shift does not
hold \(\nu\) fixed. It commutes with (11) as the original operators
do: an internal translation becomes a translation by \(z_j e_i\)
after the external change.

Equivalently the conjugated meridian generator is
\[
 \mathcal D=z\epsilon(\alpha+z)
       \bigl(z\partial_z-2\epsilon\partial_\epsilon
                          +\nu\cdot\partial_\nu-1\bigr),
 \qquad z\mathsf T^jz^{-1}=e^{j\mathcal D}.
 \tag{14}
\]
For the Borel convention \(\sum a_n\epsilon^n\mapsto
\sum a_n\eta^n/n!\), write \(I f(\eta)=\int_0^\eta f(t)\,dt\).
The corresponding formal operator dictionary is
\[
\begin{split}
 Q&\longmapsto e^{z^2I},\\
 M_i&\longmapsto e^{-z\nu_i I},\qquad
 \mathsf E_i\longmapsto e^{z\partial_{\nu_i}},\\
 \widehat{\mathcal D}
   &=z(\alpha+z)
       \bigl[(z\partial_z+\nu\cdot\partial_\nu+1)I-2\eta\bigr].
\end{split}
 \tag{15}
\]
Indeed \(I\eta\partial_\eta=\eta-I\), giving the last formula
from (14). The first two internal operators obey exactly
\(e^{-z\nu_iI}e^{z\partial_{\nu_i}}
 =e^{z^2I}e^{z\partial_{\nu_i}}e^{-z\nu_iI}\).
The external exponential is recorded here as its exact formal
conjugation; no global analytic operator bound for it is assumed.

## 5. Highest-vacuum equations and forced faces

The boundary is the highest vector and covector, not an averaged cut.
For clarity, the generic matrices underlying the source [C] have
\[
 K v_a=xQ^{-a}v_a,\quad Fv_a=v_{a+1},\quad
 E v_a=[a]_q
   \frac{xq^{1-a}-x^{-1}q^{a-1}}{q-q^{-1}}\,v_{a-1},
 \tag{16}
\]
with the negative basis vectors zero. Thus exactly
\[
                   E|0\rangle=0,\qquad \langle0|F=0.
 \tag{17}
\]
The same equations hold after the regular scaling of \(E\) by
\((q-q^{-1})^2\). They are boundary conditions on every marked
word, independent of whether its cut matrix is scalar.

The literal coefficients [F, (2)] also give the forced columns and
dual rows
\[
\begin{split}
 R^+|0,b\rangle&=x^{-b}|b,0\rangle,&
 R^-|a,0\rangle&=x^a|0,a\rangle,\\
 \langle0,a|R^+&=x^{-a}\langle a,0|,&
 \langle b,0|R^-&=x^b\langle0,b|.
\end{split}
 \tag{18}
\]
For the first column the positive transfer is forced to be zero;
for the second the negative transfer is zero. The row statements
follow by the same output constraints. All Gaussian and color
products in those entries are empty. Clock marks are evaluated on
these very labels, leaving their actual monomials and the displayed
diagonal factors. The other vacuum orientations are not replaced
by (18).

If a support form \(\ell\) is identically zero on the actual cone,
one has the additional exact pointwise equation
\[
                           (X^\ell-1)\mathcal I=0.
 \tag{19}
\]
One may retain (19), or restrict the coordinates to the saturated
lattice in the real linear span of the support. This is an integral
change/restriction of the same indices, with the dual clock weights
restricted accordingly; it is not deletion of a source term.

These equations matter for localization. At a positive input
\(a=0\), the source has transfer zero, so a factor such as
\(1-X_n\) in (6) vanishes on the whole forced face. The ratio
equation alone can then become \(0=0\). Equation (19) and the
actual vacuum columns retain information lost by that equation.
Even after forced linear faces are reduced, a non-forced factor
\(1-X^\ell\) can vanish at a complex candidate branch. No assertion
that all such factors are units is made.

The remaining local problem is analytic division and continuation
of the full source-compatible joint system, including these faces
and its retained currents. Classical implicit invertibility by itself
does not supply that division, or allow the diagonal of an eliminated
certificate to be replaced by a scalar right factor. The exact
highest-cut conditions (17) cannot be replaced using unweighted cut
scalarity after clocks have been inserted.

Complete direct sources:

| Label | Complete source | SHA256 |
|---|---|---|
| C | notes/finite_sum_annihilator.md | d6e973b5f43049d7e68b35bd32b6677871815c240c97e74b2a6bed3e00370ae3 |
| F | notes/research_classical_verma_rational_loops.md | f88f5fc4d1eb0f68f9270e581bd0e1bfd43c669cef989d9813f6000feb4e3659 |
| M | notes/research_marked_verma_full_certificate_transport.md | a2d94711bb80e69139e25b4932f0878440934c0586ddd0535dc24fcfd61987b4 |
| D | notes/research_full_clock_initial_borel_family.md | d498ddfad641c85bba0257d22dcad53679ccd2cfb7e0c16f6cc790444f9e9b77 |

Only written mathematics, source reads and hash checks were used.
Frozen proofs and public documents are unchanged.
