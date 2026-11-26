# The meridian as a monomial change of the classical path weights

Private written proof, 18 November 2026.

For the original highest-cut source, the whole classical meridian
dependence can be absorbed into its independent path weights. The
change is a rational algebraic curve in the clock torus. Its tangent
also proves that the marked pole displacement vector is nonzero at
every simple Alexander root.

The statement concerns the classical source, with all path marks
retained. It does not make the same substitution in the quantum
source, identify a hyperbolic branch, or change the physical closing
functional.

## 1. The source and its two integral path forms

Keep the fixed knot braid, original highest input/output cut zero,
ordinary pivots, and zero framing of [F] and [M]. Write \(b\) for the
strand count, \(w_\beta\) for the writhe, and
\[
 c=b-1-w_\beta\in2\mathbb Z,\qquad Q=q^2,\qquad Y=x^2
                       \quad\text{at }Q=1.
 \tag{1}
\]
The path coordinates \(k\in\mathbb Z^d\) form the fixed integral basis
of the matching lattice in [M]. Every input label and crossing transfer
is an integral linear form in \(k\). The supported paths form its
nonnegative cone. A fixed total-index grading sector is finite.

Use independent multiplicative marks
\(\mathbf z=(z_1,\ldots,z_d)\), so the mark of a path is
\(\mathbf z^k\). Denote the total-index grading by \(\tau\).
We reserve \(t_i\) for local logarithms \(z_i=e^{t_i}\).

