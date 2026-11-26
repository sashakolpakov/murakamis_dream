# A real-norm obstruction for the original unit-turn coupon map

Private written proof, 16 November 2026.

Polynomial real norm alone does not define a class preserved with
polynomial cost by the original unit-turn map. An actual cosine
charge coupon gives a direct obstruction. This does not decide the
separate stability question for fixed microscopic endpoint products.

## 1. Original normalization and the finite inequality

Put
\[
 N\ge2,\quad D=N-1,\quad q=e^{\pi i/N},\quad
 \kappa=q^{D^2/2},\quad c_j=2\cos((2j+1)\pi/N),
\]
\[
 S_s=\prod_{a=1}^s2\sin(a\pi/N),\quad S_0=1,\qquad
 e_s(Z)=S_s^{-2}\prod_{h<s}(c_h-Z).
 \tag{1}
\]
The full original Hermite algebra, turn, and signed crossing are
used. For \(\sigma=\pm1\), the unit-leaf coupon map is
\[
 U_\sigma=\kappa^\sigma T R^{-\sigma}T,\qquad
 T(R^\sigma P)=R^{-\sigma}U_\sigma P.
 \tag{2}
\]
Its literal triangular coefficients are
\[
 [e_r]U_\sigma P=
 \sum_{s=r}^k p_s(-1)^s q^{-\sigma s(r+1)}
                    \frac{S_s}{S_rS_{s-r}},
 \qquad P=\sum_{s=0}^k p_s e_s .
 \tag{3}
\]
These retain all crossing carriers and all physical first normals.
The output has ordinary degree at most \(k\).

**Theorem.** Let \(k\ge1\) be an integer satisfying
\[
                         2k(2k+1)<N.
 \tag{4}
\]
For the ordinary Chebyshev polynomial
\(f_k(Z)=T_k(Z/2)\), at either parity and either sign,
\[
 \|f_k\|_{[-2,2]}=1,\qquad
          |(U_\sigma f_k)(-2)|\ge\frac{3^k}{4}.
 \tag{5}
\]
Here the output is its literal degree-\(k\) polynomial, before
any further multiplication or trace.

*Proof.* The largest root of \(f_k\) is
\(2\cos(\pi/(2k))\). Equation (4) gives
\[
        \frac{(2k+1)\pi}{N}<\frac{\pi}{2k},
 \qquad c_k>2\cos(\pi/(2k)).
 \tag{6}
\]
In particular \(c_0,\ldots,c_k\) are distinct, all lie above
every root of \(f_k\), and \(k<\lfloor N/2\rfloor\).
Every derivative \(f_k^{(s)}\), \(0\le s\le k\), is positive
on their enclosing interval: differentiate the product of its
positive linear factors, whose leading coefficient is positive.
The real divided-difference formula therefore gives
\[
 f_k[c_0,\ldots,c_s]>0,\qquad
 p_s=(-1)^s S_s^2 f_k[c_0,\ldots,c_s]=(-1)^s a_s,\quad a_s>0.
 \tag{7}
\]
This includes \(s=0\) and \(s=k\).

At \(Z=-2\), each \(e_r(-2)\) for \(r\le k\) is positive.
Substituting (7) into (3) thus writes the entire value as
\[
 (U_\sigma f_k)(-2)=
 \sum_{0\le r\le s\le k}
 a_s\frac{S_s}{S_rS_{s-r}}\,e_r(-2)
                  \exp[-\sigma i\pi s(r+1)/N].
 \tag{8}
\]
Every displayed amplitude is positive. All phases have absolute
argument at most
\[
 \beta=\frac{\pi k(k+1)}N
       <\pi\frac{k+1}{4k+2}\le\frac{\pi}{3}.
 \tag{9}
\]
Taking real parts in (8) bounds the modulus below by one half
of the sum of its positive amplitudes.

The leading coefficient of \(f_k\) is exactly \(1/2\), so
\(a_k=S_k^2/2\). The single term \(r=s=k\) in that sum is
\[
            a_k e_k(-2)=\frac12\prod_{h=0}^{k-1}(c_h+2).
 \tag{10}
\]
Moreover (4) implies \(N>3(2k-1)\), since
\(4k^2+2k-3(2k-1)=4k^2-4k+3>0\).
Hence \((2h+1)\pi/N<\pi/3\) for \(h<k\), and \(c_h>1\).
Equations (8)--(10) give (5). \(\square\)

## 2. Actual shrinking-charge coupons and the scope of the obstruction

The canonical lattice cosine coupon is
\[
       \mathcal C_{N,1-k/N}(Z)=T_k(-Z/2)=(-1)^k f_k(Z).
 \tag{11}
\]
Thus (5) is an obstruction for original coupons, including their
first normals at double roots and the value at the odd simple root.
No arbitrary physical data have been substituted.

Fix \(0<c<1/2\), and take \(k=\lfloor c\sqrt N\rfloor\).
For all sufficiently large \(N\), (4) holds and
\[
 \|U_\sigma\mathcal C_{N,1-k/N}\|_{[-2,2]}
       \ge \frac14\,3^{\lfloor c\sqrt N\rfloor}.
 \tag{12}
\]
Consequently no constants \(C,p\), independent of \(N\), bound
these output norms by \(CN^p\), although every input has norm one
and its charge tends to one.

This example still has subexponential growth at level \(N\).
The exact low-degree estimate in the leaf source gives
\[
 \|U_\sigma\mathcal C_{N,1-k/N}\|_{[-2,2]}
 \le (2k+1)(k+1)(k+2)\,2^k
                         \left(\frac{eN}{2k}\right)^{2k}.
 \tag{13}
\]
At the indicated \(k\), its logarithm is \(O_c(\sqrt N\log N)=o(N)\).
Thus the lower bound disproves a polynomial-cost shortcut; it does
not disprove every positive filled-action margin.

In particular the theorem does not assert growth for
\(\prod_iK_N(2\cosh(\alpha_i/N),Z)\) with a fixed number of bounded
microscopic parameters. Those actual endpoint products have
additional structure. Proving a stable turn for them requires that
structure, rather than their polynomial real or physical norm alone.
No conclusion about a final trace follows by evaluating (12) before
that trace.

## 3. Coverage and direct sources

Large triangular crossing entries and the need to retain their
cancellations were already known. The statement above instead uses
the ordinary real norm of an exact original charge coupon and proves
that its transformed real norm is superpolynomial. The proof is a
finite positive-amplitude calculation with the original phases.

Both complete direct sources were read at their unchanged versions,
their used implications checked, and their hashes verified:

* [Original low-degree charged leaf map](research_low_degree_charged_leaf_reduction.md),
  SHA256 80df78ceafaa97182aebc6831651921f7f8040e1356ee07a3d0d3fbadd02846a:
  exact operator normalization, full triangular coefficients,
  the physical cosine coupon, and the quantitative upper bound (13).
* [All-degree endpoint unit-turn identities](research_full_endpoint_unit_turn_identities.md),
  SHA256 e2f69aaff28080b9dd9e11365ce18d68a9d738667917204714556681c50789e8:
  the whole-algebra range of (3), its phase convention, and the
  distinction between an endpoint identity and a norm estimate.

Only written mathematics, source-text reads and hashes were used.
No mathematical program, numerical experiment, test or build was run.
Adopted notes and public manuscripts remain unchanged.