At \(Q=1\), a positive crossing with inputs \(a,b'\) and transfer
\(n\) has coefficient
\[
 {a\choose n}x^{-a-b'+n}(1-x^{-2})^n
    ={a\choose n}
       Y^{(-a-b'-n)/2}(Y-1)^n.
 \tag{2}
\]
A negative crossing has coefficient
\[
 {b'\choose n}x^{a+b'-n}(1-x^2)^n
    =(-1)^n{b'\choose n}
       Y^{(a+b'-n)/2}(Y-1)^n.
 \tag{3}
\]
These are the literal classical specializations of [F, (2)], on a
local square-root chart. We will show that their whole path product
has integral powers of \(Y\).

Define linear forms on the full matching lattice by
\[
 \begin{split}
 N(k)&=\sum_{\text{all crossings}}n,\\
 U(k)&=\frac12\left[
       \sum_{\text{negative crossings}}(a+b'-n)
       -\sum_{\text{positive crossings}}(a+b'+n)\right].
 \end{split}
 \tag{4}
\]
The first is visibly integral. The second is also integral on that
entire lattice, rather than only on supported paths.

Here is the required parity check. Replacing \(x\) by \(-x\)
multiplies either signed crossing entry by
\((-1)^{a+b'+n}\). By [F, Section 4], this is its output/input
ratio for the staggered tensor sign
\((-1)^{\sum_i i a_i}\). Along each matching path these ratios
telescope. The highest cut is fixed and all other outputs close to
their inputs, so their whole product is one. This is a statement
about the integral matching equations; positivity is not used.
Consequently the total exponent
\[
 H(k)=
   \sum_{\text{negative}}(a+b'-n)
      +\sum_{\text{positive}}(-a-b'+n)
 \tag{5}
\]
is even on the full matching lattice. Since
\(U=H/2-\sum_{\text{positive}}n\), (4) is integral.
In the chosen integral basis write
\[
             U(k)=u\cdot k,\qquad N(k)=n\cdot k,
                       \qquad u,n\in\mathbb Z^d.
 \tag{6}
\]
The vector \(n\) in (6) is a vector of coefficients of the total
transfer form; it is distinct from the individual crossing transfers.

It follows from (2)--(4) that every classical path summand, excluding
the external framing factor, is exactly
\[
             C(k)\,\tau^{T(k)}\mathbf z^k
                      Y^{u\cdot k}(Y-1)^{n\cdot k}.
 \tag{7}
\]
Here \(C(k)\) is the product of the indicated integer binomial
coefficients and negative-crossing signs. It is independent of \(Y\).
The classical pivot \(Q^{-T}\) is one. The original external factor
is \(x^c=Y^{c/2}\), and remains outside (7).

## 2. Exact algebraic transport in the clock torus

Let \(V_0(Y,\tau,\mathbf z)\) be this full classical marked source.
For any reference \(Y_0\ne0,1\), define
\[
 \Lambda_i(Y;Y_0)=
       (Y/Y_0)^{u_i}
       \left(\frac{Y-1}{Y_0-1}\right)^{n_i}.
 \tag{8}
\]
Each component is an invertible rational function on
\(\mathbb C\setminus\{0,1\}\). No logarithm or fractional power
is needed. Equation (7) proves, path by path,
\[
 V_0(Y,\tau,\mathbf z)
       =(Y/Y_0)^{c/2}
                V_0(Y_0,\tau,\mathbf z\Lambda(Y;Y_0)).
 \tag{9}
\]
Multiplication of clock coordinates in this formula is componentwise.
The identity first holds in every finite grading sector. It therefore
holds for the entire formal grading series.

The actual determinant trace theorem [M] identifies its rational
completion as
\[
 V_0(Y,\tau,\mathbf z)=
       \frac{Y^{c/2}}{D(Y,\tau,\mathbf z)},\qquad
 D=\det\!\left(I-\tau L_\beta(\sqrt Y,\mathbf z)T_0\right),
 \quad T_0=\operatorname{diag}(0,1,\ldots,1).
 \tag{10}
\]
The projector has not been inverted. Substitution in (9) cancels
the retained scalar and gives the exact determinant identity
\[
 \boxed{\quad
 D(Y,\tau,\mathbf z)
       =D(Y_0,\tau,\mathbf z\Lambda(Y;Y_0)).
 \quad}
 \tag{11}
\]
It is an identity of the full marked rational functions, and hence
holds also at their zero divisors. In particular it can be evaluated
at \(\tau=1\). It does not follow from unmarked cut scalarity.

## 3. A nonzero marked direction at a simple pole

Use local logarithmic marks and write
\(D(Y,t)=D(Y,1,e^t)\). Define the rational vector
\[
                       \beta(Y)=u+\frac{Y}{Y-1}n.
 \tag{12}
\]
Differentiating (11), or differentiating the finite-sector identity
(7) before rational continuation, gives
\[
                         YD_Y=\beta(Y)\cdot D_t.
 \tag{13}
\]
The scalar framing contribution \(c/2\) appears on both sides
of the corresponding identity for \(V_0\) and cancels. It is not
discarded.

Let \(\alpha\ne0,1\) be a simple Alexander root. Since
\[
                     D(Y,0)=Y^{c/2}\Delta(Y),
 \tag{14}
\]
one has \(D_Y(\alpha,0)\ne0\). The marked zero divisor is locally
\(Y=\alpha(t)\). Its displacement vector is
\[
              \mu_i=\partial_{t_i}\alpha(0)
                        =-\frac{D_{t_i}(\alpha,0)}{D_Y(\alpha,0)}.
 \tag{15}
\]
Equation (13) now proves
\[
 \boxed{\qquad \beta(\alpha)\cdot\mu=-\alpha.\qquad}
 \tag{16}
\]
Thus \(\mu\ne0\) for the full independent path marks. No simplicity
assumption about an eigenvalue of \(L_\beta T_0\) is used beyond
the stated simple determinant zero.

There is also an explicit normalized clock direction:
\[
                  v=-\beta(\alpha)/\alpha,\qquad \mu\cdot v=1.
 \tag{17}
\]
Every additive clock vector has the unique decomposition
\[
          \nu=\lambda v+\nu_\perp,\qquad
          \lambda=\mu\cdot\nu,\qquad \mu\cdot\nu_\perp=0.
 \tag{18}
\]
The forms and determinant have rational coefficients in \(Y\) and
the multiplicative marks. Consequently \(\mu,v\in\mathbb Q(\alpha)^d\).
This supplies the one-variable clock coordinate without choosing a
nonzero component by trial. At a simple two-branch node it applies
to the exceptional character and segment coordinates already
computed from the same marked determinant.

## 4. Scope and complete sources

The algebraic change (8) concerns the classical path coefficients.
At \(Q\ne1\), finite color products have distinct \(Q\)-spaced
factors, so (7) is not an asserted formula for the quantum source.
The theorem supplies no quantum reduction to one variable and
does not remove the transverse marks in (18).

The nonvanishing statement uses all independent path marks. An
arbitrarily selected smaller collection can miss this direction.
Multiple Alexander roots, a geometric character map, and a nonzero
physical closing coefficient remain outside the result.

The complete proof directs, read in full with their used implications
checked, are:

| Label | Complete proof source | SHA256 |
|---|---|---|
| F | notes/research_classical_verma_rational_loops.md | f88f5fc4d1eb0f68f9270e581bd0e1bfd43c669cef989d9813f6000feb4e3659 |
| M | notes/research_marked_verma_full_certificate_transport.md | a2d94711bb80e69139e25b4932f0878440934c0586ddd0535dc24fcfd61987b4 |

All path forms, transport identities, and tangent consequences are
proved above. Only written mathematics, source reads and hash checks
were used. Frozen proofs and public manuscripts are unchanged.
